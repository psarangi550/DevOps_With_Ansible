# docker_container module in Ansible

- Manage the life cycle of docker containers.

- `Supports check mode.` Run with `--check ` and `--diff` `to view config difference and list of actions to be taken.`

- Docker SDK for Python: `Please note that the docker-py Python module has been superseded by docker (see here for details)`

- `For Python 2.6, docker-py must be used`

- `Otherwise, it is recommended to install` the `docker Python module  ` 

- `Note that both modules should not be installed at the same time` 

- `Also note that when both modules are installed and one of them is uninstalled, the other might no longer function and a reinstall of it is required`

- `Parameters`
  
  
  
  - `api_version `  
  
    - `The version of the Docker API running on the Docker Host.`
  
    - `Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon.`
  
    - `If the value is not specified in the task, the value of environment variable DOCKER_API_VERSION will be used instead`
  
    - `If the environment variable is not set, the default value will be used.`    
   
  
  
  - `auto_remove`
    
    - `Enable auto-removal of the container on daemon side when the container's process exits.`
  
  
  
  - `capabilities` 
    
    - `List of capabilities to add to the container.` 
  
  
  
  - `cleanup`
    
    - `Use with detach=false to remove the container after successful execution.`   
    
    - `choices` 
      
      -  `no`
      -  `yes`

  
  
  - `command `

    - `Command to execute when the container starts.` 
    
    - ` A command may be either a string or a list.` 
    
    - `Prior to version 2.4, strings were split on commas.` 

  
  
  - `debug ` 
    
    - `Debug mode`
    
    - `Choices:`
            
            no ←
            yes` 
  
  
  
  
  
  - `comparisons ` `which is a dict`
    
    - `"Allows to specify" how "properties of existing containers" are "compared with docker_container module options" to decide whether the container should be recreated / updated or not` 
    
    - `Must be a dictionary specifying for an option one of the keys "strict", "ignore" and "allow_more_present" `
    
    - `If "strict is specified", "values are tested for equality", and "changes always result in updating or restarting" `
    
    - `If ignore is specified, changes are ignored.` 
    
    -  `allow_more_present is allowed only for lists, sets and dict`
    
    - ` If it is specified for lists or sets, the container will only be updated or restarted if the module option contains a value which is not present in the container's options`
    
    - `The wildcard option * can be used to set one of the default values strict or ignore to *all* comparisons which are not explicitly set to other values.`
    
  
  
  
  - `detach`
    
    - `Enable detached mode to leave the container running in background.` 
    
    - `If disabled, the task will reflect the status of the container run (failed if the command failed).`
    
    -  `Choices`:
            `no`
            `yes` ←

  
  - `devices`
    
    - `List of host device bindings to add to the container.` 
    
    - `Each binding is a mapping expressed in the format <path_on_host>:<path_in_container>:<cgroup_permissions>.`

  
  
  - `domainname `
    
    - `Container domainname.`

  
  
  
  - `docker_host `
    
    - `The URL or Unix socket path used to connect to the Docker API`
    
    - `To connect to a remote host, provide the TCP connection string. For example, tcp://192.0.2.23:2376`  
    
    - `If TLS is used to encrypt the connection, the module will automatically replace tcp in the connection URL with https` 
    
    - `If the value is not specified in the task, the value of environment variable DOCKER_HOST will be used instead.`
    
    - ` If the environment variable is not set, the default value will be used.` 
    
    - `Default`:
        
        - `"unix://var/run/docker.sock"`

  
  - `entrypoint` 
    
    - `Command that overwrites the default ENTRYPOINT of the image.`

  
  - `env` which is a `dict`
    
    - `Dictionary of key,value pairs.`
    
    - `Values which might be parsed as numbers, booleans or other types by the YAML parser must be quoted (e.g. "true") in order to avoid data loss.`

  
  - `env_file`
    
    - `Path to a file, present on the target, containing environment variables FOO=BAR.` 
    
    - `If variable also present in env, then the env value will override.` 


  - `etc_hosts`
    
    - `Dict of host-to-IP mappings, where each host name is a key in the dictionary.` 
    
    - `Each host name will be added to the container's /etc/hosts file.` 

  
  - `exposed_ports`
    
    - `List of additional container ports which informs Docker that the container listens on the specified network ports at runtime.` 
    
    - `If the port is already exposed using EXPOSE in a Dockerfile, it does not need to be exposed again.` 

  
  
  - `force_kill`
    
    - `Use the kill command when stopping a running container.`

    - `Choices:`
                no ←
                yes


  - `hostname `
    
    - `The container's hostname.` 

  
  
  - `image`
    
    - `Repository path and tag used to create the container.`

    - `If an image is not found or pull is true, the image will be pulled from the registry. If no tag is included, latest will be used`
    
    -  `Can also be an image ID. If this is the case, the image is assumed to be available locally. The pull option is ignored for this case.`

  
  
  
  - `name`
    
    - `Assign a name to a new container or match an existing container.`
  
    - `When identifying an existing container name may be a name or a long or short cont` 


  
  
  - `network_mode `
    
    - `Connect the container to a network. Choices are bridge, host, none or container:<name|id>.`
    
  

  - `networks` `which is a list of dicts`
    
    - `List of networks the container belongs to.`
    
    - `To remove a container from one or more networks, use the purge_networks option.`
    
    - **Parameters**
      
      
      - `aliases `
        
        - `List of aliases for this container in this network`    
        
        - `These names can be used in the network to reach this containe` 

      
      - `ipv4_address ` :
        
        - `The container's IPv4 address in this network.`

      
      - `ipv6_address `
        
        - `The container's IPv6 address in this network.`

      
      - `links `  

        - `A list of containers to link to.`

      
      - `name`:
        
        - `The network's name.` 


  - `paused`
    
    - `Use with the started state to pause running processes inside the container.`
    
    - Choices:
            no ←
            yes

  
  
  - `kill_signal `
    
    - `Override default signal used to kill a running container.`

  
  
  - `labels`
    
    - `Dictionary of key value pairs.` 

  
  - `links`
    
    - `List of name aliases for linked containers in the format container_name:alias` 
    
    - `Setting this will force container to be restarted.` 

  
  
  - `mac_address `
    
    -  `Container MAC address (e.g. 92:d0:c6:0a:29:33).`

  - `privileged `
    
    - `Give extended privileges to the container.`
    
    - Choices:
            no ←
            yes  


  - `published_ports `
    
    - `List of ports to publish from the container to the host.`
    
    - `Use docker CLI syntax: 8000, 9000:8000, or 0.0.0.0:9000:8000, where 8000 is a container port, 9000 is a host port, and 0.0.0.0 is a host interface.`  
    
  
  
  - `pull`
    
    - `If true, always pull the latest version of an image`
    
    - `Otherwise, will only pull an image when missing.`
    
    - Choices:
            no ←
            yes 
    
  
  - `purge_networks `
    
    - `Remove the container from ALL networks not included in networks parameter.`
    
    -  `Any default networks such as bridge, if not found in networks, will be removed as well.`
    
    - Choices:
            no ←
            yes   
    
  - `read_only `    
    
    - `Mount the container's root file system as read-only.`
    
    - Choices:
            no ←
            yes 

  - `recreate `
    
    - `Use with present and started states to force the re-creation of an existing container.` 



  - `state`
    
    - `absent` - ` " A container matching the specified name will be stopped and removed " `
    
      - `Use force_kill to kill the container rather than stopping it.` 
    
      - `Use keep_volumes to retain anonymous volumes associated with the removed container` 
    
    
    - `present - "Asserts the existence of a container matching the name and any provided configuration parameters" ` 
    
      - `If no container matches the name, a container will be created`
    
      - `If a container matches the name but the provided configuration does not match, the container will be updated`
    
      - ` if it can be. If it cannot be updated, it will be removed and re-created with the requested config.`

    - `started - Asserts that the container is first present`
    
      - `if the container is not running moves it to a running state` 

      - `Use "restart" to force a matching container to be stopped and restarted.`
    
    
    - `stopped - Asserts that the container is first present`
    
      - `then if the container is running moves it to a stopped state`  

    
    - `To control what will be taken into account when comparing configuration, see the comparisons option`
    
    - `To avoid that the image version will be taken into account, you can also use the ignore_image option`
      
    - `Use the recreate option to always force re-creation of a matching container, even if it is running.`


  - `tty`
    
    -  `Allocate a pseudo-TTY.`

  - `working_dir`
    
    - `Path to the working directory.` 

  - `volumes`
    
    - `List of volumes to mount within the container.`
    
    - `Use docker CLI-style syntax: /host:/container[:mode]`  
    
    - `Mount modes can be a comma-separated list of various modes such as ro, rw, consistent, delegated, cached, rprivate, private, rshared, shared, rslave, slave, and nocopy` 

  - `volumes_from `

    - `List of container names or IDs to get volumes from.`

  - `runtime`
    
    - `Runtime to use for the container.` 

  - `restart_policy `
    
    - `Container restart policy.`
    
    - Choices:
            no
            on-failure
            always
            unless-stopped  

  - `ignore_image`
    
    -  When `state is present or started`, the m`odule compares the configuration of an existing container to requested configuration`
    
    - `The evaluation includes the image version`  
    
    - `If the image version in the registry does not match the container, the container will be recreated`
    
    - `You can stop this behavior by setting ignore_image to True.` 

  - `keep_volumes `
    
    - `Retain anonymous volumes associated with a removed container.` 
    
    - `Choices` 
      
      - `no` &lrarr;
      - `yes` 

  - `container_default_behavior`
    
    - `In older versions of this module, various module options used to have default values` 
    
    - `This caused problems with containers which use different values for these options.` 
    
    - `The default value is now no_defaults` 
    
    - `To restore the old behavior, set it to compatibility` 
    
    - `which(no_defaults as value) will ensure that the default values are used when the values are not explicitly specified by the user.` 
    
    - `This affects the auto_remove, detach, init, interactive, memory, paused, privileged, read_only, and tty options.`
    
    - Choices:

            "compatibility"

            "no_defaults" ← (default)  


**Note**
  
  - `api_version`
    
  - `auto_remove`
  
  - `cleanup`
  
  - `capalibilites`
  
  - `cap_drop`
  
  - `command`
  
  - `compairsion`
  
  - `debug`
  
  - `detach`
  
  - `devices` : `volume mapping`
  
  - `docker_host` `mentioning the docker host loc`   
  
  - `domainname` `Container domainname.`
  
  - `entrypoint ` `Command that overwrites the default ENTRYPOINT of the image.`
  
  - `env` `Dictionary of key,value pairs.`
  
  - `env_file`   `Path to a file, present on the target, containing environment variables FOO=BAR.`  
  
  - `etc_hosts` `Dict of host-to-IP mappings, where each host name is a key in the dictionary. Each host name will be added to the container's /etc/hosts fill`
  
  - `exposed_ports`  `List of additional container ports which informs Docker that the container listens on the specified network ports at runtime.`  
  
  - `force_kill `   `Use the kill command when stopping a running container.` 
  
  - `hostname` `The container's hostname.`
  
  - `ignore_image `  `while doing compairsion ignore the image version number`
  
  - `image` `Repository path and tag used to create the container`  
  
  - `name ` `Assign a name to a new container or match an existing container.` `When identifying an existing container name may be a name or a long or short container ID.`
  
  - `pull` `If true, always pull the latest version of an image. Otherwise, will only pull an image when missing.`
  
  - `purge_networks ` `Remove the container from ALL networks not included in networks parameter.`
  
  - `read_only ` :- `Mount the container's root file system as read-only.`
  
  - `recreate ` :- `Use with present and started states to force the re-creation of an existing container.`
  
  - `restart `  :- `Use with started state to force a matching container to be stopped and restarted.`
  
  - `restart_policy ` :- `Container restart policy.`