# Docker with Ansible

- In this we will `configure the docker Lab`
- `We will use ansible to pull the Docker images and experiment with Docker`
- `we will use ansible to Build containers from the images`
- `we will use ansible to  Build Customized Images and Customized container`
- `we will use ansible to  we can use the Ansible to connect to the running container`
- `Terminate and remove Docker Resources`
- `SetUp the docker lab`

  - in this lab  `docker` been on a `dedicated container` with the name as `docker`
  - as its under the ` same docker network` hence we `can` ping to the `hostname` as `ping docker`
  - `to communicate with the docker running on a dedicated container` we   `first need to install docker-client` on the `host` which is trying to `connect`
  - hence `we need to install docker on the docker hosts` through a  `shell script` ot  through `series of commands as below`
    - ```shell
      sudo apt -y update # upading the sud  packages
      sudo apt install -y docker.io # installing the docker.io client
      sudo pip3 install docker # installing docker puython library

      ```
    - or we can create the `bash script` as `below`
    - ```bash
      #! /bin/bash
      sudo apt -y update
      sudo apt install -y docker.io
      sudo pip3 install docker

       we can execute the bash script as `bash -x <scriptname.sh>`
      ```
  
  - we need to set th `DOCKER_HOST` environment variable as `export DOCKER_HOST=tcp://docker:2375` where we can see the `docker is the service running on te container named docker hence that is pingable` and `2375 is the default docker port`
  
  - now when we use the command as below
    
    - ```bash
         docker ps -a
         docker images
         # this command need to be executed on the hosts system after ionstalling the docker which can connect to the remote host and execute the docker command on the remote docker container and fetch the result out in here 
         # we can see how many container are running using the docker ps -a command 
         # we can also see how many images are runningwith the ddocker images command

    ``` 

- the `DOCKER_HOST` env variable will tell `docker` where to `execute the docker command`

- the `docker client` will connect to `DOCKER_HOST` and get the result from the `DOCKER_HOST` onto the `host system`

- we can also mentioned the `DOCKER_HOST` in an `env file` and `source that env file as well to set the DOCKER_HOST environment`

- we can run this s below 

    ```bash
        
        envfile
        ========
        export DOCKER_HOST=tcp://docker:2375
        # makign the docker_host env variable so that docker aware where to execute the docker command

        source envfile
        # sourcing the  envfile to make sure that env variable being set

    ```

- **Case1**
  
  - we can use the `docker_image` module or `community.docker.docker_image` to create `images`
  
  - here as we are pulling from the `default registry` hence we will get the `source: pull`
  
  - as we have `souce=pull` and `state=present` hence we can also use the `force_source` option out `which will perform the recreation of the image if exists`
  
  - here as we are defining the `export DOCKER_HOST=tcp://docker:2375` which will tell docker module to execute the docker command on the `DOCKER_HOST` 
  
  - we can write the `ansible playbook` as below 

    ```yaml
        
        docker_playbook.yaml
        =====================

        ---
        
        - hosts: ubuntu-c # here we are targeting the ansible host

          tasks:
            - name: pulling the images in here using the docker_image module 
              docker_image:   # here using the docker_image module
                docker_host: tcp://docker:2375 # here we need to define the docker host on which the docker command been running 
                name: "{{item}}:latest" # defining the name of the image with the tags
                source: pull   # mentioning the source as pull so pull from the registry 
                state: present # mentionning the state is present means image been exected if not found then pull/build/load based on the option 
              with_items: # defining the looping techineques
                - centos 
                - ubuntu
                - nginx
                - redis


        ...

        # if we execute the playbook as below then we will get the outpu as below 
        ansible-playbook docker_playbook.yaml
        #outout will be displayed here 
        PLAY [ubuntu-c] ************************************************************************************************************************************************************************************

          TASK [Gathering Facts] *****************************************************************************************************************************************************************************
          ok: [ubuntu-c]

          TASK [creting the docker images with docker_image module] ******************************************************************************************************************************************
          ok: [ubuntu-c] => (item=ubuntu)
          ok: [ubuntu-c] => (item=centos)
          ok: [ubuntu-c] => (item=redis)
          ok: [ubuntu-c] => (item=nginx)

          TASK [pulling the images in here using the docker_image module] ************************************************************************************************************************************
          ok: [ubuntu-c] => (item=centos)
          ok: [ubuntu-c] => (item=ubuntu)
          ok: [ubuntu-c] => (item=nginx)
          ok: [ubuntu-c] => (item=redis)

          PLAY RECAP *****************************************************************************************************************************************************************************************
          ubuntu-c                   : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

    ```

- **Case02**

  - if we want to `create` the `container out of the image` then we have to use the `docker_container` module in here 
  
  - here we need to specify the `state=present` as the `image been expected if not present then pull from registry`
  
  - we have to use the `name` as the `container name we want to ceate`
  
  - we can mention the `image name with the tags` as below we can write it as `<image>:<tags>` asainst the `image` parameter
  
  - we can use the `container_default_arguments` to `no_defauls` hence the `default value will be select for module compairesion` 
  
  - we can use the playbook as below 

  ```yaml
        
        docker_playbook.yaml
        =====================
        ---
        
        - hosts: ubuntu-c # here we are targeting the ansible host

          tasks:
            - name: pulling the images in here using the docker_image module 
              docker_image:   # here using the docker_image module
                docker_host: tcp://docker:2375 # here we need to define the docker host on which the docker command been running 
                name: "{{item}}:latest" # defining the name of the image with the tags
                source: pull   # mentioning the source as pull so pull from the registry 
                state: present # mentionning the state is present means image been exected if not found then pull/build/load based on the option 
              with_items: # defining the looping techineques
                - centos 
                - ubuntu
                - nginx
                - redis


            - name: creating the container from the image that we have pulled 
              docker_container:  # using the docker_container module in here 
                docker_host: tcp://docker:2375 # here we need to define the docker host on which the docker command been running 
                name: communitywebserver # defining the docker container name over here 
                image: nginx:latest  # here defining the image name for the docker 
                state: present # state as present means image been expected to be there to create container if not present it will pull
                pull: yes # here the pull is yes if the image not present pull from the registry
                recreate: yes # using the recreate option if the image present then recreating will happen

        ...
        
        # here if we execute the command then we can see that the container created and exited 
        # if we want to keep it running then we need to change the state to started or restart: true option which will stopp and restart the container 
        ======================================
        ansible-playbook docker_playbook.yaml
        ======================================
        # here the ouput will be as below 
        PLAY [ubuntu-c] ************************************************************************************************************************************************************************************

          TASK [Gathering Facts] *****************************************************************************************************************************************************************************
          ok: [ubuntu-c]

          TASK [creting the docker images with docker_image module] ******************************************************************************************************************************************
          ok: [ubuntu-c] => (item=ubuntu)
          ok: [ubuntu-c] => (item=centos)
          ok: [ubuntu-c] => (item=redis)
          ok: [ubuntu-c] => (item=nginx)

          TASK [creating the container from the image that we have pulled] ***********************************************************************************************************************************
          changed: [ubuntu-c]

          PLAY RECAP *****************************************************************************************************************************************************************************************
          ubuntu-c                   : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 

        # here when we do the `docker ps` we will not be able to see the `container` as its not running 
        # if we want to make it as the `container running` then we can `change the state to state=started`
        # we can write this one as below 

        docker_playbook.yaml
        =====================
        ---
        
        - hosts: ubuntu-c # here we are targeting the ansible host

          tasks:
            - name: pulling the images in here using the docker_image module 
              docker_image:   # here using the docker_image module
                docker_host: tcp://docker:2375 # here we need to define the docker host on which the docker command been running 
                name: "{{item}}:latest" # defining the name of the image with the tags
                source: pull   # mentioning the source as pull so pull from the registry 
                state: present # mentionning the state is present means image been exected if not found then pull/build/load based on the option 
              with_items: # defining the looping techineques
                - centos 
                - ubuntu
                - nginx
                - redis


            - name: creating the container from the image that we have pulled 
              docker_container:  # using the docker_container module in here 
                docker_host: tcp://docker:2375 # here we need to define the docker host on which the docker command been running 
                name: communitywebserver # defining the docker container name over here 
                image: ubuntu:latest  # here defining the image name for the docker 
                state: started # making the state as started if there were any container then it will run else it will pull it 
                pull: yes # here the pull is yes if the image not present pull from the registry
                
  
        ...
        # here if we execute the command then we can see that the container created and running
        # if we want to keep it running then we need to change the state to started only can provide the required output
        PLAY [ubuntu-c] ************************************************************************************************************************************************************************************

        TASK [Gathering Facts] *****************************************************************************************************************************************************************************
        ok: [ubuntu-c]

        TASK [creting the docker images with docker_image module] ******************************************************************************************************************************************
        ok: [ubuntu-c] => (item=ubuntu)
        ok: [ubuntu-c] => (item=centos)
        ok: [ubuntu-c] => (item=redis)
        ok: [ubuntu-c] => (item=nginx)

        TASK [creating the container from the image that we have pulled] ***********************************************************************************************************************************
        changed: [ubuntu-c]

        PLAY RECAP *****************************************************************************************************************************************************************************************
        ubuntu-c                   : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
  
  ```

- **Case03**

  - here  we will see abut creating the `custom image` and `custom container` using the `ansible`
  
  - we need to define the `Dockerfile` , here we have the `volume -mapped` folder as `/shared` we can put over there as below 
  
  - we can use the `docker_image` and `docker_module` module to `create custom docker image` and `custom docker container` we can able to see 
  
  - here we have the playbook in here as below 

    ```yaml
       docker_playbook.yaml
       ====================
       
      ---

      - hosts: ubuntu-c # here we are targeting the ansible host

        tasks:
          - name: copying the content to /shared/Dockerfile we need to create using the COPY module 
            copy: 
              dest: /shared/Dockerfile    # location of the dockerfile mentioned in here
              content: |
                        FROM nginx    # here dipplaying the nginx command out in here 
          

          - name: here creating the custom docker image using the docker_image module in here 
            docker_image:
              docker_host: tcp://docker:2375
              name: mynginx:latest
              source: build
              state: present
              build:  #defining the build dict over here
                path: /shared/
                pull: yes
              force_source: yes

          - name: creating the docker container from the custome docker images
            docker_container:
              docker_host: tcp://docker:2375
              name: "nginx{{item}}"
              image: mynginx:latest
              state: started
              ports:
                - "80{{item}}:80"
              with_sequence: 1-3
            
      ...
      # here if execute the below code then we can see the custom docker container being created from the  custom image 
      # if we execute then we can see  the `Dockerfile` created in the `/shaed/Dockerfile` dolfer
      # here also we can see that at every state the `docker_host` ned to be mentioned 
      # here on the build dict we are provding the path to the `path and pull paramter` to pull the image and create the container
      =====================================
      ansible-playbook docker_playbook.yaml
      =====================================
      # the output in here as can be described as below 
      PLAY [ubuntu-c] ************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [ubuntu-c]

      TASK [copying the content to /shared/Dockerfile we need to create using the COPY module] ***********************************************************************************************************
      ok: [ubuntu-c]

      TASK [here creating the custom docker image using the docker_image module in here] *****************************************************************************************************************
      ok: [ubuntu-c]

      TASK [creating the docker container from the custome docker images] ********************************************************************************************************************************
      changed: [ubuntu-c] => (item=1)
      changed: [ubuntu-c] => (item=2)
      changed: [ubuntu-c] => (item=3)

      PLAY RECAP *****************************************************************************************************************************************************************************************
      ubuntu-c                   : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

    
     # here if we observe thnb we can see that using the `docker images` command 
     # we can see that both the `inbuild docker image` and `customer docker image` have the `same container id`
     # as we are usign the FROM nginx to pull the nginx image 
     # we can see that below playbook for reference 
    
      docker_playbook.yaml
      ====================
       
      ---

      - hosts: ubuntu-c # here we are targeting the ansible host

        tasks:
          
          
          - name: coping the index to the /shared/index.html file 
            copy: 
              src: index.html 
              dest: /shared/index.html

      
          - name: copying the content to /shared/Dockerfile we need to create using the COPY module 
            copy: 
              dest: /shared/Dockerfile    # location of the dockerfile mentioned in here
              content: |
                        FROM nginx    # here dipplaying the nginx command out in here 
                        COPY index.html /usr/share/nginx/html/index.html

          

          - name: here creating the custom docker image using the docker_image module in here 
            docker_image:
              docker_host: tcp://docker:2375
              name: mynginx:latest
              source: build
              state: present
              build:  #defining the build dict over here
                path: /shared/
                pull: yes
              force_source: yes

          - name: creating the docker container from the custome docker images
            docker_container:
              docker_host: tcp://docker:2375
              name: "nginx{{item}}"
              image: mynginx:latest
              state: started
              ports:
                - "80{{item}}:80"
              with_sequence: 1-3
            
      ...

      # if we now execute and see the `image id` of the `nginx` and `nginx customized` their `image id` being different
      # also we can ccess the port as `curl http://docker:9001/9002/9003`
      # here docker is the hostname for the docker container where the docker is running 
      # here we are opening the mapped port so that we can see the nginx been stored out content 
      # we can see the output as below 
      # but make sure to provide prper permission to the index.html
      =====================================
      ansible-playbook docker_playbook.yaml
      =====================================
      # the output in here as can be described as below 
      PLAY [ubuntu-c] ************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [ubuntu-c]

      TASK [coping the index to the /shared/index.html file] *********************************************************************************************************************************************
      ok: [ubuntu-c]

      TASK [copying the content to /shared/Dockerfile we need to create using the COPY module] ***********************************************************************************************************
      ok: [ubuntu-c]

      TASK [here creating the custom docker image using the docker_image module in here] *****************************************************************************************************************
      ok: [ubuntu-c]

      TASK [creating the docker container from the custome docker images] ********************************************************************************************************************************
      changed: [ubuntu-c] => (item=1)
      changed: [ubuntu-c] => (item=2)
      changed: [ubuntu-c] => (item=3)

      PLAY RECAP *****************************************************************************************************************************************************************************************
      ubuntu-c                   : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    
  
    ```

  - if we are trying for any `mode` while copying then we can use the mode as `0644` i,e `-rw-r--r--`

- **Case4**
  
  - `we can connect` `ansible` to the `running container of the docker container` as well
  
  - for this we need to `redefine the inventory file` and also we have to use the ` running container name that we are going to see` 
  
  - we can define the `ansible.cfg` as below 

    ```ini
       ansible.cfg
       ===========
        [defaults]
        inventory=hosts
        host_key_checking=False
        forks=6
    
    ```

    ``` ini
        hosts
        =====
        [control]
        ubuntu-c
        
        [centos]
        centos[1:3]

        [ubuntu]
        ubuntu[1:3]

        [linux:children]
        centos
        ubuntu

        [containers] # defining the containers section in here 
        python[1:3] ansible_connection=docker ansible_python_interpreter=/usr/local/bin/python3 # based on the python interpreter in the container 
    
    
    ```
  
  - now we can use the `containers` as the `target group` for the `running container`
  
  - we can make the container running by using the `sleep infinity` command on the `bash shell`
  
  - we can execute the `ansible-playbook` as below 

    ```yaml
    
      docker_playbook.yaml
      ===================
      ---

      - hosts: ubuntu-c # here we are targeting the ansible host

        tasks:
          
          - name: installing the image for python:3.10-slim image
            docker_image:
              docker_host: tcp://docker:2375 # using the remote docker host in here
              name: python:3.10-slim # using the python:3.10-slim image
              source: pull # pulling if not available 
              state: present # excpecting the image be poresent

          - name: creating multiple pythjjon image with the name as python1/python2/python3
            docker_container: # usig the docker_container module
              docker_host: tcp://docker:2375 # using the remote docker host in here 
              name: python{{item}} #  name of the container  
              image: python:3.10-slim # image name
              state: started # starting the container 
              pull: yes # pulling if not found already
              command: sleep infinity  # providing the command to run 
            with_sequence: 1-3 # defining the sequence in here

      - host:  containers # defining the host as the container which will make sure that we have mentioned the same in the host file with the same name as container 
        gather_facts: False # ignoring the facts in here 

        tasks:
          - name: checking the ping to the running container 
            ping: # using the ping module  in here
              
      ...
    
      # here we are defining them as the target group after definign the ionventory files in here 
      # here we have able to ping to the python command out in here 
      # if we execute th code as below will be the output in here
      ========================================================

      ansible-playbook docker_playbook.yaml

      ========================================================
      # the ouput in this case will be as below 

      PLAY [ubuntu-c] ************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [ubuntu-c]

      TASK [installing the image for python:3.10-slim image] *********************************************************************************************************************************************
      ok: [ubuntu-c]

      TASK [creating multiple pythjjon image with the name as python1/python2/python3] *******************************************************************************************************************
      ok: [ubuntu-c] => (item=1)
      ok: [ubuntu-c] => (item=2)

      PLAY [containers] **********************************************************************************************************************************************************************************

      TASK [checking the ping to the running container] **************************************************************************************************************************************************
      ok: [python1]
      ok: [python2]
      ok: [python3]

      PLAY RECAP *****************************************************************************************************************************************************************************************
      python1                    : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      python2                    : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      python3                    : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
      ubuntu-c                   : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    
    ```

- **Case5**
  
  - here we will be removing all the `docker container and docker images`
  
  - for which we can use the `state=absent` in `both the docker_image and docker_container module`
  
  - hence we can use the `ansible-playbook` as below 

    ```yaml
      
      
      docker_playbook.yaml
      ===================
      ---

      - hosts: ubuntu-c # here we are targeting the ansible host

        tasks:
          
          - name: installing the image for python:3.10-slim image
            docker_image:
              docker_host: tcp://docker:2375 # using the remote docker host in here
              name: python:3.10-slim # using the python:3.10-slim image
              source: pull # pulling if not available 
              state: present # excpecting the image be poresent

          - name: creating multiple pythjjon image with the name as python1/python2/python3
            docker_container: # usig the docker_container module
              docker_host: tcp://docker:2375 # using the remote docker host in here 
              name: python{{item}} #  name of the container  
              image: python:3.10-slim # image name
              state: started # starting the container 
              pull: yes # pulling if not found already
              command: sleep infinity  # providing the command to run 
            with_sequence: 1-3 # defining the sequence in here

          - name: removing all the containers first 
            docker_container:  # using the docker_container module in here
              docker_host: tcp://docker:2375 # using the remote docker host in here
              name: python{{item}} # using the  name as python1/python2/python3
              image: python:3.10-slim  # using the python sdocker images with tag
              state: absent # removing the docker container 
            with_sequence: 1-3 # providing the loop in here
            force_kill: yes # kill the container

          - name: removing the images in here 
            docker_image:  # using the docker image module here
              docker_host: tcp://docker:2375 # using the remote docker host in here
              name: python:3.10-slim # using the python:3.10-slim image
              state: absent # excpecting the image be removed
              force_absent: true # making sure image being untagged and deleted   
      ...

      # now if we execute the command then we can see the image being created and now being removed 
      =====================================
      ansible-playbook docker_playbook.yaml
      =====================================
      # we can see the output in this case as below 

      PLAY [ubuntu-c] ************************************************************************************************************************************************************************************

      TASK [Gathering Facts] *****************************************************************************************************************************************************************************
      ok: [ubuntu-c]

      TASK [installing the image for python:3.10-slim image] *********************************************************************************************************************************************
      ok: [ubuntu-c]

      TASK [creating multiple pythjjon image with the name as python1/python2/python3] *******************************************************************************************************************
      changed: [ubuntu-c] => (item=1)
      changed: [ubuntu-c] => (item=2)

      TASK [removing all the containers first] ***********************************************************************************************************************************************************
      changed: [ubuntu-c] => (item=1)
      changed: [ubuntu-c] => (item=2)
      ok: [ubuntu-c] => (item=3)

      TASK [removing the images in here] *****************************************************************************************************************************************************************
      ok: [ubuntu-c]

      PLAY RECAP *****************************************************************************************************************************************************************************************
      ubuntu-c                   : ok=5    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    
    
    ```

