# <ins> Task Delegation </ins> #

- how to `deletgate` `specific task` to be `executed on` `specific target`

- with `task delegation` , we may have the `requirement`  to run `specific command or tasks` on `either on ansible control host or specific hosts`

- in here we will `use the ansibe_facts` i.e `derived from the target host` and will `assign` this `collected info` to a `specific host` , so that `it i.e specific  target host  can open the TCP wrapper rules accordingly`

- we will also restrict the `ssh access` so that we can work on below `target hosts`
  
  - `ubuntu-c`

  - `centos1`

  - `ubuntu1`  

- here we will be getting the `ansible facts` from the `ubuntu3 target` and with the use of `TCP Wrapper` we will restrict the `ssh access` so that only `ssh` apart from

  - `ubuntu-c`

  - `centos1`

  - `ubuntu1`  

- **Case1**
    
    - here we have the `3 plays` inside the `playbook.yaml file`
    
    - here we want to create a `dedicate SSH key pair ` using which we can connect the `ubuntu3 target host connection`  as the `first play of the playbook`
    
    - as we are creating the `dedicated ssh key pair` then we can `use that ro connect to target ubuntu3 target hosts`
    
    - here for the `first play` we are using the `ubuntu-c` which is the `ansible control host` which will generate the `ssh key pair locally` using the `openssh_keypair`  ansible module
    
    - on the `next play` we are `copying the newly generated ssh key pair` to all the `child target group host individual the linux target group`

    - here while copying we can mention the `2 things` along with the `src` and `dest` path i.e
      
      - `owner:<corresponding owner of the ssh key pair file>`
  
      - we also have to define the  `mode` for the `file` on the `remote server/ target host` once the `copy oeration been competed`  
    
    - we can use the `with_together` or `with_subelements` loop to `set the owner  and set the mode of the file`
    
    - for the `private key` we are using the mnode as `0600` i.e `-rw-------`
    
    - for the `public key with .pub extension` we are using the `permission of 0644` which is as `-rw-r--r--` 

    - in the `third part of the play` we are using the `authorized_key` module to `provision the root user` to the `authorized key` which will help in adding the `passwordless ssh authentication`

    - the `third part of the play` in the `playbook` we are running against the `ubuntu3 target user`
    
    - here basically the `copied public key` we are adding to the `users authorized key` for `passwordless ssh authentication` ,, for this we are using the `authorized_key` module
    
    - the `user will be remain the same where we perform the copy where we defined the owner` and the `same user authorized_key` we are adding the `usrs public key that we copied`   

    - we can write the `playbook` for the same as below 

        ```
            delegate_playbook.yaml
            ----------------------

            ---

            - hosts: ubuntu-c # here we are targeting the ubuntu-c ansible control hosts
              
              tasks:
              - name : Generating a SSH Key pair using the openssh_keypair module 
                openssh_keypair: # using the openssh_keypair module in here 
                    path: ~/.ssh/ubuntu3-id-rsa # generating both the private and publick key withis the name mentioned in path 

            
            # another play over here
            - hosts: linux # targeting the linux target host in here 
              tasks:
              - name: Copying the ssh keypair  to the target host in the same folder 
                copy: # using the  copy module in here 
                    owner: root # here specifying the owner for the same which has the access to the privat eand public keypair
                    src:"{{item.0}}"
                    dest:"{{item.0}}"
                    mode:"{{item.1}}"
                with_together: # using the with_together loop in  here which will be taking the set of pair as mentioned in the list
                    - [~/.ssh/ubuntu3-id-rsa, ~/.ssh/ubuntu3-id-rsa.pub ]
                    - ["0600","0644"]


            # now here we are defining another play in here as 
            - hosts: ubuntu3 #using the ubuntu3 host here
              tasks:
              - name: accessing the public key and adding to the authorized_keys folder using authorized_key module for the root user
                authorized_key:
                    user: root # here adding the root user to the autorized key
                    key: "{{lookup('file','~/.ssh/ubuntu3-id-rsa.pub')}}"
                    # reading the content from the ~/.ssh/ubuntu3-id-rsa.pub folder and using it as the key and adding the root user to it 

            ...

            # now when we execute the playbook as below 
            ansible-playbook delegate_playbook.yaml
            # the below will be the output

            PLAY [ubuntu-c] ***************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu-c]

            TASK [Generating a SSH Key pair using the openssh_keypair module] *************************************************************************************************************************************
            changed: [ubuntu-c]

            PLAY [linux] ******************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu2]
            ok: [centos1]
            ok: [centos3]
            ok: [ubuntu3]
            ok: [ubuntu1]
            ok: [centos2]

            TASK [Copying the ssh keypair  to the target host in the same folder] *********************************************************************************************************************************
            changed: [centos1] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            changed: [centos3] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            changed: [centos2] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            changed: [ubuntu2] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            changed: [ubuntu1] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            changed: [ubuntu3] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            changed: [centos3] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            changed: [centos1] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            changed: [centos2] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            changed: [ubuntu1] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            changed: [ubuntu2] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            changed: [ubuntu3] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])

            PLAY [ubuntu3] ****************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu3]

            TASK [accessing the public key and adding to the authorized_keys folder using authorized_key module for the root user] ********************************************************************************
            changed: [ubuntu3]

            PLAY RECAP ********************************************************************************************************************************************************************************************
            centos1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            centos2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            centos3                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu-c                   : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu3                    : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

            #now as the user been added to the authorized_key which been copied frm the public key then we can use the command as 
            ssh -i ~/.ssh/ubuntu3-id-rsa  root@ubuntu3
            # here we will be able to login to the ubuntu3 with the root user
            # -i option stands for the identiry key
        
        ```
     

  - **Case2**:-
    
    - here we will making the use of the `command module` against `all the target group host`
    
    - we will be validating thetwe are able to connect to the `root user of the ubuntu3` from any of the `target host` and execute the command as `date`
    
    - for the identiry key we need to provide the `option` as `-i` where we need to specify the `private key of ssh`
    
    - we can specify the `ssh oprions` woth the `-o` command    
      
      - we will be using the `StrictHostKeyChecking` as `no` as we don't want the prompt while validating the `fingure print` , hence can be specified as `StrictHostKeyChecking=no` with the `-o` option as `-o StrictHostKeyChecking=no`
      
      - we can also write to the known hosts file by using the option as `UserKnownHostFile=<specific file where we want to save the known host>` we can specify that as `UserKnownHostFile=/dev/null` here we are redirecting to the `/dev/null` which will ignore the `content theat been written into it`
      
      - here we can also mentioned the `BatchMode` option which will fail the `ssh command` if the `fingure print or key check been unaccepted`  we can spoecify the same using the command as `-o BatchMode=yes` against the `ssh command`
      
    - here also as we are using the `command module` the `content will be chnaged always` hence in order to avoid that we can use the `changed_when:False`
    
    - when we are successfully able to ssh the command will come in green color rather than the yellow which means success with changes 
    
    - we can use the `ignore_errors:True` which will ignore the `error in that particular task `
    
    - we can write the playbook as below 

        ```
        
            delegate_playbook.yaml
            ----------------------

            ---

            - hosts: ubuntu-c # here we are targeting the ubuntu-c ansible control hosts
              
              tasks:
              - name : Generating a SSH Key pair using the openssh_keypair module 
                openssh_keypair: # using the openssh_keypair module in here 
                    path: ~/.ssh/ubuntu3-id-rsa # generating both the private and publick key withis the name mentioned in path 

            
            # another play over here
            - hosts: linux # targeting the linux target host in here 
              tasks:
              - name: Copying the ssh keypair  to the target host in the same folder 
                copy: # using the  copy module in here 
                    owner: root # here specifying the owner for the same which has the access to the privat eand public keypair
                    src:"{{item.0}}"
                    dest:"{{item.0}}"
                    mode:"{{item.1}}"
                with_together: # using the with_together loop in  here which will be taking the set of pair as mentioned in the list
                    - [~/.ssh/ubuntu3-id-rsa, ~/.ssh/ubuntu3-id-rsa.pub ]
                    - ["0600","0644"]


            # now here we are defining another play in here as 
            - hosts: ubuntu3 #using the ubuntu3 host here
              tasks:
              - name: accessing the public key and adding to the authorized_keys folder using authorized_key module for the root user
                authorized_key:
                    user: root # here adding the root user to the autorized key
                    key: "{{lookup('file','~/.ssh/ubuntu3-id-rsa.pub')}}"
                    # reading the content from the ~/.ssh/ubuntu3-id-rsa.pub folder and using it as the key and adding the root user to it 

            # here we are using the another play to execute the ssh command using the command module on all target hosts
            - hosts: all # here the target ost being all target group
              tasks:
                - name: executing the ssh command over the all the target host over here 
                  command : ssh -i ~/.ssh/ubuntu3-id-rsa -o BatchMode=yes - o StrictHostKeyChecking=no -o UserKnownHostFile=/dev/null root@centos3 date # here using date cmd
                  changed_when: False #setting the change false as the False to see the green output on sucessful connection
                  ignore_errors : True # ignoring theerror happening while using the task 


            ...

            # now when we execute the playbook as below 
            ansible-playbook delegate_playbook.yaml
            # the below will be the output

            PLAY [ubuntu-c] ***************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu-c]

            TASK [Generating a SSH Key pair using the openssh_keypair module] *************************************************************************************************************************************
            ok: [ubuntu-c]

            PLAY [linux] ******************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [centos1]
            ok: [centos2]
            ok: [centos3]
            ok: [ubuntu2]
            ok: [ubuntu3]
            ok: [ubuntu1]

            TASK [Copying the ssh keypair  to the target host in the same folder] *********************************************************************************************************************************
            ok: [centos1] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [centos2] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [centos3] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [ubuntu2] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [ubuntu3] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [ubuntu1] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [centos1] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [centos2] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [centos3] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [ubuntu2] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [ubuntu3] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [ubuntu1] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])

            PLAY [ubuntu3] ****************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu3]

            TASK [accessing the public key and adding to the authorized_keys folder using authorized_key module for the root user] ********************************************************************************
            ok: [ubuntu3]

            PLAY [all] ********************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu-c]
            ok: [ubuntu1]
            ok: [ubuntu3]
            ok: [centos1]
            ok: [centos2]
            ok: [ubuntu2]
            ok: [centos3]

            TASK [executing the ssh command over the all the target host over here] *******************************************************************************************************************************
            ok: [ubuntu-c]
            ok: [centos1]
            ok: [centos2]
            ok: [ubuntu2]
            ok: [ubuntu3]
            ok: [ubuntu1]
            ok: [centos3]

            PLAY RECAP ********************************************************************************************************************************************************************************************
            centos1                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            centos2                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            centos3                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu-c                   : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu1                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu2                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu3                    : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
        
        ```

  - **case3**
    
    -  here in this case we can add `2 more play into the playbook`
    
    -  we will be make use of the `delegate_to directives` where `we are stating to execute the task on the target deligate_to provided target host` `after collecting the ansible facts` from the `taret hosts` which been provided in the `hosts section`
    
    - we are `deligating to deligate_to target host to perform the task` `after collecting the ansible_facts from the target host mentioned` in the `hosts section`
    
    - here also we are using this we are adding 2 more play into the plabook
    
    - on the first play we are adding the `line to the /etc/hosts.allow` file with the info gather from the `target host in the host section info` and only allowing `target host mentioned in the hosts section to be allowed` to connect to `ubuntu3 i.e deligated target hosts`
    
    - here in this case the `ubuntu3 target host will gather the facts from the hosts mentioned target host` and add that to the `/etc/hosts.allow` file using the `lineinfile module of ansible`
    
    - on the 2nd play we will try to target all the target host and try to connect to the `ubuntu3 target host with root user` and putting the `date command` using the `command module`
    
    - here as we have just added the `/etc/hosts.allow file with the necessary host that we want to connect` and we have not added any `deny condition` hence it will work well against the `all target group host`
    
    - we can write the playbook as below 

        ```
           delegate_playbook.yaml
            ----------------------

            ---

            - hosts: ubuntu-c # here we are targeting the ubuntu-c ansible control hosts
              
              tasks:
              - name : Generating a SSH Key pair using the openssh_keypair module 
                openssh_keypair: # using the openssh_keypair module in here 
                    path: ~/.ssh/ubuntu3-id-rsa # generating both the private and publick key withis the name mentioned in path 

            
            # another play over here
            - hosts: linux # targeting the linux target host in here 
              tasks:
              - name: Copying the ssh keypair  to the target host in the same folder 
                copy: # using the  copy module in here 
                    owner: root # here specifying the owner for the same which has the access to the privat eand public keypair
                    src:"{{item.0}}"
                    dest:"{{item.0}}"
                    mode:"{{item.1}}"
                with_together: # using the with_together loop in  here which will be taking the set of pair as mentioned in the list
                    - [~/.ssh/ubuntu3-id-rsa, ~/.ssh/ubuntu3-id-rsa.pub ]
                    - ["0600","0644"]


            # now here we are defining another play in here as 
            - hosts: ubuntu3 #using the ubuntu3 host here
              tasks:
              - name: accessing the public key and adding to the authorized_keys folder using authorized_key module for the root user
                authorized_key:
                    user: root # here adding the root user to the autorized key
                    key: "{{lookup('file','~/.ssh/ubuntu3-id-rsa.pub')}}"
                    # reading the content from the ~/.ssh/ubuntu3-id-rsa.pub folder and using it as the key and adding the root user to it 

            # here we are using the another play to execute the ssh command using the command module on all target hosts
            - hosts: all # here the target ost being all target group
              tasks:
                - name: executing the ssh command over the all the target host over here 
                  command : ssh -i ~/.ssh/ubuntu3-id-rsa -o BatchMode=yes - o StrictHostKeyChecking=no -o UserKnownHostFile=/dev/null root@centos3 date # here using date cmd
                  changed_when: False #setting the change false as the False to see the green output on sucessful connection
                  ignore_errors : True # ignoring theerror happening while using the task

            - hosts:  # here we re targeting target host as list of host of ubuntu-c , centos1 , ubuntu1
                - ubuntu-c
                - centos1
                - ubuntu1
              tasks:
                - name: Adding the entry to the /etc/hosts.allow file of the ubuntu3 deligated target host with the ansible facts collected from ubuntu-c , centos1 , ubuntu1
                  lineinfile: # using the line in file module in here 
                    path: /etc/hosts.allow # which file we want to modify we have mentioned that
                    line: "sshd: {{ansible_hostname}}.diveinto.io" # here with the line we are stating which line we want to add to the /etc/hosts.allow
                    state:present # line will be going to get added or replaced 
                  delegate_to: ubuntu-3 # here we are stating to ececute the task on the ubuntu3 deligated host using the ansible_facts that we collected from target host in hosts section 

            # here we are using the another play to execute the ssh command using the command module on all target hosts
            - hosts: all # here the target ost being all target group
              tasks:
                - name: executing the ssh command over the all the target host over here 
                  command : ssh -i ~/.ssh/ubuntu3-id-rsa -o BatchMode=yes - o StrictHostKeyChecking=no -o UserKnownHostFile=/dev/null root@centos3 date # here using date cmd
                  changed_when: False #setting the change false as the False to see the green output on sucessful connection
                  ignore_errors : True # ignoring theerror happening while using the task

            ... 

            # now when we execute the playbook as below 
            ansible-playbook delegate_playbook.yaml
            # the below will be the output

            PLAY [ubuntu-c] ***************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu-c]

            TASK [Generating a SSH Key pair using the openssh_keypair module] *************************************************************************************************************************************
            ok: [ubuntu-c]

            PLAY [linux] ******************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [centos2]
            ok: [centos1]
            ok: [ubuntu2]
            ok: [centos3]
            ok: [ubuntu3]
            ok: [ubuntu1]

            TASK [Copying the ssh keypair  to the target host in the same folder] *********************************************************************************************************************************
            ok: [centos3] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [centos1] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [centos2] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [ubuntu1] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [ubuntu3] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [ubuntu2] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [centos3] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [centos1] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [centos2] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [ubuntu1] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [ubuntu2] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [ubuntu3] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])

            PLAY [ubuntu3] ****************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu3]

            TASK [accessing the public key and adding to the authorized_keys folder using authorized_key module for the root user] ********************************************************************************
            ok: [ubuntu3]

            PLAY [all] ********************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu-c]
            ok: [centos1]
            ok: [ubuntu1]
            ok: [centos2]
            ok: [ubuntu2]
            ok: [ubuntu3]
            ok: [centos3]

            TASK [executing the ssh command over the all the target host over here] *******************************************************************************************************************************
            ok: [ubuntu-c]
            ok: [centos1]
            ok: [centos2]
            ok: [ubuntu2]
            ok: [ubuntu3]
            ok: [ubuntu1]
            ok: [centos3]

            PLAY [ubuntu-c,centos1,ubuntu1] ***********************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu-c]
            ok: [centos1]
            ok: [ubuntu1]

            TASK [deligating to the ubuntu3 target host to usethe ansible_facts from the target host and add to the ubuntu3 /etc/host.allow file] *****************************************************************
            changed: [centos1 -> ubuntu3]
            changed: [ubuntu1 -> ubuntu3]
            changed: [ubuntu-c -> ubuntu3]

            PLAY [all] ********************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu-c]
            ok: [centos2]
            ok: [centos1]
            ok: [ubuntu3]
            ok: [ubuntu2]
            ok: [ubuntu1]
            ok: [centos3]

            TASK [executing the ssh command over the all the target host over here] *******************************************************************************************************************************
            ok: [ubuntu-c]
            ok: [ubuntu1]
            ok: [centos2]
            ok: [centos1]
            ok: [ubuntu2]
            ok: [ubuntu3]
            ok: [centos3]

            PLAY RECAP ********************************************************************************************************************************************************************************************
            centos1                    : ok=8    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            centos2                    : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            centos3                    : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu-c                   : ok=8    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu1                    : ok=8    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu2                    : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu3                    : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        
        ```

  - **Case4**
    
    - now simiarly how we add the `/etc/hosts.allow` file to allow the `specifc target host to connect to particular host` , similarly we can add the `/etc/hosts.deny` file  which will restrict all the `all the host which is not there in the /etc/hosts.allow file` to connect to the hosts 
    
    - he the `/etc/hosts.deny` file will check the `/etc/hosts.allow` file for rreference if the ` specific host which is trying to connect` not there then `it will deby the connection for the same`
    
    - we can use the same `lininfile module` to `write one line to the /etc/hosts.deny file` to restrict the `rest of the target host which is not there in /etc/hosts.allow file`
    
    - here also we will writing to `2 additional play to the existing playbook`
      
      - on the `1st play` we will be `deny the rest of target host which is not listed in /etc/hosts.allow file`  on the `ubuntu3 target host` as we don't have to gather any `ansible_facts` from other hosts
      
      - on the very next play we wil be `ssh connect and vberify only the target host which are enlisted in the ubuntu3 /etc/hosts.allow` will able to connect and rest will not be able to connect to the `ubuntu3 target hosts`    
    
    - we can write the `playbook for the same as`

        ```

            delegate_playbook.yaml
            ----------------------

            ---

            - hosts: ubuntu-c # here we are targeting the ubuntu-c ansible control hosts
              
              tasks:
                - name : Generating a SSH Key pair using the openssh_keypair module 
                  openssh_keypair: # using the openssh_keypair module in here 
                    path: ~/.ssh/ubuntu3-id-rsa # generating both the private and publick key withis the name mentioned in path 


                # another play over here
                - hosts: linux # targeting the linux target host in here 
                  tasks:
                    - name: Copying the ssh keypair  to the target host in the same folder 
                      copy: # using the  copy module in here 
                        owner: root # here specifying the owner for the same which has the access to the privat eand public keypair
                        src: "{{item.0}}"
                        dest: "{{item.0}}"
                        mode: "{{item.1}}"
                      with_together: # using the with_together loop in  here which will be taking the set of pair as mentioned in the list
                        - [~/.ssh/ubuntu3-id-rsa, ~/.ssh/ubuntu3-id-rsa.pub ]
                        - ["0600","0644"]


                # now here we are defining another play in here as 
                - hosts: ubuntu3 #using the ubuntu3 host here
                  tasks:
                    - name: accessing the public key and adding to the authorized_keys folder using authorized_key module for the root user
                      authorized_key:
                        user: root # here adding the root user to the autorized key
                        key: "{{lookup('file','~/.ssh/ubuntu3-id-rsa.pub')}}"
                        # reading the content from the ~/.ssh/ubuntu3-id-rsa.pub folder and using it as the key and adding the root user to it 

                # here we are using the another play to execute the ssh command using the command module on all target hosts
                - hosts: all # here the target ost being all target group
                  tasks:
                    - name: executing the ssh command over the all the target host over here 
                      command : ssh -i ~/.ssh/ubuntu3-id-rsa -o BatchMode=yes -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@ubuntu3 date
                      changed_when: False #setting the change false as the False to see the green output on sucessful connection
                      ignore_errors : True # ignoring theerror happening while using the task

                - hosts:  # here we re targeting target host as list of host of ubuntu-c , centos1 , ubuntu1
                    - ubuntu-c
                    - centos1
                    - ubuntu1
                  tasks:
                    - name: Adding the entry to the /etc/hosts.allow file of the ubuntu3 deligated target host with the ansible facts collected from ubuntu-c ,      centos1 ,       ubuntu1
                      lineinfile: # using the line in file module in here 
                        path: /etc/hosts.allow # which file we want to modify we have mentioned that
                        line: "sshd: {{ansible_hostname}}.diveinto.io" # here with the line we are stating which line we want to add to the /etc/hosts.allow
                        state: present # line will be going to get added or replaced 
                      delegate_to: ubuntu3 # here we are stating to ececute the task on the ubuntu3 deligated host using the ansible_facts that we collected from target host in hosts section 

                - hosts: ubuntu3
                  tasks:  #here we are trying to connect to the ssh using the ssh on the command module 
                    - name: accessing the SSH key using the command module 
                      command: ssh -i ~/.ssh/ubuntu3-id-rsa -o BatchMode=yes -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@ubuntu3 date
                      changed_when: False
                      ignore_errors: True

                # here now adding another play to restrict the rest of the target host which are not listed in /etc/hosts.allow file using the hosts,deny file using the lineinfile  module 
                - hosts: ubuntu3 # here we re targeting target of ubuntu3 as don't hve to gather any ansible artifacts from  rest of the hosts
                  tasks:
                    - name: Adding the entry to the /etc/hosts.deby file of the ubuntu3 deligated target host to restreict the rest of the connection 
                      lineinfile: # using the line in file module in here 
                        path: /etc/hosts.deny # which file we want to modify we have mentioned that
                        line: "sshd: ALL" # here with the line we are stating which line we want to add to the /etc/hosts.deny
                        state: present # line will be going to get added or replaced 

                # here we are checking the ssh connection again over here as below 
                # here we are using the another play to execute the ssh command using the command module on all target hosts
                - hosts: all # here the target ost being all target group
                  tasks:
                    - name: executing the ssh command over the all the target host over here 
                      command : ssh -i ~/.ssh/ubuntu3-id-rsa -o BatchMode=yes -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@ubuntu3 date
                      changed_when: False #setting the change false as the False to see the green output on sucessful connection
                      ignore_errors : True # ignoring theerror happening while using the task 

            ...
        
            # now when we execute the playbook as below 
            ansible-playbook delegate_playbook.yaml
            # the below will be the output


            PLAY [ubuntu-c] ***************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu-c]

            TASK [Generating a SSH Key pair using the openssh_keypair module] *************************************************************************************************************************************
            ok: [ubuntu-c]

            PLAY [linux] ******************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [centos1]
            ok: [ubuntu1]
            ok: [ubuntu2]
            ok: [ubuntu3]
            ok: [centos2]
            ok: [centos3]

            TASK [Copying the ssh keypair  to the target host in the same folder] *********************************************************************************************************************************
            ok: [centos2] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [centos1] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [centos3] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [ubuntu2] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [ubuntu1] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [ubuntu3] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
            ok: [centos3] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [centos1] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [centos2] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [ubuntu2] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [ubuntu1] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
            ok: [ubuntu3] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])

            PLAY [ubuntu3] ****************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu3]

            TASK [accessing the public key and adding to the authorized_keys folder using authorized_key module for the root user] ********************************************************************************
            ok: [ubuntu3]

            PLAY [all] ********************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu-c]
            ok: [ubuntu1]
            ok: [centos1]
            ok: [ubuntu2]
            ok: [centos2]
            ok: [ubuntu3]
            ok: [centos3]

            TASK [executing the ssh command over the all the target host over here] *******************************************************************************************************************************
            ok: [ubuntu-c]
            ok: [centos1]
            ok: [centos2]
            ok: [ubuntu2]
            ok: [ubuntu3]
            ok: [ubuntu1]
            ok: [centos3]

            PLAY [ubuntu-c,centos1,ubuntu1] ***********************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu-c]
            ok: [centos1]
            ok: [ubuntu1]

            TASK [Adding the entry to the /etc/hosts.allow file of the ubuntu3 deligated target host with the ansible facts collected from ubuntu-c , centos1 , ubuntu1] ******************************************
            ok: [ubuntu-c -> ubuntu3]
            ok: [centos1 -> ubuntu3]
            ok: [ubuntu1 -> ubuntu3]

            PLAY [ubuntu3] ****************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu3]

            TASK [accessing the SSH key using the command module] *************************************************************************************************************************************************
            ok: [ubuntu3]

            PLAY [ubuntu3] ****************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [ubuntu3]

            TASK [Adding the entry to the /etc/hosts.deby file of the ubuntu3 deligated target host to restreict the rest of the connection] **********************************************************************
            changed: [ubuntu3]

            PLAY [all] ********************************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [centos1]
            ok: [centos2]
            ok: [ubuntu3]
            ok: [ubuntu1]
            ok: [ubuntu2]
            ok: [ubuntu-c]
            ok: [centos3]

            TASK [executing the ssh command over the all the target host over here] *******************************************************************************************************************************
            ok: [ubuntu-c]
            ok: [centos1]
            ok: [ubuntu1]
            fatal: [ubuntu2]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.031308", "end": "2023-09-23 01:07:48.181195", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:07:43.149887", "stderr": "kex_exchange_identification: read: Connection reset by peer\r\nConnection reset by 172.18.0.6 port 22", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer", "Connection reset by 172.18.0.6 port 22"], "stdout": "", "stdout_lines": []}
            ...ignoring
            fatal: [centos2]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.029086", "end": "2023-09-23 01:07:48.181079", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:07:43.151993", "stderr": "kex_exchange_identification: read: Connection reset by peer", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer"], "stdout": "", "stdout_lines": []}
            ...ignoring
            fatal: [ubuntu3]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.025397", "end": "2023-09-23 01:07:48.205658", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:07:43.180261", "stderr": "kex_exchange_identification: read: Connection reset by peer\r\nConnection reset by 172.18.0.6 port 22", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer", "Connection reset by 172.18.0.6 port 22"], "stdout": "", "stdout_lines": []}
            ...ignoring
            fatal: [centos3]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.027710", "end": "2023-09-23 01:07:48.464198", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:07:43.436488", "stderr": "kex_exchange_identification: read: Connection reset by peer", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer"], "stdout": "", "stdout_lines": []}
            ...ignoring

            PLAY RECAP ********************************************************************************************************************************************************************************************
            centos1                    : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            centos2                    : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=1   
            centos3                    : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=1   
            ubuntu-c                   : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu1                    : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu2                    : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=1   
            ubuntu3                    : ok=12   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=1 


        ```

  - **case5**
    
    - here we can perform the `cleanup` activity to `remove the entry that we hve added to the /etc/hosts.allow and /etc/hosts.deny  file`
    
    - hene in this case we `we can use the same lineinffile module` to remove the `host entry that we have added to the /etc/hosts.allow and /etc/hosts.deny file`
    
    - when we do this changes using the `lineinfile module` and run the playbook on the `first attempt` the `as the deny file and allow file been already there` we will get the error while doing the `ssh command` , but after 1 run it will  be going to get executed fine 
    
    - here while using the `1st play` we need to execute against the `ubuntu-c,centos1,ubuntu1 target host` as we want the `specific line in order to delete from the delegated ubuntu3 /etc/hosts.allow file` like the way we added and also we have to add the `ubuntu3 as the delegaed host`
    
    - but while removing from the `/etc/hosts.deny` we don't need any `ansible_facts` hence we can run that directly on the `ubuntu3 target hosts`  
    
    - we can write the playbook for the same as below 

        ```
            delegate_playbook.yaml
            ----------------------

            ---

            - hosts: ubuntu-c # here we are targeting the ubuntu-c ansible control hosts
              
              tasks:
                - name : Generating a SSH Key pair using the openssh_keypair module 
                  openssh_keypair: # using the openssh_keypair module in here 
                    path: ~/.ssh/ubuntu3-id-rsa # generating both the private and publick key withis the name mentioned in path 


                # another play over here
                - hosts: linux # targeting the linux target host in here 
                  tasks:
                    - name: Copying the ssh keypair  to the target host in the same folder 
                      copy: # using the  copy module in here 
                        owner: root # here specifying the owner for the same which has the access to the privat eand public keypair
                        src: "{{item.0}}"
                        dest: "{{item.0}}"
                        mode: "{{item.1}}"
                      with_together: # using the with_together loop in  here which will be taking the set of pair as mentioned in the list
                        - [~/.ssh/ubuntu3-id-rsa, ~/.ssh/ubuntu3-id-rsa.pub ]
                        - ["0600","0644"]


                # now here we are defining another play in here as 
                - hosts: ubuntu3 #using the ubuntu3 host here
                  tasks:
                    - name: accessing the public key and adding to the authorized_keys folder using authorized_key module for the root user
                      authorized_key:
                        user: root # here adding the root user to the autorized key
                        key: "{{lookup('file','~/.ssh/ubuntu3-id-rsa.pub')}}"
                        # reading the content from the ~/.ssh/ubuntu3-id-rsa.pub folder and using it as the key and adding the root user to it 

                # here we are using the another play to execute the ssh command using the command module on all target hosts
                - hosts: all # here the target ost being all target group
                  tasks:
                    - name: executing the ssh command over the all the target host over here 
                      command : ssh -i ~/.ssh/ubuntu3-id-rsa -o BatchMode=yes -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@ubuntu3 date
                      changed_when: False #setting the change false as the False to see the green output on sucessful connection
                      ignore_errors : True # ignoring theerror happening while using the task

                - hosts:  # here we re targeting target host as list of host of ubuntu-c , centos1 , ubuntu1
                    - ubuntu-c
                    - centos1
                    - ubuntu1
                  tasks:
                    - name: Adding the entry to the /etc/hosts.allow file of the ubuntu3 deligated target host with the ansible facts collected from ubuntu-c ,      centos1 ,       ubuntu1
                      lineinfile: # using the line in file module in here 
                        path: /etc/hosts.allow # which file we want to modify we have mentioned that
                        line: "sshd: {{ansible_hostname}}.diveinto.io" # here with the line we are stating which line we want to add to the /etc/hosts.allow
                        state: present # line will be going to get added or replaced 
                      delegate_to: ubuntu3 # here we are stating to ececute the task on the ubuntu3 deligated host using the ansible_facts that we collected from target host in hosts section 

                - hosts: ubuntu3
                  tasks:  #here we are trying to connect to the ssh using the ssh on the command module 
                    - name: accessing the SSH key using the command module 
                      command: ssh -i ~/.ssh/ubuntu3-id-rsa -o BatchMode=yes -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@ubuntu3 date
                      changed_when: False
                      ignore_errors: True

                # here now adding another play to restrict the rest of the target host which are not listed in /etc/hosts.allow file using the hosts,deny file using the lineinfile  module 
                - hosts: ubuntu3 # here we re targeting target of ubuntu3 as don't hve to gather any ansible artifacts from  rest of the hosts
                  tasks:
                    - name: Adding the entry to the /etc/hosts.deby file of the ubuntu3 deligated target host to restreict the rest of the connection 
                      lineinfile: # using the line in file module in here 
                        path: /etc/hosts.deny # which file we want to modify we have mentioned that
                        line: "sshd: ALL" # here with the line we are stating which line we want to add to the /etc/hosts.deny
                        state: present # line will be going to get added or replaced 

                # here we are checking the ssh connection again over here as below 
                # here we are using the another play to execute the ssh command using the command module on all target hosts
                - hosts: all # here the target ost being all target group
                  tasks:
                    - name: executing the ssh command over the all the target host over here 
                      command : ssh -i ~/.ssh/ubuntu3-id-rsa -o BatchMode=yes -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@ubuntu3 date
                      changed_when: False #setting the change false as the False to see the green output on sucessful connection
                      ignore_errors : True # ignoring theerror happening while using the task 

                # here we will be adding one more play to remove the line from  the /etc/hosts.allow in ubuntu3 hosts
                - hosts: ubuntu-c,centos1,ubuntu1 # targeting the ubuntu-c,centos1,ubuntu1 as we ned to gather the ansible_facts
                  tasks:  
                    - name: definingthe task to use the lineinfile module to remove the line from the /etc/hosts.allow file 
                      lineinfile:  # using the lineinfile module
                        path: /etc/hosts.allow
                        line: "sshd: {{ansible_hostname}}.diveinto.io"
                        state: absent #mentioning the state as absent which is remove the entry if the line found
                      delegate_to: ubuntu3

                # here we will be executing aginst the ubuntu3 host as we don't need any other info from any other hosts
                - hosts: ubuntu3 # targeting the ubuntu-c,centos1,ubuntu1 as we ned to gather the ansible_facts
                  tasks:  
                    - name: definingthe task to use the lineinfile module to remove the line from the /etc/hosts.allow file 
                      lineinfile:  # using the lineinfile module
                        path: /etc/hosts.deny #targeting the deny file in here 
                        line: "sshd: ALL" # target the content which need to be removed 
                        state: absent #mentioning the state as absent which is remove the entry if the line found

                ...
                # now when we execute the playbook as below 
                ansible-playbook delegate_playbook.yaml
                # the below will be the output 
                # ON THE 1ST RUN


                PLAY [ubuntu-c] ***************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu-c]

                TASK [Generating a SSH Key pair using the openssh_keypair module] *************************************************************************************************************************************
                ok: [ubuntu-c]

                PLAY [linux] ******************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [centos3]
                ok: [centos2]
                ok: [centos1]
                ok: [ubuntu2]
                ok: [ubuntu3]
                ok: [ubuntu1]

                TASK [Copying the ssh keypair  to the target host in the same folder] *********************************************************************************************************************************
                ok: [centos2] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
                ok: [centos3] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
                ok: [centos1] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
                ok: [ubuntu2] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
                ok: [ubuntu1] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
                ok: [ubuntu3] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
                ok: [centos2] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
                ok: [centos3] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
                ok: [centos1] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
                ok: [ubuntu1] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
                ok: [ubuntu2] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
                ok: [ubuntu3] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])

                PLAY [ubuntu3] ****************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu3]

                TASK [accessing the public key and adding to the authorized_keys folder using authorized_key module for the root user] ********************************************************************************
                ok: [ubuntu3]

                PLAY [all] ********************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos2]
                ok: [centos1]
                ok: [ubuntu1]
                ok: [ubuntu2]
                ok: [ubuntu3]
                ok: [centos3]

                TASK [executing the ssh command over the all the target host over here] *******************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos1]
                ok: [ubuntu1]
                fatal: [centos2]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.027357", "end": "2023-09-23 01:27:17.548743", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:27:12.521386", "stderr": "kex_exchange_identification: read: Connection reset by peer", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer"], "stdout": "", "stdout_lines": []}
                ...ignoring
                fatal: [ubuntu3]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.027241", "end": "2023-09-23 01:27:17.572077", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:27:12.544836", "stderr": "kex_exchange_identification: read: Connection reset by peer\r\nConnection reset by 172.18.0.6 port 22", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer", "Connection reset by 172.18.0.6 port 22"], "stdout": "", "stdout_lines": []}
                ...ignoring
                fatal: [ubuntu2]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.029702", "end": "2023-09-23 01:27:17.588466", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:27:12.558764", "stderr": "kex_exchange_identification: read: Connection reset by peer\r\nConnection reset by 172.18.0.6 port 22", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer", "Connection reset by 172.18.0.6 port 22"], "stdout": "", "stdout_lines": []}
                ...ignoring
                fatal: [centos3]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.025097", "end": "2023-09-23 01:27:17.950977", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:27:12.925880", "stderr": "kex_exchange_identification: read: Connection reset by peer", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer"], "stdout": "", "stdout_lines": []}
                ...ignoring

                PLAY [ubuntu-c,centos1,ubuntu1] ***********************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos1]
                ok: [ubuntu1]

                TASK [Adding the entry to the /etc/hosts.allow file of the ubuntu3 deligated target host with the ansible facts collected from ubuntu-c , centos1 , ubuntu1] ******************************************
                ok: [ubuntu-c -> ubuntu3]
                ok: [ubuntu1 -> ubuntu3]
                ok: [centos1 -> ubuntu3]

                PLAY [ubuntu3] ****************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu3]

                TASK [accessing the SSH key using the command module] *************************************************************************************************************************************************
                fatal: [ubuntu3]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.022455", "end": "2023-09-23 01:27:25.858158", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:27:20.835703", "stderr": "kex_exchange_identification: read: Connection reset by peer\r\nConnection reset by 172.18.0.6 port 22", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer", "Connection reset by 172.18.0.6 port 22"], "stdout": "", "stdout_lines": []}
                ...ignoring

                PLAY [ubuntu3] ****************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu3]

                TASK [Adding the entry to the /etc/hosts.deby file of the ubuntu3 deligated target host to restreict the rest of the connection] **********************************************************************
                ok: [ubuntu3]

                PLAY [all] ********************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos1]
                ok: [centos2]
                ok: [ubuntu1]
                ok: [ubuntu3]
                ok: [ubuntu2]
                ok: [centos3]

                TASK [executing the ssh command over the all the target host over here] *******************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos1]
                ok: [ubuntu1]
                fatal: [centos2]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.026720", "end": "2023-09-23 01:27:34.386079", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:27:29.359359", "stderr": "kex_exchange_identification: read: Connection reset by peer", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer"], "stdout": "", "stdout_lines": []}
                ...ignoring
                fatal: [ubuntu2]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.028292", "end": "2023-09-23 01:27:34.386058", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:27:29.357766", "stderr": "kex_exchange_identification: read: Connection reset by peer\r\nConnection reset by 172.18.0.6 port 22", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer", "Connection reset by 172.18.0.6 port 22"], "stdout": "", "stdout_lines": []}
                ...ignoring
                fatal: [ubuntu3]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.022094", "end": "2023-09-23 01:27:34.407086", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:27:29.384992", "stderr": "kex_exchange_identification: read: Connection reset by peer\r\nConnection reset by 172.18.0.6 port 22", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer", "Connection reset by 172.18.0.6 port 22"], "stdout": "", "stdout_lines": []}
                ...ignoring
                fatal: [centos3]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.039743", "end": "2023-09-23 01:27:34.698695", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:27:29.658952", "stderr": "kex_exchange_identification: read: Connection reset by peer", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer"], "stdout": "", "stdout_lines": []}
                ...ignoring

                PLAY [ubuntu-c,centos1,ubuntu1] ***********************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos1]
                ok: [ubuntu1]

                TASK [definingthe task to use the lineinfile module to remove the line from the /etc/hosts.allow file] ************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos1]
                ok: [ubuntu1]

                PLAY [ubuntu-c,centos1,ubuntu1] ***********************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos1]
                ok: [ubuntu1]

                TASK [definingthe task to use the lineinfile module to remove the line from the /etc/hosts.allow file] ************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos1]
                ok: [ubuntu1]

                PLAY RECAP ********************************************************************************************************************************************************************************************
                centos1                    : ok=12   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
                centos2                    : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=2   
                centos3                    : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=2   
                ubuntu-c                   : ok=12   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
                ubuntu1                    : ok=12   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
                ubuntu2                    : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=2   
                ubuntu3                    : ok=12   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=3   

                # ON THE SECOND RUN WILL BE AS 


                PLAY [ubuntu-c] ***************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu-c]

                TASK [Generating a SSH Key pair using the openssh_keypair module] *************************************************************************************************************************************
                ok: [ubuntu-c]

                PLAY [linux] ******************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [centos1]
                ok: [centos2]
                ok: [centos3]
                ok: [ubuntu1]
                ok: [ubuntu3]
                ok: [ubuntu2]

                TASK [Copying the ssh keypair  to the target host in the same folder] *********************************************************************************************************************************
                ok: [centos3] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
                ok: [centos2] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
                ok: [centos1] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
                ok: [ubuntu3] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
                ok: [ubuntu2] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
                ok: [ubuntu1] => (item=['~/.ssh/ubuntu3-id-rsa', '0600'])
                ok: [centos1] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
                ok: [centos3] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
                ok: [centos2] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
                ok: [ubuntu2] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
                ok: [ubuntu3] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])
                ok: [ubuntu1] => (item=['~/.ssh/ubuntu3-id-rsa.pub', '0644'])

                PLAY [ubuntu3] ****************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu3]

                TASK [accessing the public key and adding to the authorized_keys folder using authorized_key module for the root user] ********************************************************************************
                ok: [ubuntu3]

                PLAY [all] ********************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos2]
                ok: [ubuntu1]
                ok: [centos1]
                ok: [ubuntu2]
                ok: [ubuntu3]
                ok: [centos3]

                TASK [executing the ssh command over the all the target host over here] *******************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos2]
                ok: [centos1]
                ok: [ubuntu3]
                ok: [ubuntu2]
                ok: [ubuntu1]
                ok: [centos3]

                PLAY [ubuntu-c,centos1,ubuntu1] ***********************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos1]
                ok: [ubuntu1]

                TASK [Adding the entry to the /etc/hosts.allow file of the ubuntu3 deligated target host with the ansible facts collected from ubuntu-c , centos1 , ubuntu1] ******************************************
                ok: [ubuntu1 -> ubuntu3]
                ok: [centos1 -> ubuntu3]
                ok: [ubuntu-c -> ubuntu3]

                PLAY [all] ********************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [ubuntu2]
                ok: [centos1]
                ok: [centos2]
                ok: [ubuntu1]
                ok: [ubuntu3]
                ok: [centos3]

                TASK [accessing the SSH key using the command module] *************************************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos1]
                ok: [centos2]
                ok: [ubuntu1]
                ok: [ubuntu2]
                ok: [ubuntu3]
                ok: [centos3]

                PLAY [ubuntu3] ****************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu3]

                TASK [Adding the entry to the /etc/hosts.deby file of the ubuntu3 deligated target host to restreict the rest of the connection] **********************************************************************
                changed: [ubuntu3]

                PLAY [all] ********************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos1]
                ok: [centos2]
                ok: [ubuntu1]
                ok: [ubuntu2]
                ok: [ubuntu3]
                ok: [centos3]

                TASK [executing the ssh command over the all the target host over here] *******************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [centos1]
                ok: [ubuntu1]
                fatal: [centos2]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.031367", "end": "2023-09-23 01:33:15.138773", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:33:10.107406", "stderr": "kex_exchange_identification: read: Connection reset by peer", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer"], "stdout": "", "stdout_lines": []}
                ...ignoring
                fatal: [ubuntu2]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.028849", "end": "2023-09-23 01:33:15.143737", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:33:10.114888", "stderr": "kex_exchange_identification: read: Connection reset by peer\r\nConnection reset by 172.18.0.6 port 22", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer", "Connection reset by 172.18.0.6 port 22"], "stdout": "", "stdout_lines": []}
                ...ignoring
                fatal: [ubuntu3]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.025195", "end": "2023-09-23 01:33:15.157809", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:33:10.132614", "stderr": "kex_exchange_identification: read: Connection reset by peer\r\nConnection reset by 172.18.0.6 port 22", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer", "Connection reset by 172.18.0.6 port 22"], "stdout": "", "stdout_lines": []}
                ...ignoring
                fatal: [centos3]: FAILED! => {"changed": false, "cmd": ["ssh", "-i", "~/.ssh/ubuntu3-id-rsa", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "root@ubuntu3", "date"], "delta": "0:00:05.021632", "end": "2023-09-23 01:33:15.445017", "msg": "non-zero return code", "rc": 255, "start": "2023-09-23 01:33:10.423385", "stderr": "kex_exchange_identification: read: Connection reset by peer", "stderr_lines": ["kex_exchange_identification: read: Connection reset by peer"], "stdout": "", "stdout_lines": []}
                ...ignoring

                PLAY [ubuntu-c,centos1,ubuntu1] ***********************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu-c]
                ok: [ubuntu1]
                ok: [centos1]

                TASK [definingthe task to use the lineinfile module to remove the line from the /etc/hosts.allow file] ************************************************************************************************
                changed: [ubuntu-c -> ubuntu3]
                changed: [centos1 -> ubuntu3]
                changed: [ubuntu1 -> ubuntu3]

                PLAY [ubuntu3] ****************************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [ubuntu3]

                TASK [definingthe task to use the lineinfile module to remove the line from the /etc/hosts.allow file] ************************************************************************************************
                changed: [ubuntu3]

                PLAY RECAP ********************************************************************************************************************************************************************************************
                centos1                    : ok=12   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
                centos2                    : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=1   
                centos3                    : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=1   
                ubuntu-c                   : ok=12   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
                ubuntu1                    : ok=12   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
                ubuntu2                    : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=1   
                ubuntu3                    : ok=14   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=1 


        ```



