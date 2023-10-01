# amazon.aws.ec2

- `To install it` use:` ansible-galaxy collection install amazon.aws`

- `To use it in a playbook`, `specify: amazon.aws.ec2`

- `Creates or terminates ec2 instances`. 

- Note: `This module uses the older boto Python module to interact with the EC2 API`

- `amazon.aws.ec2` will `still receive bug fixes`, but `no new features `

-  Consider using the `amazon.aws.ec2_instance` module instead

- If `amazon.aws.ec2_instance` `does not support a feature you need that is available in amazon.aws.ec2, please file a feature request  `


- **parameters**
  
  - `assign_public_ip`  :-
    
    - `When provisioning within vpc, assign a public IP address`.
    
    - `Boto library must be 2.13.0+`.  
    
    - Choices:
            no
            yes 

  
  - `aws_access_key` 
    
    - `AWS access key`
    
    - `If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used`
    
    - `If profile is set this parameter is ignored.`
    
    - `Passing the "aws_access_key" and "profile" options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.`

  
  - `aws_secret_key` 
    
    - `AWS secret key. `
    
    - `If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.` 
    
    - `If profile is set this parameter is ignored`.
    
    - `Passing the "aws_secret_key" and "profile" options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.` 

  
  - `count`
    
    - `Number of instances to launch.` 
    
    - `Default`:
                `1`    
  
  
  
  - `count_tag` 
    
    -  `Used` `with` `exact_count` `to determine` `how many nodes based on a specific tag criteria should be running` 
    
    -  `one can request 25 servers` that are tagged with `class=webserver`
    
    -  `The specified tag must already exist or be passed in as the instance_tags option.`


  
  - `monitoring` 
    
    -  `Enable detailed monitoring (CloudWatch) for the instance.`
    
    -   boolean Choices:
          no ←
          yes
  
  
  - `ebs_optimized` 
    
    -  `Whether instance is using optimized EBS volumes`
    
    - Choices:

            no ←
            yes  
  
  
  
  
  - `ec2_url` 
    
    - `Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints)`. 

    - `Ignored for modules where region is required`
    
    - `Must be specified for all other modules if region is not used.`
    
    -  `If not set then the value of the EC2_URL environment variable`
  
  
  - `exact_count`
    
    - ` An integer value which indicates how many instances that match the 'count_tag' parameter should be running`

    - `Instances are either created or terminated based on this value.`

  
  - `group` 
    
    - `Security group (or list of groups) to use with the instance.`

  
  - `group_id` 
    
    - `Security group id (or list of ids) to use with the instance`

  
  - `image` 
    
    - `ami ID to use for the instance.` 
    
    - `Required when state=present.`
    
  
  -  `instance_ids` 
     
     - `list of instance ids, currently used for states: absent, running, stopped`

  
  
  - `instance_initiated_shutdown_behavior` 
    
    - `Set whether AWS will Stop or Terminate an instance on shutdown.`
    
    - `Choices`:
            
            `stop ←`
            
            `terminate`  

    
  - `id`
      
    - `Identifier for this instance or set of instances, so that the module will be idempotent with respect to EC2 instances` 


  
  - `instance_profile_name` 
    
    - `Name of the IAM instance profile (i.e. what the EC2 console refers to as an "IAM Role") to use. Boto library must be 2.5.0+.`

  
  
  - `instance_tags`  
    
    - `A hash/dictionary of tags` to `add to the new instance` or `for instances to start/stop by tag.` 
    
    -  For example `{"key":"value"}` or `{"key":"value","key2":"value2"}.`

  
  
  - `instance_type` 
    
    - `Instance type to use for the instance` 


  - `key_name` 
    
    -  `Key pair to use on the instance.`
    
    - `The SSH key must already exist in AWS in order to use this argument.`  
    
    - `Keys can be created / deleted using the amazon.aws.ec2_key module.` 

  
  - `network_interfaces`  
    
    - `A list of existing network interfaces to attach to the instance at launch` 
    
    - `When specifying existing network interfaces`, `none of the` 
      
      - `assign_public_ip`
      
      - `private_ip`
      
      - `vpc_subnet_id`, 
      
      - `group`, 
      
      - `group_id` 
    
    `parameters may be used`

    - creating a new network interface at launch we have to use 
      
      - `assign_public_ip`
      
      - `private_ip` 
      
      - `vpc_subnet_id`
      
      - `group`
      
      - `group_id` 

  
  
  
  - `vpc_subnet_id` 
    
    - The `subnet ID` `in which to launch the instance` (VPC). 

  
  
  - `private_ip`
    
    - `The private ip address to assign the instance (from the vpc subnet).`  

  
  - `zone`
    
    - `AWS availability zone in which to launch the instance`.
 


  - `profie`
    
    - `Uses a boto profile `
    
    - ` Only works with boto >= 2.24.0.`
    
    - `Using profile will override aws_access_key, aws_secret_key and security_token and support for passing them at the same time as profile has been deprecated.` 
    
    - `aws_access_key, aws_secret_key and security_token will be made mutually exclusive with profile after 2022-06-01`. 

  
  
  - `region` 
    
    - `The AWS region to use` 
    
    - `If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used `


  - `security_token` 
    
    - `AWS STS security token.`
    
    - `If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.`
    
    - `If profile is set this parameter is ignored.`

  
  
  - `state `
    
    - `Create, terminate, start, stop or restart instances` 
    
    - `The state 'restarted' was added in Ansible 2.2.`
    
    - `When state=absent, instance_ids is required.` 
    
    - `When state=running, state=stopped or state=restarted then either instance_ids or instance_tags is required.`  
    
    - Choices:
              absent
              present ←
              restarted
              running
              stopped 
   

  
  - `termination_protection`  
    
    - `Enable or Disable the Termination Protection.`
    
    -  `Defaults to false`.
    
    -  Choices:
              no
              yes

  
  - `wait`
    
    - `Wait for the instance to reach its desired state before returning`.
    
    - `Does not wait for SSH, see the 'wait_for_connection module' example for details.`
    
    - Choices:
            no ←
            yes 
  

  - `wait_timeout`

    - `How long before wait gives up, in seconds`.

  
  - `volumes` 
    
    - `A list of hash/dictionaries of volumes to add to the new instance.` 
    
    - **Parameters**
      
      - `delete_on_termination` 
        
        - `Whether the volume should be automatically deleted when the instance is terminated.`
        
        - Choices:
                  no ←
                  yes

      
      - `device_name`   
        
        - `A name for the device (For example /dev/sda)`. 

        - `Whether the volume should be encrypted using the 'aws/ebs' KMS CMK`.
        
      
      - `ephemeral`   
        
        - `Whether the volume should be ephemeral.` 
        
        - `Data on ephemeral volumes is lost when the instance is stopped`.
        
        - `Mutually exclusive with the snapshot parameter` 

      
      - `volume_size` 
        
        - ` The size of the volume (in GiB).`

      
      - `volume_type`
        
        - `The type of volume to create` 


   



