# <ins> Ansible Playbooks, Facts </ins> #

- we learn that `setup` module being run `for every iteration of playbook automatically on execution of the playbook` and gather `system info about the target system as variable`  or `gather facts about the target system as variables`

- we will look into the `facts module` as well , how to use `filter` for specific `facts`

- by default `ansible` provide `many facts` `by default `, but `there might be a requirement to gather more info or facts`

- `if we have the requirement of gather more facts` then we can `create and execute` the `custom facts`

- we can see `how to use the custom facts` in the `environment` wuthout the `super user access`

- the oofcial documentation been provided in 

    [Ansible Setup module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/setup_module.html)

- by using this `setup module` we can gather the `subset of facts`

- This module is automatically called by playbooks to gather useful variables about remote hosts that can be used in playbooks

- It can also be executed directly by /usr/bin/ansible to check what variables are available to a host

- This module is also supported for Windows targets.

# <ins> How to Fetch the Subset (Network) Which is a Part of Ansible Facts </ins> #

- lets take an example to capture the `subset info of network facts` using the `setup modiule` and using `ansible ad hoc command` against the `centos1 target hosts`

- we can gather the `subset of network facts` using the `ansible adhoc command` with `setup module` by using the `agther_subset arguement` as below 

    ```
        # the command can be written as below 
        ansible centos1 -m setup -a 'gather_subset=network'
        # here we are providing the args to the gather_subset over here as network
        # also we are providing the it against the target host as centos1
        # we are using the setup module in here

    ```

- eventhough we have provided the `gather_subset=network` , but still we will be getting a lot of info about the `facts as JSON`

- by defult the `gather_subset with the required subset of facts` but will include the `minimum subset of facts selection` as well as the `all subset of facts selection`

- but we can ignore thesee by using the `!all,!min` along `with the required subset of facts` as below 

    ```
        # the command can be written as below 
        ansible centos1 -m setup -a 'gather_subset=network !all !min'
        # here we are providing the args to the gather_subset over here as network
        # also we are providing the it against the target host as centos1
        # we are using the setup module in here
        # here we are also removing the minimum selection subset of facts and all selection subset of facts

    ```

- when we add the `!` to a `provided subset` then `we are stating` `not to provide those info or facts` i.e excluding these `facts which provided by ! symbol` 

- we can now see that those calue come from the above 2 code block , but we are still getting a lot of info

- we can compare the value outputted using the command as `wc -l` which is for `word count` as below 

    ```
        
        # the command can be written as below 
        ansible centos1 -m setup -a 'gather_subset=network' | wc -l
        # here we are providing the args to the gather_subset over here as network
        # also we are providing the it against the target host as centos1
        # we are using the setup module in here
        # here also we are using the wc- l to see the total line count by the -l option
        # and we can observe that we are getting more output in this case as we are not filtering the `all and min`


        # the command can be written as below 
        ansible centos1 -m setup -a 'gather_subset=network !all !min'
        # here we are providing the args to the gather_subset over here as network
        # also we are providing the it against the target host as centos1
        # we are using the setup module in here
        # here we are also removing the minimum selection subset of facts and all selection subset of facts
        # and we can observe that we are getting less output in this case as we are filtering the `all and min`
    
    
    ```

- in case where we are not `excluding the all and min` then the `output value will be more` but in case of `including the !all and !min` in that case the output will be higher for the `word count` 

- an alternate option is to use the `filter option`  as the `argument of the setup module`

- the `filter` option can be able to use `subset of facts` as `keyword` `directly`

- we can use this as below 

    ```
        ansible centos1 -m setup -a  'filter=<subset of facts>'
        # here when we use the filter and against thyat we can provide the subset of tasks
        # also we can see that this will providing the output in specific format 
        # also we are providing the it against the target host as centos1
        # we are using the setup module in here
        # here also we are using the filter as an option over here
    
        # the output will be in the format of 
        < Target host> | SUCCESS => {
            "ansible_facts": {
                "<subset of facts>": <value>
                "discovered_interpreter_python": "/usr/libexec/platform-python"
            },
            "changed": false
        }

        # exmple if we are trying to fetch for the subset of filter as `all_ipv4_addresses` then we can do that using it as 
        ansible centos1 -m setup -a  'filter=all_ipv4_addresses'
        # here when we use the filter and against thyat we can provide the subset of tasks
        # also we can see that this will providing the output in specific format 
        # also we are providing the it against the target host as centos1
        # we are using the setup module in here
        # here also we are using the filter as an option over here

        # the output will be as 

        centos1 | SUCCESS => {
        "ansible_facts": {
            "ansible_all_ipv4_addresses": [
                "172.18.0.5"
            ],
            "discovered_interpreter_python": "/usr/libexec/platform-python"
        },
        "changed": false
    }

    
    ```

- we can also use the `filter args of the setup module` with the help of `wildcards as subset of values`

- we can use the `filter args of setup module with wildcards values` as below 

    ```
        # exmple if we are trying to fetch for the subset of filter as `all_ipv4_addresses` as `all_ipv4` wild card then we can do that using it as 
        ansible centos1 -m setup -a  'filter=all_ipv4*'
        # here when we use the filter and against thyat we can provide the subset of tasks
        # also we can see that this will providing the output in specific format 
        # also we are providing the it against the target host as centos1
        # we are using the setup module in here
        # here also we are using the filter as an option over here

         # the output will be as 

        centos1 | SUCCESS => {
        "ansible_facts": {
            "ansible_all_ipv4_addresses": [
                "172.18.0.5"
            ],
            "discovered_interpreter_python": "/usr/libexec/platform-python"
        },
        "changed": false
        }

    
    ```

- in the `ansible variable section` we `access` the `variables in many different ways` , we can use the same prinicple `to access the specific facts about the remote hosts` 

- when the `playbook` `execute` the `gathering of facts` using the `gather_facts:True` in the `hosts` section of the playbook , then those facts collected will be placed in the `variable namespace of the ansible playbook` and `are accessable for each host`

- if we take look onto the `ansible facts` we can access the `ip address` by using the `ansible adhoc command` as below 

    ```
        ansible centos1 -m setup | more
        # her we will get all the Large JSON output
        # but if we are going through these then we can see we can access the ip address using the value as 
        ansible_facts-->ansible_default_ipv4---> addresses
        # using the below path we can access the particular value fom the JSON file that been return from the ansible ashoc command 
    

    ```

- we have the `ansible_facts` as the top of the `JSON output we got from ansible adhoc command`

- these `ansible_facts` known as the `ansible idiom` , when a `ansible module(Any Module not just the setup module)` `return` a `dictionary` with the `ansible_facts` as the `key` then it wil be added to the `root of the facts namespace` i.e `ansible` will `automatically` `add` the ` those variable aginst the ansible_facts` to the `root of the guest that is running the module`

- to put it in simple words `everything under the ansible_facts` will automatically go into `root of variable namespace in the ansible playbook`

- Essentially we can ignore the `ansible_facts` key while accessing the `ansible_facts` and using it as `variables` in the `ansible playbook`

- there is no `variable` named as `ansible_facts` from the `context` of the `variable namespace in the playbook` , but the `content underneath the ansible_facts` are directly `available` for the `variable namespace of the playbook` which can be `accessed directly with their  key name`

- we can see this with the help of a playbook as below 


    ```
        facts_playbook.yaml
        -------------------

        ---
        
        - hosts:centos1
          user:root

          tasks:
            - name: Fact Variable Accessing
              debug:
                msg: "{{ansible_default_ipv4.address}}"
                # here we are accessing the facts variable directly without providing the parent `ansible_facts`
                # but we can also using JINJA2 template for the same reference       

        ...

        # now when we execute the `playbook` with the command as `ansible-playbook facts_playbook.yaml`
        # then we are able to see the info of particular facts against the message key
        # here the output will be in the format as 

        PLAY [centos1] ****************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [centos1]

        TASK [Code Snippet for accessing the facts variable] **************************************************************************************************************************************************
        ok: [centos1] => {
            "msg": "172.18.0.5"
        }

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 

    ```

- here we are not accessing the firstlavel using the `ansible_facts` as that is not `saved to the variable namespace of ansible playbook` but we can access the `value underneath the same using it ` as `ansible_default_ipv4.address` which is in the `1 level down`

- we can also use the `bracket notation` instead of the `dot notation` as below ``ansible_default_ipv4['address']``

- we can use it as below 

    ```
        facts_playbook.yaml
        -------------------

        ---
        
        - hosts:centos1
          user:root

          tasks:
            - name: Fact Variable Accessing
              debug:
                msg: "{{ansible_default_ipv4['address']}}"
                # here we are accessing the facts variable directly without providing the parent `ansible_facts`
                # but we can also using JINJA2 template for the same reference       

        ...

        # now when we execute the `playbook` with the command as `ansible-playbook facts_playbook.yaml`
        # then we are able to see the info of particular facts against the message key
        # here the output will be in the format as 
        
        PLAY [centos1] ****************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [centos1]

        TASK [Code Snippet for accessing the facts variable] **************************************************************************************************************************************************
        ok: [centos1] => {
            "msg": "172.18.0.5"
        }

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
    

    ```

- if we want we can also get it for  all the hosts `all/linux target hosts` as below 

- we can also change to `all` in order to test it against all the `all target hosts`

    ```

        facts_playbook.yaml
        -------------------

        ---
        
        - hosts:linux
          user:root

          tasks:
            - name: Fact Variable Accessing
              debug:
                msg: "{{ansible_default_ipv4['address']}}"
                # here we are accessing the facts variable directly without providing the parent `ansible_facts`
                # but we can also using JINJA2 template for the same reference       

        ...

        # now when we execute the `playbook` with the command as `ansible-playbook facts_playbook.yaml`
        # then we are able to see the info of particular facts against the message key
        # here the output will be in the format as 
        
        PLAY [linux] ******************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu2]
        ok: [ubuntu3]
        ok: [ubuntu1]
        ok: [centos1]
        ok: [centos2]
        ok: [centos3]

        TASK [Code Snippet for accessing the facts variable] **************************************************************************************************************************************************
        ok: [ubuntu1] => {
            "msg": "172.18.0.4"
        }
        ok: [ubuntu2] => {
            "msg": "172.18.0.9"
        }
        ok: [ubuntu3] => {
            "msg": "172.18.0.3"
        }
        ok: [centos1] => {
            "msg": "172.18.0.5"
        }
        ok: [centos2] => {
            "msg": "172.18.0.6"
        }
        ok: [centos3] => {
            "msg": "172.18.0.7"
        }

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 


    # we can also use it with the `all target host` as below 

    facts_playbook.yaml
    -------------------

        ---
        
        - hosts:all

          tasks:
            - name: Fact Variable Accessing
              debug:
                msg: "{{ansible_default_ipv4['address']}}"
                # here we are accessing the facts variable directly without providing the parent `ansible_facts`
                # but we can also using JINJA2 template for the same reference       

        ...

        # now when we execute the `playbook` with the command as `ansible-playbook facts_playbook.yaml`
        # then we are able to see the info of particular facts against the message key
        # here the output will be in the format as 


        PLAY [all] ********************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [centos1]
        ok: [ubuntu2]
        ok: [ubuntu3]
        ok: [ubuntu1]
        ok: [centos2]
        ok: [centos3]

        TASK [Code Snippet for accessing the facts variable] **************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "172.18.0.2"
        }
        ok: [ubuntu1] => {
            "msg": "172.18.0.4"
        }
        ok: [ubuntu2] => {
            "msg": "172.18.0.9"
        }
        ok: [ubuntu3] => {
            "msg": "172.18.0.3"
        }
        ok: [centos1] => {
            "msg": "172.18.0.5"
        }
        ok: [centos2] => {
            "msg": "172.18.0.6"
        }
        ok: [centos3] => {
            "msg": "172.18.0.7"
        }

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu-c                   : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


    ```

# <ins> How to Use Custom Facts in Ansible Playbook </ins> #

- although `ansible` provide `multiple fact as useful info about the hosts as variables`, we might require `some additional facts` for the `from a target host` which is not provided by `ansible setup module facts` 

- we can write the `custom facts` can be written in `any language`

- but it will return a `JSON Structure` or `ini structure`

- `by default `the `custom facts` while be checked in `/etc/ansible/facts.d` directory where we will but our `custom facts executable script`

- when we write the `custom facts` then those facts will be gather as a part of `gather_facts:True` process

- any script which return a `JSON or INI` structure can be considered as the `custom facts`

- ansible custom fact path `/etc/ansible/facts.d` path will be desirable when we have the `root privileges`

- but if we don't have the `root user access for the target host` or `we want out custom facts configuration out of the root user file system` then we can `address this later ` and find a `workaround` for the same 

- the extension of the `custom fact script` will be in the format of `*.fact` but we can write the `return a structure JSON Or INI format which can be any type script that we can execute`

- the `custom facts script(which can be any script) should return JSON/INI via stdout`

- but while returning through the `INI` format we need to keep in mind that `the INI file structure should be` in the form of as below

    ```

        [block] # here we need to define the `category block` under which we want to show the result 
        <block>=<value> # the corresponding result of that 
    
    ```

- if we are returning the `INI format from custom fact executable script` then we will `fail` as the `block been mandetory for the same`

- we then have to create the directory as `/etc/ansible/facts.d` folder here using the command as `sudo mksdir -p /etc/ansible/facts.d`

- then we need ro copy the `custom facts script` returning the `JSON or INI Format` on to the location of `/etc/ansible/facts.d`  

- we can copy everything from a folder using the command as `cp ./< path to source_folder/>* <dest folder pth>`

- we can just run this `agains the localhost i.e ansible control host` as those `file and folder`  such as `(/etc/ansible/facts.d) and the custom executable script( which is a shell script) returning the JSON or INI format ` `will not be present on the target host`

- hence we can write the `custom executable script( which is a shell script) returning the JSON or INI format ` can be as below 

- but `remember` to `execute` the `playbook` from the same path `where your ansible.cfg` file present else it will take the default order in preferences

- we can erite as below 

    ```
        #custom shell script which will return the JSON and INI format facts
        # also we need to place this file under /etc/ansible/facts.d directory
        # make sure to have the executable permission for the same 
        # this will add a dictionary entry to the `ansible_facts` having the name as `ansible_local`
        # we can write the custom script as below 

        getdate.fact # naming the file as (*.fact) event though the content can be any script returning the JSON or INI format 
        ---------------
        #! /bin/bash #using the shabang code over here
        echo {\"date\":\"$(date)\"} # hwere also we need to escap the "" in this case
        # this  is in JSON format which will be return ing the JSON formatted info 

        # we can also wite in INI format which is as below 

        getdate2.fact # naming the file as (*.fact) event though the content can be any script returning the JSON or INI format 
        ------------------
        #! /bin/bash #using the shabang code over here
        echo [date]
        echo date=`date` # here instead of providing the $(<command>) we can specify that with the `` symbol

        #now we can copy this file onto the `/etc/ansiuble/facts.d`
        cp getdate.facts getdate.facts /etc/ansible/facts.d

        # now when we execute adhoc commond while we are in the same directory as the ansible.cfg then we can get the output as 
        ansible ubuntu-c -m setup | more 
        #Or
        #fetching the specific facts using the filter args as below 
        ansible ubuntu-c -m setup -a 'filter=ansible_local'
        # running against the localhost or ansible control host

        # then the result will be in the format of 
        ubuntu-c | SUCCESS => {
            "ansible_facts": { // here we can see the all the custom facts been added to the ansible_local key
                "ansible_local": {
                    "getdate": { // here it is been displaying the result as per the `getdate` which returning in JSON format where the key name is the `fact file name` and underneath the `date value which we return as JSOn displayed`
                        "date": "Thu Sep 14 21:44:10 UTC 2023"
                    },
                    "getdate2": { // here it is been displaying the result as per the `getdate2` which returning in INI format where the key name is the `fact file name` and underneath the `date value which we return as INI displayed unde the category block`
                        "date": { // category block
                            "date": "Thu Sep 14 21:44:10 UTC 2023" //dat will be displayed
                        }
                    }
                },
                "discovered_interpreter_python": "/usr/bin/python3"
            },
            "changed": false
        }

    
    ```

# <ins> How to Use the Custom Facts as the Variables in Ansible Playbook </ins> #

- we can also use the `custom facts` as the `variables` as well  in the `ansible playbook`

- for that we can define the `ansible plybook` as below 

    ```
        facts_playbook.yaml
        -------------------

        ---

        - hosts: ubuntu-c # here defining the hosts as the ansible control host or localhost
          connection: local # here using the connection to state its local it is not needed but we can , as its already configured in the inventory file

            tasks: #defining the task out in here
                - name: Handling the Custom facts playbook # provifing the task a name
                  debug: # using the debug module
                    msg: "{{ansible_local}}" # accessing the annible_local facts

        ...

        # if we now execute with the command as below 
        ansible-playbook facts_playbook.yaml
        # then we can see the output as below  

        PLAY [ubuntu-c] ***************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu-c]

        TASK [Handling the Custom facts playbook] *************************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": {
                "getdate": {
                    "date": "Thu Sep 14 21:56:51 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Thu Sep 14 21:56:51 UTC 2023"
                    }
                }
            }
        }

        PLAY RECAP ********************************************************************************************************************************************************************************************
        ubuntu-c                   : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
            
    
    ```

- we can also run the `ansible playbook` for a particular host even though we have `all target group` mentioned against the `hosts key of the ansible playbook`

- in order to user the `particular host` even though `all target group there in the hosts key of the ansible playbook` we can iuse the option as `--limit or -l`

- we need to mention the `-l/--limit <particular hosts>` against which we want to run while using the `ansible-playbook adhoc command with the yaml file` as below 

- we can write the `ansible playbook with all hosts but running for a single host` can be written as below 

    ```
        facts_playbook.yaml
        -------------------

        ---

        - hosts: all # here defining the hosts as the ansible control host or localhost

          tasks: #defining the task out in here
            - name: Handling the Custom facts playbook # provifing the task a name
              debug: # using the debug module
                msg: "{{ansible_local}}" # accessing the annible_local facts

            - name: Handling the Custom facts playbook02
              debug:
                msg: "{{ansible_local.getdate.date}}" #accessing the custom facts in here from JSON File

            - name: Handling the Custom facts playbook03
              debug:
                msg: "{{ansible_local.getdate2.date.date}}"  #accessing the custom facts in here from INI File and also we need to specify `date.date` because of category block

            - name: Handling the Normal Facts playbook04
              debug:
                msg: "{{ansible_default_ipv4.address}}"  #accessing normal facts

        ...

        # if we now execute with the command as below 
        ansible-playbook facts_playbook.yaml -l ubuntu-c
        # here we are executing with the `--linit or -l` option to see the output for only `one host` rather than everything else 
        # then we can see the output as below 
    
        PLAY [all] ********************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu-c]

        TASK [Handling the Custom facts playbook01] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": {
                "getdate": {
                    "date": "Thu Sep 14 22:43:29 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Thu Sep 14 22:43:29 UTC 2023"
                    }
                }
            }
        }

        TASK [Handling the Custom facts playbook02] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Thu Sep 14 22:43:29 UTC 2023"
        }

        TASK [Handling the Custom facts playbook03] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Thu Sep 14 22:43:29 UTC 2023"
        }

        TASK [Handling the Normal Facts playbook04] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "172.18.0.2"
        }

        PLAY RECAP ********************************************************************************************************************************************************************************************
        ubuntu-c                   : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
    
    
    
    ```


- these `custom facts` which been displayed as `ansible_local` key in `ansible_facts` also present in the `hostvars` as well 

- hence we can access them from the `hostvars` section of it by using it as

- but as we know for using the `hostvars section` we need to provid the `ansible_hostname` which will answer the ` target host` question asked by `ansible`

- also as we are using the `ansible_hostname` we need to make sure `gather_facts:True` which is by default 



    ```

        facts_playbook.yaml
        -------------------
        ---

        - hosts: all

          tasks:
            - name: Handling the Custom facts playbook01
              debug:
                msg: "{{ansible_local}}"
            
            - name: Handling the Custom facts playbook02
              debug:
                msg: "{{ansible_local.getdate.date}}"

            - name: Handling the Custom facts playbook03
              debug:
                msg: "{{ansible_local.getdate2.date.date}}"

            - name: Handling the Normal Facts playbook04
              debug:
                msg: "{{ansible_default_ipv4.address}}"

            - name: Handling the Custom facts playbook05
              debug:
                msg: "{{hostvars[ansible_hostname].ansible_local.getdate.date}}" # here using the hostvars with ansible_hostname we are getting the value

            - name: Handling the Custom facts playbook06
              debug:
                msg: "{{hostvars[ansible_hostname].ansible_local.getdate2.date.date}}" # here using the hostvars with ansible_hostname we are getting the value


        ...
        # if we now execute with the command as below 
        ansible-playbook facts_playbook.yaml -l ubuntu-c
        # here we are executing with the `--linit or -l` option to see the output for only `one host` rather than everything else 
        # then we can see the output as below 
        
        PLAY [all] ********************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu-c]

        TASK [Handling the Custom facts playbook01] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": {
                "getdate": {
                    "date": "Thu Sep 14 22:53:55 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Thu Sep 14 22:53:55 UTC 2023"
                    }
                }
            }
        }

        TASK [Handling the Custom facts playbook02] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Thu Sep 14 22:53:55 UTC 2023"
        }

        TASK [Handling the Custom facts playbook03] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Thu Sep 14 22:53:55 UTC 2023"
        }

        TASK [Handling the Normal Facts playbook04] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "172.18.0.2"
        }

        TASK [Handling the Custom facts playbook05] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Thu Sep 14 22:53:55 UTC 2023"
        }

        TASK [Handling the Custom facts playbook06] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Thu Sep 14 22:53:55 UTC 2023"
        }

        PLAY RECAP ********************************************************************************************************************************************************************************************
        ubuntu-c                   : ok=7    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            
    
    ```

- if we want to now configure for all the `target host` i.e `all/linux` in that case we can provide the below `playbook.yaml` file

- the `file` module has the `args` as `recurse:True` if we want to create a directory inside another directory

- also for creating the `dirctory` the `state` will be as `directory`

- while using the copy module to copy the custom facts executable script wwith returning JSON or INI we need to mention the mode as `mode: preserve` if we want to preserve the mode or we can manually provide `755` which means `-rwxr-xe-x` as the permission which is `for user readable,writable,exeutable and for group readable,executable and for other s well readable and executable` so that the `custom script can be executed`

- also we need to `refresh` the `facts on the target host once we added the custom facts` for that we can just `call the setup module` which will refresh the `facts and add the custom facts into the anible_facts for each hosts`

- here we are implicitly running the `setup module` which can `refresh the facts` and add the `custom facts that we added returned ansible_local to the anisble_facts for eahc  of the host` dictionary

- we can write the `playbook.yaml` file as below 

    ```
        ---

    - hosts: all

      tasks:
        - name: Crating the Playbook in multiple Hosts
          file:
            path: /etc/ansible/facts.d
            state: directory # here we are stating the directory will be off as direcory in this case for creating folder
            recurse: True # we can provide recuirese True to make the directory inside

        - name: Using Copy Module To Copy the file from local to remote01
          copy:
            src: getdate.fact
            dest: /etc/ansible/facts.d
            mode: preserve # here we are setting the mode as preserve so that while copying the permission will be copuied too
        
        - name: Using Copy Module To Copy the file from local to remote02
          copy:
            src: getdate2.fact
            dest: /etc/ansible/facts.d 
            mode: preserve # here we are setting the mode as preserve so that while copying the permission will be copuied too

        - name: Refresh the Facts
          setup: # here only providing the setup module which will run during the playbook execution like the adhoc command and custom facts will be added to the ansible_facts   
          # here are just mentioning the setup module to run which will refresh the ansible_facts and add the custom facts into the ansible_facts

        - name: Handling the Custom facts playbook01
          debug:
            msg: "{{ansible_local}}"
        
        - name: Handling the Custom facts playbook02
          debug:
            msg: "{{ansible_local.getdate.date}}"

        - name: Handling the Custom facts playbook03
          debug:
            msg: "{{ansible_local.getdate2.date.date}}"

        - name: Handling the Normal Facts playbook04
          debug:
            msg: "{{ansible_default_ipv4.address}}"

        - name: Handling the Custom facts playbook05
          debug:
            msg: "{{hostvars[ansible_hostname].ansible_local.getdate.date}}"

        - name: Handling the Custom facts playbook06
          debug:
            msg: "{{hostvars[ansible_hostname].ansible_local.getdate2.date.date}}"


        ...
        # if we now execute with the command as below 
        ansible-playbook facts_playbook.yaml 
        # here we are executing with for all the `target hosts`
        # then we can see the output as below 


        PLAY [all] ********************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [centos1]
        ok: [ubuntu2]
        ok: [ubuntu3]
        ok: [ubuntu1]
        ok: [centos2]
        ok: [centos3]

        TASK [Crating the Playbook in multiple Hosts] *********************************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [centos1]
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [ubuntu3]
        ok: [centos2]
        ok: [centos3]

        TASK [Using Copy Module To Copy the file from local to remote01] **************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [centos1]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [ubuntu3]
        ok: [centos2]
        ok: [centos3]

        TASK [Using Copy Module To Copy the file from local to remote02] **************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [centos1]
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [ubuntu3]
        ok: [centos2]
        ok: [centos3]

        TASK [Refresh the Facts] ******************************************************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [ubuntu1]
        ok: [centos1]
        ok: [ubuntu2]
        ok: [ubuntu3]
        ok: [centos2]
        ok: [centos3]

        TASK [Handling the Custom facts playbook01] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": {
                "getdate": {
                    "date": "Thu Sep 14 23:44:14 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Thu Sep 14 23:44:14 UTC 2023"
                    }
                }
            }
        }
        ok: [ubuntu1] => {
            "msg": {
                "getdate": {
                    "date": "Thu Sep 14 23:44:14 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Thu Sep 14 23:44:14 UTC 2023"
                    }
                }
            }
        }
        ok: [ubuntu2] => {
            "msg": {
                "getdate": {
                    "date": "Thu Sep 14 23:44:14 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Thu Sep 14 23:44:14 UTC 2023"
                    }
                }
            }
        }
        ok: [ubuntu3] => {
            "msg": {
                "getdate": {
                    "date": "Thu Sep 14 23:44:14 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Thu Sep 14 23:44:15 UTC 2023"
                    }
                }
            }
        }
        ok: [centos1] => {
            "msg": {
                "getdate": {
                    "date": "Thu Sep 14 23:44:14 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Thu Sep 14 23:44:14 UTC 2023"
                    }
                }
            }
        }
        ok: [centos2] => {
            "msg": {
                "getdate": {
                    "date": "Thu Sep 14 23:44:15 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Thu Sep 14 23:44:15 UTC 2023"
                    }
                }
            }
        }
        ok: [centos3] => {
            "msg": {
                "getdate": {
                    "date": "Thu Sep 14 23:44:15 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Thu Sep 14 23:44:15 UTC 2023"
                    }
                }
            }
        }

        TASK [Handling the Custom facts playbook02] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [ubuntu1] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [ubuntu2] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [ubuntu3] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [centos1] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [centos2] => {
            "msg": "Thu Sep 14 23:44:15 UTC 2023"
        }
        ok: [centos3] => {
            "msg": "Thu Sep 14 23:44:15 UTC 2023"
        }

        TASK [Handling the Custom facts playbook03] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [ubuntu1] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [ubuntu2] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [ubuntu3] => {
            "msg": "Thu Sep 14 23:44:15 UTC 2023"
        }
        ok: [centos1] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [centos2] => {
            "msg": "Thu Sep 14 23:44:15 UTC 2023"
        }
        ok: [centos3] => {
            "msg": "Thu Sep 14 23:44:15 UTC 2023"
        }

        TASK [Handling the Normal Facts playbook04] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "172.18.0.2"
        }
        ok: [ubuntu1] => {
            "msg": "172.18.0.4"
        }
        ok: [ubuntu2] => {
            "msg": "172.18.0.9"
        }
        ok: [ubuntu3] => {
            "msg": "172.18.0.3"
        }
        ok: [centos1] => {
            "msg": "172.18.0.5"
        }
        ok: [centos2] => {
            "msg": "172.18.0.6"
        }
        ok: [centos3] => {
            "msg": "172.18.0.7"
        }

        TASK [Handling the Custom facts playbook05] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [ubuntu1] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [ubuntu2] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [ubuntu3] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [centos1] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [centos2] => {
            "msg": "Thu Sep 14 23:44:15 UTC 2023"
        }
        ok: [centos3] => {
            "msg": "Thu Sep 14 23:44:15 UTC 2023"
        }

        TASK [Handling the Custom facts playbook06] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [ubuntu1] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [ubuntu2] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [ubuntu3] => {
            "msg": "Thu Sep 14 23:44:15 UTC 2023"
        }
        ok: [centos1] => {
            "msg": "Thu Sep 14 23:44:14 UTC 2023"
        }
        ok: [centos2] => {
            "msg": "Thu Sep 14 23:44:15 UTC 2023"
        }
        ok: [centos3] => {
            "msg": "Thu Sep 14 23:44:15 UTC 2023"
        }

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu-c                   : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


    
    ```


- we need to unsderstand that `facts` are nothing but `just to run the setup module`

- we can just `run the setup module` as above in order to refresh facts so that `if we have any custom facts that weill be added to ansible_facts dict`

- we can `add the custom facts` and `refresh the setup module to run the setp to refresh the facts` at the same moment `dynamically`

- by default the `ansible` expects the `custom facts script` on the `/etc/ansible/facts.d` folder , which need a `root privileges`

- if the `user` does not have the permission then we can use the below `ansible playbook script`

- here we need to `create` the `facts.d` folder in the `current working directory`

- we need to put the `custom facts scripts` in to the `created facts.d` file 

- then we need to `copy the facts.d directory with custom facts that we created to each target host /home/<user> folder`

- we can have to copy the `facts.d directory to ----> /home/<user> directory` of each `target hosts`

- then while we `run the setup module to refresh the facts` we need to provide an `argument` named as `fact_path`

- this `fact_path` will redirect the `setup module to look for custom facts in facts.d folder in /home/<user> rather than in /etc/ansible/facts.d folder which need admin access` while refreshing the setup

- before running the `playbook` there should not be any `custom facts in the facts.d directory` in the `/etc/ansible/facts.d directory` for recomended use for which we need to use the `state=absent` as args to the file module

- we can use the ansible command for this as below 

    ```
        ansible linux -m file -a 'path=/etc/ansible/facts.d/getdate.fact state=absent'
        # here we are removing the custom facts from /etc/ansible/facts.d folder for getdate.fact
        ansible linux -m file -a 'path=/etc/ansible/facts.d/getdate2.fact state=absent'
        # here we are removing the custom facts from /etc/ansible/facts.d folder for getdate2.fact
        
        # the output will be as for gatedte and gatedate2
        centos2 | CHANGED => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/libexec/platform-python"
            },
            "changed": true,
            "path": "/etc/ansible/facts.d/getdate.fact",
            "state": "absent"
        }
        centos1 | CHANGED => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/libexec/platform-python"
            },
            "changed": true,
            "path": "/etc/ansible/facts.d/getdate.fact",
            "state": "absent"
        }
        ubuntu2 | CHANGED => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/bin/python3"
            },
            "changed": true,
            "path": "/etc/ansible/facts.d/getdate.fact",
            "state": "absent"
        }
        ubuntu1 | CHANGED => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/bin/python3"
            },
            "changed": true,
            "path": "/etc/ansible/facts.d/getdate.fact",
            "state": "absent"
        }
        ubuntu3 | CHANGED => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/bin/python3"
            },
            "changed": true,
            "path": "/etc/ansible/facts.d/getdate.fact",
            "state": "absent"
        }
        centos3 | CHANGED => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/libexec/platform-python"
            },
            "changed": true,
            "path": "/etc/ansible/facts.d/getdate.fact",
            "state": "absent"
        }

    # the other output will be s 
    centos1 | CHANGED => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/libexec/platform-python"
    },
            "changed": true,
            "path": "/etc/ansible/facts.d/getdate2.fact",
            "state": "absent"
        }
        centos2 | CHANGED => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/libexec/platform-python"
            },
            "changed": true,
            "path": "/etc/ansible/facts.d/getdate2.fact",
            "state": "absent"
        }
        ubuntu2 | CHANGED => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/bin/python3"
            },
            "changed": true,
            "path": "/etc/ansible/facts.d/getdate2.fact",
            "state": "absent"
        }
        ubuntu1 | CHANGED => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/bin/python3"
            },
            "changed": true,
            "path": "/etc/ansible/facts.d/getdate2.fact",
            "state": "absent"
        }
        ubuntu3 | CHANGED => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/bin/python3"
            },
            "changed": true,
            "path": "/etc/ansible/facts.d/getdate2.fact",
            "state": "absent"
        }
        centos3 | CHANGED => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/libexec/platform-python"
            },
            "changed": true,
            "path": "/etc/ansible/facts.d/getdate2.fact",
            "state": "absent"
        }

    ```

- here also we need to make sure that `we are using the linux user not the all user`

- because as we are using the `ansible control host such as ubuntu-c` as its is a `local ansible connection not a ssh connection with root or sudo privileges` when we try to remove and copy the file then we will be getting the error 

- but `we can use ansible control host as root user` as `target remote host with root or sudo priviledges` to do the same 


- now we can create the `playbook.yaml` as below test it against the `linux user(which is the parent of ubuntu and centos)`

    ```
        facts_playbook.yaml
        --------------------

        ---
        
        - hosts:linux # here we are using the linux host in this case 
          
          tasks:
            - name: Crating the Playbook in multiple Hosts
              file:
                path: /home/ansible/facts.d
                state: directory
                recurse: True # we can provide recuirese True to make the directory inside

            - name: Using Copy Module To Copy the file from local to remote01
              copy:
                src: getdate.fact
                dest: /home/ansible/facts.d
                mode: preserve 
            
            - name: Using Copy Module To Copy the file from local to remote02
              copy:
                src: getdate2.fact
                dest: /home/ansible/facts.d
                mode: preserve

            - name: Refresh the Facts
              setup: # here only providing the setup module which will run during the playbook execution like the adhoc command and custom facts will be added to the ansible_facts   
                fact_path: /home/ansible/facts.d

            - name: Handling the Custom facts playbook01
              debug:
                msg: "{{ansible_local}}"
            
            - name: Handling the Custom facts playbook02
              debug:
                msg: "{{ansible_local.getdate.date}}"

            - name: Handling the Custom facts playbook03
              debug:
                msg: "{{ansible_local.getdate2.date.date}}"

            - name: Handling the Normal Facts playbook04
              debug:
                msg: "{{ansible_default_ipv4.address}}"

            - name: Handling the Custom facts playbook05
              debug:
                msg: "{{hostvars[ansible_hostname].ansible_local.getdate.date}}"

            - name: Handling the Custom facts playbook06
              debug:
                msg: "{{hostvars[ansible_hostname].ansible_local.getdate2.date.date}}"


        ...

        # if we now execute the pipeeline as below 
        ansible-playbook facts_playbook.yaml
        # then we can see the outpput for all without having the root access we can move the file to the `/home/ansible/facts.d` folder
        # we also copied the ansible custom facts into the `/home/ansible/facts.d`
        # then we refreshed the `setup module to update the custom facts` and also providing the `fact_path` so that `ansible consider using it from the custom localtion i.e /home/ansible/hosts.d  rather than the default location /etc/ansible/facts.d`
        # also we need to make sure that we will be using it against the linux user not all user 
        
        
        # the output in here will be as 
        PLAY [all] ********************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [ubuntu3]
        ok: [ubuntu2]
        ok: [centos1]
        ok: [ubuntu1]
        ok: [centos2]
        ok: [centos3]

        TASK [Crating the Playbook in multiple Hosts] *********************************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [centos1]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [ubuntu3]
        ok: [centos2]
        ok: [centos3]

        TASK [Using Copy Module To Copy the file from local to remote01] **************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [centos1]
        ok: [ubuntu2]
        ok: [ubuntu1]
        ok: [ubuntu3]
        ok: [centos2]
        ok: [centos3]

        TASK [Using Copy Module To Copy the file from local to remote02] **************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [centos1]
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [ubuntu3]
        ok: [centos2]
        ok: [centos3]

        TASK [Refresh the Facts] ******************************************************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [centos1]
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [ubuntu3]
        ok: [centos2]
        ok: [centos3]

        TASK [Handling the Custom facts playbook01] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": {
                "getdate": {
                    "date": "Fri Sep 15 05:38:28 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Fri Sep 15 05:38:28 UTC 2023"
                    }
                }
            }
        }
        ok: [ubuntu1] => {
            "msg": {
                "getdate": {
                    "date": "Fri Sep 15 05:38:28 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Fri Sep 15 05:38:28 UTC 2023"
                    }
                }
            }
        }
        ok: [ubuntu2] => {
            "msg": {
                "getdate": {
                    "date": "Fri Sep 15 05:38:28 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Fri Sep 15 05:38:28 UTC 2023"
                    }
                }
            }
        }
        ok: [ubuntu3] => {
            "msg": {
                "getdate": {
                    "date": "Fri Sep 15 05:38:28 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Fri Sep 15 05:38:28 UTC 2023"
                    }
                }
            }
        }
        ok: [centos1] => {
            "msg": {
                "getdate": {
                    "date": "Fri Sep 15 05:38:28 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Fri Sep 15 05:38:28 UTC 2023"
                    }
                }
            }
        }
        ok: [centos2] => {
            "msg": {
                "getdate": {
                    "date": "Fri Sep 15 05:38:29 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Fri Sep 15 05:38:29 UTC 2023"
                    }
                }
            }
        }
        ok: [centos3] => {
            "msg": {
                "getdate": {
                    "date": "Fri Sep 15 05:38:29 UTC 2023"
                },
                "getdate2": {
                    "date": {
                        "date": "Fri Sep 15 05:38:29 UTC 2023"
                    }
                }
            }
        }

        TASK [Handling the Custom facts playbook02] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [ubuntu1] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [ubuntu2] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [ubuntu3] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [centos1] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [centos2] => {
            "msg": "Fri Sep 15 05:38:29 UTC 2023"
        }
        ok: [centos3] => {
            "msg": "Fri Sep 15 05:38:29 UTC 2023"
        }

        TASK [Handling the Custom facts playbook03] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [ubuntu1] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [ubuntu2] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [ubuntu3] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [centos1] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [centos2] => {
            "msg": "Fri Sep 15 05:38:29 UTC 2023"
        }
        ok: [centos3] => {
            "msg": "Fri Sep 15 05:38:29 UTC 2023"
        }

        TASK [Handling the Normal Facts playbook04] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "172.18.0.2"
        }
        ok: [ubuntu1] => {
            "msg": "172.18.0.9"
        }
        ok: [ubuntu2] => {
            "msg": "172.18.0.3"
        }
        ok: [ubuntu3] => {
            "msg": "172.18.0.7"
        }
        ok: [centos1] => {
            "msg": "172.18.0.8"
        }
        ok: [centos2] => {
            "msg": "172.18.0.4"
        }
        ok: [centos3] => {
            "msg": "172.18.0.6"
        }

        TASK [Handling the Custom facts playbook05] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [ubuntu1] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [ubuntu2] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [ubuntu3] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [centos1] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [centos2] => {
            "msg": "Fri Sep 15 05:38:29 UTC 2023"
        }
        ok: [centos3] => {
            "msg": "Fri Sep 15 05:38:29 UTC 2023"
        }

        TASK [Handling the Custom facts playbook06] ***********************************************************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [ubuntu1] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [ubuntu2] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [ubuntu3] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [centos1] => {
            "msg": "Fri Sep 15 05:38:28 UTC 2023"
        }
        ok: [centos2] => {
            "msg": "Fri Sep 15 05:38:29 UTC 2023"
        }
        ok: [centos3] => {
            "msg": "Fri Sep 15 05:38:29 UTC 2023"
        }

        PLAY RECAP ********************************************************************************************************************************************************************************************
        centos1                    : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu-c                   : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

    
    ```




