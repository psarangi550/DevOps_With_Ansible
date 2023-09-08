# <ins> Setting Up the Ansible Lab </ins> #

- `Ansible` is an `agentless architecture` , it does not need an `installation of agent` on the `target` to communicate with the `ansible`

- But it does need a `connection/connectivity` between the `ansible control host` to the `inventory target` with a `trusted relationship`

- when using the `Linux` we can do that using the `SSH` i.e. is the `Secure shell`

- we can use the `SSH` to configure a `password less` connection between the `host` and the `inventory target` which is also contain the `host`

- we can login to any of the `host` of the `target host` by using the `ansible control host` without any `password`

# <ins> Docker Installation </ins> #

- `Docker` is a `container offering` which uses the `OS level virtualization` allowing the `software to be delivered as container `

- `coontainer` are `isolated from each other` and within the `container` we can bundle 
  
  - `software library`
  - `configuration file` 

    that each container require

- `docker run --rm` used to clean up the after the `container being disposed`

- we can verify the `architecture` using the commnd as `cat /etc/os-release` or by using the `uname -a` command 

- we can access the `File System Access Layer i.e File Sharing` in case of `Mac OS X` but in case of `Windows thats not available because of WSL` its `native to windows`

- While installing in the `ubuntu iage for a Linux system` then we can see the below info 
  
  - curl -fsSL https://gat.docker.com -o get-docker.sh  # this will downloas the `get-docker.sh` file which should be ready to run
  
  - sh get-docker.sh # in order to run the bash file in this case 

- for installing the `docker compose` on the `Linux Machine` we can use it as below 

    ```
        apt search docker-compose # this will search for the repo inside the linux machine 
        # but in order to work with Ansible we should have the docker-compose which should be 1.29 which is the last revised version

        # we can also installed using the project based approach as below 
        
        # go to the below url as 
        https://docs.docker.com/compose/cli-command/#install-on-linux
        # this will open up the page where we can use the command to install the docker compose latest version 
        
        # execute the command till the chmod command
        
        chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
        # this will make the docker compose as the docker sub command where we need to use the command such as `docker-compose version` 
        
        
        # but we can use the docker compose globally by using the below command  
        
        cp $DOCKER_CONFIG/cli-plugins/docker-compose /usr/local/bin
        # the above command will make sure to available all the docker-compose as a global command 

        # we can check the docker-compose version using it as 
        docker-compose version # this command will provide the docker-compose version in here

        # when we add to the `/usr/local/bin` then we can use the value as 
        docker compose version
        Or docker compose version

        # we need to add the user to the docker group using the command as below 
        sudo usermod -aG  docker $USER
        # this will help in adding the current user to the docker group

        # we can login to the user using the command as 
        su - $USER # this will ask for the user username password which created by the Linux root user
    
    ```