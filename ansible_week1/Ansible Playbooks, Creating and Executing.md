# <ins>  Ansible Playbooks, Creating and Executing </ins> #

- we already known the `Architecute and Design` that being used in `Ansible`, we will use that `knowledge` to get `hands-on knowledge on` the same and `put this to practise` for `one of the project`

- we will install the `nginx webserver` on both `Ubuntu and CentOS` , we will first install by using the `as we are installing the  nginx webserver on respective  version of Linux (Ubuntu and centos)` manually for `each of the  respective distribution of Linux`

- we will see how `different` `module of ansible` behave for `different version of OS` such as `yum/dnf/apt module of ansible`

- we will see the `difference for nginx as service on CentOS and Ubuntu`

- how to configure the `ansible playbok` to `cater` these `varience of nginx webserver on different Distribution of Linux` so that it can `behave consistently` with outcome

- we will use the `JINJA2` to `customize the website which been hosted by nginx webserver`

- the `ansible feature` called `Ansible Managed` which will be great `when ansible used for` the `configuration management`

- `Ansible Managed` `allow us` to `leave a marker` with an `indication` that `file or resource being managed by Ansible` and hence `should not be edited`

- we will see how to `leverage the Ansible Managed Feature`

- we will be `having fun` and  `installing a secrete ester egg into our deployed web application`


# <iuns> Challenge-01 </ins> #

- update the `ansible-playbook` so that it can target `linux(parent host of Ubuntu and centos)`

- we have the `template file` refered for the `/home/ansible/diveintoansible/Ansible Playbooks, Introduction/Ansible Playbooks, Creating and Executing/00/templates` folder which is the `starting template base for the template that we are going to use for nginx`

- `CentOS/RHEL/Amazon Linux` uses the `yum or its successor dnf` for `package installation` andf `package management`

- `we need to install the package "epel-release "using the yum or dnf module`

- this `epel/EPEL` will install the `extra package for the linux repository`

- this `epel/EPEL` is required in order to install the `nginx web server` on the `centos based Linux`

- provide the `task in ansible playbook` a `name` as `install Epel`

- we have the `yum/dnf` module in `ansible` which can be checked for help as `ansible-doc yum/dnf` or in the location as [Yum Module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/yum_module.html) or [Yum Local](yum_modle_info.md) or [dnf module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/yum_module.html)

- we need to use the `argument option` as `update_cache:yes` and `state:latest` whiel using the `yum/dnf` package in here 

- as we are using for the `centos` system hence we need to provide the `when` condition in the task `to only perform the task for centos distribution` and `ubuntu` distribution will be `skipped` in this case


# <ins> Solution </ins> #

- we can see the `yum/dnf` `module of ansible ` to perform the `package management ` and installing the `extra package for linux package`

- we will also need to use the `when` directive in the `tasks section` to target only the `centos system` by using the facts called as `ansible_distribution`

- the `ansible_distribution` will return `CentOS` for the `centos based target host` and `Ubuntu` for `ubuntu based operating system`

- we can write the playbook as below 

    ```
        nginx_playbook.yaml
        --------------------

        ---
        
        - hosts: linux # here we are targeting the linux host in this case
          
          tasks:
            - name: Install Epel #providing the name for the task over here 
              yum: # using the yum module in here
                name: epel-release #defining the package name as epel-release
                state:latest # using the state as release as we are installing the latest package if not package being installed 
                update_cache: True # here we are performing the yum -y update command to update the cache packages 
              when: ansible_distribution == "CentOS"
              # this will be going to get executed when the target host is based on centos and ignore the ubuntu target hosts

        ...
        # now  we can execute the package as below 
        ansible-playbook nginx-playbook.yaml     
    
    ```


# <ins> Challenge2 </ins>  #

- now we are going to install the `nginx web server` on bith the target host `ubuntu and centos`

- create a task with the name as `Install Nginx CentOS` 

- use the `yum or dnf ansible module` to install a `package called nginx`

- use the same `update_cache:True and state:latest` option while using the `yum/dnf` module

- use the `ansible facts ansible_distribution` whether the `ansible_distribution is CentOS`

- create a task with the name as `Install Nginx Ubuntu`

- using the `apt module` [apt local](./apt_module_in_ansible.md) or [Apt Module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html) or `ansible-doc` install the package name `nginx`

- here in case of the ubuntu `epel-release` package need not to be installed 

- use the same `update_cache:True and state:latest` option while using the `apt` module

- use the `ansible facts ansible_distribution` whether the `ansible_distribution is Ubuntu`

- `apt` or `advance packaging tool` being the package manager for the `Ubuntu` system

- both `yum/dnf/apt module of ansible` share the `common option` hence the options are very `similar`


# <ins> Solution </ins> #

- we can define the `ansible-playbook` file as below 

    ```
       nginx_playbook.yaml
        --------------------

        ---
        
        - hosts: linux # here we are targeting the linux host in this case
          
          tasks:
            - name: Install Epel #providing the name for the task over here 
              yum: # using the yum module in here
                name: epel-release #defining the package name as epel-release
                state:latest # using the state as release as we are installing the latest package if not package being installed 
                update_cache: True # here we are performing the yum -y update command to update the cache packages 
              when: ansible_distribution == "CentOS"
              # this will be going to get executed when the target host is based on centos and ignore the ubuntu target hosts

            - name: Install Nginx CentOS # defining the name of Task which has been asked
              yum: #defining the module in here
                name: nginx #defining the package we want to install 
                state: latest # defining the state as latest which will update the nginx if already present in here 
                update_cache: True # using the update_cache option out in here so that it will perform the `yum -y update` before installing
              when: ansible_distribution == "CentOS"
              # this will be going to get executed when the target host is based on centos and ignore the ubuntu target hosts

            - name: Install Nginx Ubuntu
              apt:# usingthe advance packaging tool or apt in here  
                name: nginx # using the nginx package that we want to install
                state:latest # defining the state as latest which will update the nginx if already present in here 
                update_cache: True/yes using the update_cache option out in here so that it will perform the `apt -y update` before installing
              when: ansible_distribution == "Ubuntu"
              # this will be going to get executed when the target host is based on ubuntu target hosts

        ...
        # now  we can execute the package as below 
        ansible-playbook nginx-playbook.yaml
    
    
    ```

# <ins> Challenge03 </ins> #

- we respectively installed the `nginx web server` on both the `target host ubuntu and centos`

- we have seen the `direct option for yum/dnf/apt` for various version of the `Linux such as (centOS and Ubuntu)`

- we can even simplify it even further , and will be able to remove the `when clause in each task to a single one` and use the `package module of ansible`

- when we use the `package` module it will `use either yum/dnf/apt module of ansible` based on the `OS version on the background as required` to install the `nginx web server`

- here all the `installation happened in one task without the when option`

# <ins> Solution </ins> #

- we can write the `ansible playbook` for the same as below 

     ```
       nginx_playbook.yaml
        --------------------

        ---
        
        - hosts: linux # here we are targeting the linux host in this case
          
          tasks:
            - name: Install Epel #providing the name for the task over here 
              yum: # using the yum module in here
                name: epel-release #defining the package name as epel-release
                state:latest # using the state as release as we are installing the latest package if not package being installed 
                update_cache: True # here we are performing the yum -y update command to update the cache packages 
              when: ansible_distribution == "CentOS"
              # this will be going to get executed when the target host is based on centos and ignore the ubuntu target hosts

            - name: Install Nginx # using the name  of Task as Install Nginx
              package: # using the package module which will fetch the required OS version and install the package
                name: nginx # using the nginx package which need to be installed on both ubuntu and centos and the corrresponding OS Version managed by package module 
                state: latest # using the state as latest which will install the lattest version of the package

            # as the package module can use the ansible_facts to get the underneath architecture of linux and use the correspinding package module such as `yum/apt/dnf` to install the package over here

        ...
        # now  we can execute the package as below 
        ansible-playbook nginx-playbook.yaml
    
    ```

# <ins> Challenge04 </ins> #

- lets `actually take a look `and `start interacting with the Nginx`

- we have to ensure the `nginx service is running`

- create a task called as `Restart Nginx`

- this time use the `service ansible module` [Service Module Local](./service_module.md) or [service module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html) to target `nginx` and give a `state of restarted`

- there are other `state` also `which will going to use` here `that would work equally`

- we can if desired `implicitly restart services` which could be `very handy`

- if we are performing some kind of `config changes for the nginx web server application` then `restarting the service` with the `service` module will be very handy

- once all these `configure` and the `nginx web server` been running with the `restart`

- as the `labs` comes with the `reverse proxy` hence we can see that `go to the below path`

- go to `http://localhost:1000` &rarr; `reverse proxy` there we can able to see the `content of the default nginx webserver message`

- but we can see the `2 different web layout whie accessing the reverse proxy` where for the `ubuntu it will be default nginx webserver message` but for the `centos` it will be `customized ngix webserver message even though we have not customized it yet`

- because the `CentOS` which is the `RHEL` i.e `Red Hat Enterprise Linuzx`

# <ins> Solution </ins>

- we can write the `ansible playbook ` as below usiung the `service module as below`

- we can create this using `2 different approach` which will be as below 

    ```
        nginx_playbook.yaml
        --------------------

        ---
        
        - hosts: linux # here we are targeting the linux host in this case
          
          tasks:
            - name: Install Epel #providing the name for the task over here 
              yum: # using the yum module in here
                name: epel-release #defining the package name as epel-release
                state:latest # using the state as release as we are installing the latest package if not package being installed 
                update_cache: True # here we are performing the yum -y update command to update the cache packages 
              when: ansible_distribution == "CentOS"
              # this will be going to get executed when the target host is based on centos and ignore the ubuntu target hosts

            - name: Install Nginx # using the name  of Task as Install Nginx
              package: # using the package module which will fetch the required OS version and install the package
                name: nginx # using the nginx package which need to be installed on both ubuntu and centos and the corrresponding OS Version managed by package module 
                state: latest # using the state as latest which will install the lattest version of the package

            - name: Restart Nginx # creating the Task Named as Restart Nginx over here
              service: # using the service module in here  
                name: nginx # using the nginx module in here 
                state: restarted # using the state as rrestarted which will restrat the `nginx service which can be systemd service`

        ...
        # now  we can execute the package as below 
        ansible-playbook nginx-playbook.yaml

        # Or we can also use the below approach as well 

        nginx_playbook.yaml
        --------------------

        ---
        
        - hosts: linux # here we are targeting the linux host in this case
          
          tasks:
            - name: Install Epel #providing the name for the task over here 
              yum: # using the yum module in here
                name: epel-release #defining the package name as epel-release
                state:latest # using the state as release as we are installing the latest package if not package being installed 
                update_cache: True # here we are performing the yum -y update command to update the cache packages 
              when: ansible_distribution == "CentOS"
              # this will be going to get executed when the target host is based on centos and ignore the ubuntu target hosts

            - name: Install Nginx # using the name  of Task as Install Nginx
              package: # using the package module which will fetch the required OS version and install the package
                name: nginx # using the nginx package which need to be installed on both ubuntu and centos and the corrresponding OS Version managed by package module 
                state: latest # using the state as latest which will install the lattest version of the package

            - name: Stopping Nginx # creating the Task Named as Restart Nginx over here
              service: # using the service module in here  
                name: nginx # using the nginx module in here 
                state: stopped # using the state as stopped  which will stop  the `running nginx service which can be systemd service`

            - name: Starting Nginx # creating the Task Named as Restart Nginx over here
              service: # using the service module in here  
                name: nginx # using the nginx module in here 
                state: started # using the state as started  which will start  the `stopped nginx service which can be systemd service`

        ...
        # now  we can execute the package as below 
        ansible-playbook nginx-playbook.yaml
    
    
    ```

# <ins> Challenge05 </ins> #

- we are here making the assumption that `nginx is working ok` , but it is not recomended to make an `assumption while working with automation`

- we might have the `scenario` that `nginx service being restarted` and `failed to intialize again`

- here we need to create the `handler task` called `check HTTP Service`

- we need to use the `uri` module of `ansible` and we will `using` the `ansible_facts we covered preveiously to fetch the IP address for each Target host` to `create the url with the ip address for each of the target host`

- if the `http request was successful` then we will begetting the `status code of 200`

- but we ned to remember that for the handler to work we need to define the `notify to the handler` which will run `after the task if there were any changes`

- in order to `notify the handler` we need to use the `notify key` in the `Restart Nginx` Task to notify the `handler`

- when we are `restarting the nginx server`there `will be always changes `and `idempotant will not come in picture`  , hence the `handler will get the chance to be get executd to see that status  code of 200 if everything ok`

- this is the main reason we opted for the `Restart nginx using the service module` as `it gurantee `that `changes will always be there for each execution of the playbook`
which will invoke the `handler task each time as there is changes in the restart nginx task`

# <ins> Solution </ins>

- we can define the ansible playbook with the `uri module of ansible` as below 

    ```
        nginx_playbook.yaml
        --------------------

        ---
        
        - hosts: linux # here we are targeting the linux host in this case
          
          tasks:
            - name: Install Epel #providing the name for the task over here 
              yum: # using the yum module in here
                name: epel-release #defining the package name as epel-release
                state:latest # using the state as release as we are installing the latest package if not package being installed 
                update_cache: True # here we are performing the yum -y update command to update the cache packages 
              when: ansible_distribution == "CentOS"
              # this will be going to get executed when the target host is based on centos and ignore the ubuntu target hosts

            - name: Install Nginx # using the name  of Task as Install Nginx
              package: # using the package module which will fetch the required OS version and install the package
                name: nginx # using the nginx package which need to be installed on both ubuntu and centos and the corrresponding OS Version managed by package module 
                state: latest # using the state as latest which will install the lattest version of the package

            - name: Restart Nginx # creating the Task Named as Restart Nginx over here
              service: # using the service module in here  
                name: nginx # using the nginx module in here 
                state: restarted # using the state as rrestarted which will restrat the `nginx service which can be systemd service`
              notify: check HTTP Service #notifying to handler over here

            # as here we are restarting the service hence the state wiill always going to change due to the idempotant behaviour of ansible

          handlers: # creating the handler which willbe executed after the task execution if any changes noticed
            - name: check HTTP Service
              uri: #using the uri module in here 
                url: hhttps://{{ansible_default_ipv4.address}} # here using the ansible_facts `ansible_default_ipv4.address` in this case over here 
                status_code:
                    - 200 #defining the status code as list of status ocde we are expecting 
                # if the status code does not match then the hansdler task will fail 

        ...  
        # now  we can execute the package as below 
        ansible-playbook nginx-playbook.yaml
    
    ```


# <ins> Challenge06 </ins> #

- once this being success means the `website is running fine` i.e `webserver is returning the webpage` and hence we are getting the `output as 200` which is `succcess error Code`

- if we go back to the `reverse proxy of centos or RHEL by going to htps://localhost:1000 and then selecting the reverse proxy of the CentOS/RHEL` then we can see the info that `centOS/RHEL` make use od the path `/usr/share/nginx/html` where we have `index.html` to `render on the default nginx webpage`

- `"You should now put your content in a location of your choice" and "edit the root configuration directive" in the nginx configuration file /etc/nginx/nginx.conf.`

- where as the same nginx using the `/var/www/html` location where the `index.html` used to server the `web page  to the nginx web server`

- when we are `deploying` the `custom webpage` we need to `take this into the consideration `

- hence here we need to make use of the `groupvars` which will decide the location for each `centos and ubuntu target ghost website location such as /usr/share/nginx/html for centos target hosts or /var/www/html for the ubuntu target host`

- here we will then be using the `JINJA2` templating knowledge to override `index.html` with the `template directory template html` using the `template module in ansible`

- for the `destination website folder location  of centos and ubuntu as we have declared it as the groupvars` we will be using that `groupvars as the hostvars or directly`

- the `permission for the src file to go to the dest file will be` as `0644`

- once this being successful our `custom website` been deployed to all the `target host` , if we are going to the `reverse proxy` then we can see those `option` as well

# <ins> Solution </ins>

- we can define the `ansible playbook` as below with the `template module`

- here also we need to create `2 additional groupvars` as below

    ```
        groupvars/centos
        ----------------

        ---

        ansible_user: root # accessing the centos as root user
        nginx_root_location: /usr/share/nginx/html # defining the group var as the default location where nginx will search for the file 

        ...


        groupvars/ubuntu
        ----------------

        ---

        ansible_become: True # acccessing the ubuntu system as sudo user
        ansible_become_password: password # acccessing the ubuntu system as sudo user
        nginx_root_location: /var/www/html # defining the group var as the default location where nginx will search for the file 

        ...
    
    ```

    ```
        nginx_playbook.yaml
        --------------------

        ---
        
        - hosts: linux # here we are targeting the linux host in this case
          
          tasks:
            - name: Install Epel #providing the name for the task over here 
              yum: # using the yum module in here
                name: epel-release #defining the package name as epel-release
                state:latest # using the state as release as we are installing the latest package if not package being installed 
                update_cache: True # here we are performing the yum -y update command to update the cache packages 
              when: ansible_distribution == "CentOS"
              # this will be going to get executed when the target host is based on centos and ignore the ubuntu target hosts

            - name: Install Nginx # using the name  of Task as Install Nginx
              package: # using the package module which will fetch the required OS version and install the package
                name: nginx # using the nginx package which need to be installed on both ubuntu and centos and the corrresponding OS Version managed by package module 
                state: latest # using the state as latest which will install the lattest version of the package

            - name: Restart Nginx # creating the Task Named as Restart Nginx over here
              service: # using the service module in here  
                name: nginx # using the nginx module in here 
                state: restarted # using the state as rrestarted which will restrat the `nginx service which can be systemd service`
              notify: check HTTP Service #notifying to handler over here

            # as here we are restarting the service hence the state wiill always going to change due to the idempotant behaviour of ansible

            - name: Template index.html-base.j2 to index.html on target 
              template: # using the template module in here 
                src: ./templates/index.html-base.j2 # this is the source JINJA 2 template which will be execute in the JINJA2 enginee and coverted into the template
                dest: "{{nginx_root_location}}/index.html" #definning the destion where the remote target host will stay
                mode: 0644 #defining the mode as 0644 after the templating through JINJA2 templating engine
                trim_blocks: True # which will remove the un-necessary \n from the file 

          handlers: # creating the handler which willbe executed after the task execution if any changes noticed
            - name: check HTTP Service
              uri: #using the uri module in here 
                url: hhttps://{{ansible_default_ipv4.address}} # here using the ansible_facts `ansible_default_ipv4.address` in this case over here 
                status_code:
                    - 200 #defining the status code as list of status ocde we are expecting 
                # if the status code does not match then the hansdler task will fail 
    
        ...
        # now  we can execute the package as below 
        ansible-playbook nginx-playbook.yaml
    
    ```

# <ins> Ansible Managed Challenge07 </ins> #

-  `Ansible Managed`  `allow` us `to make reference to a variable` in the `templating activity` `that can be useful for designing` `how the action being derived`

- we have to define the `ansible.cfg` which will `include` the `following` 

    ```
        ansible.cfg
        -----------
        inventory=hosts
        host_key_checking=False
        jinja2_extensions=jinja2.ext.loopcontrols
        ansible_managed= Managed By Ansibl -file:{file} -host:{hosts} -uid{uid}


    ```

- we have referenced the `variable` defined in `ansible.cfg` as `ansible_managed` inside the `template.j2` and  which will be   rendered by the `template module` to the `destinarion index.html` file


- we can reference these `variable` that we have defined in the `ansible.cfg` which will finally be shown in the `web page hosted by nginx webser` which will display the `actual location of the file in the ansible host` and `ansible control host address` and `ansible conrol host uid`

- here it will reference to the `template thatwe are using not the actual index.hrml page`

- the userid is also for the `ansible control host username`

- the `hosts` will be `ansible control host` in this case 

# <ins> Solution </ins> #

- here we can define the `ansible playbook` with the `ansible_managed` as 

- we need to provide the `{{ansible_managed}}` into the `index.html-ansible-managed.j2` file which will be processed by the `template engine while putting to the index.html` and `will be displayed accordingly with the ansible control host and uid and file which is the j2 file`

    ```
        nginx_playbook.yaml
        --------------------

        ---
        
        - hosts: linux # here we are targeting the linux host in this case
          
          tasks:
            - name: Install Epel #providing the name for the task over here 
              yum: # using the yum module in here
                name: epel-release #defining the package name as epel-release
                state:latest # using the state as release as we are installing the latest package if not package being installed 
                update_cache: True # here we are performing the yum -y update command to update the cache packages 
              when: ansible_distribution == "CentOS"
              # this will be going to get executed when the target host is based on centos and ignore the ubuntu target hosts

            - name: Install Nginx # using the name  of Task as Install Nginx
              package: # using the package module which will fetch the required OS version and install the package
                name: nginx # using the nginx package which need to be installed on both ubuntu and centos and the corrresponding OS Version managed by package module 
                state: latest # using the state as latest which will install the lattest version of the package

            - name: Restart Nginx # creating the Task Named as Restart Nginx over here
              service: # using the service module in here  
                name: nginx # using the nginx module in here 
                state: restarted # using the state as rrestarted which will restrat the `nginx service which can be systemd service`
              notify: check HTTP Service #notifying to handler over here

            # as here we are restarting the service hence the state wiill always going to change due to the idempotant behaviour of ansible

            - name: Template index.html-ansible_managed.j2 to index.html on target # here we are changing the name of template file i.e `.j2` file that we will use
              template: # using the template module in here 
                src: ./templates/index.html-ansible_managed.j2 # this is the source JINJA 2 template which will be execute in the JINJA2 enginee and coverted into the template
                dest: "{{nginx_root_location}}/index.html" #definning the destion where the remote target host will stay
                mode: 0644 # defining the mode as 0644 after the templating through JINJA2 templating engine
                trim_blocks: True # which will remove the un-necessary \n from the file 

          handlers: # creating the handler which willbe executed after the task execution if any changes noticed
            - name: check HTTP Service
              uri: #using the uri module in here 
                url: hhttps://{{ansible_default_ipv4.address}} # here using the ansible_facts `ansible_default_ipv4.address` in this case over here 
                status_code:
                    - 200 #defining the status code as list of status ocde we are expecting 
                # if the status code does not match then the hansdler task will fail 
    
        ...
        # now  we can execute the package as below 
        ansible-playbook nginx-playbook.yaml

    ```

# <ins> Challenge08 </ins> #

- we can distringuish between the `ubuntu or centos hosts` in the `web page served by the nginx web server`

- update the playbook with to include the `var files` which being in the folder of `vars/logo.yaml`

- update the `preveious Task` to `Template index.html-logos.j2 to index.html on target`

- also we need to update the `src directory` to `index.hrml-logos.j2` files in here 

- the `variable file` i.e `vars/logo.yaml` has the `data entry` to distinguish between the `CentOS and Ubuntu` logo

- if the content is more then use the `more` command rather than the `cat command` in linux


# <ins> Solution </ins> #

- we can define the `ansible-playbook`  in here as below 

- here we need to use the `var_files` declrative directive to define the `file system`

    ```
        nginx_playbook.yaml
        --------------------

        ---
        
        - hosts: linux # here we are targeting the linux host in this case

          var_files: defining the var_files declarative directive to specify the variable file which will be in yaml format
            - ./vars/logo.yaml # definning the logo.yaml file in here 
          
          tasks:
            - name: Install Epel #providing the name for the task over here 
              yum: # using the yum module in here
                name: epel-release #defining the package name as epel-release
                state:latest # using the state as release as we are installing the latest package if not package being installed 
                update_cache: True # here we are performing the yum -y update command to update the cache packages 
              when: ansible_distribution == "CentOS"
              # this will be going to get executed when the target host is based on centos and ignore the ubuntu target hosts

            - name: Install Nginx # using the name  of Task as Install Nginx
              package: # using the package module which will fetch the required OS version and install the package
                name: nginx # using the nginx package which need to be installed on both ubuntu and centos and the corrresponding OS Version managed by package module 
                state: latest # using the state as latest which will install the lattest version of the package

            - name: Restart Nginx # creating the Task Named as Restart Nginx over here
              service: # using the service module in here  
                name: nginx # using the nginx module in here 
                state: restarted # using the state as rrestarted which will restrat the `nginx service which can be systemd service`
              notify: check HTTP Service #notifying to handler over here

            # as here we are restarting the service hence the state wiill always going to change due to the idempotant behaviour of ansible

            - name: Template index.html-logo.j2 to index.html on target # here we are changing the name of template file i.e `.j2` file that we will use
              template: # using the template module in here 
                src: ./templates/index.html-logo.j2 # this is the source JINJA 2 template which will be execute in the JINJA2 enginee and coverted into the template
                dest: "{{nginx_root_location}}/index.html" #definning the destion where the remote target host will stay
                mode: 0644 # defining the mode as 0644 after the templating through JINJA2 templating engine
                trim_blocks: True # which will remove the un-necessary \n from the file 

          handlers: # creating the handler which willbe executed after the task execution if any changes noticed
            - name: check HTTP Service
              uri: #using the uri module in here 
                url: hhttps://{{ansible_default_ipv4.address}} # here using the ansible_facts `ansible_default_ipv4.address` in this case over here 
                status_code:
                    - 200 #defining the status code as list of status ocde we are expecting 
                # if the status code does not match then the hansdler task will fail 
    
        ...
        # now  we can execute the package as below 
        ansible-playbook nginx-playbook.yaml  
    
    ```


# <ins> Ester Egg Challenge </ins> #

- ester egg basically `where we have something which is most often hidden` thats usually `fun or interesting`

- when someone click the `image of the webpage hosted by nginx server` it will redirect you to a `secret game` known as `playbook stacker`

- here we need to insall the `unzip module` using the `package module of ansible`

- use the `unarchive module of ansible` to unzip the file to the location of `nginx_root_location` which we set as the `groupvars` for `centos and ubut target` which is `/usr/share/nginx/html for centos and /var/www/html for ubuntu target host`

- create a task as `Unarchieve playbook stacker game`

- set the `mode` as `0755`

- updte the `Template index.hrml-logos.j2 to index.html on target` task to `Template index.html-ester_egg.j2 to index.html on target`

- and use the `template file` as `index.html-ester_egg.j2 ` to copy to the `nginx_root_location` using the `template module of ansible`



# <ins> Solution </ins> #

- we can define the `ansible playbook` in here as 

- we need to make use of the `unarchive module of ansible`[unarchive module local](./unarchive_module.md) or [unarchive module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/unarchive_module.html) over here 

    ```

        nginx_playbook.yaml
        --------------------

        ---
        
        - hosts: linux # here we are targeting the linux host in this case

          var_files: defining the var_files declarative directive to specify the variable file which will be in yaml format
            - ./vars/logo.yaml # definning the logo.yaml file in here 
          
          tasks:
            - name: Install Epel #providing the name for the task over here 
              yum: # using the yum module in here
                name: epel-release #defining the package name as epel-release
                state:latest # using the state as release as we are installing the latest package if not package being installed 
                update_cache: True # here we are performing the yum -y update command to update the cache packages 
              when: ansible_distribution == "CentOS"
              # this will be going to get executed when the target host is based on centos and ignore the ubuntu target hosts

            - name: Install Nginx # using the name  of Task as Install Nginx
              package: # using the package module which will fetch the required OS version and install the package
                name: nginx # using the nginx package which need to be installed on both ubuntu and centos and the corrresponding OS Version managed by package module 
                state: latest # using the state as latest which will install the lattest version of the package

            - name: Restart Nginx # creating the Task Named as Restart Nginx over here
              service: # using the service module in here  
                name: nginx # using the nginx module in here 
                state: restarted # using the state as rrestarted which will restrat the `nginx service which can be systemd service`
              notify: check HTTP Service #notifying to handler over here

            # as here we are restarting the service hence the state wiill always going to change due to the idempotant behaviour of ansible

            - name : Install Unzip # creating a Task to instal the unzip package
              package: # using the package module in  here 
                name: unzip # specifying the name which will install the unzip package
                state: latest # using he latest state installing the latest version of unzip package 

            - name: Unarchieve playbook stacker game # here providing the name to the stacker game in here 
              unarchive: #using the unarchive module in here 
                src: ./files/playbook_stacker.zip #definign the source of the zip file to be unarchive
                dest: "{{hostvars[ansible_hostname].nginx_root_location}}/index.html" # accessing the groupvars using the hostvars and solving the hostname question by ansible_hostname
                mode:0755 #defining the mode in here
                remote_src: False # copying the file before doing an unarchive action

            - name: Template index.html-ester_egg.j2 to index.html on target # here we are changing the name of template file i.e `.j2` file that we will use
              template: # using the template module in here 
                src: ./templates/index.html-ester_egg.j2 # this is the source JINJA 2 template which will be execute in the JINJA2 enginee and coverted into the template
                dest: "{{nginx_root_location}}/index.html" #definning the destion where the remote target host will stay, here we are using the groupvars directly
                mode: 0644 # defining the mode as 0644 after the templating through JINJA2 templating engine
                trim_blocks: True # which will remove the un-necessary \n from the file 

          handlers: # creating the handler which willbe executed after the task execution if any changes noticed
            - name: check HTTP Service
              uri: #using the uri module in here 
                url: hhttps://{{ansible_default_ipv4.address}} # here using the ansible_facts `ansible_default_ipv4.address` in this case over here 
                status_code:
                    - 200 #defining the status code as list of status ocde we are expecting 
                # if the status code does not match then the hansdler task will fail 
    
        ...
        # now  we can execute the package as below 
        ansible-playbook nginx-playbook.yaml  
        

    ```

- now rhen we go back to the `reverse proxy` and go to the `custom templated web page hosted by nginx web server` then we can see that `when we clck on the ubuntu or centos` logo `the playbook stacker game` will open up


