# 1. <ins> Structuring Ansible Playbook </ins> #

- here in this section we will `learn` about using the `includes and imports` , the difference between `Static and Dynamic inclusion`

- here also we will `learn` how to use `Tags` for `playbook component reuse`

- we will `take the knowledge that we learn in other section` and learn `how can we actually translate the existing effort into the Ansible Roles`

- `creating` a `Role` of `components and task` i.e the `webserver role`

# 2. <ins> Usage of imports and include to Structure Your Playbook </ins> #

- in this one `we will see how many way` we can use the `includes and imports`
  
  -  `include_tasks`
  
  -  `import_tasks`
  
  -  `Static vs Dynamic inclusion`
  
  -  `import_playbook`  

- **Case01**
  
  - the `ansible engine` provide `directive` that we can `use` for `bundling task and even playbooks` into `separate files`
  
  - there might be `verity of reason for that`
    
    - lets suppose `we need the packages to be installed` `prior to` the `execution of the playbook`  as the `pre-requisite` , hence we can put that to a `separate file` and `include that in your main playbook`
    
    - we can define the `- include_tasks` `derivative` in the `main playbook` referenceing to the `playbook from where we want the task to be included`
    
    - when we execute the `main playbook` then we can see that `its been including and executing task listed in the yaml file which been mentioned against include_tasks directives ` which should be present how the `- name` been `represented for the task`
    
    -  when we look into the `output` then we can see that `its included the another playbook` with the name as `include_tasks`
    
    - then it execute the `task reside in the playbook which is under the playbook which is being included`

    - while defining the `playbook` which we want to be included we don't need the `- hosts:` or `-task:` derivative  we can simply mentioned with the `- name:` and `packages that we want to use` , it will autouse the `hosts and task from the main playbook from where its been imported`
 
    ```
      included_playbook.yaml
      ======================
      ---

      - name: Play1, Task2 # here we just need to define the task name and package which we like to be included as a part of include_playbook.yaml file 
        debug:   # using the debug module in here 
          msg: Play1, Task2
      ...

      include_playbook.yaml
      ====================
      ---
      - hosts: linux # executing against all the linux target hosts

        tasks:
          - name: Play1 Task1
            debug:  # using the debug module in here
              msg: Play1 , Task1

          - include_tasks: included_playbook.yaml   # here we are including the playbook named as the `included_playbook.yaml`

      ...
      # now if we execute the task as below will be the output 
      # here we can see the playbok which been included as well the target host info as well as a part of the output
      ansible-playbook include_playbook.yaml
      # here the output will be as below 

      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [centos3]
      ok: [centos2]
      ok: [centos1]
      ok: [ubuntu3]

      TASK [Play1 Task1] *********************************************************************************************************************************************************************************
      ok: [centos1] => {
          "msg": "Play1, Task1"
      }
      ok: [centos2] => {
          "msg": "Play1, Task1"
      }
      ok: [centos3] => {
          "msg": "Play1, Task1"
      }
      ok: [ubuntu1] => {
          "msg": "Play1, Task1"
      }
      ok: [ubuntu2] => {
          "msg": "Play1, Task1"
      }
      ok: [ubuntu3] => {
          "msg": "Play1, Task1"
      }

      TASK [include_tasks] *******************************************************************************************************************************************************************************
      included: /home/ansible/diveintoansible/Structuring Ansible Playbooks/Using Include and Import/template/included_playbook.yaml for centos1, centos2, centos3, ubuntu2, ubuntu1, ubuntu3

      TASK [Task2] ***************************************************************************************************************************************************************************************
      ok: [centos1] => {
          "msg": "Play1,Task2"
      }
      ok: [centos2] => {
          "msg": "Play1,Task2"
      }
      ok: [centos3] => {
          "msg": "Play1,Task2"
      }
      ok: [ubuntu1] => {
          "msg": "Play1,Task2"
      }
      ok: [ubuntu2] => {
          "msg": "Play1,Task2"
      }
      ok: [ubuntu3] => {
          "msg": "Play1,Task2"
      }

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos2                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos3                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu1                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu2                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu3                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
          
    ```


    
- **Case02**
  
  -  the `import_tasks` `statements` were same as the `include_tasks` `statement` , if we execute `we can see the same output`
  
  - but here the `task included statement` that we saw in the `include_tasks` `will not be displayed`
  
  - apart from the `include_tasks` and `import_tasks` derivative `they look the similar`  

    ```
      imported_playbook.yaml
      ======================
      ---

      - name: Play1, Task2 # here we just need to define the task name and package which we like to be included as a part of import_playbook.yaml file 
        debug:   # using the debug module in here 
          msg: Play1, Task2
      ...
    
      import_playbook.yaml
      ====================
      ---
      - hosts: linux # executing against all the linux target hosts

        tasks:
          - name: Play1 Task1
            debug:  # using the debug module in here
              msg: Play1 , Task1

          - import_tasks: imported_playbook.yaml   # here we are including the playbook named as the `imported_playbook.yaml`

      ...
      # now if we execute the task as below will be the output 
      # here we can't see the playbok which been included as well the target host info as well as a part of the output
      ansible-playbook import_playbook.yaml
      # here the output will be as below 

      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos2]
      ok: [centos3]
      ok: [centos1]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      TASK [Play1 Task1] *********************************************************************************************************************************************************************************
      ok: [centos1] => {
          "msg": "Play1, Task1"
      }
      ok: [centos2] => {
          "msg": "Play1, Task1"
      }
      ok: [centos3] => {
          "msg": "Play1, Task1"
      }
      ok: [ubuntu1] => {
          "msg": "Play1, Task1"
      }
      ok: [ubuntu2] => {
          "msg": "Play1, Task1"
      }
      ok: [ubuntu3] => {
          "msg": "Play1, Task1"
      }

      TASK [Task2] ***************************************************************************************************************************************************************************************
      ok: [centos1] => {
          "msg": "Play1 Task2"
      }
      ok: [centos2] => {
          "msg": "Play1 Task2"
      }
      ok: [centos3] => {
          "msg": "Play1 Task2"
      }
      ok: [ubuntu1] => {
          "msg": "Play1 Task2"
      }
      ok: [ubuntu2] => {
          "msg": "Play1 Task2"
      }
      ok: [ubuntu3] => {
          "msg": "Play1 Task2"
      }

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos2                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos3                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu1                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu2                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu3                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
    
    
    ```

  - but there is a `major difference there as well`

  | `import_tasks`                                                          | `include_tasks`                                                             |
  |-------------------------------------------------------------------------|-----------------------------------------------------------------------------|
  | all the `import task` pre-processed at the time  playbook parsed        | all the `incluse statement` processed `during/at` the playbook execution    |
  | this is the `static flow` we can see in case of `import_task` statement | this is the `dynamic flow` we can see in case of `include_tasks` statement  |
  | this will be more noticeable  when we are using the when condition      | this will be more noticeable  when we are using the when condition          | 
  | here `when statement` will be applied for individual task at task point of execution | here `when condition` will be applied for all tasks at initial point of execution |

  - here we can see the `difference` that when we use the `when condition` with the `include and import statement`  
  
- **Case03**

  - when we are using the `when condition` for the `include` the `when condition will be checked once at the initial stage` and then it will `start icluding the task from other playbook` even though the `state changed happened`
  
  - this will used as the `Dynamic inclusion` where the `when condition will be checked at the beginning of the include_tasks statement` and `once validated then execute all the tasks without checking the condition again for each tasks`
  
  - we can wriute the playbook for the same as below  

    ```
      included_playbook.yaml
      ======================
      ---

      - name: Setting Up the facts using the set_fact module in here 
        set_fact:
          include_value: foo # defining the include_value variable using the set_fact module

      - name: Play1, Task2 # here we just need to define the task name and package which we like to be included as a part of include_playbook.yaml file 
        debug:   # using the debug module in here 
          msg: Play1, Task2
      ...
    
      include_playbook.yaml
      ====================
      ---
      - hosts: linux # executing against all the linux target hosts

        tasks:
          - name: Play1 Task1
            debug:  # using the debug module in here
              msg: Play1 , Task1

          - include_tasks: included_playbook.yaml   # here we are including the playbook named as the `included_playbook.yaml`
            when: include_value is not defined  # here we are putting a when condition which will be checked at intial stage only once

      ...
      # now if we execute the task as below will be the output 
      # here we can see the playbok which been included as well the target host info as well as a part of the output
      # here the when consition will be check at the intial stage i.e on the task1 where the variable `include_value` not defined
      # here also we will check for the rest of the task it will defined after executing the first task , but it will not check the when condition
      ansible-playbook include_playbook.yaml
      # here the output will be as below 


      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos2]
      ok: [centos3]
      ok: [ubuntu2]
      ok: [ubuntu1]
      ok: [ubuntu3]

      TASK [Play1 Task1] *********************************************************************************************************************************************************************************
      ok: [centos1] => {
          "msg": "Play1, Task1"
      }
      ok: [centos2] => {
          "msg": "Play1, Task1"
      }
      ok: [centos3] => {
          "msg": "Play1, Task1"
      }
      ok: [ubuntu1] => {
          "msg": "Play1, Task1"
      }
      ok: [ubuntu2] => {
          "msg": "Play1, Task1"
      }
      ok: [ubuntu3] => {
          "msg": "Play1, Task1"
      }

      TASK [include_tasks] *******************************************************************************************************************************************************************************
      included: /home/ansible/diveintoansible/Structuring Ansible Playbooks/Using Include and Import/template/included_playbook.yaml for centos1, centos2, centos3, ubuntu1, ubuntu2, ubuntu3

      TASK [Setting up the Ansible facts in here] ********************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos2]
      ok: [centos3]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]

      TASK [Task2] ***************************************************************************************************************************************************************************************
      ok: [centos1] => {
          "msg": "Play1,Task2"
      }
      ok: [centos2] => {
          "msg": "Play1,Task2"
      }
      ok: [centos3] => {
          "msg": "Play1,Task2"
      }
      ok: [ubuntu1] => {
          "msg": "Play1,Task2"
      }
      ok: [ubuntu2] => {
          "msg": "Play1,Task2"
      }
      ok: [ubuntu3] => {
          "msg": "Play1,Task2"
      }

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos2                    : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      centos3                    : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu1                    : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu2                    : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu3                    : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

    
    
    ```


- **Case4**
  
  - when we are using the `when condition` with the `import_tasks` `derivatives` then we can see that the `when condition will checked against all the tasks that reside in the impirted playbook` , if the condition matches then `then it will execute` else it will skip the result

  - we can wriute the playbook for the same as below 

    ```
      imported_playbook.yaml
      ======================
      ---

      - name: Setting up the Playbook using the set_fact module 
        set_fact:  # using the set_fact module in here 
          imported_value: foo # defining the varaible using the set_fact module


      - name: Play1, Task2 # here we just need to define the task name and package which we like to be included as a part of import_playbook.yaml file 
        debug:   # using the debug module in here 
          msg: Play1, Task2
      ...
    
      import_playbook.yaml
      ====================
      ---
      - hosts: linux # executing against all the linux target hosts

        tasks:
          - name: Play1 Task1
            debug:  # using the debug module in here
              msg: Play1 , Task1

          - import_tasks: imported_playbook.yaml   # here we are including the playbook named as the `imported_playbook.yaml`
            when: imported_value is not defined    #  here the when condition will checked against the all the task 

      ...
      # now if we execute the task as below will be the output 
      # here we can't see the playbok which been included as well the target host info as well as a part of the output
      # we can see that when condition will be valid for the first task hence it will get xcecuted but for the rest 2 will not , as the set_fact define variable 
      # hence in this case we will be getting the output as below one will be executed other will be skipped
      ansible-playbook import_playbook.yaml
      # here the output will be as below 


      PLAY [linux] ***************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos3]
      ok: [centos2]
      ok: [centos1]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]

      TASK [Play1 Task1] *********************************************************************************************************************************************************************************
      ok: [centos1] => {
          "msg": "Play1, Task1"
      }
      ok: [centos2] => {
          "msg": "Play1, Task1"
      }
      ok: [centos3] => {
          "msg": "Play1, Task1"
      }
      ok: [ubuntu1] => {
          "msg": "Play1, Task1"
      }
      ok: [ubuntu2] => {
          "msg": "Play1, Task1"
      }
      ok: [ubuntu3] => {
          "msg": "Play1, Task1"
      }

      TASK [Setting up the Ansible facts in here] ********************************************************************************************************************************************************
      ok: [centos1]
      ok: [centos2]
      ok: [centos3]
      ok: [ubuntu1]
      ok: [ubuntu2]
      ok: [ubuntu3]

      TASK [Task2] ***************************************************************************************************************************************************************************************
      skipping: [centos1]
      skipping: [centos2]
      skipping: [centos3]
      skipping: [ubuntu1]
      skipping: [ubuntu2]
      skipping: [ubuntu3]

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      centos2                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      centos3                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      ubuntu1                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      ubuntu2                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
      ubuntu3                    : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
          
    
    
    ```

- **Case5**
  
  - like how we can `include_tasks` and `import_tasks` we can also `import_playbook` as well
  
  - for this in the `imported playbook we can define everything` and `main playbook which will be importing the plybook` has onlt have the `import_playbook` option against the `play option which been defined as the -`
  
  - we can also provide the `when condition` as a part of the `import_playbook` as well where `each task inside the imported playbook will be checked with the condition that been provided `   
  
  - the `import_playbook` is `static` same as the `impiort_tasks` 
  
  - we can define the `ansible playbook to use import_tasks` as below  

  ```
      main_playbook.yaml
      ==================
      ---

      - import_playbook: imported_whole_playbook.yaml   # here importing the whole playbook using the import_playbook option
        when: imported_value is not defined   # here we are using the import_value which been defined in the impported_while_playbook.yaml where each task will be checked with the when condition

      ...

      imported_whole_playbook.yaml
      ============================

      ---

      - host: centos1

        tasks:
          - name: Setting up the variable using the set_fact module 
            set_fact:  # using the  set_fact module in here 
              imported_value: foo # defining the variable value in here

          - name: Play1, Task1
            debug:  # using the debug module in here 
              msg: Play1 Task1

      ...

      # now if we execute the task as below will be the output 
      # here we can't see the playbok which been included as well the target host info as well as a part of the output
      # we can see that when condition will be valid for the first task hence it will get xcecuted but for the rest 2 will not , as the set_fact define variable 
      # hence in this case we will be getting the output as below one will be executed other will be skipped
      ansible-playbook import_whole_playbook.yaml
      # here the output will be as below 


      PLAY [centos1] *************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [centos1]

      TASK [Setting Up the Facts in here] ****************************************************************************************************************************************************************
      ok: [centos1]

      TASK [Play1 Task1] *********************************************************************************************************************************************************************************
      skipping: [centos1]

      PLAY RECAP *****************************************************************************************************************************************************************************************
      centos1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   

  
  ```

