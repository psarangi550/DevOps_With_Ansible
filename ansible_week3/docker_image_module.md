# docker_image module in ansible

- `Build`, `load` or `pull` `an image,` `making the image available for creating containers`.

- `Also supports tagging an image into a repository `

- `archiving an image to a .tar file` 

- `Docker SDK for Python:` Please note that the `docker-py Python module` has been `superseded by docker` (see here for details)

- `For Python 2.6, docker-py must be used`

- `Otherwise, it is recommended to install` the `docker` `Python module`

- `Note that both modules should not be installed at the same time`

- `Also note that when both modules are installed and one of them is uninstalled, the other might no longer function and a reinstall of it is required`


- **Parameters**
  
  - `api_version`
    
    - `The version of the Docker API running on the Docker Host` 
    
    - `Defaults to the latest version of the API supported by Docker SDK for Python and the docker daemon`
    
    - `If the value is not specified in the task, the value of environment variable DOCKER_API_VERSION will be used instead.`
    
    -  `If the environment variable is not set, the default value will be used. `
    
    -   `Default`:
                - `"auto"`

  
  - `archive_path`
    
    - `Use with` `state present` `to archive an image to a .tar file`. 

  
  
  
  - `build`
    
    - `dictionary`:- `Specifies options used for building images`. 
    
    
    - **parameters**
      
      
      
      - `args`
        
        - `Provide a dictionary`of `key:value` `build arguments that map to Dockerfile ARG directive.`   
        
        - `Docker expects the value to be a string`. `For convenience any non-string values will be converted to strings.` 
        
      
      
      - `cache_from` 
        
        - `List of image names to consider as cache source.` 

      
      
      - `container_limits`
        
        - `A dictionary of limits applied to each container created by the build process.` 
        
        - **paramters**

          
          - `cpusetcpus`  
           
           - `CPUs in which to allow execution, e.g., "0-3", "0,1" `
        
          
          
          - `cpushares`  
            
            - `CPU shares (relative weight).` 

          
          
          - `memory`
            
            - `Set memory limit for build.`
         
          
          
          - `memswap`

            - `Total memory (memory + swap), -1 to disable swap.`

      
      
      - `dockerfile` 
        
        - `Use with "state present "and "source build" to "provide an alternate name for the Dockerfile to use when building an image".`
        
        - `This can also include a relative path (relative to path).` 

      
      
      - `etc_hosts`
        
        - `Extra hosts to add to /etc/hosts in building containers, as a mapping of hostname to IP address.`

      
      
      - `http_timeout`
        
        - `Timeout for HTTP requests during the image build operation. Provide a positive integer value for the number of seconds.` 

      
      
      - `network`
        
        - `The network to use for RUN build instructions.`

      
      
      - `nocache`
        
        - `Do not use cache when building an image.` 
        
        - `Choices`:
                no ←
                yes
      
      
      - `path`
        
        - `Use with state 'present' to build an image. Will be the path to a directory containing the context and Dockerfile for building an image.` 
        
      
      
      - `pull` 
        
        - `When building an image downloads any updates to the "FROM image in Dockerfile".` 
        
        - `Choices`:
                no ←
                yes
      
      
      
      - `rm`
        
        - `Remove intermediate containers after build.`  

        -     Choices:
                    no
                    yes ←

    
    
      - `target`    
          
          - `When building an image specifies an intermediate build stage by name as a final stage for the resulting image.`

    
    
      - `use_config_proxy`
        
        - `If set to yes and a proxy configuration is specified in the docker client configuration (by default $HOME/.docker/config.json)` 
        
        - `corresponding environment variables will be set in the container being built.` 

  
  
  - `buildargs`
    
    - `Provide a dictionary of key:value build arguments that map to Dockerfile ARG directive`. 
    
    - `Docker expects the value to be a string. For convenience any non-string values will be converted to strings.` 
    
    - `Please use build.args instead. This option will be removed in Ansible 2.12.`
  
  
  
  - `Debug mode`  
    
    -  Choices:
            no ←
            yes

  
  
  
  - `docker_host`
    
    - The `URL` or `Unix socket path ` `used to connect to the Docker API `
    
    - `To connect to a remote host, provide the TCP connection string. For example, tcp://192.0.2.23:2376` 
    
    - `If TLS is used to encrypt the connection, the module will automatically replace tcp in the connection URL with https.` 

    - `If the value is not specified in the task, the value of environment variable DOCKER_HOST will be used instead`
    
    - `If the environment variable is not set, the default value will be used.`
    
    - `Default:"unix://var/run/docker.sock"`  

  
  - `force`
    
    - `Use with "state absent" to "un-tag and remove all images matching the specified name"` 
    
    - `Use with "state present" to "build, load or pull an image when the image already exists."` 
    
    - `Also use with "state present" "to force tagging an image".` 
    
    - `Please stop using this option, and use the more specialized force options force_source, force_absent and force_tag instead.` 

  
  
  - `force_source`
    
    - `Use with s"tate present" "to build, load or pull "  an image (depending on the value of the source option) when the image already exists.` 

  
  
  - `force_tag` 
    
    - `Use with state present to force tagging an image.` 

  
  
  - `force_absent`
    
    - `Use with state absent to un-tag and remove all images matching the specified name.` 

  
  
  - `load_path`
    
    - `Use with state present to load an image from a .tar file.` 
    
  
  
  -  `name`
    
    - `Image name.`   
    
    - `Name format will be one of: name, repository/name, registry_server:port/name.` 
    
    - ` When pushing or pulling an image the name can optionally include the tag by appending ':tag_name'.` 
    
    - `Note that image IDs (hashes) are not supported.` 

  
  
  - `nocache`
    
    - `Do not use cache when building an image.`
    
    - `Please use build.nocache instead. This option will be removed in Ansible 2.12.`  

  
  
  - `path`
    
    - `Use with state 'present' to build an image` 
    
    - `Will be the path to a directory containing the context and Dockerfile for building an image.` 
    
    - `Set source to build if you want to build the image.` 
    
    - `The option will be set automatically before Ansible 2.12 if this option is used. From Ansible 2.12 on, you have to set source to build` 
    
    - `Please use build.path instead. This option will be removed in Ansible 2.12.` 

  
  
  - `pull`
    
    - `When building an image downloads any updates to the FROM image in Dockerfile`.
    
    -` Please use build.pull instead. This option will be removed in Ansible 2.12.`
    
    - ` The default is currently yes. This will change to no in Ansible 2.12`

    - `Choices`:
            no
            yes
	
  
  - `push`
    
    - `Push the image to the registry.` 
    
    - `Specify the registry as part of the name or repository parameter.`
    
    -  `Choices`:
                no ←
                yes
  

  
  
  - `repository`
    
    - `Full path to a repository` 
    
    - `Use with state present to tag the image into the repository.`
    
    - `Expects format repository:tag` 
    
    - `If no tag is provided, will use the value of the tag parameter or latest` 

  
  
  - `rm`
    
    - `Remove intermediate containers after build.` 
    
    - `Please use build.rm instead. This option will be removed in Ansible 2.12.` 

  
  - `source`
    
    - `Determines where the module will try to retrieve the image from.` 
    
    - `Use build to build the image from a Dockerfile. "build.path must be specified" when this value is used.` 
    
    - `Use load to load the image from a .tar file. "load_path must be specified" when this value is used.` 
    
    - `Use pull to pull the image from a registry.` 
    
    - `Use local to make sure that the image is already available on the local docker daemon, i.e. do not try to build, pull or load the image.` 
    
    -     Choices:
                build
                load
                pull
                local

  
  
  
  
  - `state`
    
    - `Make assertions about the state of an image.`
    
    - `When absent an image will be removed. Use the force option to un-tag and remove all images matching the provided name.`  
    
    - `When present check if an image exists using the provided name and tag. If the image is not found or the force option is used, the image will either be pulled, built or loaded, depending on the source option.` 
    
    - `By default the image will be pulled from Docker Hub, or the registry specified in the image's name` 
    
    - `so to make sure that you are pulling, set source to pull`
    
    - `To build the image, "provide a path value set to a directory containing a context and Dockerfile", and "set source to build"`
    
    - ` To load an image, specify load_path to provide a path to an archive file.`
    
    - `To tag an image to a repository, provide a repository path.`   
    
    - `If the name contains a repository path, it will be pushed.` 
    
    - `Note:* state=build is DEPRECATED and will be removed in Ansible 2.11. Specifying build will behave the same as present` 

    -     Choices:
                absent
                present ←
                build
  
  
  
  - `tag`
    
    - `Used to select an image when pulling` 
    
    - `Will be added to the image when pushing, tagging or building. ` 
    
    - `Defaults to latest.` 
    
    - `If name parameter format is name:tag, then tag value from name will take precedence.` 

  
  
  - `timeout`
    
    - `The maximum amount of time in seconds to wait on a response from the API.`
    
    -` If the value is not specified in the task, the value of environment variable DOCKER_TIMEOUT will be used instead.`
    
    - `If the environment variable is not set, the default value will be used.`
    
    - `Default`:
                `60` 

