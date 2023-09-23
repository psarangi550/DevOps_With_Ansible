# <ins> Asynchronous Parallel Serial Task </ins> #

- this section being focused on the `performance aspect` of `Ansible` 

- here we will see , `how to improve the ansible execution performance` by `using some of the feature that built into Ansible `

- we will `discuss` about the `ansible playbook performance and bottleneck`

- also we will be looking into 
  
  - `polling` 

  - `Asynchronous Job Identifiers`

  - `Asyncronous status handling`

  - `Serial execution`
  
  - `Batch Execution`

  - `Alternative execution Statergies ` `to facilitate` `parallel execution `

- for understanding `performance imporvement for ansible` we have look into the `common pitfall during ansible execution`

# <ins> common pitfall while using Ansible Playbook Execution </ins> #

- we have look into the `area of ansible` which is `inefficient or does not work really well`

- we will address the `pitfall` , as we are going with the `cases` and how to get the `performance improvement`

- **Case1**

- here we are using the `command module` in here in the `ansible-playbook` as below 

    ```
        slow-playbook.yaml
        ------------------

        ---
        
        - hosts: linux
          tasks:
            - name: Task1
              command: /bin/sleep 5
  
            - name: Task2
              command: /bin/sleep 5
  
            - name: Task3
              command: /bin/sleep 5
  
            - name: Task4
              command: /bin/sleep 5
  
            - name: Task5
              command: /bin/sleep 5

        ...

        # here if execute the task as below 
        time ansible-playbook slow-playbook.yaml
        # executing the task with the time command to evaluate the time
        

        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [centos2]
        ok: [centos1]
        ok: [ubuntu1]
        ok: [ubuntu3]
        ok: [ubuntu2]
        ok: [centos3]

        TASK [Task1] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [centos2]
        changed: [ubuntu3]
        changed: [ubuntu2]
        changed: [ubuntu1]
        changed: [centos3]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]
        changed: [ubuntu2]
        changed: [ubuntu3]
        changed: [centos1]
        changed: [centos2]
        changed: [centos3]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [ubuntu1]
        changed: [ubuntu2]
        changed: [centos2]
        changed: [ubuntu3]
        changed: [centos3]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [ubuntu1]
        changed: [centos2]
        changed: [ubuntu2]
        changed: [ubuntu3]
        changed: [centos3]

        TASK [Task5] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [ubuntu1]
        changed: [centos2]
        changed: [ubuntu2]
        changed: [ubuntu3]
        changed: [centos3]

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


        real    0m56.638s
        user    0m6.873s
        sys     0m3.130s





        # we need to observe few things"---->
        
        - the first Task i.e `Task1` will execute in all the `different host` and followed by the `seconda task executed on all host` and so on

        - hence the above task will take around `30 seconds` expected `not considering the overhead and gather facts`
        
        - we can see that while executing `out of 6 target host to which we are targeting` ` 5 out of the target host completed the task` and `wait for the 6th task to be completed` 
        
        - here the ansible execution statergies is of `linear execution statergy` which is the default startergy for the `ansible playbook`
        
        - until the `Given Task` not being completed on `all the host` the `ansible-playbook` execution will not be moved to `execute the next lined up task` 
        
        - the `playbook execution` need to wait for `all task should executed and finished` on all `corresponding hosts` before executing the `rest of the tasks`

        - if a `tak need to be executed and finished on one of specific host` the rest of that that got finished on the other host have to wait for that all the task acccross all the host to be completed before moving onto the next iteration of task
    

    ```

- here we are waiting for the `particular task to be exeecuted on the target host` and then we can `move to the next task in line` 

- if we had a `task executing on the specific host of the target group` then `it would hold up the rest of the future task thats been planned for target group`

- if we had a `task executing on the specific host of the target group` then it would `hold up the rest of completed task of the other hosts in the target group as well`

- **Improvemeent1**
  
  - we can improve this by `executing the task on a specific host` rather than `all the host in the target group`
  
  - here we can use the `when condition` to `specify which task will run on which host `  
  
  - in this case the rest of the `as the task been dedicated for a specific host` hence `specific host will execute the task rather than all the host`
  
  - all the `rest of the target host can be skipped executing the task` which can `improve the time`
  
  - we can erite it out as below `playbook`
    
    ```
        impriove_slow-playbook.yaml
        ------------------

        ---
        
        - hosts: linux
          tasks:
            - name: Task1
              command: /bin/sleep 5
              when ansible_hostname == "centos1"
  
            - name: Task2
              command: /bin/sleep 5
              when ansible_hostname == "centos2"
  
            - name: Task3
              command: /bin/sleep 5
              when ansible_hostname == "centos3"
  
            - name: Task4
              command: /bin/sleep 5
              when ansible_hostname == "ubuntu1"
  
            - name: Task5
              command: /bin/sleep 5
              when ansible_hostname == "ubuntu2"

            - name: Task6
              command: /bin/sleep 5
              when ansible_hostname == "ubuntu3"

        ...
    
        # here in this case we can execute the script as below 
        ansible-playbook impriove_slow-playbook.yaml

        
        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [centos2]
        ok: [centos1]
        ok: [ubuntu3]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [centos3]

        TASK [Task1] ******************************************************************************************************************************************************************************************
        skipping: [ubuntu1]
        skipping: [ubuntu2]
        skipping: [ubuntu3]
        skipping: [centos2]
        skipping: [centos3]
        changed: [centos1]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        skipping: [ubuntu1]
        skipping: [ubuntu2]
        skipping: [ubuntu3]
        skipping: [centos1]
        skipping: [centos3]
        changed: [centos2]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        skipping: [ubuntu1]
        skipping: [ubuntu2]
        skipping: [ubuntu3]
        skipping: [centos1]
        skipping: [centos2]
        changed: [centos3]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        skipping: [ubuntu2]
        skipping: [ubuntu3]
        skipping: [centos1]
        skipping: [centos2]
        skipping: [centos3]
        changed: [ubuntu1]

        TASK [Task5] ******************************************************************************************************************************************************************************************
        skipping: [ubuntu1]
        skipping: [ubuntu3]
        skipping: [centos1]
        skipping: [centos2]
        skipping: [centos3]
        changed: [ubuntu2]

        TASK [Task6] ******************************************************************************************************************************************************************************************
        skipping: [ubuntu1]
        skipping: [ubuntu2]
        skipping: [centos1]
        skipping: [centos2]
        skipping: [centos3]
        changed: [ubuntu3]

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
        centos2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
        centos3                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
        ubuntu1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
        ubuntu2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   


        real    0m35.638s
        user    0m4.601s
        sys     0m1.843s    

        # we have few observation over here 

        - here we are executing the `particular task based on the particular host` , hence the `rest of the task execution` can be `skippped`
        - ansible_hostname provide the specific host value whereas ansible_distribution will provide the distribution name such as ubuntu or centos 
        - but here also we are observing that `five of the host which are not marching skipped and then the 6th one getting execued`
    
    
    ```

  - **Improvement2**
    
    - `ansible` has the `asynchronous feature support for the tasks execution ` which will help in running the `long running tasks` , where we don't want to keep the `ssh connection will not stay open` or `task should not take more than the ssh timeout value` , if the task is taking more time then it will going to be `ssh timeout will happen and ssh connection will be closed`
    
    - we can simply `run the task` and `check for its status later or poll later for status`
    
    - we can se the `async` valuw which means `wait at least for specified number of seconds` we can provide that as `async=<total number of secs to wait>`
    
    - we can then use `poll` `which` will be `checking the status` `of the task` for `specified number of seconds` and the poll value can be mentioned as `poll=<specified number of seconds to check eah time for status of the task>`
    
    - when we set the `poll=<specified seconds> ` then it will `check/poll` for the `status of the task each of the specified seconds`

    - we can see the below `ansible playbook` for reference 

        ```

            improve2_slow_playbook.yaml
            ---------------------------

            ---
        
            - hosts: linux
            
              tasks:
                - name: Task1
                  command: /bin/sleep 5
                  async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
                  poll: 1 # here this will check for the status of the job for every 1 seconds
                  when: ansible_hostname == "centos1" # putting the when condition to check against a particular target host rather the all the linux target host

                - name: Task1
                  command: /bin/sleep 5
                  async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
                  poll: 1 # here this will check for the status of the job for every 1 seconds
                  when: ansible_hostname == "centos2" # putting the when condition to check against a particular target host rather the all the linux target host

                - name: Task1
                  command: /bin/sleep 5
                  async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
                  poll: 1 # here this will check for the status of the job for every 1 seconds
                  when: ansible_hostname == "centos3" # putting the when condition to check against a particular target host rather the all the linux target host

                - name: Task1
                  command: /bin/sleep 5
                  async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
                  poll: 1 # here this will check for the status of the job for every 1 seconds
                  when: ansible_hostname == "ubuntu1" # putting the when condition to check against a particular target host rather the all the linux target host

                - name: Task1
                  command: /bin/sleep 5
                  async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
                  poll: 1 # here this will check for the status of the job for every 1 seconds
                  when: ansible_hostname == "ubuntu2" # putting the when condition to check against a particular target host rather the all the linux target host

                - name: Task1
                  command: /bin/sleep 5
                  async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
                  poll: 1 # here this will check for the status of the job for every 1 seconds
                  when: ansible_hostname == "ubuntu3" # putting the when condition to check against a particular target host rather the all the linux target host
        
        
            ...
            # when we execute the playbook as below 
            ansible-playbook improve2_slow_playbook.yaml


            PLAY [linux] ***************************************************************************************************************************************************************************

            TASK [Gathering Facts] *****************************************************************************************************************************************************************
            ok: [ubuntu3]
            ok: [ubuntu2]
            ok: [ubuntu1]
            ok: [centos2]
            ok: [centos1]
            ok: [centos3]

            TASK [Task1] ***************************************************************************************************************************************************************************
            skipping: [ubuntu1]
            skipping: [ubuntu2]
            skipping: [ubuntu3]
            skipping: [centos2]
            skipping: [centos3]
            ASYNC POLL on centos1: jid=339097426482.18409 started=1 finished=0
            ASYNC POLL on centos1: jid=339097426482.18409 started=1 finished=0
            ASYNC POLL on centos1: jid=339097426482.18409 started=1 finished=0
            ASYNC POLL on centos1: jid=339097426482.18409 started=1 finished=0
            ASYNC OK on centos1: jid=339097426482.18409
            changed: [centos1]

            TASK [Task2] ***************************************************************************************************************************************************************************
            skipping: [ubuntu1]
            skipping: [ubuntu2]
            skipping: [ubuntu3]
            skipping: [centos1]
            skipping: [centos3]
            ASYNC POLL on centos2: jid=855367207410.16907 started=1 finished=0
            ASYNC POLL on centos2: jid=855367207410.16907 started=1 finished=0
            ASYNC POLL on centos2: jid=855367207410.16907 started=1 finished=0
            ASYNC OK on centos2: jid=855367207410.16907
            changed: [centos2]

            TASK [Task3] ***************************************************************************************************************************************************************************
            skipping: [ubuntu1]
            skipping: [ubuntu2]
            skipping: [ubuntu3]
            skipping: [centos1]
            skipping: [centos2]
            ASYNC POLL on centos3: jid=571363769865.16314 started=1 finished=0
            ASYNC POLL on centos3: jid=571363769865.16314 started=1 finished=0
            ASYNC POLL on centos3: jid=571363769865.16314 started=1 finished=0
            ASYNC POLL on centos3: jid=571363769865.16314 started=1 finished=0
            ASYNC OK on centos3: jid=571363769865.16314
            changed: [centos3]

            TASK [Task4] ***************************************************************************************************************************************************************************
            skipping: [ubuntu2]
            skipping: [ubuntu3]
            skipping: [centos1]
            skipping: [centos2]
            skipping: [centos3]
            ASYNC POLL on ubuntu1: jid=345147938511.28334 started=1 finished=0
            ASYNC POLL on ubuntu1: jid=345147938511.28334 started=1 finished=0
            ASYNC POLL on ubuntu1: jid=345147938511.28334 started=1 finished=0
            ASYNC OK on ubuntu1: jid=345147938511.28334
            changed: [ubuntu1]

            TASK [Task5] ***************************************************************************************************************************************************************************
            skipping: [ubuntu1]
            skipping: [ubuntu3]
            skipping: [centos1]
            skipping: [centos2]
            skipping: [centos3]
            ASYNC POLL on ubuntu2: jid=315569593684.27013 started=1 finished=0
            ASYNC POLL on ubuntu2: jid=315569593684.27013 started=1 finished=0
            ASYNC POLL on ubuntu2: jid=315569593684.27013 started=1 finished=0
            ASYNC POLL on ubuntu2: jid=315569593684.27013 started=1 finished=0
            ASYNC OK on ubuntu2: jid=315569593684.27013
            changed: [ubuntu2]

            TASK [Task6] ***************************************************************************************************************************************************************************
            skipping: [ubuntu1]
            skipping: [ubuntu2]
            skipping: [centos1]
            skipping: [centos2]
            skipping: [centos3]
            ASYNC POLL on ubuntu3: jid=954528250035.26016 started=1 finished=0
            ASYNC POLL on ubuntu3: jid=954528250035.26016 started=1 finished=0
            ASYNC POLL on ubuntu3: jid=954528250035.26016 started=1 finished=0
            ASYNC POLL on ubuntu3: jid=954528250035.26016 started=1 finished=0
            ASYNC OK on ubuntu3: jid=954528250035.26016
            changed: [ubuntu3]

            PLAY RECAP *****************************************************************************************************************************************************************************
            centos1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
            centos2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
            centos3                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
            ubuntu1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
            ubuntu2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
            ubuntu3                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   



            # we can see the below execution observation 
            - Here the execution will be similar to the earlier one like in the `Improvement 2`
            - here we ar waiting for the all the tasks from all the host executed before we we move on to the next task 
            - also we can see the 5 host are getting skipped and 1 getting executed , but untill that one complete that  execution will not move to the next song 
        
        ```

  - **Improvement3**

  - we can mention the `poll=0` which means `fire the task and forget` and we will not be checking for the status in every `given seconds of time`\
  
  - here also we are changing `one of the sleep value` to `30sec` in here 

  - we can write the `playbook` for this as below  

    ```
      improve3_slow_playbook.yaml
      ---------------------------

      ---
        
      - hosts: linux
      
        tasks:
          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "centos1" # putting the when condition to check against a particular target host rather the all the linux target host

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "centos2" # putting the when condition to check against a particular target host rather the all the linux target host

          - name: Task1
            command: /bin/sleep 30 # making one of task as 30 seconds
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "centos3" # putting the when condition to check against a particular target host rather the all the linux target host

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "ubuntu1" # putting the when condition to check against a particular target host rather the all the linux target host

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll:0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "ubuntu2" # putting the when condition to check against a particular target host rather the all the linux target host

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "ubuntu3" # putting the when condition to check against a particular target host rather the all the linux target host

      ...
       
      when we execute the task using the ansible command as below 
      time ansible-playbook improve3_slow_playbook.yaml


      PLAY [linux] ******************************************************************************************************************************************************************************************

      TASK [Gathering Facts] ********************************************************************************************************************************************************************************
      ok: [ubuntu3]
      ok: [centos3]
      ok: [ubuntu2]
      ok: [centos1]
      ok: [ubuntu1]
      ok: [centos2]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos2]
      skipping: [centos3]
      changed: [centos1]

      TASK [Task2] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos3]
      changed: [centos2]

      TASK [Task3] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos2]
      changed: [centos3]

      TASK [Task4] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos2]
      skipping: [centos3]
      changed: [ubuntu1]

      TASK [Task5] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos2]
      skipping: [centos3]
      changed: [ubuntu2]

      TASK [Task6] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [centos1]
      skipping: [centos2]
      skipping: [centos3]
      changed: [ubuntu3]

      PLAY RECAP ********************************************************************************************************************************************************************************************
      centos1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      centos2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      centos3                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      ubuntu1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      ubuntu2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      ubuntu3                    : ok=2    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   


      real    0m6.397s
      user    0m3.308s
      sys     0m1.400s




      # here we can observe exection as 

      - the task will be going to be get completed soon before the `30sec` time that we have provided 

      - we also can see the `ansible playbook` got executed way before the `30 sec` i.e in `6 sec`
      
      - which suggest that the task are still running on the back ground eventhough the playbook execution ended 
      
      - we can see the background executed task using the command as `ps -ef | grep ssh`

        ps -ef | grep ssh 

        # the output will be in the format as 
        root          48       1  0 Sep21 ?        00:00:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
        ansible   140017       1  0 00:13 ?        00:00:00 ssh: /dev/shm/492fe51149 [mux]
        ansible   140020       1  0 00:13 ?        00:00:00 ssh: /dev/shm/c0b9c19401 [mux]
        ansible   140023       1  0 00:13 ?        00:00:00 ssh: /dev/shm/b86a8a16f1 [mux]
        ansible   140026       1  0 00:13 ?        00:00:00 ssh: /dev/shm/d0b36aa9b1 [mux]
        ansible   140029       1  0 00:13 ?        00:00:00 ssh: /dev/shm/6428c6c94e [mux]
        ansible   140032       1  0 00:13 ?        00:00:00 ssh: /dev/shm/ce10987877 [mux]


      - also we can see that if we wait for the `60 seconds` we can see those task are getting closed and the output will be rediced down as below 

        ps -ef | grep ssh

        # the output will be in the format as 
        # here we can see that all [mux] task got deleted successfully after the background task execution completed 

        root          48       1  0 Sep21 ?        00:00:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
        ansible   140985    1582  0 00:14 pts/0    00:00:00 grep --color=auto ssh

      - this is not a valid approach for getting the content from the task but it is a great way for saving the time
      
      - eventhough the `process on the target host running on background the playbook execution ended`
    
    ```

  - **Improvement4**
  
    - here we can make use of the `register` the `output` that we are getting from each of the `async command` task 
    
    - this `register context` wil contains all the `output` including the `executed output + skipped output`
    
    - we can use the `ansible playbook` as below 
    
      ```
      improve4_slow_playbook.yaml
      ---------------------------

      ---
        
      - hosts: linux
      
        tasks:
          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "centos1" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register1 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "centos2" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register2 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 30 # making one of task as 30 seconds
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "centos3" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register3 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "ubuntu1" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register4 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll:0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "ubuntu2" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register5 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "ubuntu3" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register6 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Debugging one of register using the debug module with var
            debug: # using the debug module in here 
              var: result1 # using the var attribute to define the vars and can't use JINJA2 as its already implicit

          - name: Debugging one of register using the debug module with vmsg with JINJA2 template
            debug: # using the debug module in here 
              msg: "{{result1}}" # with the JINJA2 defining the message in here 

      ...
      
      when we execute the task using the ansible command as below 
      time ansible-playbook improve4_slow_playbook.yaml

      PLAY [linux] ******************************************************************************************************************************************************************************************

      TASK [Gathering Facts] ********************************************************************************************************************************************************************************
      ok: [centos3]
      ok: [centos2]
      ok: [centos1]
      ok: [ubuntu3]
      ok: [ubuntu2]
      ok: [ubuntu1]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos2]
      skipping: [centos3]
      changed: [centos1]

      TASK [Task2] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos3]
      changed: [centos2]

      TASK [Task3] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos2]
      changed: [centos3]

      TASK [Task4] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos2]
      skipping: [centos3]
      changed: [ubuntu1]

      TASK [Task5] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos2]
      skipping: [centos3]
      changed: [ubuntu2]

      TASK [Task6] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [centos1]
      skipping: [centos2]
      skipping: [centos3]
      changed: [ubuntu3]

      TASK [showing value in Debug Mode in vars] ************************************************************************************************************************************************************
      ok: [ubuntu2] => {
          "register1": {
              "changed": false,
              "skip_reason": "Conditional result was False",
              "skipped": true
          }
      }
      ok: [ubuntu1] => {
          "register1": {
              "changed": false,
              "skip_reason": "Conditional result was False",
              "skipped": true
          }
      }
      ok: [ubuntu3] => {
          "register1": {
              "changed": false,
              "skip_reason": "Conditional result was False",
              "skipped": true
          }
      }
      ok: [centos1] => {
          "register1": {
              "ansible_job_id": "877675128130.2594",
              "changed": true,
              "failed": 0,
              "finished": 0,
              "results_file": "/root/.ansible_async/877675128130.2594",
              "started": 1
          }
      }
      ok: [centos2] => {
          "register1": {
              "changed": false,
              "skip_reason": "Conditional result was False",
              "skipped": true
          }
      }
      ok: [centos3] => {
          "register1": {
              "changed": false,
              "skip_reason": "Conditional result was False",
              "skipped": true
          }
      }

      TASK [showing value in Debug Mode in vars] ************************************************************************************************************************************************************
      ok: [ubuntu1] => {
          "msg": {
              "changed": false,
              "skip_reason": "Conditional result was False",
              "skipped": true
          }
      }
      ok: [ubuntu2] => {
          "msg": {
              "changed": false,
              "skip_reason": "Conditional result was False",
              "skipped": true
          }
      }
      ok: [ubuntu3] => {
          "msg": {
              "changed": false,
              "skip_reason": "Conditional result was False",
              "skipped": true
          }
      }
      ok: [centos1] => {
          "msg": {
              "ansible_job_id": "877675128130.2594",
              "changed": true,
              "failed": 0,
              "finished": 0,
              "results_file": "/root/.ansible_async/877675128130.2594",
              "started": 1
          }
      }
      ok: [centos2] => {
          "msg": {
              "changed": false,
              "skip_reason": "Conditional result was False",
              "skipped": true
          }
      }
      ok: [centos3] => {
          "msg": {
              "changed": false,
              "skip_reason": "Conditional result was False",
              "skipped": true
          }
      }

      PLAY RECAP ********************************************************************************************************************************************************************************************
      centos1                    : ok=4    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      centos2                    : ok=4    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      centos3                    : ok=4    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      ubuntu1                    : ok=4    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      ubuntu2                    : ok=4    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      ubuntu3                    : ok=4    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   


      real    0m5.100s
      user    0m3.142s
      sys     0m1.451s


      # these are the observetion :-

      - the `context of the register` can vary `based on whether they are executed or skipped`

      - based on the execution we can see which output that got executed by 

        - start key
        - finished key
        - ansible_job_id key

      - based on this we can also see which of the task which got skipped 

        - skipped: true

      - one more thing to notice in here with respect to the `debug` module

        - when we are using the `msg` parameter we can see the `key as msg` and `value as the value of the register output with executed and skipped task`

        - when we are using the `var` paramter we can see the `key as the regier variable name` and the value is register output with executed and skipped task
      
      - also foir the successfully executed task we can see the key as `ansible_job_id`

      - this actually be `used by the async module as an input` `to fetch the status of the async task`

      - based the JINJA2 templating we can figure out a way to filter which task got exexuted and whats their `ansible_job_id` skipping the skipped task
      
    ``` 

  - **improvement5**
  
    - we can make use of the `JINJA2 templating` to fetch which of the `task got exeuted and which are skipped` and filter the `executed task only to get the ansible_job_id`
    
    - we here keep few things in mind
      
      - when we execute the `task on all the target hosts` all the `executed and skipped result` will going to `stored to the register output`
      
      - we have to use the `JINJA2` filtering in order to get the `successfully executed job and from their we can see the ansible_job_id`
      
      - when we xecute the `debug module with msg or var` it will check for the `expression or variable in every host` 
    
    - hence the pplaybook can be written as below
    
      ```
      improve5_slow_playbook.yaml
      ---------------------------

      ---
        
      - hosts: linux

        vars: # defining the variable section with emty list as the value and variable is jobid
          jobid: [] # specifying the jobid as empty list in here 
      
        tasks:
          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "centos1" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register1 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "centos2" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register2 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 30 # making one of task as 30 seconds
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "centos3" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register3 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "ubuntu1" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register4 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll:0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "ubuntu2" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register5 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "ubuntu3" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register6 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: using setfacts module for filtering ansible_job_id
            set_fact: # using the set_fact module in here 
              jobid: > # derfining the variable name as jobid and using the multiline option in YAML
                     {% if item.ansible_job_id is defined -%} # using the is defined to fetch from all task output(both executed and skipped one) which have the ansible_job_id
                        {{jobid+[item.ansible_job_id]}} # if it exists then adding the value to empty list var that we define in vars section
                      {% else -%} # defining the else condition out in here 
                        {{jobid}} # keping this as the empty list
                      {% endif %}
                      # as a part of the JINJA2  template we are updating the value of the jobid if there is ansible_job_id value else it will still be the same
              with_items: # defining the with_items loop in here with alll the tasks register context which will be for both success and skipped taks
                  - "{{register1}}"
                  - "{{register2}}"
                  - "{{register3}}"
                  - "{{register4}}"
                  - "{{register5}}"
                  - "{{register6}}"

          - name: Debugging with the vars option in here 
            debug: # using the debug module in here 
              var : jobid # here using the var hence the ut put will be as `{"jobid":[<ansible_playbook id that we got from the set_fact for each hosts>]}`
              # fetching the var i.e jobid that we manipulated in JINJA2 for every host

      ...
      
      when we execute the task using the ansible command as below 
      time ansible-playbook improve5_slow_playbook.yaml
      
      PLAY [linux] ******************************************************************************************************************************************************************************************

      TASK [Gathering Facts] ********************************************************************************************************************************************************************************
      ok: [centos3]
      ok: [centos2]
      ok: [centos1]
      ok: [ubuntu3]
      ok: [ubuntu1]
      ok: [ubuntu2]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos2]
      skipping: [centos3]
      changed: [centos1]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos3]
      changed: [centos2]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos2]
      changed: [centos3]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos2]
      skipping: [centos3]
      changed: [ubuntu1]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos2]
      skipping: [centos3]
      changed: [ubuntu2]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [centos1]
      skipping: [centos2]
      skipping: [centos3]
      changed: [ubuntu3]

      TASK [using setfacts module for filtering ansible_job_id] *********************************************************************************************************************************************
      ok: [ubuntu1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '15618120188.8450', 'results_file': '/root/.ansible_async/15618120188.8450', 'changed': True})
      ok: [ubuntu2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '334764957083.6327', 'results_file': '/root/.ansible_async/334764957083.6327', 'changed': True})
      ok: [ubuntu1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '889038112081.7814', 'results_file': '/root/.ansible_async/889038112081.7814', 'changed': True})
      ok: [ubuntu1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '769436816947.7823', 'results_file': '/root/.ansible_async/769436816947.7823', 'changed': True})
      ok: [centos1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '884701433301.6350', 'results_file': '/root/.ansible_async/884701433301.6350', 'changed': True})
      ok: [centos2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '144102151981.6511', 'results_file': '/root/.ansible_async/144102151981.6511', 'changed': True})
      ok: [centos3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})

      TASK [debug] ******************************************************************************************************************************************************************************************
      ok: [ubuntu1] => {
          "jobid": [
              "15618120188.8450"
          ]
      }
      ok: [ubuntu2] => {
          "jobid": [
              "889038112081.7814"
          ]
      }
      ok: [ubuntu3] => {
          "jobid": [
              "769436816947.7823"
          ]
      }
      ok: [centos1] => {
          "jobid": [
              "334764957083.6327"
          ]
      }
      ok: [centos2] => {
          "jobid": [
              "884701433301.6350"
          ]
      }
      ok: [centos3] => {
          "jobid": [
              "144102151981.6511"
          ]
      }

      PLAY RECAP ********************************************************************************************************************************************************************************************
      centos1                    : ok=4    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      centos2                    : ok=4    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      centos3                    : ok=4    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      ubuntu1                    : ok=4    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      ubuntu2                    : ok=4    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      ubuntu3                    : ok=4    changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   


      real    0m5.336s
      user    0m3.717s
      sys     0m1.614s
      
      
    # here are few observation 
  
    - if we are executing this then we will be getting the `ansible_job_id` for every host as everyhost only executed once with the sleep because of the when condition

    - we can also achieve the same using the register in the `set_facts` module and doing the `iteration` over the `register context output`

    - also we got the all the `background process` thats been running on `all the target hosts` even after the `playbook execution got completed`

      
    ```        

  - **implement6**

    - as we have the `ansible_job_id for all the target host background process` hence we can reutilize this to wait for the `background task` to be completed 
    
    - for this we can make use of the `async_status` `module of the ansible` to get the `status by providing the ansible_job_id`
    
    - using the `async_jb_id` in the `async_status` mdoule we can make sure to `stop the background task before the plybook execution` 
    
    - here is a playbook for the same which been described here 

      
      ```
      improve6_slow_playbook.yaml
      ---------------------------

      ---
        
      - hosts: linux

        vars: # defining the variable section with emty list as the value and variable is jobid
          jobid: []
      
        tasks:
          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "centos1" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register1 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "centos2" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register2 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 30 # making one of task as 30 seconds
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "centos3" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register3 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "ubuntu1" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register4 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll:0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "ubuntu2" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register5 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            when: ansible_hostname == "ubuntu3" # putting the when condition to check against a particular target host rather the all the linux target host
            register: register6 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: using setfacts module for filtering ansible_job_id
            set_fact: # using the set_fact module in here 
              jobid: > # derfining the variable name as jobid and using the multiline option in YAML
                     {% if item.ansible_job_id is defined -%} # using the is defined to fetch from all task output(both executed and skipped one) which have the ansible_job_id
                        {{jobid+[item.ansible_job_id]}} # if it exists then adding the value to empty list var that we define in vars section
                      {% else -%} # defining the else condition out in here 
                        {{jobid}} # keping this as the empty list
                      {% endif %}
                      # as a part of the JINJA2  template we are updating the value of the jobid if there is ansible_job_id value else it will still be the same
              with_items: # defining the with_items loop in here with alll the tasks register context which will be for both success and skipped taks
                  - "{{register1}}"
                  - "{{register2}}"
                  - "{{register3}}"
                  - "{{register4}}"
                  - "{{register5}}"
                  - "{{register6}}"

          - name: Debugging with the vars option in here 
            debug: # using the debug module in here 
              var : jobid # here using the var hence the ut put will be as `{"jobid":[<ansible_playbook id that we got from the set_fact for each hosts>]}`
              # fetching the var i.e jobid that we manipulated in JINJA2 for every host

          - name: Stopping the async task by using the anisble_job_id with the async_status module 
            async_status: # using the async status_module
              jid: "{{item}}" # here we are using the item which been provided with with_item
              mode: status # using the mode status we can get the status of the task 
            with_items: # using the with_items loop in here 
              - "{{jobid}}" # here we are checking in each host the jobid variable value and providing it as loop
            register: result_output # result context for the application 
            until: result_output.finished # untill the task got finished 
            retries: 30 # using the 30 retries in this case



      ...

      when we execute the task using the ansible command as below 
      time ansible-playbook improve6_slow_playbook.yaml
      
      
      PLAY [linux] ******************************************************************************************************************************************************************************************

      TASK [Gathering Facts] ********************************************************************************************************************************************************************************
      ok: [centos2]
      ok: [centos3]
      ok: [centos1]
      ok: [ubuntu2]
      ok: [ubuntu3]
      ok: [ubuntu1]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos2]
      skipping: [centos3]
      changed: [centos1]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos3]
      changed: [centos2]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos2]
      changed: [centos3]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos2]
      skipping: [centos3]
      changed: [ubuntu1]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu3]
      skipping: [centos1]
      skipping: [centos2]
      skipping: [centos3]
      changed: [ubuntu2]

      TASK [Task1] ******************************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [centos1]
      skipping: [centos2]
      skipping: [centos3]
      changed: [ubuntu3]

      TASK [using setfacts module for filtering ansible_job_id] *********************************************************************************************************************************************
      ok: [ubuntu1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '841960704087.8820', 'results_file': '/root/.ansible_async/841960704087.8820', 'changed': True})
      ok: [ubuntu3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '642689405155.6628', 'results_file': '/root/.ansible_async/642689405155.6628', 'changed': True})
      ok: [ubuntu3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '150673525066.8168', 'results_file': '/root/.ansible_async/150673525066.8168', 'changed': True})
      ok: [centos1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [ubuntu3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '293191509068.8177', 'results_file': '/root/.ansible_async/293191509068.8177', 'changed': True})
      ok: [centos1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '866338237752.6651', 'results_file': '/root/.ansible_async/866338237752.6651', 'changed': True})
      ok: [centos1] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '318139552926.6844', 'results_file': '/root/.ansible_async/318139552926.6844', 'changed': True})
      ok: [centos2] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})
      ok: [centos3] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False'})

      TASK [debug] ******************************************************************************************************************************************************************************************
      ok: [ubuntu1] => {
          "jobid": [
              "841960704087.8820"
          ]
      }
      ok: [ubuntu2] => {
          "jobid": [
              "150673525066.8168"
          ]
      }
      ok: [ubuntu3] => {
          "jobid": [
              "293191509068.8177"
          ]
      }
      ok: [centos1] => {
          "jobid": [
              "642689405155.6628"
          ]
      }
      ok: [centos2] => {
          "jobid": [
              "866338237752.6651"
          ]
      }
      ok: [centos3] => {
          "jobid": [
              "318139552926.6844"
          ]
      }

      TASK [Stopping the async task by using the anisble_job_id with the async_status module] ***************************************************************************************************************
      FAILED - RETRYING: [centos3]: Stopping the async task by using the anisble_job_id with the async_status module (30 retries left).
      FAILED - RETRYING: [centos2]: Stopping the async task by using the anisble_job_id with the async_status module (30 retries left).
      FAILED - RETRYING: [centos1]: Stopping the async task by using the anisble_job_id with the async_status module (30 retries left).
      FAILED - RETRYING: [ubuntu2]: Stopping the async task by using the anisble_job_id with the async_status module (30 retries left).
      FAILED - RETRYING: [ubuntu3]: Stopping the async task by using the anisble_job_id with the async_status module (30 retries left).
      FAILED - RETRYING: [ubuntu1]: Stopping the async task by using the anisble_job_id with the async_status module (30 retries left).
      FAILED - RETRYING: [centos3]: Stopping the async task by using the anisble_job_id with the async_status module (29 retries left).
      changed: [centos2] => (item=866338237752.6651)
      changed: [centos1] => (item=642689405155.6628)
      changed: [ubuntu2] => (item=150673525066.8168)
      changed: [ubuntu3] => (item=293191509068.8177)
      changed: [ubuntu1] => (item=841960704087.8820)
      changed: [centos3] => (item=318139552926.6844)

      PLAY RECAP ********************************************************************************************************************************************************************************************
      centos1                    : ok=5    changed=2    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      centos2                    : ok=5    changed=2    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      centos3                    : ok=5    changed=2    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      ubuntu1                    : ok=5    changed=2    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      ubuntu2                    : ok=5    changed=2    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
      ubuntu3                    : ok=5    changed=2    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   


      real    0m15.778s
      user    0m4.870s
      sys     0m2.107s
            
      # here are few of the observation 

      - we can see that at the end as we have captured the `ansible_job_id` using which we are trying to get the `process id of the background task`

      - in this particular way we can see the task where the  `sleep 5` will be waiting to be completed as then the `sleep 30sec task` will be completed 

      - here we are using the `async_status` module to `wait for the background task to be completed before finidhing the playbook execution`

      - also we are instructing to provide the `retires of 30`

      - also we will be using the `<regiter_output_variable>.finished` to check whether the task been completed from the background process then only we can close the playbook

      
      ```

  - **improvement7**
  
    - now insted of running for `each task on specific target by the use of when` we can ignore that to see the `overall benifit`
    
    - as we have proided the `when` condition hene it is going to be get executed on the `matched target host` while `skipping the others` 
    
    - here we are ignoing the `when condition provided in each taks` so that `task can be performed in all the hosts rather than the dedicted one`

    - the ansible playbook for the same will be as 

      ```
      improve7_slow_playbook.yaml
      ---------------------------

      ---
        
      - hosts: linux

        vars: # defining the variable section with emty list as the value and variable is jobid
          jobid: []
      
        tasks:
          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            register: register1 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            register: register2 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 30 # making one of task as 30 seconds
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            register: register3 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            register: register4 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll:0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            register: register5 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: Task1
            command: /bin/sleep 5
            async: 10 # here we are asking the at least  wait for 10s for executionn else the ssh timeout and ssh close connection will occure
            poll: 0 # here we are making the poll value as 0 which means fire and forget and don't check for status of the task 
            register: register6 # definingg the register 1 which will collect the executed as well as the skipped output

          - name: using setfacts module for filtering ansible_job_id
            set_fact: # using the set_fact module in here 
              jobid: > # derfining the variable name as jobid and using the multiline option in YAML
                     {% if item.ansible_job_id is defined -%} # using the is defined to fetch from all task output(both executed and skipped one) which have the ansible_job_id
                        {{jobid+[item.ansible_job_id]}} # if it exists then adding the value to empty list var that we define in vars section
                      {% else -%} # defining the else condition out in here 
                        {{jobid}} # keping this as the empty list
                      {% endif %}
                      # as a part of the JINJA2  template we are updating the value of the jobid if there is ansible_job_id value else it will still be the same
              with_items: # defining the with_items loop in here with alll the tasks register context which will be for both success and skipped taks
                  - "{{register1}}"
                  - "{{register2}}"
                  - "{{register3}}"
                  - "{{register4}}"
                  - "{{register5}}"
                  - "{{register6}}"

          - name: Debugging with the vars option in here 
            debug: # using the debug module in here 
              var : jobid # here using the var hence the ut put will be as `{"jobid":[<ansible_playbook id that we got from the set_fact for each hosts>]}`
              # fetching the var i.e jobid that we manipulated in JINJA2 for every host

          - name: Stopping the async task by using the anisble_job_id with the async_status module 
            async_status: # using the async status_module
              jid: "{{item}}" # here we are using the item which been provided with with_item
              mode: status # using the mode status we can get the status of the task 
            with_items: # using the with_items loop in here 
              - "{{jobid}}" # here we are checking in each host the jobid variable value and providing it as loop
            register: result_output # result context for the application 
            until: result_output.finished # untill the task got finished 
            retries: 30 # using the 30 retries in this case
        
        ...

        when we execute the task using the ansible command as below 
        time ansible-playbook improve6_slow_playbook.yaml



          PLAY [linux] ******************************************************************************************************************************************************************************************

          TASK [Gathering Facts] ********************************************************************************************************************************************************************************
          ok: [centos2]
          ok: [centos1]
          ok: [centos3]
          ok: [ubuntu2]
          ok: [ubuntu1]
          ok: [ubuntu3]

          TASK [Task1] ******************************************************************************************************************************************************************************************
          changed: [centos3]
          changed: [centos2]
          changed: [centos1]
          changed: [ubuntu3]
          changed: [ubuntu1]
          changed: [ubuntu2]

          TASK [Task1] ******************************************************************************************************************************************************************************************
          changed: [centos1]
          changed: [centos2]
          changed: [ubuntu3]
          changed: [ubuntu2]
          changed: [ubuntu1]
          changed: [centos3]

          TASK [Task1] ******************************************************************************************************************************************************************************************
          changed: [centos1]
          changed: [centos2]
          changed: [centos3]
          changed: [ubuntu1]
          changed: [ubuntu2]
          changed: [ubuntu3]

          TASK [Task1] ******************************************************************************************************************************************************************************************
          changed: [centos3]
          changed: [centos2]
          changed: [centos1]
          changed: [ubuntu2]
          changed: [ubuntu1]
          changed: [ubuntu3]

          TASK [Task1] ******************************************************************************************************************************************************************************************
          changed: [ubuntu1]
          changed: [centos2]
          changed: [centos3]
          changed: [ubuntu2]
          changed: [centos1]
          changed: [ubuntu3]

          TASK [Task1] ******************************************************************************************************************************************************************************************
          changed: [centos2]
          changed: [centos1]
          changed: [ubuntu1]
          changed: [centos3]
          changed: [ubuntu3]
          changed: [ubuntu2]

          TASK [using setfacts module for filtering ansible_job_id] *********************************************************************************************************************************************
          ok: [ubuntu2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '58060512296.8724', 'results_file': '/root/.ansible_async/58060512296.8724', 'changed': True})
          ok: [ubuntu3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '892424771308.8733', 'results_file': '/root/.ansible_async/892424771308.8733', 'changed': True})
          ok: [centos1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '785975650396.7047', 'results_file': '/root/.ansible_async/785975650396.7047', 'changed': True})
          ok: [ubuntu1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '612731375305.9392', 'results_file': '/root/.ansible_async/612731375305.9392', 'changed': True})
          ok: [ubuntu2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '787740371857.8751', 'results_file': '/root/.ansible_async/787740371857.8751', 'changed': True})
          ok: [centos1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '661436571381.7067', 'results_file': '/root/.ansible_async/661436571381.7067', 'changed': True})
          ok: [ubuntu1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '167254388720.9419', 'results_file': '/root/.ansible_async/167254388720.9419', 'changed': True})
          ok: [centos3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '604239228925.7279', 'results_file': '/root/.ansible_async/604239228925.7279', 'changed': True})
          ok: [ubuntu3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '13985695581.8760', 'results_file': '/root/.ansible_async/13985695581.8760', 'changed': True})
          ok: [ubuntu2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '598519498481.8778', 'results_file': '/root/.ansible_async/598519498481.8778', 'changed': True})
          ok: [centos2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '839045723092.7070', 'results_file': '/root/.ansible_async/839045723092.7070', 'changed': True})
          ok: [centos1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '122687666481.7087', 'results_file': '/root/.ansible_async/122687666481.7087', 'changed': True})
          ok: [ubuntu1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '565624729188.9446', 'results_file': '/root/.ansible_async/565624729188.9446', 'changed': True})
          ok: [centos3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '563807970079.7299', 'results_file': '/root/.ansible_async/563807970079.7299', 'changed': True})
          ok: [ubuntu3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '32325783391.8787', 'results_file': '/root/.ansible_async/32325783391.8787', 'changed': True})
          ok: [ubuntu2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '708493019379.8805', 'results_file': '/root/.ansible_async/708493019379.8805', 'changed': True})
          ok: [ubuntu1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '989430653563.9473', 'results_file': '/root/.ansible_async/989430653563.9473', 'changed': True})
          ok: [centos2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '747878637359.7090', 'results_file': '/root/.ansible_async/747878637359.7090', 'changed': True})
          ok: [centos1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '289492893106.7107', 'results_file': '/root/.ansible_async/289492893106.7107', 'changed': True})
          ok: [ubuntu2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '651193494153.8832', 'results_file': '/root/.ansible_async/651193494153.8832', 'changed': True})
          ok: [centos1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '132493479713.7127', 'results_file': '/root/.ansible_async/132493479713.7127', 'changed': True})
          ok: [ubuntu3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '195821310010.8814', 'results_file': '/root/.ansible_async/195821310010.8814', 'changed': True})
          ok: [centos3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '774604623777.7319', 'results_file': '/root/.ansible_async/774604623777.7319', 'changed': True})
          ok: [centos1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '670201636179.7147', 'results_file': '/root/.ansible_async/670201636179.7147', 'changed': True})
          ok: [centos2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '905568530717.7110', 'results_file': '/root/.ansible_async/905568530717.7110', 'changed': True})
          ok: [centos3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '806434153420.7339', 'results_file': '/root/.ansible_async/806434153420.7339', 'changed': True})
          ok: [ubuntu1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '100468801300.9500', 'results_file': '/root/.ansible_async/100468801300.9500', 'changed': True})
          ok: [centos2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '668702080136.7130', 'results_file': '/root/.ansible_async/668702080136.7130', 'changed': True})
          ok: [ubuntu2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '733350927249.8859', 'results_file': '/root/.ansible_async/733350927249.8859', 'changed': True})
          ok: [ubuntu3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '366122355289.8841', 'results_file': '/root/.ansible_async/366122355289.8841', 'changed': True})
          ok: [ubuntu1] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '476545157455.9527', 'results_file': '/root/.ansible_async/476545157455.9527', 'changed': True})
          ok: [centos2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '700788246853.7150', 'results_file': '/root/.ansible_async/700788246853.7150', 'changed': True})
          ok: [centos3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '291258894091.7359', 'results_file': '/root/.ansible_async/291258894091.7359', 'changed': True})
          ok: [ubuntu3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '518938542398.8868', 'results_file': '/root/.ansible_async/518938542398.8868', 'changed': True})
          ok: [centos3] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '84355154551.7379', 'results_file': '/root/.ansible_async/84355154551.7379', 'changed': True})
          ok: [centos2] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '899801870126.7170', 'results_file': '/root/.ansible_async/899801870126.7170', 'changed': True})

          TASK [debug] ******************************************************************************************************************************************************************************************
          ok: [ubuntu1] => {
              "jobid": [
                  "612731375305.9392",
                  "167254388720.9419",
                  "565624729188.9446",
                  "989430653563.9473",
                  "100468801300.9500",
                  "476545157455.9527"
              ]
          }
          ok: [ubuntu2] => {
              "jobid": [
                  "58060512296.8724",
                  "787740371857.8751",
                  "598519498481.8778",
                  "708493019379.8805",
                  "651193494153.8832",
                  "733350927249.8859"
              ]
          }
          ok: [ubuntu3] => {
              "jobid": [
                  "892424771308.8733",
                  "13985695581.8760",
                  "32325783391.8787",
                  "195821310010.8814",
                  "366122355289.8841",
                  "518938542398.8868"
              ]
          }
          ok: [centos1] => {
              "jobid": [
                  "785975650396.7047",
                  "661436571381.7067",
                  "122687666481.7087",
                  "289492893106.7107",
                  "132493479713.7127",
                  "670201636179.7147"
              ]
          }
          ok: [centos2] => {
              "jobid": [
                  "839045723092.7070",
                  "747878637359.7090",
                  "905568530717.7110",
                  "668702080136.7130",
                  "700788246853.7150",
                  "899801870126.7170"
              ]
          }
          ok: [centos3] => {
              "jobid": [
                  "604239228925.7279",
                  "563807970079.7299",
                  "774604623777.7319",
                  "806434153420.7339",
                  "291258894091.7359",
                  "84355154551.7379"
              ]
          }

          TASK [Stopping the async task by using the anisble_job_id with the async_status module] ***************************************************************************************************************
          FAILED - RETRYING: [centos3]: Stopping the async task by using the anisble_job_id with the async_status module (30 retries left).
          FAILED - RETRYING: [centos2]: Stopping the async task by using the anisble_job_id with the async_status module (30 retries left).
          FAILED - RETRYING: [centos1]: Stopping the async task by using the anisble_job_id with the async_status module (30 retries left).
          FAILED - RETRYING: [ubuntu3]: Stopping the async task by using the anisble_job_id with the async_status module (30 retries left).
          FAILED - RETRYING: [ubuntu2]: Stopping the async task by using the anisble_job_id with the async_status module (30 retries left).
          FAILED - RETRYING: [ubuntu1]: Stopping the async task by using the anisble_job_id with the async_status module (30 retries left).
          changed: [centos3] => (item=604239228925.7279)
          changed: [centos2] => (item=839045723092.7070)
          changed: [centos1] => (item=785975650396.7047)
          changed: [ubuntu3] => (item=892424771308.8733)
          changed: [ubuntu2] => (item=58060512296.8724)
          changed: [ubuntu1] => (item=612731375305.9392)
          changed: [centos3] => (item=563807970079.7299)
          changed: [centos2] => (item=747878637359.7090)
          changed: [centos1] => (item=661436571381.7067)
          changed: [ubuntu3] => (item=13985695581.8760)
          changed: [ubuntu2] => (item=787740371857.8751)
          changed: [ubuntu1] => (item=167254388720.9419)
          changed: [centos3] => (item=774604623777.7319)
          changed: [centos2] => (item=905568530717.7110)
          changed: [centos1] => (item=122687666481.7087)
          changed: [ubuntu3] => (item=32325783391.8787)
          changed: [ubuntu1] => (item=565624729188.9446)
          changed: [ubuntu2] => (item=598519498481.8778)
          changed: [centos3] => (item=806434153420.7339)
          changed: [centos1] => (item=289492893106.7107)
          changed: [centos2] => (item=668702080136.7130)
          changed: [ubuntu3] => (item=195821310010.8814)
          changed: [ubuntu1] => (item=989430653563.9473)
          changed: [centos2] => (item=700788246853.7150)
          changed: [centos3] => (item=291258894091.7359)
          changed: [centos1] => (item=132493479713.7127)
          changed: [ubuntu2] => (item=708493019379.8805)
          changed: [ubuntu3] => (item=366122355289.8841)
          changed: [centos2] => (item=899801870126.7170)
          changed: [centos3] => (item=84355154551.7379)
          changed: [centos1] => (item=670201636179.7147)
          changed: [ubuntu1] => (item=100468801300.9500)
          changed: [ubuntu2] => (item=651193494153.8832)
          changed: [ubuntu3] => (item=518938542398.8868)
          changed: [ubuntu1] => (item=476545157455.9527)
          changed: [ubuntu2] => (item=733350927249.8859)

          PLAY RECAP ********************************************************************************************************************************************************************************************
          centos1                    : ok=10   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
          centos2                    : ok=10   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
          centos3                    : ok=10   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
          ubuntu1                    : ok=10   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
          ubuntu2                    : ok=10   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
          ubuntu3                    : ok=10   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


          real    0m14.900s
          user    0m8.654s
          sys     0m4.530s


        # here are few observation 

        - here `all the task` will be performed against `all the host` rather than the `dedicated host`

        - but we can still see that the `first 5 task` executed at  first thenn waiting for the next one to be completed beofre moving on 

        - thi is because of  `5 form priniciple` we will be discussing next 

        - once `all the background task for completed` then only we can see the `playbook execution`   
      
      
      ```

  - **Improvement8**
    
    - `ansible` has `multiple starterfy` which is benifial for the `execution of the ansible playbook `

    - by default `ansible` work on the `5 forks` hence we will see that the first `5 host task to sleep for 5 sec` will be exeecuted first then it will will got for the `6th host` to `sleep for 5 more seconds` before going to the `next scheduled task`
    
    - hence we are waiting for the `10 seconds` as we are running `6 hosts` for a `particular task to be executed on all host` before going to the `next scheduled tasks`
    
    - due to this `5 forks principle` the `the first 5 host will sleep for 5 sec` and `6th one will sleep gain for next 5 sec` which constitute `10 sec of waiting time for the task in all host`
    
    - we can also increase the `fors value` in the `ansible.cfg` file as below 

      ```
        ansible.cfg
        -----------
        [defauls]
        inventory=host
        host_key_checking=False
        jinja2_extensions=jinja2.ext.loopcontrols
        forks=6 # which can execute the same task accross all the 6 different host  which was 5 (by default)
      
      ```
    
    - now if we run the `same playbook` again we can see that `it wwill not going to wait for the last one while executing the first 5` rather `all 6 host will execute the task simulteniously`
  
- **serial Execution**

  - **case1**

  - we can also `distribute host` into `batches` and `execute the task` using the `serial execution`

  - here this will be benifical for the `rolling update in the batch of system` here the `target host will be devided into the batches of target host ` and execute the task 

  - we need to define the `serial=<no of targethost at a time>` in the `hosts section of the playbook`
  
  - when we mention the `serial wth the corresponding value` then we can see that `at a time mentioned number of target host are beein working`

  - here is a playbook example for the same 

    ```

      serial-playbook.yaml
      ------------------

        ---
        
        - hosts: linux #using the linux host in here 
          gather_facts: False # using the gather_facts as False it will not show the fcts
          serial: 2 # dividing the task into the batches of 2

          tasks:
            - name: Task1
              command: /bin/sleep 5
  
            - name: Task2
              command: /bin/sleep 5
  
            - name: Task3
              command: /bin/sleep 5
  
            - name: Task4
              command: /bin/sleep 5
  
            - name: Task5
              command: /bin/sleep 5

        ...
        # the output for the serial execution will be as below 
        time ansible-playbook serial-playbook.yaml

        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Task1] ******************************************************************************************************************************************************************************************
        changed: [ubuntu2]
        changed: [ubuntu1]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]
        changed: [ubuntu2]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [ubuntu2]
        changed: [ubuntu1]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [ubuntu2]
        changed: [ubuntu1]

        TASK [Task5] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]
        changed: [ubuntu2]

        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Task1] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [ubuntu3]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [ubuntu3]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [ubuntu3]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [ubuntu3]

        TASK [Task5] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [ubuntu3]

        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Task1] ******************************************************************************************************************************************************************************************
        changed: [centos2]
        changed: [centos3]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [centos2]
        changed: [centos3]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [centos3]
        changed: [centos2]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [centos2]
        changed: [centos3]

        TASK [Task5] ******************************************************************************************************************************************************************************************
        changed: [centos2]
        changed: [centos3]

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


        real    0m21.173s
        user    0m3.269s
        sys     0m1.658s
  
  
      # here we can see that  the `target host been devided into the batches` and start executing the task defined in order 

  
    ```

  -**case2**
  
  - we can also provide the `list of serial as list expression` we can provide that in the `incremeental order`
  
  - hence for the `each time while selecting the batch of target host` based on the `specified number the target host will be picked up`
  
  - if it in increasing order then `1 st time batch of target host` will be less but as it in increasing order the `next time more target host` can be picked up

  - here is a playbook example for reference 
    
    
    ```
    
      serial-playbook.yaml
      ------------------

        ---
        
        - hosts: linux #using the linux host in here 
          gather_facts: False # using the gather_facts as False it will not show the fcts
          serial :
            - 1
            - 2
            - 3

          tasks:
            - name: Task1
              command: /bin/sleep 5
  
            - name: Task2
              command: /bin/sleep 5
  
            - name: Task3
              command: /bin/sleep 5
  
            - name: Task4
              command: /bin/sleep 5
  
            - name: Task5
              command: /bin/sleep 5

            - name: Task6
              command: /bin/sleep 5

        ...
        
        # the output for the serial execution will be as below 
        time ansible-playbook serial-playbook.yaml


        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Task1] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]

        TASK [Task5] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]

        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Task1] ******************************************************************************************************************************************************************************************
        changed: [ubuntu3]
        changed: [ubuntu2]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [ubuntu2]
        changed: [ubuntu3]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [ubuntu2]
        changed: [ubuntu3]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [ubuntu2]
        changed: [ubuntu3]

        TASK [Task5] ******************************************************************************************************************************************************************************************
        changed: [ubuntu2]
        changed: [ubuntu3]

        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Task1] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [centos2]
        changed: [centos3]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [centos2]
        changed: [centos3]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [centos3]
        changed: [centos2]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [centos2]
        changed: [centos1]
        changed: [centos3]

        TASK [Task5] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [centos2]
        changed: [centos3]

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


        real    1m21.650s
        user    0m6.789s
        sys     0m2.485s

        # here are few observation 
        
        - as we have provided first as 1 hence on the 1 st attempt 1 target host will be picked up as batch 

        - on the next attempt as it is 2 hence it will picked up 2 target host and similarly on the 3d run picked 3 target host as batch 

        - here on the `first batch` we are `executing against one host` and `2nd btch we are executing against the 2 host` and on the `3rd batch` we are executing against `3 hosts`
    
    
    ```
  - **case3**
  
  - we can also mention the `percentage value as list inside the serial derivative`

  - based on the `percentage value the no of target host wil be picked as batch`

  - tthis will be benifial if we are working on the `large number of target host` or we are executing `variance number of target host which can be changed in future`

  - hence we can execute the task as below 

    ```
      serial-playbook.yaml
      ------------------

        ---
        
        - hosts: linux #using the linux host in here 
          gather_facts: False # using the gather_facts as False it will not show the fcts
          serial : # here mentioning the serial as the percentage value 
            - 15%
            - 35%
            - 50%

          tasks:
            - name: Task1
              command: /bin/sleep 5
  
            - name: Task2
              command: /bin/sleep 5
  
            - name: Task3
              command: /bin/sleep 5
  
            - name: Task4
              command: /bin/sleep 5
  
            - name: Task5
              command: /bin/sleep 5

            - name: Task6
              command: /bin/sleep 5

        ...
        
        # the output for the serial execution will be as below 
        time ansible-playbook serial-playbook.yaml

        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Task1] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]

        TASK [Task5] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]

        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Task1] ******************************************************************************************************************************************************************************************
        changed: [ubuntu3]
        changed: [ubuntu2]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [ubuntu2]
        changed: [ubuntu3]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [ubuntu2]
        changed: [ubuntu3]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [ubuntu2]
        changed: [ubuntu3]

        TASK [Task5] ******************************************************************************************************************************************************************************************
        changed: [ubuntu2]
        changed: [ubuntu3]

        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Task1] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [centos2]
        changed: [centos3]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [centos2]
        changed: [centos3]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [centos3]
        changed: [centos2]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [centos2]
        changed: [centos1]
        changed: [centos3]

        TASK [Task5] ******************************************************************************************************************************************************************************************
        changed: [centos1]
        changed: [centos2]
        changed: [centos3]

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


        real    1m21.650s
        user    0m6.789s
        sys     0m2.485s

        # it will have the same observation as preveious one
  
    
    ```

- **Ansible Free startergy to support the Parallel execution**

- the `defult statergy of ansible is linear statergy`

- in this  statergy `until the same task been executed on all host` the process will not move to the `next set of futute task`

- but in the latest version we can change the `statergy` to `free statergy`

- in this particular statergy ` all the task will broken up and execute in different different hosts independently as free way`

- we need to define the `statergy` keyword in the `hosts section` to define the `free statergy` as `statergy:free`

-  the ansible playbook for the same can be written as below 

  ```
  
    statergy-playbook.yaml
    ------------------

        ---
        
        - hosts: linux #using the linux host in here 
          gather_facts: False # using the gather_facts as False it will not show the fcts
          strategy: free # defining the free strategy here

          tasks:
            - name: Task1
              command: /bin/sleep {{3 |  random }} # using the random JINJA2 template
  
            - name: Task2
              command: /bin/sleep {{3 |  random }} # using the random JINJA2 template
  
            - name: Task3
              command: /bin/sleep {{3 |  random }} # using the random JINJA2 template
  
            - name: Task4
              command: /bin/sleep {{3 |  random }} # using the random JINJA2 template
  
            - name: Task5
              command: /bin/sleep {{3 |  random }} # using the random JINJA2 template

            - name: Task6
              command: /bin/sleep {{3 |  random }} # using the random JINJA2 template

        ...
        
        # the output for the serial execution will be as below 
        time ansible-playbook statergy-playbook.yaml


        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Task1] ******************************************************************************************************************************************************************************************
        changed: [centos2]
        changed: [centos1]
        changed: [ubuntu3]
        changed: [ubuntu1]
        changed: [ubuntu2]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [centos2]
        changed: [centos1]

        TASK [Task1] ******************************************************************************************************************************************************************************************
        changed: [centos3]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [ubuntu3]
        changed: [ubuntu1]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [centos2]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [ubuntu2]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [centos1]

        TASK [Task2] ******************************************************************************************************************************************************************************************
        changed: [centos3]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [ubuntu3]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [centos2]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [centos1]

        TASK [Task3] ******************************************************************************************************************************************************************************************
        changed: [ubuntu2]
        changed: [centos3]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [ubuntu3]

        TASK [Task5] ******************************************************************************************************************************************************************************************
        changed: [centos2]
        changed: [centos1]

        TASK [Task4] ******************************************************************************************************************************************************************************************
        changed: [ubuntu1]
        changed: [ubuntu2]
        changed: [centos3]

        TASK [Task5] ******************************************************************************************************************************************************************************************
        changed: [ubuntu3]
        changed: [ubuntu1]
        changed: [ubuntu2]
        changed: [centos3]

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=5    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

         
         # here we can see the below observtion 
         ---------------------------------------

        - all the task will be broken in multiple parts and executed in different different hosts

        - the default statergy of the ansible been overidden hence we are not we can execute the `task even though the same task is not completed in all the hosts`

        - as per the default statergy of ansible  `until the same task been executed on all host` the process will not move to the `next set of futute task` which is now being overridden

        - make sure not to provide the `forks=6 in ansible.cfg` as it can accomodate 6 will not work as expected provide default which is of 5 
  
  ```
