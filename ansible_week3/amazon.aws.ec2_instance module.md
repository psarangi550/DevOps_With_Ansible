# `<u>`amazon.aws.ec2_instance module `</u>`

- To check whether it is installed, run `ansible-galaxy collection list`

- To install it, use: `ansible-galaxy collection install amazon.aws`

- To use it in a playbook, specify: `amazon.aws.ec2_instance`  


- `Create and manage AWS EC2 instances.`

- This `module does not support creating` [EC2 Spot instances](https://aws.amazon.com/ec2/spot/).

- `The amazon.aws.ec2_spot_instance module can create and manage spot instances`

- **Parameter**

  - `access_key`

    - `AWS access key ID`.
    - `The AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variables may also be used in decreasing order of preference.`
  
  
  - `vpc_subnet_id`

    - `The subnet ID in which to launch the instance (VPC)`.
    - `If none is provided`, `amazon.aws.ec2_instance will chose the default zone of the default VPC.`
  
  
  - `availability_zone`

    - `Specify an availability zone to use the default subnet it`
    
    - `Useful if not specifying the vpc_subnet_id parameter.`
    
    - `If no subnet, ENI, or availability zone is provided, the default subnet in the default VPC will be used in the first AZ (alphabetically sorted).  `
  
  
  - `count`

    - `Number of instances to launch.`
    - `Setting this value will result in always launching new instances`.
    - `Mutually exclusive with exact_count`.
  
  - `exact_count`

    - `An integer value` `which indicates` `how many instances that match the filters parameter should be running`.
    - `Instances are either created or terminated based on this value.`
    - `If termination takes place, least recently created instances will be terminated based on Launch Time.`
    - `Mutually exclusive with count, instance_ids.`
  
  - `filters`

    - `A dict of filters to apply when deciding whether existing instances match and should be altered `
    - `Each dict item consists of a filter key and a filter value`
    - `for possible filters. Filter names and values are case sensitive.`
    - `By default`, `instances are filtered` `for counting by their “Name” tag, base AMI, state (running, by default), and subnet ID `
  
  
  - `image` :- which is a `dictionary`

    - `An image to use for the instance`
    - The `amazon.aws.ec2_ami_info` `module` may be `used to retrieve images`
    - `One of image or image_id are required when instance is not already present. `
    - **paramters**

      - `id`  :- `The AMI ID.`
      - `kernel` :- `a string AKI to override the AMI kernel`.
      - `ramdisk` :- `Overrides the AMI’s default ramdisk ID.`
  
  
  - `image_id`

    - `This is an alias for image.id.`
    - `ami ID to use for the instance`
    - One of `image or image_id` are `required` `when instance is not already present`.
  - `instance_ids`

    - `If you specify one or more instance IDs, only instances that have the specified IDs are returned.`
    - `Mutually exclusive with exact_count.`
    - `Default: [] `
  - `instance_initiated_shutdown_behavior`

    - `Whether to "stop or terminate" an instance upon shutdown.`
  - `instance_type`

    - `Instance type to use for the instance`
    - `Only required when instance is not already present.`
    - At least `one of instance_type` or `launch_template` `must be specificed` `when launching an instance.`
  - `key_name`

    - `Name of the SSH access key to assign to the instance` - `must exist in the region the instance is created.`
    - `Use amazon.aws.ec2_key to manage SSH keys.`
  - `name`

    - `The Name tag for the instance.`
  
  
  
  - `cpu_options` which is a `dictionary`

    - `Reduce the number of vCPU exposed to the instance.`
    - `Those parameters can only be set at instance launch`
    - The `two suboptions` `threads_per_core` and `core_count` are `mandatory`.
    - **paramter**

      - `core_count` :- `Set the number of core to enable. `
      - `threads_per_core` :-  `Select the number of threads per core to enable`
      - Choices:

        `1`

        `2`
  
  
  - `ebs_optimized`

    - Whether instance is should use optimized EBS volumes,
  
  
  - `network` which is a `dictionary`

    - `Either a dictionary containing the key interfaces corresponding to a list of network interface IDs`  or `containing specifications for a single network interface`.
    - `Use` the `amazon.aws.ec2_eni ``module` to `create ENIs with special settings`.
    - **parameters**

      - `assign_public_ip` :-
      - `When true assigns a public IP address to the interface.`
      - Choices:

        `false`

        `true`
      - `delete_on_termination`

        - `Delete the interface when the instance it is attached to is terminated.`
        - Choices:

          `false`

          `true`
      - `description`
      - `A description for the network interface.`
      - `groups`

        - `A list of security group IDs to attach to the interface.`
      - `private_ip_address`

        - `An IPv4 address to assign to the interface.`
      - `private_ip_addresses`

        - `A list of IPv4 addresses to assign to the network interface`.
      - `subnet_id`

        - `The subnet to connect the network interface to.`
  - `region`

    - `The AWS region to use.`
    - The `AWS_REGION` or `EC2_REGION` environment variables may also be used.
    - `For global services such as IAM, Route53 and CloudFront, region is ignored`.
  - `secret_key`

    - `AWS secret access key.`
    - The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.
  - `security_group`

    - `A security group ID or name.`
    - `Mutually exclusive with security_groups`.
  - `security_groups`

    - `A list of security group IDs or names (strings).`
    - `Mutually exclusive with security_group`.
    - Default: []
  - `state`

    - `Goal state for the instances.`
    - `state=present`: `ensures instances exist`, `but does not guarantee any state (e.g. running). Newly-launched instances will be run by EC2.`
    - `state=running`: `state=present + ensures the instances are running`
    - `state=started`: `state=running + waits for EC2 status checks to report OK if wait=true`
    - s `tate=stopped:` `ensures an existing instance is stopped.`
    - `state=rebooted:` `convenience alias for state=stopped immediately followed by state=running`
    - `state=restarted`: `convenience alias for state=stopped immediately followed by state=started`
    - `state=terminated: ensures an existing instance is terminated.`
    - `state=absent: alias for state=terminated `
    - BELOW STAGES ARE THERE:-

      "present" ← (default)

      "terminated"

      "running"

      "started"

      "stopped"

      "restarted"

      "rebooted"

      "absent"
  - `wait`

    - `Whether or not to wait for the desired state (use (wait_timeout) to customize this). `
    - Choices:

      false

      true ← (default)
  - `wait_timeout`

    - `How long to wait (in seconds) for the instance to finish booting/terminating.`
    - `Default: 600`
  - `tags`:

    - `A dictionary representing the tags to be applied to the resource.`
    - `If the tags parameter is not set then tags will not be modified.`
