# <ins> Blocks </ins> #

- `blocks are the feeature that been added to ansible 2`

- `block` allow us to `group` `a number of tasks` into `blocks` 

- they also provide `other benifits` ` such as error handling`

- **Case01**
  
  - we need to define the `block` inside the `tasks` section

  - blocks accept the `list of task execution` 
  
  - we can provide the `block with the name attribute` like how we are doing it for the `task with name attribute` if we arwe using the `ansible 2.3 version`
  
  - else we need to remove the `name attribute` from the `block declarative directive` if we are using the `< ansible 2.3 version`   
  
  - we need to provide the `- <module name>` instad of the `- name` attribute if we are using the `ansible 2.3 version` 
  
  - we can define an `ansible playbook` with the `usage of block` as below 

    ```
        sample_block_playbook.yaml
        ==========================

        ---
    
        - hosts: linux # defining the linux host in here 

          tasks:   #defining the task inside which we need to define the blocks in here     
            - name: Defining the tasks with the usage of block as well 

              block:   # defining the block declarative derivate in here to define blocks
                
                - name: block contains list of tasks which need to be get executed but name can only be used with ansible2.3 01
                  debug:  # using the debug module in here
                    msg: Example 1 with Block

                - name: block contains list of tasks which need to be get executed but name can only be used with ansible2.3 02
                  debug:  # usingthe debug module to print the message agianst all the hosts
                    msg: Example 2 with Block

                - name: block contains list of tasks which need to be get executed but name can only be used with ansible2.3 03
                  debug:  # usingthe debug module to print the message agianst all the hosts
                    msg: Example 3 with Block

        ...

        # here can execute the tasks using the ansible-playbook command as below 
        ansible-playbook sample_block_playbook.yaml
        # the output in here can be as 


        PLAY [linux] ************************************************************************************************************************************************************************

        TASK [Gathering Facts] **************************************************************************************************************************************************************
        ok: [centos1]
        ok: [centos2]
        ok: [centos3]
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [ubuntu3]

        TASK [block contains list of tasks which need to be get executed but name can only be used with ansible2.3 01] **********************************************************************
        ok: [centos1] => {
            "msg": "Example 1 with Block"
        }
        ok: [centos2] => {
            "msg": "Example 1 with Block"
        }
        ok: [centos3] => {
            "msg": "Example 1 with Block"
        }
        ok: [ubuntu1] => {
            "msg": "Example 1 with Block"
        }
        ok: [ubuntu2] => {
            "msg": "Example 1 with Block"
        }
        ok: [ubuntu3] => {
            "msg": "Example 1 with Block"
        }

        TASK [block contains list of tasks which need to be get executed but name can only be used with ansible2.3 02] **********************************************************************
        ok: [centos1] => {
            "msg": "Example 2 with Block"
        }
        ok: [centos2] => {
            "msg": "Example 2 with Block"
        }
        ok: [centos3] => {
            "msg": "Example 2 with Block"
        }
        ok: [ubuntu1] => {
            "msg": "Example 2 with Block"
        }
        ok: [ubuntu2] => {
            "msg": "Example 2 with Block"
        }
        ok: [ubuntu3] => {
            "msg": "Example 2 with Block"
        }

        TASK [block contains list of tasks which need to be get executed but name can only be used with ansible2.3 03] **********************************************************************
        ok: [centos1] => {
            "msg": "Example 3 with Block"
        }
        ok: [centos2] => {
            "msg": "Example 3 with Block"
        }
        ok: [centos3] => {
            "msg": "Example 3 with Block"
        }
        ok: [ubuntu1] => {
            "msg": "Example 3 with Block"
        }
        ok: [ubuntu2] => {
            "msg": "Example 3 with Block"
        }
        ok: [ubuntu3] => {
            "msg": "Example 3 with Block"
        }

        PLAY RECAP **************************************************************************************************************************************************************************
        centos1                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    
    ```

  - **Case2**
    
    - we can use the `normal ansible-playbook command/derivative` that we use `while using the task description` while using the `blocks` as well
    
    - here we can use the `with_items` which been used for the `looping` and also we can use the `when declarative to provide the conditioning as well`
    
    - we can define the `ansible playbook` as below in this case 

        ```
            sample_block_playbook.yaml
            ==========================

            ---
        
            - hosts: linux # defining the linux host in here 

              tasks:   #defining the task inside which we need to define the blocks in here     
                - name: Defining the tasks with the usage of block as well 

                  block:   # defining the block declarative derivate in here to define blocks
                    
                    - name: block contains list of tasks which need to be get executed but name can only be used with ansible2.3 centos
                      debug:  # using the debug module in here
                        msg: Example 1 with Block for CentOS hosts
                      when: ansible_distribution == "CentOS" # using the when declarative directive in here with condition

                    - name: block contains list of tasks which need to be get executed but name can only be used with ansible2.3 ubuntu
                      debug:  # usingthe debug module to print the message agianst all the hosts
                        msg: Example 2 with Block for Ubuntu hosts
                      when: ansible_distribution == "Ubuntu" # using the when declarative directive in here with condition 

                    - name: block contains list of tasks which need to be get executed but name can only be used with ansible2.3 ubuntu using the loops
                      debug:  # usingthe debug module to print the message agianst all the hosts
                        msg: Here the Example with {{item}}
                      with_items:  # using the with_items loop in here where each value will be considered againbst all the target hosts total 18 result
                        - x
                        - y
                        - z

            ...

            # here can execute the tasks using the ansible-playbook command as below 
            ansible-playbook sample_block_playbook.yaml
            # the output in here can be as 

            PLAY [linux] ************************************************************************************************************************************************************************

            TASK [Gathering Facts] **************************************************************************************************************************************************************
            ok: [centos3]
            ok: [centos2]
            ok: [ubuntu2]
            ok: [centos1]
            ok: [ubuntu1]
            ok: [ubuntu3]

            TASK [block contains list of tasks which need to be get executed but name can only be used with ansible2.3 centos] ******************************************************************
            ok: [centos1] => {
                "msg": "Example 1 with Block for CentOS hosts"
            }
            ok: [centos2] => {
                "msg": "Example 1 with Block for CentOS hosts"
            }
            ok: [centos3] => {
                "msg": "Example 1 with Block for CentOS hosts"
            }
            skipping: [ubuntu1]
            skipping: [ubuntu2]
            skipping: [ubuntu3]

            TASK [block contains list of tasks which need to be get executed but name can only be used with ansible2.3 ubuntu] ******************************************************************
            skipping: [centos1]
            skipping: [centos2]
            skipping: [centos3]
            ok: [ubuntu1] => {
                "msg": "Example 2 with Block for Ubuntu hosts"
            }
            ok: [ubuntu2] => {
                "msg": "Example 2 with Block for Ubuntu hosts"
            }
            ok: [ubuntu3] => {
                "msg": "Example 2 with Block for Ubuntu hosts"
            }

            TASK [block contains list of tasks which need to be get executed but name can only be used with ansible2.3 ubuntu using the loops] **************************************************
            ok: [centos1] => (item=x) => {
                "msg": "Here the Example with x"
            }
            ok: [centos1] => (item=y) => {
                "msg": "Here the Example with y"
            }
            ok: [centos1] => (item=z) => {
                "msg": "Here the Example with z"
            }
            ok: [centos2] => (item=x) => {
                "msg": "Here the Example with x"
            }
            ok: [centos2] => (item=y) => {
                "msg": "Here the Example with y"
            }
            ok: [centos2] => (item=z) => {
                "msg": "Here the Example with z"
            }
            ok: [centos3] => (item=x) => {
                "msg": "Here the Example with x"
            }
            ok: [centos3] => (item=y) => {
                "msg": "Here the Example with y"
            }
            ok: [centos3] => (item=z) => {
                "msg": "Here the Example with z"
            }
            ok: [ubuntu1] => (item=x) => {
                "msg": "Here the Example with x"
            }
            ok: [ubuntu1] => (item=y) => {
                "msg": "Here the Example with y"
            }
            ok: [ubuntu1] => (item=z) => {
                "msg": "Here the Example with z"
            }
            ok: [ubuntu2] => (item=x) => {
                "msg": "Here the Example with x"
            }
            ok: [ubuntu2] => (item=y) => {
                "msg": "Here the Example with y"
            }
            ok: [ubuntu2] => (item=z) => {
                "msg": "Here the Example with z"
            }
            ok: [ubuntu3] => (item=x) => {
                "msg": "Here the Example with x"
            }
            ok: [ubuntu3] => (item=y) => {
                "msg": "Here the Example with y"
            }
            ok: [ubuntu3] => (item=z) => {
                "msg": "Here the Example with z"
            }

            PLAY RECAP **************************************************************************************************************************************************************************
            centos1                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
            centos2                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
            centos3                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
            ubuntu1                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
            ubuntu2                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
            ubuntu3                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
        
        ```

  - **Case03**
    
    - if we are using the `block` like the same as the `tasks` until now
    
    - the `benifit` of using the `block` will be we can use the `error handling along with it` like how we do for python using the `try/except/finally` in the `ansible playbook`
    
    - we can define a `rescue` block where we can defne the `except block code` 
    
    - if a `block task` got failed then only the `rescue` block going to be `get running`
    
    - we can define the `always` to define the `executed no matter what like the finally clause`
    
    - we can define the `block` with `rescue` and `always` as below `ansible playbook`
    
    - in this example we are `installing the patch as well as the python-dnspython module` using the `package` module
    
    - the `python-dnspython` module being available for the `ubuntu OS` but  does not support `centos OS` , currently not available for both `ubuntu and centos`  
    
    - also in this case we will be using the `rescue` component , if there were error while installing the `patch and python-dnspython package` then rollback the `patch package` as well in this case 
    
    - we will print the `debug statement` in the `always` block which will be going to be `executed no matter what`   

        ```
        
            sample_block_playbook.yaml
            ==========================

            ---
        
            - hosts: linux # defining the linux host in here 

              tasks:   #defining the task inside which we need to define the blocks in here     
                - name: Defining the tasks with the usage of block as well 

                  block:   # defining the block declarative derivate in here to define blocks
                    
                    - name: installing the patch package here 
                      package:  # using the package module in here 
                        name: patch  # using the patch module in this case 
                        state: latest  # using the latest version of the software

                    - name: installing the python-dnspython module in here 
                      package:  # using the package module in here 
                        name: python-dnspython
                        state: latest  # using the latest version of the software
                  
                  rescue:    #defining the rescue block in here 

                    - name: removing the patch module in case of error 
                      package:   # using the package module in here 
                        name: patch   # remove the patch module in here
                        state: absent  # using the state as absent in here 

                    - name: removing the python-dnspython module in case of error  
                      package:   # using the package module in here 
                        name: python-dnspython   # remove the python-dnspython module in here
                        state: absent  # using the state as absent in here 

                  always:
                    - name: this blcok will be execute no matter what 
                      debug: # using the debug module in here 
                        msg: Run no matter what like the finally block

            ...
        
            # here can execute the tasks using the ansible-playbook command as below 
            ansible-playbook sample_block_playbook.yaml
            # the output in here can be as 
        

            PLAY [linux] *************************************************************************************************************************************************************************

            TASK [Gathering Facts] ***************************************************************************************************************************************************************
            ok: [centos3]
            ok: [centos1]
            ok: [centos2]
            ok: [ubuntu1]
            ok: [ubuntu2]
            ok: [ubuntu3]

            TASK [Install patch] *****************************************************************************************************************************************************************
            changed: [centos2]
            changed: [centos3]
            changed: [centos1]
            changed: [ubuntu2]
            changed: [ubuntu1]
            changed: [ubuntu3]

            TASK [Install python-dnspython] ******************************************************************************************************************************************************
            fatal: [centos1]: FAILED! => {"changed": false, "failures": ["No package python-dnspython available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
            fatal: [centos2]: FAILED! => {"changed": false, "failures": ["No package python-dnspython available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
            fatal: [centos3]: FAILED! => {"changed": false, "failures": ["No package python-dnspython available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
            fatal: [ubuntu1]: FAILED! => {"changed": false, "msg": "No package matching 'python-dnspython' is available"}
            fatal: [ubuntu3]: FAILED! => {"changed": false, "msg": "No package matching 'python-dnspython' is available"}
            fatal: [ubuntu2]: FAILED! => {"changed": false, "msg": "No package matching 'python-dnspython' is available"}

            TASK [Rollback patch] ****************************************************************************************************************************************************************
            changed: [centos2]
            changed: [centos1]
            changed: [centos3]
            changed: [ubuntu1]
            changed: [ubuntu3]
            changed: [ubuntu2]

            TASK [Rollback python-dnspython] *****************************************************************************************************************************************************
            ok: [centos2]
            ok: [centos1]
            ok: [centos3]
            ok: [ubuntu1]
            ok: [ubuntu3]
            ok: [ubuntu2]

            TASK [debug] *************************************************************************************************************************************************************************
            ok: [centos1] => {
                "msg": "This always runs, regardless"
            }
            ok: [centos2] => {
                "msg": "This always runs, regardless"
            }
            ok: [centos3] => {
                "msg": "This always runs, regardless"
            }
            ok: [ubuntu1] => {
                "msg": "This always runs, regardless"
            }
            ok: [ubuntu2] => {
                "msg": "This always runs, regardless"
            }
            ok: [ubuntu3] => {
                "msg": "This always runs, regardless"
            }

            PLAY RECAP ***************************************************************************************************************************************************************************
            centos1                    : ok=5    changed=2    unreachable=0    failed=0    skipped=0    rescued=1    ignored=0   
            centos2                    : ok=5    changed=2    unreachable=0    failed=0    skipped=0    rescued=1    ignored=0   
            centos3                    : ok=5    changed=2    unreachable=0    failed=0    skipped=0    rescued=1    ignored=0   
            ubuntu1                    : ok=5    changed=2    unreachable=0    failed=0    skipped=0    rescued=1    ignored=0   
            ubuntu2                    : ok=5    changed=2    unreachable=0    failed=0    skipped=0    rescued=1    ignored=0   
            ubuntu3                    : ok=5    changed=2    unreachable=0    failed=0    skipped=0    rescued=1    ignored=0 
                        
        
        ```

  - **note**
    
    - as currently the `python-dnspython` not available for `both Centos and Ubuntu OS` hence the `package will be removed because of the rescue option in ansible playbook`  


