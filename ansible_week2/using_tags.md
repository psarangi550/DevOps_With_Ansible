# Using Tags in Ansible

- here we will be looking into

  - `Using Tags`
  - `Segmentation with Tags`
  - `Execution with Tags`
  - `Skipping With Tags`
  - `Playbook Tags`
  - `Special Tags`
  - `Tag Inheritance`
- `Tags` are great when we are working with `large playbook` or `playbook that include other playbook`
- if we want to `run part of the configuration` ` without running the whole playbook`
- **Case01**

  - here we will be taking the `ngix playbook` that `we have used earlier for reference` on the `centos and ubuntu` `target hosts`
  - we can define the `nginx playbook with the tags` as below

    ```yaml
      nginx_playbook.yaml
      ===================
      ---

      - hosts: linux

        tasks:
          - name: Installing EPEL Package
      	    yum:    # using the yum module in here 
      	      name: epel-releae  # defining the packahe name in here
      	      update_cache: true # setting the update_cahce which will run the yum -y update command
              state: latest   # using the state latest to latest to install the latest version
            tags:    # defining the tags in here
      	      - install-epel  # using the tags as install-epel 

          - name: Install Nginx
            package:
              name: nginx
              state: latest
            tags:
              - install-nginx

          - name: Restart Nginx Service
            service:
              name: nginx
              state: restarted
            tags:
              - restart-nginx
            notify: check HTTP Service

          - name: Publishing the template to the required directory
            template:
              src: ./templates/index.html-easter_egg.j2
              dest: "{{hostvars[ansible_hostname].nginx_root_loc}}/index.html"
              mode: 0644
            tags:
              - deploy-app

          - name: Install Unzip
            package:
              name: unzip
              state: latest

          - name: unzipping the playbook stacker into the nginx location
            unarchive:
              src: ./files/playbook_stacker.zip
              dest: "{{nginx_root_loc}}"
            tags:
              - deploy-app

        handlers:
          - name: check HTTP Service
            uri:
              url: "http://{{ansible_default_ipv4.address}}"
              status_code:
                - 200
      ...


    ```
- if we want to run a `particular tasks` based on the `tags` using the `--tags <tag name attribute>`
- here we want to run the `Installing EPEL Package` tasks with the help of `install-epel` tags then we can run that as below
- we need to run the task with the help of the `tags` as below

  ```bash

     ansible-playbook nginx_playbook.yaml --tags "install-epel"
     # here we are using the `install-epel` tags in order to run the corresponding task
     # we need to provide the tag name against the --tags in the quotes structure 
     # hence the output in this case will be as below 
     # here we can see that it only run the `Installing EPEL Package` tasks as we put the `install-epel` tags against it


      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos2]
      ok: [centos3]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Install EPEL] ********************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      ok: [centos3]
      ok: [centos2]
      ok: [centos1]

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu1                    : ok=1    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      ubuntu2                    : ok=1    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      ubuntu3                    : ok=1    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0  



  ```
- if we want we can also run multiple tags as well we can do as well providing  multiple tags against the `--tags` option as `--tags "tag1,tag2"`
- if we want to run the `Install Nginx` and `Restart Nginx` Task then we can use it as below

  ```bash

      ansible-playbook nginx_playbook.yaml --tags "install-nginx,restart-nginx"
    
      # here we  are using the multiple tags in here as above separatd by the comma insude the quotes 
      # the output in this case will be as below 
    
    PLAY [linux] ***************************************************************************************************************************************************************************************

    TASK [Gathering Facts] *****************************************************************************************************************************************************************************
    ok: [centos2]
    ok: [centos1]
    ok: [centos3]
    ok: [ubuntu2]
    ok: [ubuntu1]
    ok: [ubuntu3]

    PLAY [linux] ***************************************************************************************************************************************************************************************

    TASK [Install Nginx] *******************************************************************************************************************************************************************************
    ok: [centos3]
    ok: [centos2]
    ok: [centos1]
    ok: [ubuntu2]
    ok: [ubuntu1]
    ok: [ubuntu3]

    TASK [Restart Nginx Service] ***********************************************************************************************************************************************************************
    changed: [centos3]
    changed: [centos1]
    changed: [ubuntu1]
    changed: [centos2]
    changed: [ubuntu2]
    changed: [ubuntu3]

    RUNNING HANDLER [check HTTP Service] ***************************************************************************************************************************************************************
    ok: [centos3]
    ok: [centos2]
    ok: [centos1]
    ok: [ubuntu2]
    ok: [ubuntu1]
    ok: [ubuntu3]

    PLAY RECAP *****************************************************************************************************************************************************************************************
    centos1                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    centos2                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    centos3                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    ubuntu1                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    ubuntu2                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    ubuntu3                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0    

  ```

- we can also `skip tags` using the option as `skip-tags "<tag1>" ` option out in here as below

- if we want to execute the playbook `without executing the deploy-app tags` then we can run that  one as below 

- we can show the `ansible playbook` execution in this case as below 

  ``` bash

      ansible-playbook nginx_playbook.yaml --skip-tags "deploy-app"
      # this will execute the entire playbook but will not execute the `task which been tagged as deploy-app`
      # also we can see that the below output in this case 

    PLAY [linux] ***************************************************************************************************************************************************************************************

    TASK [Gathering Facts] *****************************************************************************************************************************************************************************
    ok: [centos2]
    ok: [centos3]
    ok: [centos1]
    ok: [ubuntu1]
    ok: [ubuntu2]
    ok: [ubuntu3]

    PLAY [linux] ***************************************************************************************************************************************************************************************

    TASK [Gathering Facts] *****************************************************************************************************************************************************************************
    ok: [centos1]
    ok: [centos2]
    ok: [centos3]
    ok: [ubuntu1]
    ok: [ubuntu2]
    ok: [ubuntu3]

    TASK [Install EPEL] ********************************************************************************************************************************************************************************
    skipping: [ubuntu1]
    skipping: [ubuntu2]
    skipping: [ubuntu3]
    ok: [centos2]
    ok: [centos3]
    ok: [centos1]

    TASK [Install Nginx] *******************************************************************************************************************************************************************************
    ok: [centos2]
    ok: [centos3]
    ok: [centos1]
    ok: [ubuntu2]
    ok: [ubuntu1]
    ok: [ubuntu3]

    TASK [Restart Nginx Service] ***********************************************************************************************************************************************************************
    changed: [centos3]
    changed: [ubuntu2]
    changed: [ubuntu1]
    changed: [centos1]
    changed: [centos2]
    changed: [ubuntu3]

    TASK [Install Unzip] *******************************************************************************************************************************************************************************
    ok: [centos2]
    ok: [centos1]
    ok: [centos3]
    ok: [ubuntu1]
    ok: [ubuntu2]
    ok: [ubuntu3]

    RUNNING HANDLER [check HTTP Service] ***************************************************************************************************************************************************************
    ok: [centos2]
    ok: [ubuntu1]
    ok: [centos1]
    ok: [ubuntu2]
    ok: [centos3]
    ok: [ubuntu3]

    PLAY RECAP *****************************************************************************************************************************************************************************************
    centos1                    : ok=7    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    centos2                    : ok=7    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    centos3                    : ok=7    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    ubuntu1                    : ok=6    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
    ubuntu2                    : ok=6    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
    ubuntu3                    : ok=6    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0     
      
  ```

- when we run `ansible` there will be a default tag with the name of `all` be assigned 

- when we run `--tags "all"` then all the `tag and untag` will be going to execute in case of `all tags` 

- we can execute this as below 

  ```bash
     
     # here if we want to execute against the `all` tags then we can use it as below 
     ansible-playbook nginx_playbook.yaml --tags "all"
     # here we are execute against the tags all which will execute all the `tagged and untagged task` in here 
     # we can see the output as below 
      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos2]
      ok: [centos3]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]

      TASK [Install EPEL] ********************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      ok: [centos3]
      ok: [centos2]
      ok: [centos1]

      TASK [Install Nginx] *******************************************************************************************************************************************************************************
      ok: [centos3]
      ok: [centos2]
      ok: [centos1]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      TASK [Restart Nginx Service] ***********************************************************************************************************************************************************************
      changed: [centos1]
      changed: [ubuntu1]
      changed: [centos2]
      changed: [ubuntu2]
      changed: [centos3]
      changed: [ubuntu3]

      TASK [Publishing the template to the required directory] *******************************************************************************************************************************************
      ok: [centos3]
      ok: [centos1]
      ok: [centos2]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]

      TASK [Install Unzip] *******************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos3]
      ok: [centos2]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]

      TASK [unzipping the playbook stacker into the nginx location] **************************************************************************************************************************************
      changed: [centos3]
      changed: [centos1]
      changed: [centos2]
      changed: [ubuntu2]
      changed: [ubuntu1]
      changed: [ubuntu3]

      RUNNING HANDLER [check HTTP Service] ***************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos3]
      ok: [ubuntu2]
      ok: [centos2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos2                    : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos3                    : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu1                    : ok=8    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      ubuntu2                    : ok=8    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      ubuntu3                    : ok=8    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0  
  
  ```

- we can define the `tags` for a `particular play in the playbook` as `below`

- when we execute the `tags with the tag which is against the play then we can see the output as below`

  ```yaml
      
      nginx_playbook.yaml
      ===================
      ---

      - hosts: linux
        tags: webapp # here we are providing the tags as the webapp to run the entire play with the mentioned tags

        tasks:
          - name: Installing EPEL Package
      	    yum:    # using the yum module in here 
      	      name: epel-releae  # defining the packahe name in here
      	      update_cache: true # setting the update_cahce which will run the yum -y update command
              state: latest   # using the state latest to latest to install the latest version
            tags:    # defining the tags in here
      	      - install-epel  # using the tags as install-epel 

          - name: Install Nginx
            package:
              name: nginx
              state: latest
            tags:
              - install-nginx

          - name: Restart Nginx Service
            service:
              name: nginx
              state: restarted
            tags:
              - restart-nginx
            notify: check HTTP Service

          - name: Publishing the template to the required directory
            template:
              src: ./templates/index.html-easter_egg.j2
              dest: "{{hostvars[ansible_hostname].nginx_root_loc}}/index.html"
              mode: 0644
            tags:
              - deploy-app

          - name: Install Unzip
            package:
              name: unzip
              state: latest

          - name: unzipping the playbook stacker into the nginx location
            unarchive:
              src: ./files/playbook_stacker.zip
              dest: "{{nginx_root_loc}}"
            tags:
              - deploy-app

        handlers:
          - name: check HTTP Service
            uri:
              url: "http://{{ansible_default_ipv4.address}}"
              status_code:
                - 200
      ...

  ```
- now we can run the playbook with the tags as `--tags webapp` as below

  ```bash

      absible-playbook nginx_playbook.yaml --tags webapp
      # here executing the tasg with the tags as webapp in this case 
      # here in this case we will be getting the result as below 
      
      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos3]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]
      ok: [centos2]

      TASK [Install EPEL] ********************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      ok: [centos1]
      ok: [centos3]
      ok: [centos2]

      TASK [Install Nginx] *******************************************************************************************************************************************************************************
      ok: [centos2]
      ok: [centos1]
      ok: [centos3]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      TASK [Restart Nginx Service] ***********************************************************************************************************************************************************************
      changed: [centos1]
      changed: [ubuntu2]
      changed: [ubuntu1]
      changed: [centos2]
      changed: [centos3]
      changed: [ubuntu3]

      TASK [Publishing the template to the required directory] *******************************************************************************************************************************************
      ok: [centos3]
      ok: [centos2]
      ok: [centos1]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      TASK [Install Unzip] *******************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos3]
      ok: [centos2]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]

      TASK [unzipping the playbook stacker into the nginx location] **************************************************************************************************************************************
      changed: [centos1]
      changed: [centos3]
      changed: [centos2]
      changed: [ubuntu2]
      changed: [ubuntu1]
      changed: [ubuntu3]

      RUNNING HANDLER [check HTTP Service] ***************************************************************************************************************************************************************
      ok: [centos3]
      ok: [centos2]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [centos1]
      ok: [ubuntu3]

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos2                    : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos3                    : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu1                    : ok=8    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      ubuntu2                    : ok=8    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      ubuntu3                    : ok=8    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
  
  ```

- when we are  running the `task` with the `tags related to the entire play` then might be chance of `unexpectdly facts been missing`

- as the `gather_facts` will be associate itself to the `tags which will be in play level as tags`

- now when we run the task which been derived from `ansible_facts` and associate itself with `another tag` then in `that case we will be getting error` 

- as we know over here if we are running the `Restart Nginx` task which will trigger the `handler` which is `check HTTP Requet`

- but if we want to run only the `restart-nginx tags associated Task` then we can see that `Gathering of facts not happening  as we have associate the gather_facts to the play level tags which is of webapp` as here we are not running the `restart-nginx` tags hence `gather_facts` will not run hence the `handler which been dependent on the ansible_facts` will going to be get failed 

- we can see that in the below `ansible-playbook`  example out in here 

  ```bash

      ansible-playbook nginx_playbook.yaml --tags "restart-nginx"
      # here we have the playbook where the tags associated with the play level tags
      # but we are running the tags which is not the play level tags
      # hence in this case we will be getting the error as the gather_facts will only work in case of play level tags ben used
      # if we are using the tags which are not associoated with the play level tags then gather_facts will not work
      # hence in that case we will not be run any task marked with tags which are dependent on the  ansible_facts

      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Restart Nginx Service] ***********************************************************************************************************************************************************************
      changed: [ubuntu2]
      changed: [centos2]
      changed: [ubuntu1]
      changed: [centos1]
      changed: [centos3]
      changed: [ubuntu3]

      RUNNING HANDLER [check HTTP Service] ***************************************************************************************************************************************************************
      fatal: [centos1]: FAILED! => {"msg": "The task includes an option with an undefined variable. The error was: 'ansible_default_ipv4' is undefined. 'ansible_default_ipv4' is undefined\n\nThe error appears to be in '/home/ansible/diveintoansible/Structuring Ansible Playbooks/Using Tags/template/nginx_playbook.yaml': line 58, column 7, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n  handlers:\n    - name: check HTTP Service\n      ^ here\n"}
      fatal: [centos2]: FAILED! => {"msg": "The task includes an option with an undefined variable. The error was: 'ansible_default_ipv4' is undefined. 'ansible_default_ipv4' is undefined\n\nThe error appears to be in '/home/ansible/diveintoansible/Structuring Ansible Playbooks/Using Tags/template/nginx_playbook.yaml': line 58, column 7, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n  handlers:\n    - name: check HTTP Service\n      ^ here\n"}
      fatal: [centos3]: FAILED! => {"msg": "The task includes an option with an undefined variable. The error was: 'ansible_default_ipv4' is undefined. 'ansible_default_ipv4' is undefined\n\nThe error appears to be in '/home/ansible/diveintoansible/Structuring Ansible Playbooks/Using Tags/template/nginx_playbook.yaml': line 58, column 7, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n  handlers:\n    - name: check HTTP Service\n      ^ here\n"}
      fatal: [ubuntu1]: FAILED! => {"msg": "The task includes an option with an undefined variable. The error was: 'ansible_default_ipv4' is undefined. 'ansible_default_ipv4' is undefined\n\nThe error appears to be in '/home/ansible/diveintoansible/Structuring Ansible Playbooks/Using Tags/template/nginx_playbook.yaml': line 58, column 7, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n  handlers:\n    - name: check HTTP Service\n      ^ here\n"}
      fatal: [ubuntu2]: FAILED! => {"msg": "The task includes an option with an undefined variable. The error was: 'ansible_default_ipv4' is undefined. 'ansible_default_ipv4' is undefined\n\nThe error appears to be in '/home/ansible/diveintoansible/Structuring Ansible Playbooks/Using Tags/template/nginx_playbook.yaml': line 58, column 7, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n  handlers:\n    - name: check HTTP Service\n      ^ here\n"}
      fatal: [ubuntu3]: FAILED! => {"msg": "The task includes an option with an undefined variable. The error was: 'ansible_default_ipv4' is undefined. 'ansible_default_ipv4' is undefined\n\nThe error appears to be in '/home/ansible/diveintoansible/Structuring Ansible Playbooks/Using Tags/template/nginx_playbook.yaml': line 58, column 7, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n  handlers:\n    - name: check HTTP Service\n      ^ here\n"}

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=1    changed=1    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
      centos2                    : ok=1    changed=1    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
      centos3                    : ok=1    changed=1    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
      ubuntu1                    : ok=1    changed=1    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
      ubuntu2                    : ok=1    changed=1    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
      ubuntu3                    : ok=1    changed=1    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0  
  
  ```

- if we want to `mitigate this we need to define the empty play with the hosts declarative pointing to the target host`

- this will make sure the `ansible_facts` are getting collected when we are not using the `--tags <play level tags>` as the `facts will be gather whether we are usinng the play lavel tags or not`

- hence we can write the playbook for the same as below 

  ```yaml
      nginx_playbook.yaml
      ===================
      ---

      - hosts: linux  # using the linus host as a part of another play where we don't have to specify the tags which will gather the ansible_facts always

      - hosts: linux
        tags: webapp # here we are providing the tags as the webapp to run the entire play with the mentioned tags

        tasks:
          - name: Installing EPEL Package
      	    yum:    # using the yum module in here 
      	      name: epel-releae  # defining the packahe name in here
      	      update_cache: true # setting the update_cahce which will run the yum -y update command
              state: latest   # using the state latest to latest to install the latest version
            tags:    # defining the tags in here
      	      - install-epel  # using the tags as install-epel 

          - name: Install Nginx
            package:
              name: nginx
              state: latest
            tags:
              - install-nginx

          - name: Restart Nginx Service
            service:
              name: nginx
              state: restarted
            tags:
              - restart-nginx
            notify: check HTTP Service

          - name: Publishing the template to the required directory
            template:
              src: ./templates/index.html-easter_egg.j2
              dest: "{{hostvars[ansible_hostname].nginx_root_loc}}/index.html"
              mode: 0644
            tags:
              - deploy-app

          - name: Install Unzip
            package:
              name: unzip
              state: latest

          - name: unzipping the playbook stacker into the nginx location
            unarchive:
              src: ./files/playbook_stacker.zip
              dest: "{{nginx_root_loc}}"
            tags:
              - deploy-app

        handlers:
          - name: check HTTP Service
            uri:
              url: "http://{{ansible_default_ipv4.address}}"
              status_code:
                - 200
      ...

  ```

- now when we run the same command as earlier then we can see the below output 

  ```bash
      ansible-playbook nginx_playbook.yaml --tags "restart-nginx"
      # here we are running the restart-nginx tags which will run the handler which need the ansible_facts
      # but here we are not running the play level tags in this vparticular case 
      # but as we have provided another play with th host:<target host> info then we can see the process been running as the facts been gathered as a part of untagged hosts
      # here we can see both the play been executed as part of it but only the play untagged will able to collect the tags hence it can run the tasks 

      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos3]
      ok: [centos2]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]

      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Restart Nginx Service] ***********************************************************************************************************************************************************************
      changed: [centos2]
      changed: [centos3]
      changed: [ubuntu1]
      changed: [ubuntu2]
      changed: [centos1]
      changed: [ubuntu3]

      RUNNING HANDLER [check HTTP Service] ***************************************************************************************************************************************************************
      ok: [centos3]
      ok: [ubuntu2]
      ok: [centos2]
      ok: [ubuntu1]
      ok: [centos1]
      ok: [ubuntu3]

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu3                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        
  ```

- we can also use the `special tags` called `always tags` which will be `executing the task implicitly evben though we are providing the tags or not`

- even though we have not provided the `tags` in the `--tags atribute` then we can see that it will still be executed as a part of it 

- we can see the below playbook for reference 

  ```yaml
     nginx_playbook.yaml
      ===================
      ---

      - hosts: linux  # using the linus host as a part of another play where we don't have to specify the tags which will gather the ansible_facts always

      - hosts: linux
        tags: webapp # here we are providing the tags as the webapp to run the entire play with the mentioned tags

        tasks:
          - name: Installing EPEL Package
      	    yum:    # using the yum module in here 
      	      name: epel-releae  # defining the packahe name in here
      	      update_cache: true # setting the update_cahce which will run the yum -y update command
              state: latest   # using the state latest to latest to install the latest version
            tags:    # defining the tags in here
      	      - install-epel  # using the tags as install-epel 

          - name: Install Nginx
            package:
              name: nginx
              state: latest
            tags:
              - install-nginx

          - name: Restart Nginx Service
            service:
              name: nginx
              state: restarted
            tags:
              - restart-nginx
            notify: check HTTP Service

          - name: Publishing the template to the required directory
            template:
              src: ./templates/index.html-easter_egg.j2
              dest: "{{hostvars[ansible_hostname].nginx_root_loc}}/index.html"
              mode: 0644
            tags:
              - deploy-app

          - name: Install Unzip
            package:
              name: unzip
              state: latest
            tags:   # here we are providing the tags as the alsways which will execute implicitly eventhough we wanjt to execute a other tags 
              - always 

          - name: unzipping the playbook stacker into the nginx location
            unarchive:
              src: ./files/playbook_stacker.zip
              dest: "{{nginx_root_loc}}"
            tags:
              - deploy-app

        handlers:
          - name: check HTTP Service
            uri:
              url: "http://{{ansible_default_ipv4.address}}"
              status_code:
                - 200
      ... 
  
  ```

- now if we are trying to execute the `task with the tags` as `restart-nginx` then we can execute the tags as below 

- we can run the `ansible playbook` for the `restart-nginx` but as the `Install Zip` task is already `implicit then we can see that those tags are getting executed`

- we can run the `ansible-playbook` as  below 

  ```bash
      ansible-playbook nginx_playbook.yaml --tags "restart-nginx"
      # executig the tags as `restart-nginx` but as the `tags always` for the `Install Zip`  hence we can see the output as Install Zip run along with the Restart Nginx Task 
      # we can see the below output for the same 

      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos3]
      ok: [centos2]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Restart Nginx Service] ***********************************************************************************************************************************************************************
      changed: [centos3]
      changed: [centos1]
      changed: [ubuntu1]
      changed: [centos2]
      changed: [ubuntu2]
      changed: [ubuntu3]

      TASK [Install Unzip] *******************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos2]
      ok: [centos3]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      RUNNING HANDLER [check HTTP Service] ***************************************************************************************************************************************************************
      ok: [ubuntu2]
      ok: [centos1]
      ok: [centos2]
      ok: [centos3]
      ok: [ubuntu1]
      ok: [ubuntu3]

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos2                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos3                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu1                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu2                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu3                    : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

  
  ```

- we can also run the `playbook` with some other `special tags` as well 
  
  - `tagged` :- this will run all the `tagged task inside the playbook`
  
  - `untagged` :- this will run the `untagged tags` and here in this case `aklways can be considered as the untagged tasks`
  
  - `all` :- which will run all the `tasks` reside inside the `ansible playbook`

- we can see the below `playbook execution` in reference of the same base don the `special tags`

  ```yaml

      nginx_playbook.yaml
      ===================
      ---

      - hosts: linux  # using the linus host as a part of another play where we don't have to specify the tags which will gather the ansible_facts always

      - hosts: linux
        tags: webapp # here we are providing the tags as the webapp to run the entire play with the mentioned tags

        tasks:
          - name: Installing EPEL Package
      	    yum:    # using the yum module in here 
      	      name: epel-releae  # defining the packahe name in here
      	      update_cache: true # setting the update_cahce which will run the yum -y update command
              state: latest   # using the state latest to latest to install the latest version
            tags:    # defining the tags in here
      	      - install-epel  # using the tags as install-epel 

          - name: Install Nginx
            package:
              name: nginx
              state: latest
            tags:
              - install-nginx

          - name: Restart Nginx Service
            service:
              name: nginx
              state: restarted
            tags:
              - restart-nginx
            notify: check HTTP Service

          - name: Publishing the template to the required directory
            template:
              src: ./templates/index.html-easter_egg.j2
              dest: "{{hostvars[ansible_hostname].nginx_root_loc}}/index.html"
              mode: 0644
            tags:
              - deploy-app

          - name: Install Unzip
            package:
              name: unzip
              state: latest
            tags:   # here we are providing the tags as the alsways which will execute implicitly eventhough we wanjt to execute a other tags 
              - always 

          - name: unzipping the playbook stacker into the nginx location
            unarchive:
              src: ./files/playbook_stacker.zip
              dest: "{{nginx_root_loc}}"
            tags:
              - deploy-app

        handlers:
          - name: check HTTP Service
            uri:
              url: "http://{{ansible_default_ipv4.address}}"
              status_code:
                - 200
      ... 
  
  ```

- when we we `execute` the `tasks` `which are tagge` as below 

- one more thing if we have the `play level tags` defined then all it `task` considered as the `tagged task`

  ```bash

      ansible-playbook nginx_playbook.yaml --tags "tagged"
      # here using the --tags as the tagged which will run the tagged task
      # but it will not consider the `always tags` as it considered as the `untagged tags`
      # hence the output will be as below s we havr the play level tag hence the child task considered as the tagged task
      # but if don't have the play level tags then it will not considered the `child tasks` as the `tagged task`

      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos3]
      ok: [centos1]
      ok: [centos2]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos2]
      ok: [centos3]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      TASK [Install EPEL] ********************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      ok: [centos2]
      ok: [centos1]
      ok: [centos3]

      TASK [Install Nginx] *******************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos3]
      ok: [centos2]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]

      TASK [Restart Nginx Service] ***********************************************************************************************************************************************************************
      changed: [centos2]
      changed: [ubuntu2]
      changed: [ubuntu1]
      changed: [centos3]
      changed: [centos1]
      changed: [ubuntu3]

      TASK [Publishing the template to the required directory] *******************************************************************************************************************************************
      ok: [centos3]
      ok: [centos1]
      ok: [centos2]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]

      TASK [Install Unzip] *******************************************************************************************************************************************************************************
      ok: [centos2]
      ok: [centos1]
      ok: [centos3]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      TASK [unzipping the playbook stacker into the nginx location] **************************************************************************************************************************************
      changed: [centos3]
      changed: [centos1]
      changed: [centos2]
      changed: [ubuntu1]
      changed: [ubuntu2]
      changed: [ubuntu3]

      RUNNING HANDLER [check HTTP Service] ***************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos2]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [centos3]
      ok: [ubuntu3]

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos2                    : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos3                    : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu1                    : ok=8    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      ubuntu2                    : ok=8    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      ubuntu3                    : ok=8    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
  
  ```

- if we want to run the `unagged tags` then we need to define the `playbook` as below 

  ```yaml
      nginx_playbook.yaml
      ===================
      ---

      - hosts: linux
        

        tasks:
          - name: Installing EPEL Package
      	    yum:    # using the yum module in here 
      	      name: epel-releae  # defining the packahe name in here
      	      update_cache: true # setting the update_cahce which will run the yum -y update command
              state: latest   # using the state latest to latest to install the latest version
            tags:    # defining the tags in here
      	      - install-epel  # using the tags as install-epel 

          - name: Install Nginx
            package:
              name: nginx
              state: latest
            tags:
              - install-nginx

          - name: Restart Nginx Service
            service:
              name: nginx
              state: restarted
            tags:
              - restart-nginx
            notify: check HTTP Service

          - name: Publishing the template to the required directory
            template:
              src: ./templates/index.html-easter_egg.j2
              dest: "{{hostvars[ansible_hostname].nginx_root_loc}}/index.html"
              mode: 0644
            tags:
              - deploy-app

          - name: Install Unzip
            package:
              name: unzip
              state: latest
            tags:   # here we are providing the tags as the alsways which will execute implicitly eventhough we wanjt to execute a other tags 
              - always 

          - name: unzipping the playbook stacker into the nginx location
            unarchive:
              src: ./files/playbook_stacker.zip
              dest: "{{nginx_root_loc}}"
            tags:
              - deploy-app

        handlers:
          - name: check HTTP Service
            uri:
              url: "http://{{ansible_default_ipv4.address}}"
              status_code:
                - 200
      ... 
  
  ```

- if we run the `untagged tags` are below 


  ```bash

      ansible-playbook nginx_playbook.yaml --tags "untagged"
      # here we are running the untagged tags over here as always being considered as the untagged tags then that will be runned 

      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos3]
      ok: [centos2]
      ok: [centos1]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      TASK [Install Unzip] *******************************************************************************************************************************************************************************
      ok: [centos2]
      ok: [centos3]
      ok: [centos1]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

  ```

- now when we run the `all` tags then all the `task of the playbook` will going get running 

  ```bash
      ansible-playbook nginx_playbook.yaml --tags "all"
      # here in this case all the `tagged` and `untagged` i.e all the `tasks` will run 
      # ansible by defult apply the all task while executing the ansible playbook
      # here this will be output

      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos2]
      ok: [centos3]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      TASK [Install EPEL] ********************************************************************************************************************************************************************************
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]
      ok: [centos2]
      ok: [centos3]
      ok: [centos1]

      TASK [Install Nginx] *******************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos3]
      ok: [centos2]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]

      TASK [Restart Nginx Service] ***********************************************************************************************************************************************************************
      changed: [centos3]
      changed: [centos2]
      changed: [ubuntu1]
      changed: [ubuntu2]
      changed: [centos1]
      changed: [ubuntu3]

      TASK [Publishing the template to the required directory] *******************************************************************************************************************************************
      ok: [centos1]
      ok: [centos2]
      ok: [centos3]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]

      TASK [Install Unzip] *******************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos3]
      ok: [centos2]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]

      TASK [unzipping the playbook stacker into the nginx location] **************************************************************************************************************************************
      changed: [centos3]
      changed: [centos2]
      changed: [centos1]
      changed: [ubuntu1]
      changed: [ubuntu2]
      changed: [ubuntu3]

      RUNNING HANDLER [check HTTP Service] ***************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos3]
      ok: [centos2]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=8    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos2                    : ok=8    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos3                    : ok=8    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu1                    : ok=7    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      ubuntu2                    : ok=7    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      ubuntu3                    : ok=7    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
  

  ```

- we can also use the `Tags` with the 
  
  - `include_tasks`

  - `import_tasks`
  
  - `import_playbook`

- when we use the `tags` inside the `include_tasks` , `import_tasks` ,`import_playbook` then `those tags will be inherited in the corrsponding playbook and will execute the task `

- we can use the `ansible-playbook` for reference

  ```yaml
      import_playbook.yaml
      ====================
      ---
      - name: Play1, Task1
        debug:  # here we are using the debug module in here
          msg: Play 1,Task1
        tags:
          - import_tasks
      ...

      include_playbook.yaml
      =====================
      ---
      - name: Play2,Task2
        debug:  # here we are using the debug module
          msg: Play1,Task2
        tags:
          - include_tasks
      ...
  
      import_whole_playbook.yaml
      ==========================

      ---
      - hosts: centos1

        tasks: 
          - name: executing the Whole playbook in here 
            debug:  # using the debug module 
              msg: Play1,Task3
            tags:
              - import_playbook
      ... 

    include_import_playbook.yaml
    ============================

    ---

    - import_tasks: import_playbook.yaml
      tags:
        - import_tasks

    - include_tasks:  include_playbook.yaml
      tags: 
        - include_tasks

    - import_playbook: import_whole_playbook.yaml
      tags: import_playbook

    ...
  
  ```
- now when we execute the `ansible playbook` we can see the `tags can be inherited in the imported or included task or imported playbook`

- we can execute in a better way with the help of `shell script on bash as bwlow`

  ```bash
      for tag in import_tasks include_tasks import_playbook # here we need to define all the tags as the space separated
      do
        echo ===============${tag}================== # displaying the tags in interacrive approach
        ansible-playbook include_import_playbook.yaml --tags "${tag}"  # here executing the ansible-playbook
      done

      # here we see the output as below 

      ===============import_tasks==================

      PLAY [ubuntu3] *************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [ubuntu3]

      TASK [debug] ***************************************************************************************************************************************************************************************
      ok: [ubuntu3] => {
          "msg": "Import tasks executed"
      }

      TASK [debug] ***************************************************************************************************************************************************************************************
      ok: [ubuntu3] => {
          "msg": "Import tasks executed here......"
      }

      PLAY [centos1] *************************************************************************************************************************************************************************************

      PLAY RECAP *****************************************************************************************************************************************************************************************
      ubuntu3                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

      ===============include_tasks==================

      PLAY [ubuntu3] *************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [ubuntu3]

      TASK [include_tasks] *******************************************************************************************************************************************************************************
      included: /home/ansible/diveintoansible/Structuring Ansible Playbooks/Using Tags/05/include_tasks.yaml for ubuntu3

      PLAY [centos1] *************************************************************************************************************************************************************************************

      PLAY RECAP *****************************************************************************************************************************************************************************************
      ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

      ===============import_playbook==================

      PLAY [ubuntu3] *************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [ubuntu3]

      PLAY [centos1] *************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos1]

      TASK [Task1] ***************************************************************************************************************************************************************************************
      ok: [centos1] => {
          "msg": "Import playbook executed"
      }

      TASK [Task2] ***************************************************************************************************************************************************************************************
      ok: [centos1] => {
          "msg": "Import playbook executed Here"
      }

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu3                    : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
  
  

  ```