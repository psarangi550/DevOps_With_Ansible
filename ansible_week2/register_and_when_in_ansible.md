# <ins> Register and When in Ansible </ins> #

- we will learn about the `how to register output` , with the `register directives`

- how to `make use of the registered output`

- how to `work around` `differences with the registered output`

- we will learn about the `filter` related to the `registered content`

- `in all of this` we will `making more use of when` and `utilizing "when with the register"`

- we saw the `ansible adhoc command line utility` can be used in `verity of way` , `an area which is more convinient` `is the command module`

- as the `command module` is the `default module of ansible if no module provided` hence we can ignore specifying `-m command` while using the `ansible adhoc command`

- we can display the `hostname` with the `sort format` using the `option` as `hostname -s` as the command 

- we can write the `ansible adhoc command` as below 

    ```
        ansible all -a 'hostname -s' -o
        # here the command we are using is `hostname -s` which will show `short version of the hostname command`
        # also we are suing the -o option for the oneline
        # here are not using any nodule with -m hence the command module will be considered in here

        # the output will be as below
        # here the shortname of the host been showing to the stdout

        ubuntu-c | CHANGED | rc=0 | (stdout) ubuntu-c
        centos2 | CHANGED | rc=0 | (stdout) centos2
        centos1 | CHANGED | rc=0 | (stdout) centos1
        centos3 | CHANGED | rc=0 | (stdout) centos3
        ubuntu1 | CHANGED | rc=0 | (stdout) ubuntu1
        ubuntu2 | CHANGED | rc=0 | (stdout) ubuntu2
        ubuntu3 | CHANGED | rc=0 | (stdout) ubuntu3
    
    ```

- we can create the `put it on to the ansible playbook` as below 

    ```
        register_output.yaml
        --------------------

        ---

        - hosts: linux # using the linux host in here 
          

          tasks:

            - name: fetching the hostname of the target host in short form using command module 
                command : hostname -s # providing the command against the command module 
                register: hostname_output # here creating a register with the register directives in here 

        ...
        # if we execute the playbook in here 
        ansible-playbook register_output.yaml
        # then the output will be as 

        PLAY [linux] ***************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************
        ok: [centos2]
        ok: [centos3]
        ok: [centos1]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [ubuntu3]

        TASK [fetching the hostname of the target host in short form using command module] *****************************************************************************************************
        changed: [centos2]
        changed: [centos1]
        changed: [centos3]
        changed: [ubuntu2]
        changed: [ubuntu1]
        changed: [ubuntu3]

        PLAY RECAP *****************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


    
    ```

- here we can't see the `output hostname` that been captured using the `register directives`

- here we can see the `change` been happended from the `logs` but will not able to calcaulate that the `registerd output`

- we can `define a variable` where we want to `register the output` `from the context of executed module` and use that `variable later on`
 
- if we want to capture the `register variable` which `contains the output of the execution of the module` then we can define the `playbook` as below 

    ```
        register_output.yaml
        --------------------

        ---

        - hosts: linux # using the linux host in here 
          

          tasks:

            - name: fetching the hostname of the target host in short form using command module 
              command : hostname -s # providing the command against the command module 
              register: hostname_output # here creating a register with the register directives in here 

            - name: grabing the register variable using the debug module 
              debug: # using the debug module in here 
                var: hostname_output
                # the var attribute is mutually exclusive with the msg attribute
                # also we can use the `var` directly without the JINJA2 templating as its been in built to it  

        ...

        # if we execute the playbook in here 
        ansible-playbook register_output.yaml
        # then the output will be as 


        PLAY [linux] ***************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************
        ok: [centos2]
        ok: [centos3]
        ok: [centos1]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [ubuntu3]

        TASK [fetching the hostname of the target host in short form using command module] *****************************************************************************************************
        changed: [centos3]
        changed: [centos1]
        changed: [centos2]
        changed: [ubuntu1]
        changed: [ubuntu2]
        changed: [ubuntu3]

        TASK [grabing the register variable using the debug module] ****************************************************************************************************************************
        ok: [centos1] => {
            "hostname_output": {
                "changed": true,
                "cmd": [
                    "hostname",
                    "-s"
                ],
                "delta": "0:00:00.004518",
                "end": "2023-09-19 02:20:31.259784",
                "failed": false,
                "msg": "",
                "rc": 0,
                "start": "2023-09-19 02:20:31.255266",
                "stderr": "",
                "stderr_lines": [],
                "stdout": "centos1",
                "stdout_lines": [
                    "centos1"
                ]
            }
        }
        ok: [centos2] => {
            "hostname_output": {
                "changed": true,
                "cmd": [
                    "hostname",
                    "-s"
                ],
                "delta": "0:00:00.003654",
                "end": "2023-09-19 02:20:31.260477",
                "failed": false,
                "msg": "",
                "rc": 0,
                "start": "2023-09-19 02:20:31.256823",
                "stderr": "",
                "stderr_lines": [],
                "stdout": "centos2",
                "stdout_lines": [
                    "centos2"
                ]
            }
        }
        ok: [centos3] => {
            "hostname_output": {
                "changed": true,
                "cmd": [
                    "hostname",
                    "-s"
                ],
                "delta": "0:00:00.004309",
                "end": "2023-09-19 02:20:31.257660",
                "failed": false,
                "msg": "",
                "rc": 0,
                "start": "2023-09-19 02:20:31.253351",
                "stderr": "",
                "stderr_lines": [],
                "stdout": "centos3",
                "stdout_lines": [
                    "centos3"
                ]
            }
        }
        ok: [ubuntu1] => {
            "hostname_output": {
                "changed": true,
                "cmd": [
                    "hostname",
                    "-s"
                ],
                "delta": "0:00:00.003409",
                "end": "2023-09-19 02:20:31.310104",
                "failed": false,
                "msg": "",
                "rc": 0,
                "start": "2023-09-19 02:20:31.306695",
                "stderr": "",
                "stderr_lines": [],
                "stdout": "ubuntu1",
                "stdout_lines": [
                    "ubuntu1"
                ]
            }
        }
        ok: [ubuntu2] => {
            "hostname_output": {
                "changed": true,
                "cmd": [
                    "hostname",
                    "-s"
                ],
                "delta": "0:00:00.004740",
                "end": "2023-09-19 02:20:31.337645",
                "failed": false,
                "msg": "",
                "rc": 0,
                "start": "2023-09-19 02:20:31.332905",
                "stderr": "",
                "stderr_lines": [],
                "stdout": "ubuntu2",
                "stdout_lines": [
                    "ubuntu2"
                ]
            }
        }
        ok: [ubuntu3] => {
            "hostname_output": {
                "changed": true,
                "cmd": [
                    "hostname",
                    "-s"
                ],
                "delta": "0:00:00.004217",
                "end": "2023-09-19 02:20:31.608393",
                "failed": false,
                "msg": "",
                "rc": 0,
                "start": "2023-09-19 02:20:31.604176",
                "stderr": "",
                "stderr_lines": [],
                "stdout": "ubuntu3",
                "stdout_lines": [
                    "ubuntu3"
                ]
            }
        }

        PLAY RECAP *****************************************************************************************************************************************************************************
        centos1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    
    
    ```



- it will  be providing the value against the `registervariable as the key` as in the above on `hostnmame_output` as the variable hence we will be getting the `output` as `{hostnmame_output:<value we got from the regier output result>}`

- this will `register output` will provide the below info 
  
  - `list of commad and paramter` that got executed with the `cmd` key and `list of commands with space delimited values`
  
  - we can also see the `start` and `endtime` of the `command took to execute on each of the target host`
  
  - we can see the `return code` with `rc value` i.e the `0 means command successfully executed` and `non negetive means command did not got executed`
  
  - we can see also the changes made to the target host using `changed` with the `True or False` value 
  
  - we can see the `stderr` info as well , if not `stderr` then it will come as `empty string`
  
  - also we can see the `stdout` info with the `stdout` value 

  - along with that we can get the info about the `stdout_lines` and `stderr_lines` which will provide the `each line of the stdout or stderr` as the `separate entry to the  list that showing as the value against it`

  - we can even use this `register output` value by `accessing them with ./[] notation to get further info`


- we can get the `stdout` of the above command as below

- for that the ansible playbook can be written as below 

    ```

        register_output.yaml
        --------------------

        ---

        - hosts: linux # using the linux host in here 
          

          tasks:

            - name: fetching the hostname of the target host in short form using command module 
              command : hostname -s # providing the command against the command module 
              register: hostname_output # here creating a register with the register directives in here 

            - name: grabing the register variable using the debug module 
              debug: # using the debug module in here 
                var: hostname_output.stdout # accessing the stdout key of the registered output
                # the var attribute is mutually exclusive with the msg attribute
                # also we can use the `var` directly without the JINJA2 templating as its been in built to it  

        ...
    
        # if we execute the playbook in here 
        ansible-playbook register_output.yaml
        # then the output will be as 

        PLAY [linux] ***************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************
        ok: [centos2]
        ok: [centos3]
        ok: [centos1]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [ubuntu3]

        TASK [fetching the hostname of the target host in short form using command module] *****************************************************************************************************
        changed: [centos1]
        changed: [centos3]
        changed: [centos2]
        changed: [ubuntu2]
        changed: [ubuntu1]
        changed: [ubuntu3]

        TASK [grabing the register variable using the debug module] ****************************************************************************************************************************
        ok: [centos1] => {
            "hostname_output.stdout": "centos1"
        }
        ok: [centos2] => {
            "hostname_output.stdout": "centos2"
        }
        ok: [centos3] => {
            "hostname_output.stdout": "centos3"
        }
        ok: [ubuntu1] => {
            "hostname_output.stdout": "ubuntu1"
        }
        ok: [ubuntu2] => {
            "hostname_output.stdout": "ubuntu2"
        }
        ok: [ubuntu3] => {
            "hostname_output.stdout": "ubuntu3"
        }

        PLAY RECAP *****************************************************************************************************************************************************************************
        centos1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            
    
    ```

- up untill now we are using the `when` directive to `fetch particular distribution for particular linux diustribution`

- one point to note that `while using the when directory` we don't gave to define the `JINJA2 template` as it comes as `implicit value`

- but we can use the `and` condition while defining the `multiple condition` against the when clause as below 

- we can define the `ansible playbook` for the same as 

    ```
        register_output.yaml
        --------------------

        ---

        - hosts: linux # using the linux host in here 
          

          tasks:

            - name: fetching the hostname of the target host in short form using command module 
              command : hostname -s # providing the command against the command module 
              register: hostname_output # here creating a register with the register directives in here 
              when: ansible_distribution == "CentOS" and ansible_distribution_major_version == "8"
              # using the when directive without JINJA2 templating and with `and` condition as well

            - name: grabing the register variable using the debug module 
              debug: # using the debug module in here 
                var: hostname_output.stdout # accessing the stdout key of the registered output
                # the var attribute is mutually exclusive with the msg attribute
                # also we can use the `var` directly without the JINJA2 templating as its been in built to it  

        ...  

        # if we execute the playbook in here 
        ansible-playbook register_output.yaml
        # then the output will be as 
        # here we can see that it got executed for the centos but ubuntu one got skipped


        PLAY [linux] ***************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************
        ok: [centos1]
        ok: [centos2]
        ok: [centos3]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [ubuntu3]

        TASK [fetching the hostname of the target host in short form using command module] *****************************************************************************************************
        skipping: [ubuntu1]
        skipping: [ubuntu2]
        skipping: [ubuntu3]
        changed: [centos3]
        changed: [centos2]
        changed: [centos1]

        TASK [grabing the register variable using the debug module] ****************************************************************************************************************************
        ok: [centos1] => {
            "hostname_output.stdout": "centos1"
        }
        ok: [centos2] => {
            "hostname_output.stdout": "centos2"
        }
        ok: [centos3] => {
            "hostname_output.stdout": "centos3"
        }
        ok: [ubuntu1] => {
            "hostname_output.stdout": "VARIABLE IS NOT DEFINED!"
        }
        ok: [ubuntu2] => {
            "hostname_output.stdout": "VARIABLE IS NOT DEFINED!"
        }
        ok: [ubuntu3] => {
            "hostname_output.stdout": "VARIABLE IS NOT DEFINED!"
        }

        PLAY RECAP *****************************************************************************************************************************************************************************
        centos1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
        ubuntu2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0  
    
    
    ```

- we can also execute the same `when directive with` `or` command as well for which we can declared as below 

    ```
    
       register_output.yaml
        --------------------

        ---

        - hosts: linux # using the linux host in here 
          

          tasks:

            - name: fetching the hostname of the target host in short form using command module 
              command : hostname -s # providing the command against the command module 
              register: hostname_output # here creating a register with the register directives in here 
              when: (ansible_distribution == "CentOS" and ansible_distribution_major_version == "8") or 
                    (ansible_distribution =="Ubuntu" and ansible_distribution_major_version=="22" )
              # using the when directive without JINJA2 templating and with `and along with or condition` condition as well

            - name: grabing the register variable using the debug module 
              debug: # using the debug module in here 
                var: hostname_output.stdout # accessing the stdout key of the registered output
                # the var attribute is mutually exclusive with the msg attribute
                # also we can use the `var` directly without the JINJA2 templating as its been in built to it  

        ...   
        # if we execute the playbook in here 
        ansible-playbook register_output.yaml
        # then the output will be as 
        # here we can see that it got executed for the centos and ubuntu

        PLAY [linux] ***************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************
        ok: [centos1]
        ok: [centos2]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [centos3]
        ok: [ubuntu3]

        TASK [fetching the hostname of the target host in short form using command module] *****************************************************************************************************
        changed: [centos3]
        changed: [centos2]
        changed: [centos1]
        changed: [ubuntu2]
        changed: [ubuntu1]
        changed: [ubuntu3]

        TASK [grabing the register variable using the debug module] ****************************************************************************************************************************
        ok: [centos1] => {
            "hostname_output.stdout": "centos1"
        }
        ok: [centos2] => {
            "hostname_output.stdout": "centos2"
        }
        ok: [centos3] => {
            "hostname_output.stdout": "centos3"
        }
        ok: [ubuntu1] => {
            "hostname_output.stdout": "ubuntu1"
        }
        ok: [ubuntu2] => {
            "hostname_output.stdout": "ubuntu2"
        }
        ok: [ubuntu3] => {
            "hostname_output.stdout": "ubuntu3"
        }

        PLAY RECAP *****************************************************************************************************************************************************************************
        centos1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

    
    ```

- if we want to make the `target host` more versitile where it can support the `current and future` `ansible_distribution_major_version`

- if we are using this then we can see that then we need to `convert the string value` into the `integer value` as the `ansible_distribution_major_version` comes in `string format`

- we can use the `int JINJA2 filter` as `ansible_distribution_major_version | int ` and define the `playbook` as below 

    ```
        register_output.yaml
        --------------------

        ---

        - hosts: linux # using the linux host in here 
          

          tasks:

            - name: fetching the hostname of the target host in short form using command module 
              command : hostname -s # providing the command against the command module 
              register: hostname_output # here creating a register with the register directives in here 
              when: (ansible_distribution == "CentOS" and ansible_distribution_major_version| int >= 8 ) or 
                    (ansible_distribution =="Ubuntu" and ansible_distribution_major_version | int >=22 )
              # using the when directive without JINJA2 templating and with `and along with or condition` condition as well
              # here using the JINJA2 filter called in converting it to the integer and comparing the value then 

            - name: grabing the register variable using the debug module 
              debug: # using the debug module in here 
                var: hostname_output.stdout # accessing the stdout key of the registered output
                # the var attribute is mutually exclusive with the msg attribute
                # also we can use the `var` directly without the JINJA2 templating as its been in built to it  

        ...  
        
        # if we execute the playbook in here 
        ansible-playbook register_output.yaml
        # then the output will be as 
        # here we can see that it got executed for the centos and ubuntu

        PLAY [linux] ***************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************
        ok: [centos1]
        ok: [centos2]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [centos3]
        ok: [ubuntu3]

        TASK [fetching the hostname of the target host in short form using command module] *****************************************************************************************************
        changed: [centos3]
        changed: [centos2]
        changed: [centos1]
        changed: [ubuntu2]
        changed: [ubuntu1]
        changed: [ubuntu3]

        TASK [grabing the register variable using the debug module] ****************************************************************************************************************************
        ok: [centos1] => {
            "hostname_output.stdout": "centos1"
        }
        ok: [centos2] => {
            "hostname_output.stdout": "centos2"
        }
        ok: [centos3] => {
            "hostname_output.stdout": "centos3"
        }
        ok: [ubuntu1] => {
            "hostname_output.stdout": "ubuntu1"
        }
        ok: [ubuntu2] => {
            "hostname_output.stdout": "ubuntu2"
        }
        ok: [ubuntu3] => {
            "hostname_output.stdout": "ubuntu3"
        }

        PLAY RECAP *****************************************************************************************************************************************************************************
        centos1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    
    
    ```

- we can also mention the `and condition` isnide the `when directives` like the `list of condition` while declaring the `when directive` as below 

- when we mentioned the `list of condition as we define the list in the when directive` that will be converted to the `and condition in when directive`

- hene we can use it as below 

    ```
    
        register_output.yaml
        --------------------

        ---

        - hosts: linux # using the linux host in here 
          

          tasks:

            - name: fetching the hostname of the target host in short form using command module 
              command : hostname -s # providing the command against the command module 
              register: hostname_output # here creating a register with the register directives in here 
              when: 
                -ansible_distribution == "CentOS" 
                - ansible_distribution_major_version| int >= 8
                # here  we are declaring multiple command with the option as list that we discussed
                # using the when directive without JINJA2 templating and with `and` condition as well
                # here using the JINJA2 filter called in converting it to the integer and comparing the value then 

            - name: grabing the register variable using the debug module 
              debug: # using the debug module in here 
                var: hostname_output.stdout # accessing the stdout key of the registered output
                # the var attribute is mutually exclusive with the msg attribute
                # also we can use the `var` directly without the JINJA2 templating as its been in built to it  

        ...  
        # if we execute the playbook in here 
        ansible-playbook register_output.yaml
        # then the output will be as 
        # here we can see that it got executed for centos ignoring the ubuntu


        PLAY [linux] ***************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************
        ok: [centos3]
        ok: [centos1]
        ok: [centos2]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [ubuntu3]

        TASK [fetching the hostname of the target host in short form using command module] *****************************************************************************************************
        skipping: [ubuntu1]
        skipping: [ubuntu2]
        skipping: [ubuntu3]
        changed: [centos1]
        changed: [centos2]
        changed: [centos3]

        TASK [grabing the register variable using the debug module] ****************************************************************************************************************************
        ok: [centos1] => {
            "hostname_output.stdout": "centos1"
        }
        ok: [centos2] => {
            "hostname_output.stdout": "centos2"
        }
        ok: [centos3] => {
            "hostname_output.stdout": "centos3"
        }
        ok: [ubuntu1] => {
            "hostname_output.stdout": "VARIABLE IS NOT DEFINED!"
        }
        ok: [ubuntu2] => {
            "hostname_output.stdout": "VARIABLE IS NOT DEFINED!"
        }
        ok: [ubuntu3] => {
            "hostname_output.stdout": "VARIABLE IS NOT DEFINED!"
        }

        PLAY RECAP *****************************************************************************************************************************************************************************
        centos1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
        ubuntu2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
    
    ```

- we can use the `ansible adhoc command with the setup module to get the filtered facts` as below 

    ```
        # we can execute the value as below 
        ansible linux -m setup -a filter='ansible_distribution*'
        # here we are targeting the linux target group
        # also using the module as the setup module 
        # and we are using the filter as the argument in here 

        # the output JSON will be as below 
        centos2 | SUCCESS => {
    "ansible_facts": {
        "ansible_distribution": "CentOS",
        "ansible_distribution_file_parsed": true,
        "ansible_distribution_file_path": "/etc/redhat-release",
        "ansible_distribution_file_variety": "RedHat",
        "ansible_distribution_major_version": "8",
        "ansible_distribution_release": "NA",
        "ansible_distribution_version": "8.5",
        "discovered_interpreter_python": "/usr/libexec/platform-python"
    },
    "changed": false
    }
    centos1 | SUCCESS => {
        "ansible_facts": {
            "ansible_distribution": "CentOS",
            "ansible_distribution_file_parsed": true,
            "ansible_distribution_file_path": "/etc/redhat-release",
            "ansible_distribution_file_variety": "RedHat",
            "ansible_distribution_major_version": "8",
            "ansible_distribution_release": "NA",
            "ansible_distribution_version": "8.5",
            "discovered_interpreter_python": "/usr/libexec/platform-python"
        },
        "changed": false
    }
    centos3 | SUCCESS => {
        "ansible_facts": {
            "ansible_distribution": "CentOS",
            "ansible_distribution_file_parsed": true,
            "ansible_distribution_file_path": "/etc/redhat-release",
            "ansible_distribution_file_variety": "RedHat",
            "ansible_distribution_major_version": "8",
            "ansible_distribution_release": "NA",
            "ansible_distribution_version": "8.5",
            "discovered_interpreter_python": "/usr/libexec/platform-python"
        },
        "changed": false
    }
    ubuntu2 | SUCCESS => {
        "ansible_facts": {
            "ansible_distribution": "Ubuntu",
            "ansible_distribution_file_parsed": true,
            "ansible_distribution_file_path": "/etc/os-release",
            "ansible_distribution_file_variety": "Debian",
            "ansible_distribution_major_version": "22",
            "ansible_distribution_release": "jammy",
            "ansible_distribution_version": "22.04",
            "discovered_interpreter_python": "/usr/bin/python3"
        },
        "changed": false
    }
    ubuntu1 | SUCCESS => {
        "ansible_facts": {
            "ansible_distribution": "Ubuntu",
            "ansible_distribution_file_parsed": true,
            "ansible_distribution_file_path": "/etc/os-release",
            "ansible_distribution_file_variety": "Debian",
            "ansible_distribution_major_version": "22",
            "ansible_distribution_release": "jammy",
            "ansible_distribution_version": "22.04",
            "discovered_interpreter_python": "/usr/bin/python3"
        },
        "changed": false
    }
    ubuntu3 | SUCCESS => {
        "ansible_facts": {
            "ansible_distribution": "Ubuntu",
            "ansible_distribution_file_parsed": true,
            "ansible_distribution_file_path": "/etc/os-release",
            "ansible_distribution_file_variety": "Debian",
            "ansible_distribution_major_version": "22",
            "ansible_distribution_release": "jammy",
            "ansible_distribution_version": "22.04",
            "discovered_interpreter_python": "/usr/bin/python3"
        },
        "changed": false
    }
    
    ```

- one thing to keep on mind that `not for every module` the `skipped:true` or `filed:True` been enbabled so we need to keep that in mind

- hence we can use the `changed section of the registered output` which will be shown in both the registered output 

- we can use that in the `debug module` to see the `particular varaible value` as below based on `changed or skipped` as below

- we can write the playbook for the same as below 

    ```
        register_output.yaml
        --------------------

        ---

        - hosts: linux # using the linux host in here 
          

          tasks:

            - name: fetching the hostname of the target host in short form using command module 
              command : hostname -s # providing the command against the command module 
              register: hostname_output # here creating a register with the register directives in here 
              when: 
                -ansible_distribution == "CentOS" 
                - ansible_distribution_major_version| int >= 8
                # here  we are declaring multiple command with the option as list that we discussed
                # using the when directive without JINJA2 templating and with `and` condition as well
                # here using the JINJA2 filter called in converting it to the integer and comparing the value then 

            - name: grabing the register variable using the debug module 01
              debug: # using the debug module in here 
                var: hostname_output.stdout # accessing the stdout key of the registered output
                # the var attribute is mutually exclusive with the msg attribute
                # also we can use the `var` directly without the JINJA2 templating as its been in built to it  
              when: hostname_output.changed # this will provide the value as the True hence the debug can show that info

            - name: grabing the register variable using the debug module 02
              debug: # using the debug module in here 
                var: hostname_output.stdout # accessing the stdout key of the registered output
                # the var attribute is mutually exclusive with the msg attribute
                # also we can use the `var` directly without the JINJA2 templating as its been in built to it  
              when: not (hostname_output.changed) # this will provide the value as the False which is not changed or skipped one hence the debug can show that info

        ...  

        # if we execute the playbook in here 
        ansible-playbook register_output.yaml
        # then the output will be as 
        # here we can see that it got executed for centos ignoring the ubuntu


        PLAY [linux] ***************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************
        ok: [centos3]
        ok: [centos2]
        ok: [centos1]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [ubuntu3]

        TASK [fetching the hostname of the target host in short form using command module] *****************************************************************************************************
        skipping: [ubuntu1]
        skipping: [ubuntu2]
        skipping: [ubuntu3]
        changed: [centos1]
        changed: [centos2]
        changed: [centos3]

        TASK [grabing the register variable using the debug module] ****************************************************************************************************************************
        ok: [centos1] => {
            "hostname_output.stdout": "centos1"
        }
        ok: [centos2] => {
            "hostname_output.stdout": "centos2"
        }
        ok: [centos3] => {
            "hostname_output.stdout": "centos3"
        }
        skipping: [ubuntu1]
        skipping: [ubuntu2]
        skipping: [ubuntu3]

        TASK [grabing the register variable using the debug module 02] *************************************************************************************************************************
        skipping: [centos1]
        skipping: [centos2]
        skipping: [centos3]
        ok: [ubuntu1] => {
            "hostname_output.stdout": "VARIABLE IS NOT DEFINED!"
        }
        ok: [ubuntu2] => {
            "hostname_output.stdout": "VARIABLE IS NOT DEFINED!"
        }
        ok: [ubuntu3] => {
            "hostname_output.stdout": "VARIABLE IS NOT DEFINED!"
        }

        PLAY RECAP *****************************************************************************************************************************************************************************
        centos1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
        centos2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
        centos3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
        ubuntu1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
        ubuntu2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
    
    
    ```

- we can also use this to `install` the `patch package` if it `does not exist using the register with the when option`

- when the `change is true` then it will `install` the package else in case of `changes is false` it will not install the ackage 

- we can define the `ansible playbook` as below 

    ```
        register_output.yaml
        --------------------

        ---

        - hosts: linux # using the linux host in here 
          

          tasks:

            - name: fetching the hostname of the target host in short form using command module 
              command : hostname -s # providing the command against the command module 
              register: hostname_output # here creating a register with the register directives in here 
              when: 
                -ansible_distribution == "CentOS" 
                - ansible_distribution_major_version| int >= 8
                # here  we are declaring multiple command with the option as list that we discussed
                # using the when directive without JINJA2 templating and with `and` condition as well
                # here using the JINJA2 filter called in converting it to the integer and comparing the value then 


            - name: grabing the register variable using the debug module 01
              package: # using the package module in here 
                name: patch # installing the patch package in here
                state: present #defining the sate as present tom install the package
              when: hostname_output.changed # this will provide the value as the True hence the debug can show that info

        ...  
 
        # if we execute the playbook in here 
        ansible-playbook register_output.yaml
        # then the output will be as 
        # here we can see that it got executed for centos and ignore the ubuntu


        PLAY [linux] ***************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************
        ok: [centos2]
        ok: [centos3]
        ok: [centos1]
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [ubuntu3]

        TASK [fetching the hostname of the target host in short form using command module] *****************************************************************************************************
        skipping: [ubuntu1]
        skipping: [ubuntu2]
        skipping: [ubuntu3]
        changed: [centos2]
        changed: [centos1]
        changed: [centos3]

        TASK [grabing the register variable using the debug module 01] *************************************************************************************************************************
        skipping: [ubuntu1]
        skipping: [ubuntu2]
        skipping: [ubuntu3]
        ok: [centos3]
        ok: [centos2]
        ok: [centos1]

        PLAY RECAP *****************************************************************************************************************************************************************************
        centos1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=1    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
        ubuntu2                    : ok=1    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
        ubuntu3                    : ok=1    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
        
            
    
    ```

- we can also use the `is` directive tom mention `while checking the true or false boolean value`

- hence we can write this s below 

    ```

        register_output.yaml
        --------------------

        ---

        - hosts: linux # using the linux host in here 
          

          tasks:

            - name: fetching the hostname of the target host in short form using command module 
              command : hostname -s # providing the command against the command module 
              register: hostname_output # here creating a register with the register directives in here 
              when: 
                -ansible_distribution == "CentOS" 
                - ansible_distribution_major_version| int >= 8
                # here  we are declaring multiple command with the option as list that we discussed
                # using the when directive without JINJA2 templating and with `and` condition as well
                # here using the JINJA2 filter called in converting it to the integer and comparing the value then 


            - name: grabing the register variable using the debug module 01
              debug: # using the debug module
                var: hostname_output # outputing the registed output
              when: hostname_output is changed # this will provide the value as the True hence the debug can show that info



        ...  
    
        # if we execute the playbook in here 
        ansible-playbook register_output.yaml
        # then the output will be as 
        # here we can see that it got executed for centos ignoring the ubuntu

        PLAY [linux] ***************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************
        ok: [centos2]
        ok: [centos1]
        ok: [centos3]
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [ubuntu3]

        TASK [fetching the hostname of the target host in short form using command module] *****************************************************************************************************
        skipping: [ubuntu1]
        skipping: [ubuntu2]
        skipping: [ubuntu3]
        changed: [centos2]
        changed: [centos1]
        changed: [centos3]

        TASK [grabing the register variable using the debug module 01] *************************************************************************************************************************
        ok: [centos1] => {
            "hostname_output": {
                "changed": true,
                "cmd": [
                    "hostname",
                    "-s"
                ],
                "delta": "0:00:00.004194",
                "end": "2023-09-19 03:54:27.630751",
                "failed": false,
                "msg": "",
                "rc": 0,
                "start": "2023-09-19 03:54:27.626557",
                "stderr": "",
                "stderr_lines": [],
                "stdout": "centos1",
                "stdout_lines": [
                    "centos1"
                ]
            }
        }
        ok: [centos2] => {
            "hostname_output": {
                "changed": true,
                "cmd": [
                    "hostname",
                    "-s"
                ],
                "delta": "0:00:00.003260",
                "end": "2023-09-19 03:54:27.612278",
                "failed": false,
                "msg": "",
                "rc": 0,
                "start": "2023-09-19 03:54:27.609018",
                "stderr": "",
                "stderr_lines": [],
                "stdout": "centos2",
                "stdout_lines": [
                    "centos2"
                ]
            }
        }
        ok: [centos3] => {
            "hostname_output": {
                "changed": true,
                "cmd": [
                    "hostname",
                    "-s"
                ],
                "delta": "0:00:00.003411",
                "end": "2023-09-19 03:54:27.632329",
                "failed": false,
                "msg": "",
                "rc": 0,
                "start": "2023-09-19 03:54:27.628918",
                "stderr": "",
                "stderr_lines": [],
                "stdout": "centos3",
                "stdout_lines": [
                    "centos3"
                ]
            }
        }
        skipping: [ubuntu1]
        skipping: [ubuntu2]
        skipping: [ubuntu3]

        PLAY RECAP *****************************************************************************************************************************************************************************
        centos1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=1    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
        ubuntu2                    : ok=1    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
        ubuntu3                    : ok=1    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0  
    
    
    
    ```

- in the similar repect we can mention the `if the regiser output have the skipped info then we can install the patch package`

- this will help in installing the `patch package for the ubuntu OS` as it getting `skipped as a part of the centos check with the when condition on the preveious task`

- we can write the playbook for the same as 

    ```
        register_output.yaml
        --------------------

        ---

        - hosts: linux # using the linux host in here 
          

          tasks:

            - name: fetching the hostname of the target host in short form using command module 
              command : hostname -s # providing the command against the command module 
              register: hostname_output # here creating a register with the register directives in here 
              when: 
                -ansible_distribution == "CentOS" 
                - ansible_distribution_major_version| int >= 8
                # here  we are declaring multiple command with the option as list that we discussed
                # using the when directive without JINJA2 templating and with `and` condition as well
                # here using the JINJA2 filter called in converting it to the integer and comparing the value then 


            - name: grabing the register variable using the debug module 01
              debug: # using the debug module
                var: hostname_output # outputing the registed output
              when: hostname_output is skipped # this will provide the value as the True hence the debug can show that info



        ...  

        # if we execute this using the ansible playbook then we can see the info as below 
        ansible-playbook register_playbook.html


        PLAY [linux] ***************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************
        ok: [centos1]
        ok: [centos2]
        ok: [centos3]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [ubuntu3]

        TASK [fetching the hostname of the target host in short form using command module] *****************************************************************************************************
        skipping: [ubuntu1]
        skipping: [ubuntu2]
        skipping: [ubuntu3]
        changed: [centos3]
        changed: [centos2]
        changed: [centos1]

        TASK [grabing the register variable using the debug module 01] *************************************************************************************************************************
        skipping: [centos1]
        skipping: [centos2]
        skipping: [centos3]
        ok: [ubuntu1] => {
            "hostname_output": {
                "changed": false,
                "skip_reason": "Conditional result was False",
                "skipped": true
            }
        }
        ok: [ubuntu2] => {
            "hostname_output": {
                "changed": false,
                "skip_reason": "Conditional result was False",
                "skipped": true
            }
        }
        ok: [ubuntu3] => {
            "hostname_output": {
                "changed": false,
                "skip_reason": "Conditional result was False",
                "skipped": true
            }
        }

        PLAY RECAP *****************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
        centos2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
        centos3                    : ok=2    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
        ubuntu1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
        ubuntu2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0  
    

    ```

- through the help of `register and when` we can target ` target host` `based on their outcome`

# NOTE:

- we can also use the `python get()` to get the value from the `ansible playbook` as well



