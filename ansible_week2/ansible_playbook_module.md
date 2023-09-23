# <ins> Ansible Playbook Deep Dive </ins> #

- the first video on this section will be on `ansible playbook module`

- we will see about the `ansible playbook module` with `hands on example`

- then we will learn about the `dynamic inventories`
  
  - How to `create dynamic inventories` and `use dynamic inventories`

- `Register` :- to `registering` the `info` `while executing the tasks`

- `making use` of the `registered info` for `later consumption`

- we will also `look further with` the `usage of when`

- ansible has `multitude of different way of using loops` and we will explore those `many possibilty of using loops`

- we will look into the `performance aspect` as well , How to `improve our ansible playbook execution` with `different approaches`

    - `Asynchronous`

    - `Serial`

    - `parallel`

- `Task Delegation` :- `allow` us `to run the ansible playbook task` `using` `specific target`

- `Ansible Magic Variables` :- `which si a specific set of variables` that `can be benificial` 

- `blocks` :- `to structure task in blocks` `with optional recovery approaches `

- `valuts` :- `Ansible Vaults` which will be useful for `securing information`


# <ins> ansible playbook module </ins> #

- `ansible` is a `battery included framework` `with thousand of builtin modules` which cover `multitude of area and technical speciality`

- here we will learn about `some of the module` `we are likely to use in everyday playbook creation`

- these `ansible playbook modules` are 
  
  - `set_fact` 

  - `pause`

  - `prompt`

  - `wait_for`
  
  - `assemble`

  - `add_host`

  - `group_by`

  - `fetch`


- **set_fact**

  - `Used for gathering facts while executing the playbook`
  
  - `Dynamically add or change facts during the execution`

  - the documentation link being 
    
    - [set_fact module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/set_fact_module.html)

  - Examples:- 

   - **Case1**

        - we can define the `ansible playbook` using the `set_fact` module of `ansible`

        - we can write the playbook as below 

            ```
            
                set_fact_playbook.yaml # defining the yaml playbook in here
                ----------------------

                ---

                - hosts: ubuntu3,centos3 # her we are targeting the centos3 and ubuntu3 target hosts
                  
                  tasks: # defining the task with set_fact nodule in here
                    
                    - name: Setting Up Facts in Here
                        set_fact: # using the  set_fact module
                            our_facts : Ansible Rocks...!
                            # here we are defining the variable which can be used as the facts in other tasks

                    - name: Accesssing the custom define fact variable facts
                        debug: #using the debug module in here 
                            msg: "{{our_facts}}"

                     
                ...
                # now we are executing the ansible playbook using the command as below 
                ansible-playbook set_fact_playbook.yaml
                # the output will be in the form of as 
                
                PLAY [centos3,ubuntu3] ********************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [centos3]
                ok: [ubuntu3]

                TASK [Setting Up the Facts] ***************************************************************************************************************************************************************************
                ok: [centos3]
                ok: [ubuntu3]

                TASK [Accessing the Facts01] **************************************************************************************************************************************************************************
                ok: [centos3] => {
                    "msg": "Ansible Rocks..!"
                }
                ok: [ubuntu3] => {
                    "msg": "Ansible Rocks..!"
                }

                PLAY RECAP ********************************************************************************************************************************************************************************************
                centos3                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
                ubuntu3                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
            
            
            ```

    - **Case2**

        - we can define the `multiple set_fact variable using the set_fact module as below`

        - we can use the playbook as below 

            ```
            
                set_fact_playbook.yaml # defining the yaml playbook in here
                ----------------------

                ---

                - hosts: ubuntu3,centos3 # her we are targeting the centos3 and ubuntu3 target hosts
                  
                  tasks: # defining the task with set_fact nodule in here
                    
                    - name: Setting Up Facts in Here
                        set_fact: # using the  set_fact module
                            our_facts : Ansible Rocks...!
                            ansible_distribution: "{{ansible_distribution | upper}}" # here we are overriding the inbuilt ansible_distribution facts with the upper filter
                            # here we are defining the variable which can be used as the facts in other tasks
                            # here we are defining the ansible default fact variable and making it as upper case 

                    - name: Accesssing the custom define fact variable 
                        debug: #using the debug module in here 
                            msg: "{{our_facts}}"

                    - name: Accesssing the custom define fact variable 
                        debug: #using the debug module in here 
                            msg: "{{ansible_distribution}}"

                ...
                # now we are executing the ansible playbook using the command as below 
                ansible-playbook set_fact_playbook.yaml
                # the output will be in the form of as 

                PLAY [centos3,ubuntu3] ********************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [centos3]
                ok: [ubuntu3]

                TASK [Setting Up the Facts] ***************************************************************************************************************************************************************************
                ok: [centos3]
                ok: [ubuntu3]

                TASK [Accessing the Facts01] **************************************************************************************************************************************************************************
                ok: [centos3] => {
                    "msg": "Ansible Rocks..!"
                }
                ok: [ubuntu3] => {
                    "msg": "Ansible Rocks..!"
                }

                TASK [Accessing the Facts02] **************************************************************************************************************************************************************************
                ok: [centos3] => {
                    "msg": "CENTOS"
                }
                ok: [ubuntu3] => {
                    "msg": "UBUNTU"
                }

                PLAY RECAP ********************************************************************************************************************************************************************************************
                centos3                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
                ubuntu3                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
            
            
            ```

    - **Case3**

        - we can also use the `task directive` `when directive` to while defining the `same custom facts` based of `different OS Version`

        - we can define the `same custom facts variable` for `differnt different OS` rather than creating the `separate groupvars`, using the `when directives` along with `set_fact` module and use it in the common facts as below 

        - this can be used `While we are using the ansible creating and executing` and we need to define different `location of nginx` based on the `ubuntu or centos distribution` as `nginx location for ubuntu was in /var/ww/html and for centos it is of /usr/sare/nginx/html` rather in thatcase we can use the `set_fact` module with `when task directive` which can remove the dependency fom the `inventory file`

        - we can define the `ansible plybook` for the same as below 

            ```
                set_fact_playbook.yaml # defining the yaml playbook in here
                ----------------------

                ---

                - hosts: ubuntu3,centos3 # her we are targeting the centos3 and ubuntu3 target hosts
                  
                  tasks: # defining the task with set_fact nodule in here
                    
                    - name: Setting Up Facts in Here for CentOS
                      set_fact: # using the  set_fact module
                        webserver_port : 80
                        webserver_location: /usr/share/nginx/html
                        webserver_user: root
                      when: ansible_distribution == "CentOS" # here defining the custom variable facts for the CentOS distribution

                    - name: Setting Up Facts in Here for Ubuntu
                      set_fact: #using the set_facts module in here 0
                        webserver_port : 80
                        webserver_location: /var/www/html
                        webserver_user: root
                      when: ansible_distribution == "Ubuntu" # here defining the custom variable facts for the Ubuntu distribution

                    - name: Accesssing the custom define fact variable # here we are accessing the common variable in this case over here
                      debug: #using the debug module in here 
                        msg: { webserver_port : "{{webserver_port}}" , webserver_location : "{{webserver_location}}" , webserver_user: "{{webserver_user}}" }
                        # using the message atribut to access the common define properties
                
                ...
                # now we are executing the ansible playbook using the command as below 
                ansible-playbook set_fact_playbook.yaml
                # the output will be in the form of as 

                PLAY [centos3,ubuntu3] ********************************************************************************************************************************************************************************

                TASK [Gathering Facts] ********************************************************************************************************************************************************************************
                ok: [centos3]
                ok: [ubuntu3]

                TASK [Setting Up Facts in Here for CentOS] ************************************************************************************************************************************************************
                ok: [centos3]
                skipping: [ubuntu3]

                TASK [Setting Up Facts in Here for Ubuntu] ************************************************************************************************************************************************************
                skipping: [centos3]
                ok: [ubuntu3]

                TASK [Accesssing the custom define fact variable] *****************************************************************************************************************************************************
                ok: [centos3] => {
                    "msg": {
                        "webserver_location": "/usr/share/nginx/html",
                        "webserver_port": 80,
                        "webserver_user": "root"
                    }
                }
                ok: [ubuntu3] => {
                    "msg": {
                        "webserver_location": "/var/www/html",
                        "webserver_port": 80,
                        "webserver_user": "root"
                    }
                }

                PLAY RECAP ********************************************************************************************************************************************************************************************
                centos3                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
                ubuntu3                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0  

    
    
            ```


- **Pause**

  - in `mark twain` the `right word may be effective` , but `no word is more effective as a rightly time paused `

  -  `Pause a playbook execution` for a `set amount of time` or `until a prompt is acknowledged`

  - it allow us to `pause the playbook execution for "certain given period"`

  - it also allow to `pausing "utill a specific prompt is acknowledged"`
  
  - the documentation link being 
    
    - [set_fact module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/pause_module.html) 
   
  - **case01**
    
    -  we can define the `ansible playbook` with the `pause module of ansible as below`

    - when we use the `pause module` we will get the prompt as `ctrl+c` and take an action `C to continiue` or `A to abort`

    - when we press `ctrl+c` then it will wait for the `next course of action` and `once the timeout reached then it will return the output`

    - based on the `input provided` i.e `C to continue early` or `A to abort` necessary action will be taken

    - we can see the ansible playbook as below 


    ```
        pause_playbook.yaml
        -------------------

        ---
    
        - hosts: centos3,ubuntu3 #defining the target hosts in here 
          
          tasks:
            - name : Pausing based on the seconds and minute value
              seconds: 5 #defining the seconds to wait for 
        
        # this will prompt for ctrl+c followed by the option of C to continue Early or A Abort

        # based on the action the corresponding action taken , if the timeout reached then return the output
    
        ...
        
        # if we  execute this then we can get the response as below 
        ansible-playbook pause_playbook.yaml
        # the output will be in the format as 
        
        
        PLAY [ubuntu3,centos3] ********************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [centos3]
        ok: [ubuntu3]

        TASK [Pausing for 1 Sec] ******************************************************************************************************************************************************************************
        Pausing for 1 seconds
        (ctrl+C then 'C' = continue early, ctrl+C then 'A' = abort)
        ok: [ubuntu3]

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos3                    : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 

        # if we  execute this then we can get the response as below 
        ansible-playbook pause_playbook.yaml
        # the output will be in the format as 
        # here we are choosing the ctrl+c with the `A for abort option`

        PLAY [ubuntu3,centos3] ********************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [centos3]
        ok: [ubuntu3]

        TASK [Pausing for 1 Sec] ******************************************************************************************************************************************************************************
        Pausing for 5 seconds
        (ctrl+C then 'C' = continue early, ctrl+C then 'A' = abort)
        Press 'C' to continue the play or 'A' to abort 
        fatal: [ubuntu3]: FAILED! => {"msg": "user requested abort!"}

        NO MORE HOSTS LEFT ************************************************************************************************************************************************************************************

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos3                    : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   

        # if we  execute this then we can get the response as below 
        ansible-playbook pause_playbook.yaml
        # the output will be in the format as 
        # here we are choosing the ctrl+c with the `C for continue early option`

        PLAY [ubuntu3,centos3] ********************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [centos3]
        ok: [ubuntu3]

        TASK [Pausing for 1 Sec] ******************************************************************************************************************************************************************************
        Pausing for 5 seconds
        (ctrl+C then 'C' = continue early, ctrl+C then 'A' = abort)
        Press 'C' to continue the play or 'A' to abort 
        ok: [ubuntu3]

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos3                    : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


    
    ```

    - if we want to  prompt the user `for manual intervention` then we can use the `prompt argument` in the `pause module`

    - we can write the `pause module with prompt argument as below`
    
    - if a `task` need to be `manually verified before continuing` then we can use the `prompt module`

    - this essentially prompt the user to `take action` util theat the `task will be in paused state`


        ```
            pause_playbook.html
            -------------------

            ---

            - hosts: ubuntu3,centos3 #defining the target host in here 
              
              tasks: #defining the tasks over here 
                - name: Need Manual Intervension or acknowledgfement from user using the pause module
                  pause: # defining the pause module in here
                    prompt: Please Enter to continue or (ctrl+c) to abort 
            ...

            # if we  execute this then we can get the response as below 
            ansible-playbook pause_playbook.yaml
            
            PLAY [ubuntu3,centos3] ********************************************************************************************************************************************************************************

            TASK [Gathering Facts] ********************************************************************************************************************************************************************************
            ok: [centos3]
            ok: [ubuntu3]

            TASK [Pausing for 1 Sec] ******************************************************************************************************************************************************************************
            [Pausing for 1 Sec]
            Please Enter to Continue or (ctrl+c) To abort:
            ^Mok: [ubuntu3]

            PLAY RECAP ********************************************************************************************************************************************************************************************
            centos3                    : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

        
        ```

- **wait_for module** 

  - rather than `providing a prompt` which ask `user to manually check` whether the `condition been met or not` , untill then the `task will wait`  if we use the `pause module with prompt`
  
  - we can check the `ports` are being used after the `service being enable` or `path` been available in the `remote host` , untill that we can make the `tasks wait` using the `wait_for` module with `conditional check`

  - the `wait_for` module will `pause` the `task execution` untill certain condition being met , once met the `the task can continue to execute`

  -  we can check the `port:80` available `after we  restarted our nginx web server` using this module as below 


    ```
    
        wait_for_playbook.yaml
        ----------------------

        ---

        - hosts: linux # using the linux hosts in this case 
          
          tasks:
            - name: Restarting the Nginx Service using the Service module
              service: # using the service module 
                name: nginx # providing the nginx service in here 
                state: restarted # using the state as restarted in here 

            - name: Using Wait For Module to validate and pause if need untill the port 80 in use which is the default nginx port being available
              wait_for: # using the wait_for module 
                port: 80 #waiting for the port 80 being aviailable or in use

        ...

        # we can execute the playbook as get the response as 
        ansible-playbook wait_for_playbook.yaml

        PLAY [centos3,ubuntu3] ********************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [centos3]
        ok: [ubuntu3]

        TASK [Restart Nginx] **********************************************************************************************************************************************************************************
        changed: [centos3]
        changed: [ubuntu3]

        TASK [waiting for the Port to be available] ***********************************************************************************************************************************************************
        ok: [centos3]
        ok: [ubuntu3]

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            
    
    ```

    - now we can `stop the service or ssh connection`  to `centos3 target host` and `execute the playbook on background` then we can see that the `playbook been waiting for the service to start ot ssh connection to be established`
    
    - as soon as we `restart the service` or `connect the ssh connection` then we can see the `waited background ansible playbook task` got `executed`

    - we can execute the `ansible playbook` on the `background` by adding the `& symbol` at the end as `ansible-playbook <name of playbook>.yaml &`

    - this will return the `ps id` and return the `control as well`

    - now we can stop the service using the `ansible adhoc command` as below

        ```
            ansible centos -m service -a 'name=nginx state=stopped'
            # here using the name as the nginx and state as stopped to stop the service as the service module option
            # aslo we can use the service module with the ansible adhoc command
        
            #then we can run the ansible playbook on the background
            ansible-playbook wait_for_playbook.yaml &
            # running the playbook on the background and returnning the `psid` and the `terminal` here

            #now when we restart the service of centos again we can also get the response from the ansible-playbook waited task as well 
            ansible centos -m service -a 'name=nginx state=started'
            # here restrting the nginx service on the centos using the service module as adhoc command
            # here we will also be able to see the response from the ansible-playbook waiting for the task
        
        ```


- **assemble module**

  - `assemble module` allow us to `beaksown the configuration file` into `segments` and `assemble broken configuration file segments` into `onefile which is the destination configuration file`  on the `target system or target hosts`

  - great to use,  `when we have an application or tool` `that requires configuration file as one file` , but `we want to manage those configuration separately`

  - ansible can be `scalable upto thousand of target hosts` hence the `corresponding configuration file` can be `larger`

  - lets suppose we have the `config file wfor thousand target host each having one entry to the config file` in that case the `configuration file will be much larger`

  - rather we can create `separate configuration file` for each `target host` and `at the end we can combine them as a sinbgle file at the destination file`

  - we can use the `assemble` module which can help in `merging the config file of separate target host into the one destination configuration file which thwe application can use`

  -  we can use the `ssemble module` to `create a single destination file` based on `collection of configuration file` which considered as the `segment in destination file`
  
  - as our `centos1` tyarget host use a `separate ssh port as 2222` rather than the `default ssh port 22`  hence we can create the `separate configuration file for the same`

  - ssh command provide the `option as -F where we can specify the configuration files` tpo connect to the `target hosts`

  - here we need to create the file name as `sshd_config` which is by defult present in `/etc/ssh/sshd_config`

  - we can create the `config file` with the `sshd_name` and use it to connect the `centos1` host

  - but also we do have the `conf.d` folder which is present in the `current working directory` which contains the `default ssh configuration` as below 

    ```
        conf.d/defaults
        ---------------

        ## Default # here we need to provide the ## to define the group

        Port 22 # defining the port as 22 where P in caps
        Protocol 2 # defining the Protool as 2 
        ForwardX11 yes # these coniguration can be fetched in /etc/ssh/sshd_config file 
        GSSAPIAuthentication no # these coniguration can be fetched in /etc/ssh/sshd_config file 

    
    ```

  - here we have the `conf.d` folder in that folder we have the `cenos1` as well where we have define the `configuration` based on the `centos1 host` as below 

    ```
        conf.d/centos1
        --------------
        ## custom Host for centos1
        Host centos1 # definning the hostname as centos 1 where we are targeting 
            User root #defining the user as root with U in capital
            Port 2222 # defining the port with capital P with the required port
    
    ```

  - now we can create the `sshd_config` in our `current working directory which will behave as the destination file` where we can use for the `-F config option` to define the `configuration file to connect to the centos1 host`
  
  - but for that we need to `assemble` the `file in the conf.d` folder i.e `default and centos1 config file which is the broken segment of the configuration into the destination file which is sshd_config` using the `assemble module of ansible`
  
  - for that we can use the `ansible playbook` as below 

    ```

        assemble_playbook.yaml
        ----------------------

        ---

        - hosts: ubuntu-c # targeting the ubutu-c target host in here

          tasks:
            - name : Assembling the fragmented section of the config into a destination file
              assemble: # using the assemble module in here 
                src: conf.d # using the conf.d folder in here
                dest: sshd_config # usignt he destination file as sshd_config in here
                backup: True # this will crete a backup file with the timestamp info in here
                delimiter: "##################" # this will add the delimeter when merging the file when one file end and another one added 
                # using the destination as the current working directory in sshd_connection file  
    
        ...

        # when we use the ansible playbook execution as below 
        ansible-playbook assemble_playbook.yaml
        # then the file will be displayed as below 
        
        PLAY [ubuntu-c] ***************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu-c]

        TASK [Adding the configuration file in here] **********************************************************************************************************************************************************
        ok: [ubuntu-c]

        PLAY RECAP ********************************************************************************************************************************************************************************************
        ubuntu-c                   : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
    
    ```

  - now we can see the `sshd_config` file been created in the `current working directory with config of defaults as well as centos host` as below 

    ```
        sshd_config
        -----------
        ## Default # here we need to provide the ## to define the group

        Port 22 # defining the port as 22 where P in caps
        Protocol 2 # defining the Protool as 2 
        ForwardX11 yes # these coniguration can be fetched in /etc/ssh/sshd_config file 
        GSSAPIAuthentication no # these coniguration can be fetched in /etc/ssh/sshd_config file


        ##################### # as we have provided the delimeter as ##### on the ansible playbook

        ## custom Host for centos1
        Host centos1 # definning the hostname as centos 1 where we are targeting 
            User root #defining the user as root with U in capital
            Port 2222 # defining the port with capital P with the required port
    
    
    
    ```

  - now when we trey to connect to the centos1 or any other host as it has `both the default and centos1 target host` using the `-F as below` it will able to connect
  
  - we can use the ssh with option `-F` for the config file to connect as `ssh -F  sshd_config <user>@<target hosts>` here we are using the `target hosts` in here with `user`
  
  - we are directing the `config file as the destination file which contains the info about the both the defaults and centos1 configuration`

  - where each `sepoarate configuration` can be managed by the `source control`, but from the `ansible end` we can `collect and push it`


- **add_hosts module**
  
  - this module help in adding the `target host` dynamically as per the `playbook` 

  - great for `when a resource is created during th execution` and we want to include that in the `ansible playbook` on the later part

  - `add host` module help in adding the `target host` into the `ansible play` during the `execution of playbook` and we can `subsequently use it as well`
  
  - we can also use the `add_hosts` module to `create ansible group` to which ` we can add the hostname` and use the `hostname` later `on subsequent play`

  - we can use the `create the ansible group and add host to the group` and use that `goup with host on the subsequent play`

  - then we can use  `untill now one play in the playbook` but we can define `n number of play` defined as `- symbol`

  - in case of using the `add_hosts` module multiple `play of the playbook` comes to play

  -  whille defining the `multiple play we can define ` below 

    ```
        add_hosts_playbook.yaml
        -----------------------

        ---

        - hosts:<hostname>

        - hosts:<hostname>

        ...

        #Or

        add_hosts_playbook.yaml
        -----------------------

        ---

        - 
            # here we can define the 1st host 
            
            hosts:<hostname>

        - 
            # here we can define the 2nd host 
        
            hosts:<hostname>

        ...
    
    ```

  - we can define the `ansible-playbook` with the `add_hosts` module as below 

    ```
        add_hosts_playbook.yaml
        -----------------------

        ---

        - hosts: ubuntu-c # here we are using the ubuntu-c ansible control hosts
          
          tasks:
            - name : creating the Host on the fly and adding to the ansible group for later use 
              add_host: # using the add_host module in here
                name: centos3 # definig the target host over here
                group: adhoc_group1,adhoc_group2 #creating the group to which the host eill be added which can be used later
                # here we are creating the group out in here 

        - hosts: adhoc_group1 #here we are using the adhoc_group1 which been added with centos1 host
          tasks:
            - name : pinging to the group with the host details 
              ping: #using the ping module in here 

        ...
        # when we use the ansible playbook execution as below 
        ansible-playbook add_hosts_playbook.yaml
        # then the file will be displayed as below 
        PLAY [ubuntu-c] ***************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu-c]

        TASK [Adding New Host in here] ************************************************************************************************************************************************************************
        ok: [ubuntu-c]

       # here we can see the another play of the playbook with the name as centos3
       
        PLAY [centos3] ****************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [centos3]

        TASK [Using the Dynamically Added Hosts] **************************************************************************************************************************************************************
        ok: [centos3]

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu-c                   : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    
    
    ```

- **group_by module**
  
  - create the `groups based on the facts as key `

  - use the `facts` to `dynamically create the associated group where the hostname resides` 

  - `group_by` module will help in `similar to the add_hosts module` add the `hosts to the ansible_group` but the `host` can be resolved from the `key of the ansible facts`

  - we can use the `ansible playbook` as below for this

    ```
        group_by_playbook.yaml
        -----------------------

        ---

        - hosts: linux # using the linux target host in here 
          
          tasks: 
            - name: using the Group by module to add host to the group based on the key of the ansible facts
              group_by: # using the group by module
                key: cust_{{ansible_distribution | lower }}  # here we are using he key args we are creating the group and addng the value of the ansible_distribution into it

        
        - hosts: cust_centos # here using the cust_centos which will be forming from the groupby_module and ansible group formed with name cust_centos and cust_ubuntu here using cust_centos 
          
          tasks: 
            - name: using the created group herer host being added 
              ping: #using the ping module in  here 

        ...

        # when we use the ansible playbook execution as below 
        ansible-playbook group_by_playbook.yaml
        # then the file will be displayed as below 


        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [centos2]
        ok: [centos1]
        ok: [ubuntu3]
        ok: [centos3]

        TASK [using the Group by module to add host to the group based on the key of the ansible facts] *******************************************************************************************************
        changed: [centos1]
        changed: [centos2]
        changed: [centos3]
        changed: [ubuntu1]
        changed: [ubuntu2]
        changed: [ubuntu3]

        PLAY [cust_centos] ************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [centos1]
        ok: [centos3]
        ok: [centos2]

        TASK [using the created group herer host being added] *************************************************************************************************************************************************
        ok: [centos1]
        ok: [centos3]
        ok: [centos2]

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            
    
    ```

- **fetch module**

  - if wewant to `capture file from the remote system or target host` then we can use the `fetch module`

  - here if we want to capture the `etc/redhat-release file` which which is in the `/etc/redhat-release file` to the `/tmp/readhat-releas/ folder`

  - in that case we can use the `fetch module` with the `ansible playbook` as below


    ```

        fetch_playbook.yaml
        -------------------


        ---

        - hosts: centos # here we are targeting the centos host in here 

          tasks: 
            - name : using the fetch playbook in here as below 
              fetch: # using the fetch module
                src: /etc/redhat-release
                dest: /tmp/redhat-release
                fail_on_missing: true # check file present on the remte server and readable


        ...
        
        # when we use the ansible playbook execution as below 
        ansible-playbook fetch_playbook.yaml
        # then the file will be displayed as below 

        PLAY [centos] *****************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [centos3]
        ok: [centos1]
        ok: [centos2]

        TASK [using the fetch playbook in here as below] ******************************************************************************************************************************************************
        changed: [centos1]
        changed: [centos2]
        changed: [centos3]

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
            
    ```

- now if we for check in the `ubutu-c ansible control host` in the `/tmp/redhat-release folder` then we can see  the `folder structure as below`

- for `each of the hosts` will be `create a directory` inside that we have the `source folder structure` to fetch the file 

    ```

    
        /tmp/redhat-release
        -------------------
        cento1
            - etc
                - redhat-release
        centos2
            - etc
                - redhat-release
        centos3
            - etc
                - redhat-release
    
    ```














