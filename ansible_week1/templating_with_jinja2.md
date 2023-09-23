# <ins> Templating With JINJA2 </ins> #

- `ansible` uses the `JINJA2 templating language`

- we can use the `double curly braces i.e {}` in order to access the `variables in JINJA2`

- `jinja 2` in iteself is a `extensive templating language` with `many books and resources dedicated to this subject alone`

- make sure to `re-review` will be `benificial` , more effective `JINJA2` will be more effective `ansible`

- the `JINJA2 templating ` is being `used in 2 ways in ansible`
  
    - `syntatical languge within the ansible playbook`

    - `template agent in the configuration file`

- here we will look into how to use the below spect of the `JINJA2 templating`
  
  - `if/elif/else block in jinja2`

  - `for loop in ansible`

  - ` break and continue`

  - `ranges`

  - `jinja2 filters`

- **Case01**

  - the `jinja2 comments` can be provided in by `{# <comment> #}` 

  - we can use the `{% %}` in order to definee the `JINJA2 Statement Holders` where we writedoen the `jinja2 statements`

  - if we have to use the `if` statement we can do that using it as `{% if <condition> %} <result> {% endif %}`   

  - we can use the ` - markup of YAML at the end of jinja2 statement as {% if <condition> -%}` which will `remove` the `empty carriage return ` as when we use the `comment as {# #}` or by the use of `{% %}` an `empty carriage will be returned`

  - we can use the below `ansible playbook for reference`

    
    ```

        jinja2_template.yaml
        --------------------
        ---

        - hosts: linux
          
          tasks:
            - name: prepearing the JINJA2 template
              debug:
                msg: >

                     --==Amsible JINJA2 execution==--

                     {# here we are using the comment with the - symbol to remove the empty carriage returned by the YAML JINJA2 -#}  
                     {% if anisble_hostname == "ubuntu-c" %} # here we are using the Jinja2 Statetement {% %} with a `-`  which could remove the returned empty carraige by if 
                        This is Ubuntu-c machine
                     {% endif %} # using the endif to close the jijja2 template

        ...
        # now when we execute the command as below 
        ansible-playbook jinja2_template.yaml
        # then we will get the output as below 
        
        PLAY [all] ********************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [centos2]
        ok: [centos3]
        ok: [centos1]
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [ubuntu3]

        TASK [Checking the Usage of If block with JINJA2 templating in Ansible Playbook] **********************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nThis is ubuntu-c\n"
        }
        ok: [centos1] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\n"
        }
        ok: [centos2] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\n"
        }
        ok: [centos3] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\n"
        }
        ok: [ubuntu1] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\n"
        }
        ok: [ubuntu2] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\n"
        }
        ok: [ubuntu3] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\n"
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

- **Case02**

- we can also use the `elif` block same as the `if block` with the `-` at the end to remove the `empty carraige return by JINJA2 if/elif/else statement`

- but here need to provide the `>` in the `YAML` to indicate all belong to the `same string distibuted over multiple string`

- we can define the `elif block in JINJA2` as below 

    ```

        jinja2_template.yaml
        --------------------
        ---

        - hosts: linux
          
          tasks:
            - name: prepearing the JINJA2 template
              debug:
                msg: >

                     --==Amsible JINJA2 execution==--

                     {# here we are using the comment with the - symbol to remove the empty carriage returned by the YAML JINJA2 -#}  
                     {% if anisble_hostname == "ubuntu-c" %} # here we are using the Jinja2 Statetement {% %} with a `-`  which could remove the returned empty carraige by if 
                        This is Ubuntu-c machine
                     {% elif anisble_hostname == 'centos1' -%}
                        This is CentOS1 machine
                     {% endif %} # using the endif to close the jijja2 template

        ...
    
        # now when we execute the command as below 
        ansible-playbook jinja2_template.yaml
        # then we will get the output as below 


        PLAY [all] ********************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [centos1]
        ok: [centos2]
        ok: [centos3]
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [ubuntu3]

        TASK [Checking the Usage of If block with JINJA2 templating in Ansible Playbook] **********************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nThis is ubuntu-c\n"
        }
        ok: [centos1] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nThis is centos1\n"
        }
        ok: [centos2] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\n"
        }
        ok: [centos3] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\n"
        }
        ok: [ubuntu1] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\n"
        }
        ok: [ubuntu2] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\n"
        }
        ok: [ubuntu3] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\n"
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

- **Case03**

- we can also use the `else block` with the `- as the JINJA2 statement as {% else -%}` in order to remove the `empty returned carriage` in this case 

- we can also use the `else block in JINJA2 template as below`

    ```
    jinja2_template.yaml
        --------------------
        ---

        - hosts: linux
          
          tasks:
            - name: prepearing the JINJA2 template
              debug:
                msg: >

                     --==Amsible JINJA2 execution==--

                     {# here we are using the comment with the - symbol to remove the empty carriage returned by the YAML JINJA2 -#}  
                     {% if anisble_hostname == "ubuntu-c" %} # here we are using the Jinja2 Statetement {% %} with a `-`  which could remove the returned empty carraige by if 
                        This is Ubuntu-c machine
                     {% elif anisble_hostname == 'centos1' -%}
                        This is CentOS1 machine
                     {% else -%}
                        {{ansible_hostname}} # using the  anisble_hostname as the facts variable in here to print the hostname of target if it does not match the requirement
                     {% endif %} # using the endif to close the jijja2 template

        ...
    
        # now when we execute the command as below 
        ansible-playbook jinja2_template.yaml
        # then we will get the output as below 
        PLAY [all] ********************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [centos1]
        ok: [centos2]
        ok: [centos3]
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [ubuntu3]

        TASK [Checking the Usage of If block with JINJA2 templating in Ansible Playbook] **********************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nThis is ubuntu-c\n"
        }
        ok: [centos1] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nThis is centos1\n"
        }
        ok: [centos2] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\ncentos2\n"
        }
        ok: [centos3] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\ncentos3\n"
        }
        ok: [ubuntu1] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nubuntu1\n"
        }
        ok: [ubuntu2] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nubuntu2\n"
        }
        ok: [ubuntu3] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nubuntu3\n"
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

- **Case4**

 - we can see if a `variable been defined or not` using the `is defined` keywords in here 

- we can use the below `ansible playbook` as for reference 

    ```
        jinja2_template.yaml
        --------------------
        ---

        - hosts: linux
          
          tasks:
            - name: prepearing the JINJA2 template
              debug:
                msg: >

                     --==Amsible JINJA2 execution==--

                     {# here we are using the comment with the - symbol to remove the empty carriage returned by the YAML JINJA2 -#}  
                     {% if example_varable is defined -%} # here using the `is defined` keyword  we are considering that whether the example_variable present or not
                        example variable defined 
                     {% else -%}
                        example variable not defined
                     {% endif %} 

        ...
        # now when we execute the command as below 
        ansible-playbook jinja2_template.yaml
        # then we will get the output as below 

        PLAY [all] ********************************************************************************************************************************************************************************************

        TASK [Gathering Facts] ********************************************************************************************************************************************************************************
        ok: [ubuntu-c]
        ok: [centos2]
        ok: [centos1]
        ok: [centos3]
        ok: [ubuntu1]
        ok: [ubuntu2]
        ok: [ubuntu3]

        TASK [Checking the Usage of If block with JINJA2 templating in Ansible Playbook] **********************************************************************************************************************
        ok: [ubuntu-c] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nexample variable not defined\n"
        }
        ok: [centos1] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nexample variable not defined\n"
        }
        ok: [centos2] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nexample variable not defined\n"
        }
        ok: [centos3] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nexample variable not defined\n"
        }
        ok: [ubuntu1] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nexample variable not defined\n"
        }
        ok: [ubuntu2] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nexample variable not defined\n"
        }
        ok: [ubuntu3] => {
            "msg": "\n--== Ansible Jinja2 if statement ==--\nexample variable not defined\n"
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

- **Case5**



