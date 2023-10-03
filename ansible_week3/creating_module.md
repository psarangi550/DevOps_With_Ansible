# Creating Modules

- here we will be looking at `downloading` the `Ansible source code`

- then we will be looking at `Using the Developer Hacking tool to interrogate the Ansible module` behind the `backround`

- we will looking into the `structure of the ansible module` and how to `report` the `success or error condition` 

- we will also be looking at `creating a ping module in shell script`

- using the `Leverage of the Ansible module framework` we will convert the `shell script` to a `python script`

- here we will display the `debug info for any failure`    

- the topic of `creating_module` can `initially sound challenging` but lit can be `done in any scripting or programming language`

- there are few adv of using `python language` hence we will use `python to create module`

-  **Case01** 

   - here we will create a `ansible custom module` named as `icmp ping` which is for `Internet Control Message Protocol`
   
   - the `ping` present inside the `Ansible module` is an `Ansible ping i.e just a connection check`
   
   - here we will create a `network icmp ping` using the `shell script` by creating a `custom ping module`
   
   - but before going into the `creating the shell script and using it as the custom module` we can look at the `ansible source code`
   
   - we can `clone the source code` as `git clone https://github.com/ansible/ansible.git` in order to clone the `ansible into` `hoe directory of the User` i.e `/home/<user>`
   
   - here we will be using the `test-module` of the `ansible source code to test the built-in ansible module` 
   
   - also we will be changing  the `python3 location on the test-module.py by changin it to` from `#!/usr/bin/env python` to `#!/usr/bin/env python3` inside the `test-module` which is present in `~/ansible/hacking/test-module.py`
   
   - then we can use the `test-module` as an `python module to execute command on some other module`
   
   - we can use the command as below 

    ```shell
        # but before doing that in ansible 2.14 we need to set the  environment for running the ansible source code command 
        source ~/ansible/hacking/env-setup
        # this will first st the PATH,PYTHONPATH for reference 
        ~/ansible/hacking/test-module -m  ~/ansible/lib/ansible/modules/command.py -a hostname
        # when we specify the test-module then it identify python as the executable
        # here we are utilizing the test-module to execute the `command module which is present in ~/ansible/lib/ansible/modules/command.py`
        # here we need to provide the actual location of the `module that we want to execute`
        # also we can utilize the test-module.py file instead of test-module as below 
        ~/ansible/hacking/test-module.py -m  ~/ansible/lib/ansible/modules/command.py -a hostname
        # when we specify the test-module.py then it identify python as the executable
        # here as we are providing the valid args  against the `-a` option then we can get a JSON Message as below 
        # for the successful one we have the `changed`, `rc` and `stdout` in the `returned JSON
        # the output will be as below 
        * including generated source, if any, saving to: /home/ansible/.ansible_module_generated
        * ansiballz module detected; extracted module source to: /home/ansible/debug_dir
        ***********************************
        RAW OUTPUT

        {"changed": true, "stdout": "ubuntu-c", "stderr": "", "rc": 0, "cmd": ["hostname"], "start": "2023-10-01 22:57:22.463257", "end": "2023-10-01 22:57:22.468990", "delta": "0:00:00.005733", "msg": "", "invocation": {"module_args": {"_raw_params": "hostname", "_uses_shell": false, "expand_argument_vars": true, "stdin_add_newline": true, "strip_empty_ends": true, "argv": null, "chdir": null, "executable": null, "creates": null, "removes": null, "stdin": null}}}


        ***********************************
        PARSED OUTPUT
        {
            "changed": true,
            "cmd": [
                "hostname"
            ],
            "delta": "0:00:00.005733",
            "end": "2023-10-01 22:57:22.468990",
            "invocation": {
                "module_args": {
                    "_raw_params": "hostname",
                    "_uses_shell": false,
                    "argv": null,
                    "chdir": null,
                    "creates": null,
                    "executable": null,
                    "expand_argument_vars": true,
                    "removes": null,
                    "stdin": null,
                    "stdin_add_newline": true,
                    "strip_empty_ends": true
                }
            },
            "msg": "",
            "rc": 0,
            "start": "2023-10-01 22:57:22.463257",
            "stderr": "",
            "stdout": "ubuntu-c"
        }


        # but when we wxecut e the wrong command we can see the fiels as `failed`, `message`, `rc` value as well
        ~/ansible/hacking/test-module.py -m  ~/ansible/lib/ansible/modules/command.py -a xxyyzz
        # the output will be as below 

        * including generated source, if any, saving to: /home/ansible/.ansible_module_generated
        * ansiballz module detected; extracted module source to: /home/ansible/debug_dir
        ***********************************
        RAW OUTPUT

        {"rc": 2, "stdout": "", "stderr": "", "cmd": "xyz", "failed": true, "msg": "[Errno 2] No such file or directory: b'xyz'", "invocation": {"module_args": {"_raw_params": "xyz", "_uses_shell": false, "expand_argument_vars": true, "stdin_add_newline": true, "strip_empty_ends": true, "argv": null, "chdir": null, "executable": null, "creates": null, "removes": null, "stdin": null}}}


        ***********************************
        PARSED OUTPUT
        {
            "cmd": "xyz",
            "failed": true,
            "invocation": {
                "module_args": {
                    "_raw_params": "xyz",
                    "_uses_shell": false,
                    "argv": null,
                    "chdir": null,
                    "creates": null,
                    "executable": null,
                    "expand_argument_vars": true,
                    "removes": null,
                    "stdin": null,
                    "stdin_add_newline": true,
                    "strip_empty_ends": true
                }
            },
            "msg": "[Errno 2] No such file or directory: b'xyz'",
            "rc": 2,
            "stderr": "",
            "stdout": ""
        }
    
    
    ```

- if we have the `command execute successfully` then it can be having parameter such as `changed or stdout or rc where rc will be 0 for success` in JSON Format

- if we have the `command not executed successfully` then we wil get the result with parameter in as `failed or message or rc which no negetive value` in JSON Format

- here we will be mimicing the `JSON Output having the same format as we have mentioned earlier` from `shell script`

- we can develope the `shell script` as below 

    ```shell
        icmp.sh
        ========
        #!/bin/bash   #using the shabang
        ping -c 1 127.0.0.1 >/dev/null 2>/dev/null
        # here we are using the ping command and redirect the  stream to /dev/null folder
        if [ $? == 0 ]; # checking the last command executed successfullt or not
        then
        echo "{\"changed\": true, \"rc\": 0}" # echoing the message as success format JSON
        else
        echo "{\"failed\": true, \"msg\": \"failed to ping\", \"rc\": 1}" # echoing the message as failed format JSON
        fi
    
    ```
- now when we execute the `shell script` then it will send the reponse as `{"changed":true, "rc":0}` because the `ping command run successfully` else it will throw the `{"failed":true,"msg":"failed to ping", "rc": 1}` if the ping command not successful which can be `defined in the below`

    ```shell
        icmp.sh
        ========
        #!/bin/bash   #using the shabang
        ping -c 1 129.0.0.1 >/dev/null 2>/dev/null
        # here we are using the ping command and redirect the  stream to /dev/null folder
        if [ $? == 0 ]; # checking the last command executed successfullt or not
        then
        echo "{\"changed\": true, \"rc\": 0}" # echoing the message as success format JSON
        else
        echo "{\"failed\": true, \"msg\": \"failed to ping\", \"rc\": 1}" # echoing the message as failed format JSON
        fi
    
    ```

- we can also take help of the `ansible source code test-module` to `show its output JSON file`

- we can execute that as below for the `1st` and `2nd case`

    ```bash
        # for the 1st case
        ~/ansible/hacking/test-module.py -m icmp.sh 
        # here we are using the ansible tyest-module to execute the shell or bash script over here 
        #now we can see the output as below 
        * including generated source, if any, saving to: /home/ansible/.ansible_module_generated
        ***********************************
        RAW OUTPUT
        {"changed": true, "rc": 0}


        ***********************************
        PARSED OUTPUT
        {
            "changed": true,
            "rc": 0
        }
        # for the 2nd case 
        ~/ansible/hacking/test-module.py -m icmp.sh
        #here will be the output
        * including generated source, if any, saving to: /home/ansible/.ansible_module_generated
        ***********************************
        RAW OUTPUT
        {"failed": true, "msg": "failed to ping", "rc": 1}


        ***********************************
        PARSED OUTPUT
        {
            "failed": true,
            "msg": "failed to ping",
            "rc": 1
        }
            
    ```


- the `ansible custom module` can be written in `any language` as long as they provide the `JSON Return output in the mentioned JSON format`

- here while escaping the characters we need to take care that `both the containting and escaping character is of (double quotes in shell script)`

-  we can use the `ansible source code test-module` which will help in `executing the shell script as below`

    ```bash
        # ansible test module can help execute the  shell script that we ahve 
        ~/ansible/hacking/test-module -m icmp.sh
        or
        ~/ansible/hacking/test-module.py -m icmp.sh
        # executing the shell script as the module using the test-module utility which will help in telling its an python executable 
        # here will be the following result
        * including generated source, if any, saving to: /home/ansible/.ansible_module_generated
        ***********************************
        RAW OUTPUT
        {"change":true , "rc":0}


        ***********************************
        PARSED OUTPUT
        {
            "change": true,
            "rc": 0
        }
        # we can  get the failed result for failed icmp.sh script as 2nd one above
        # then the ouput will be as 
        ~/ansible/hacking/test-module.py -m template/icmp.sh -a 'target=128.0.0.1'
        # here providing the -a option means we are providing the target value to the icmp.sh script 
        # then the output will be as 
        * including generated source, if any, saving to: /home/ansible/.ansible_module_generated
        ***********************************
        RAW OUTPUT
        { "failed":true , "rc":1, "msg": "cannot ping"}


        ***********************************
        PARSED OUTPUT
        {
            "failed": true,
            "msg": "cannot ping",
            "rc": 1
        }


    ```

- if we are looking to the `icmp.sh` file which took an `aegs` as below 

    ```bash
        icmp.sh
        ========
        #!/bin/bash
        source $1 >/dev/null  2>/dev/null

        # ansible custom/built in module expect all the variable should be passed as file 
        # which will `appear` as the `1st argument to the script`
        # when we use the `test-module` also `snaible build in module` hence expect the `1st argument of the script is the file`
        # it will read through the `read the  content of the file` and `then compare that to the argument provided`
        # when the args matching `content of the script file` then that will called as the content 

        # when we execute the command as `~/ansible/hacking/test-module -m icmp.sh -a 'target=centos1' `
        # then it will first read the entire content of the shell script or custom module content as the file 
        # then it compare the value provided with command -a `target=centos1` then target match the file content of the shell script's target
        # hence in here the `target` considered as the variable  


        # own language
        --------------

        # every variable need to passed to the module as we are using this shell script as module
        # when this module executed then the test-module take the content of the module pass to it 
        # then when we define the argument that we want to pass then ansible will perform a check if the  content match then that args will be called as variable with corresponding value 
        # when we pass this module to the test-module then it will read the ntire content
        # then when we peovide args that matched to the module then that cosiderd as the variable 
        # here in this case we are passing the target as the variable as it checked against the content of the shell script to considered as variable 

        TARGET = ${target:-127.0.0.1}  # here we are defining the variable with the value  

        ping -c 2 ${TARGET} >/dev/null 2>/dev/null  # here the ping module uses the user provided value of target

        if [ $? == 0 ]
        then 
        echo "{\"changed\": true,\"rc\":0}" 
        else
        echo "{\"failed\": true, \"msg\": \"failed to ping\", \"rc\": 1}"
        fi    
    
    ```

- we can also provide the `wrong host as below` then we can see the below output 

    ```bash
        ~/ansible/hacking/test-module.py -m template/icmp.sh -a 'target=centos4'
        # here we can see that centos4 does not exist hence in this case we will be getting a failed reponse as below 

        * including generated source, if any, saving to: /home/ansible/.ansible_module_generated
        ***********************************
        RAW OUTPUT
        { "failed":true , "rc":1, "msg": "cannot ping"}


        ***********************************
        PARSED OUTPUT
        {
            "failed": true,
            "msg": "cannot ping",
            "rc": 1
        }
            
    
    ```

- if we see the `output` we can see the `source been wriiten to the /home/ansible/.ansible_module_generated`

- we can also fetch the `argument that pass which become variable ` then we can see that as `/home/ansible/.ansible_test_module_arguments`

- we can mimic the `behaviour of the test-module` as below 

    ```bash
        /home/ansible/.ansible_module_generated /home/ansible/.ansible_test_module_arguments
        # here when we execute this we can see the same output we get earlier 
        # because in here the /home/ansible/.ansible_module_generated  where the variable as file been parsed which is our shell script as the source
        # /home/ansible/.ansible_test_module_arguments will show the args we passed to it 
        # which can be seen using the command as `cat /home/ansible/.ansible_module_generated` or `cat /home/ansible/.ansible_test_module_arguments`
        # we can se the outcome as same as the before run one 
        { "failed":true , "rc":1, "msg": "cannot ping"}

    ```

- **Case2**
  
  - the `ansible` expect the `custom module to be in the directory` called as the `library` which is being relative to the `ansibe-playbook`
  
  - `we can define the module i.e shell script module` in the `library` folder the  `library/icmp.sh`
  
  - we can define the `playbook` as below 

    ```yaml

        custom_playbook.yaml
        =====================
        ---

        - hosts: linux  # targeting the linux host here 
        
          tasks:
            - name: custom module executing in here
              icmp:
                taget: 127.0.0.1

            - name: custom module executing in here 
              icmp:
                target: 128.0.0

        ...


        # in case of the trouble we can use the below module which will set the python3 as python
        # sudo apt install python-is-python3
        # we also need to define the custom module as below 
     bash
        library/icmp
        ============
        #!/bin/bash
        source $1 >/dev/null  2>/dev/null

        # ansible custom/built in module expect all the variable should be passed as file 
        # which will `appear` as the `1st argument to the script`
        # when we use the `test-module` also `snaible build in module` hence expect the `1st argument of the script is the file`
        # it will read through the `read the  content of the file` and `then compare that to the argument provided`
        # when the args matching `content of the script file` then that will called as the content 

        # when we execute the command as `~/ansible/hacking/test-module -m icmp.sh -a 'target=centos1' `
        # then it will first read the entire content of the shell script or custom module content as the file 
        # then it compare the value provided with command -a `target=centos1` then target match the file content of the shell script's target
        # hence in here the `target` considered as the variable  


        # own language
        --------------

        # every variable need to passed to the module as we are using this shell script as module
        # when this module executed then the test-module take the content of the module pass to it 
        # then when we define the argument that we want to pass then ansible will perform a check if the  content match then that args will be called as variable with corresponding value 
        # when we pass this module to the test-module then it will read the ntire content
        # then when we peovide args that matched to the module then that cosiderd as the variable 
        # here in this case we are passing the target as the variable as it checked against the content of the shell script to considered as variable 

        TARGET = ${target:-127.0.0.1}  # here we are defining the variable with the value  

        ping -c 2 ${TARGET} >/dev/null 2>/dev/null  # here the ping module uses the user provided value of target

        if [ $? == 0 ]
        then 
        echo "{\"changed\": true,\"rc\":0}" 
        else
        echo "{\"failed\": true, \"msg\": \"failed to ping\", \"rc\": 1}"
        fi   
        

        # now when  we execute the ansible-playbook as 
        # ansible-playbook custom_playbook.yaml
        # then the output will be as below 

        [WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under development. This is
        a rapidly changing source of code and can become unstable at any point.

        PLAY [linux] ***************************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************************
        ok: [centos2]
        ok: [centos1]
        ok: [centos3]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [ubuntu3]

        TASK [custom module executing in here] *************************************************************************************************************************************************************
        ok: [centos1]
        ok: [centos2]
        ok: [centos3]
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [ubuntu3]

        TASK [custom module executing in here] *************************************************************************************************************************************************************
        fatal: [centos1]: FAILED! => {"changed": false, "msg": "cannot ping", "rc": 1}
        fatal: [centos2]: FAILED! => {"changed": false, "msg": "cannot ping", "rc": 1}
        fatal: [centos3]: FAILED! => {"changed": false, "msg": "cannot ping", "rc": 1}
        fatal: [ubuntu1]: FAILED! => {"changed": false, "msg": "cannot ping", "rc": 1}
        fatal: [ubuntu2]: FAILED! => {"changed": false, "msg": "cannot ping", "rc": 1}
        fatal: [ubuntu3]: FAILED! => {"changed": false, "msg": "cannot ping", "rc": 1}

        PLAY RECAP *****************************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=2    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=2    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=2    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=2    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0    
    
    
    ```

- **Case3**
  
  - if we want we can use the `python as a module as well in here inside the library directory`
  
  -  here we can write the `ansible custom module`  by using it as below 

    ```python 
        library/icmp.py
        ===============

        
        # defining the documentation yaml
        ANSIBLE_METADATA = {
            'metadata_version': '1.1',
            'status': ['preview'],
            'supported_by': 'community'
        }

        DOCUMENTATION = '''
        ---
        module: icmp

        short_description: simple module for icmp ping

        version_added: "2.10"

        description:
            - "simple module for icmp ping"

        options:
            target:
                description:
                    - The target to ping
                required: true

        author:
            - James Spurin (@spurin)
        '''

        EXAMPLES = '''
        # Ping an IP
        - name: Ping an IP
        icmp:
            target: 127.0.0.1

        # Ping a host
        - name: Ping a host
        icmp:
            target: centos1
        '''

        RETURN = '''
        '''
        #! /usr/bin/env python/python3
        from ansible.module_utils.basic import AnsibleModule 
        # importing the AnsibleModule class from ansible.module_utils.basic folder

        def run_command(): # defining the run_command function in here 
            
            module_args=dict(
                target=dict(type='str', required=True)
            ) # defining the module parameter as the target which is having type as str and required params

            result=dict(
                changed: False # defining the changed as False in here 
            )

            module=AnsibleModule(argument_spec=module_args,supports_check_mode=True)

            if module.check_mode: # if the check mode actiavted then 
                retrun result

            print_json=module.run_command(f"ping -c 2 {module.params['target']}")
            # using the run_command method on the module object we can eun the particular command 
            # defining the ping command with the passing target argument
            # now we can put the condition as below 

            if module.params["target"]: # if the target option exist in the module pasrams 
                result["debug"] = print_json
                # here with the debug we are showing the entire code of debug message
                # printing the entire command as debug 
                # considering the first args as the return code 
                result["rc"]= print_json[0]
                # adding the return case
                if  result["rc"]: # if the return code is successful then 
                    result["failed"= True]
                    module.fail_json(msg="cant ping",**result)
                    # here we are packing the fail_json with the result dictionary which will introduce the failed as true  dict to unpack and JSON return value
                else:
                    module.exit_json(**result)
                    # here as the rc==0 hence th command passed successfully and here we are just processing the result as the dict to unpack and JSON return valu

    ```

- we can execute this as `ansible developer Hacking Test module` as below

    ```bash
        ~/ansible/hacking/test-module -m library/icmp.py -a 'target=127.0.0.1'
        # here using the ansible Hacking test-module using which we are executing the command 
        # then the output as below 
         including generated source, if any, saving to: /home/ansible/.ansible_module_generated
        * ansiballz module detected; extracted module source to: /home/ansible/debug_dir
        ***********************************
        RAW OUTPUT

        {"changed": true, "debug": [0, "PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.\n64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.064 ms\n64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.035 ms\n\n--- 127.0.0.1 ping statistics ---\n2 packets transmitted, 2 received, 0% packet loss, time 1015ms\nrtt min/avg/max/mdev = 0.035/0.049/0.064/0.014 ms\n", ""], "rc": 0, "invocation": {"module_args": {"target": "127.0.0.1"}}}


        ***********************************
        PARSED OUTPUT
        {
            "changed": true,
            "debug": [
                0,
                "PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.\n64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.064 ms\n64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.035 ms\n\n--- 127.0.0.1 ping statistics ---\n2 packets transmitted, 2 received, 0% packet loss, time 1015ms\nrtt min/avg/max/mdev = 0.035/0.049/0.064/0.014 ms\n",
                ""
            ],
            "invocation": {
                "module_args": {
                    "target": "127.0.0.1"
                }
            },
            "rc": 0
        }
    
    ```

- in `python` there are `lot of templated code available for writing the own ansible custom module`

- we get the `command line args and output` are able to get in here 

- we can also run the `Documentation` using the `ansible-doc` command line

- we can provide the `example and return YAML` while defining the `ansible custom module as python`

- if we want to `publish the custom ansible module` to the `ansible source` then `it can fullfill the requirement`   

- we can also use the `other module such as command/setup/ etc` inside `our custom module`

- we can see the documentation for that inside 

    - [Ansible Custom Module python](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html)

- this can `provide the sample temple for the python module in here which can be reused`


- now when we define the `custom_playbook` as below and `execute then the repsonse as below`

    ```yaml

        custom_playbook.yaml
        =====================
        ---

        - hosts: linux  # targeting the linux host here 
        
          tasks:
            - name: custom module executing in here
              icmp:
                taget: 127.0.0.1

            - name: custom module executing in here 
              icmp:
                target: 128.0.0

        ...

        # now when we execute the command the output will be as below 
    
        [WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under development. This is
        a rapidly changing source of code and can become unstable at any point.

        PLAY [linux] ***************************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************************
        ok: [centos3]
        ok: [centos2]
        ok: [centos1]
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [ubuntu3]

        TASK [custom module executing in here] *************************************************************************************************************************************************************
        fatal: [centos3]: FAILED! => {"changed": false, "msg": "missing required arguments: target"}
        fatal: [centos1]: FAILED! => {"changed": false, "msg": "missing required arguments: target"}
        fatal: [centos2]: FAILED! => {"changed": false, "msg": "missing required arguments: target"}
        fatal: [ubuntu1]: FAILED! => {"changed": false, "msg": "missing required arguments: target"}
        fatal: [ubuntu2]: FAILED! => {"changed": false, "msg": "missing required arguments: target"}
        fatal: [ubuntu3]: FAILED! => {"changed": false, "msg": "missing required arguments: target"}

        PLAY RECAP *****************************************************************************************************************************************************************************************
        centos1                    : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
    
    
    ```

- now we check the `ansible-doc` command to see the `output` then we can see that it will `display the documentation `

- the poutput in here will be as 

    ```bash
        ansible-doc -M library icmp
        # here we are deining the library as the module in here 
        # then we can see thebelow output
        # then will weill display the documetation as below if the documetation defined 
        > ICMP    (/home/ansible/diveintoansible/Creating Modules and Plugins/Creating Modules/template/library/icmp.py)

                simple module for icmp ping

        ADDED IN: version 2.10

        OPTIONS (= is mandatory):

        = target
                The target to ping


        AUTHOR: James Spurin (@spurin)

        METADATA:
        metadata_version: '1.1'
        status:
        - preview
        supported_by: community


    ```