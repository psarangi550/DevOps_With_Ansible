# amazon.aws.ec2_security_group module

- `This module is part of the amazon.aws collection (version 6.4.0).`

- ` You might already have this collection installed if you are using the ansible package`

- It is not included in ansible-core

- To check whether it is installed, `run ansible-galaxy collection list`

- To install it, use: `ansible-galaxy collection install amazon.aws`

- `Maintains EC2 security groups.`

- `Aliases: ec2_group`


- **Parameters**
  
  - `access_key` :-
    
    - `AWS access key ID.`
    
    - The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` `environment variables may also be used` in `decreasing order of preference`.  
    
    - Support for the `EC2_ACCESS_KEY` `environment variable` has `been deprecated` and will be removed in a release after 2024-12-01. 

  
  - `aws_ca_bundle`
    
    - The `location of a CA Bundle` to `use when validating SSL certificates.` 
    
    - The `AWS_CA_BUNDLE` `environment variable may also be used.` 

  
  - `group_id`
    
    - `Id of group to delete (works only with absent).` 
    
    - `One of` and `only one of name or group_id is required.`
    
  
  - `profile` 
      
      - `A named AWS profile to use for authentication.`
      
      - `The AWS_PROFILE environment variable may also be used.`

      - `The profile option is mutually exclusive with the aws_access_key, aws_secret_key and security_token options.` 

  
  - `name`
  
    - `Name of the security group.`
    
    - `One of and only one of name or group_id is required.`
    
    - `Required if state=present`.   

  
  - `description`
    
    - `Description of the security group.`

   - `Required when state is present.`

  
  - `state`
    
    - `Create or delete a security group.` 
    
    - `Choices`:

      - `"present" ← (default)`

      - `"absent"`

  
  - `tags`
    
    - `A dictionary representing the tags to be applied to the resource.` 
    
    - `If the tags parameter is not set then tags will not be modified.`
 

  - `vpc_id`
  
    - `ID of the VPC to create the group in.`


  - `region`

    - `The AWS region to use.`
    
    - `For global services` such as `IAM, Route53 and CloudFront`, `region is ignored.` 
    
    - The `AWS_REGION` or `EC2_REGION` `environment variables may also be used`. 
    
    - `Support for the EC2_REGION environment variable has been deprecated and will be removed in a release after 2024-12-01. `

  
  - `secret_key`

    - `AWS secret access key.`
    
    - The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in `decreasing order of preference. `
    
    - The `secret_key` and `profile` options are `mutually exclusive.` 
    
    - `Support for the EC2_SECRET_KEY environment variable has been deprecated and will be removed in a release after 2024-12-01. `

  
  - `rules`
  
    - `List of "firewall inbound rules" to enforce in this security group`. 
    
    - `If none are supplied`, `no inbound rules will be enabled`.
    
    - `Rules list may "include its own name" in "group_name" `
    
    - `This allows idempotent loopback additions (e.g. allow group to access itself)`. 
    
    - **parameters**
    
      - `cidr_ip`
        
        - The `IPv4 CIDR range` `traffic is coming from`. 
        
        - You can specify only one of
          
          - `cidr_ip`
          
          - `cidr_ipv6`
          
          - `ip_prefix` 
          
          - `group_id`
          
          - `group_name`.  

    - `cidr_ipv6`
        
        - The `IPv6 CIDR range traffic is coming from.` 
        
        - You can specify only one of
          
          - `cidr_ip`
          
          - `cidr_ipv6`
          
          - `ip_prefix` 
          
          - `group_id`
          
          - `group_name`. 

    - `from_port`
      
      - `Mutually exclusive with` `icmp_code`, `icmp_type` and `ports`. 
      
      - `The start of the range of ports that traffic is going to.` 
      
      - A value can be between `0 to 65535.` 
      
      - When `proto=icmp` a `value of -1` `indicates all ports.` 

    - `to_port`
      
      - `Mutually exclusive with` `icmp_code`, `icmp_type` and `ports`.  
      
      - `The end of the range of ports that traffic is going to`. 
      
      - A value can be between `0 to 65535.` 
      
      - When `proto=icmp` a `value of -1` `indicates all ports.`   

  - `group_desc`
    
    - If the group_name is set and the Security Group doesn’t exist a new Security Group will be created with group_desc as the description.

  - `group_id`:-
    
    - `The ID of the Security Group that traffic is coming from `
    
    - You can specify only one of
          
          - `cidr_ip`
          
          - `cidr_ipv6`
          
          - `ip_prefix` 
          
          - `group_id`
          
          - `group_name`. 
    
    - `group_name`
      
      - `Name of the Security Group that traffic is coming from.`
      
      - `If the Security Group doesn’t exist a new Security Group will be created with group_desc as the description.`
      
      - `group_name can accept values of type str and list.`
      
      - You can specify only one of
          
          - `cidr_ip`
          
          - `cidr_ipv6`
          
          - `ip_prefix` 
          
          - `group_id`
          
          - `group_name`.  


    - `ip_prefix`
    
      - `The IP Prefix https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-prefix-lists.html that traffic is coming from.`
      
      - `You can specify only one of cidr_ip, cidr_ipv6, ip_prefix, group_id and group_name`. 

    - `proto`:-
      
      - `The IP protocol name (tcp, udp, icmp, icmpv6) or number `
      
      - `Default: "tcp" `

    - `ports`
      
      - `A list of ports that traffic is going to.`
      
      - ` Elements of the list can be a single port (for example 8080)`, or a `range of ports specified as <START>-<END>, (for example 1011-1023).` 

      - `Mutually exclusive with ` `icmp_code`, `icmp_type`, `from_port` and `to_port`.
      
  - `rules_egress` 
    
    - `List of firewall outbound rules to enforce in this group (see example)`
    
    - `If none are supplied, a default "all-out rule is assumed". `
    
    - `If an empty list is supplied, no outbound rules will be enabled.`
    
    - `cidr_ip` :-
       
      - `The IPv4 CIDR range traffic is going to.`
      
      - You can specify only one of
          
          - `cidr_ip`
          
          - `cidr_ipv6`
          
          - `ip_prefix` 
          
          - `group_id`
          
          - `group_name`.   

  - `cidr_ipv6`
        
        - The `IPv6 CIDR range traffic is going to.` 
        
        - You can specify only one of
          
          - `cidr_ip`
          
          - `cidr_ipv6`
          
          - `ip_prefix` 
          
          - `group_id`
          
          - `group_name`. 
  
  - `from_port` 
    
    - `The start of the range of ports that traffic is going to.` 
    
    - `A value can be between 0 to 65535. `
    
    - `When proto=icmp a value of -1 indicates all ports.` 
    
    - `Mutually exclusive with icmp_code, icmp_type and ports. `


  - `to_port`
    
    - `The end of the range of ports that traffic is going to.`
    
    - `A value can be between 0 to 65535.` 
    
    - `When proto=icmp a value of -1 indicates all ports.`  
    
    - `Mutually exclusive with icmp_code, icmp_type and ports.` 

  - `port`
    
    - `A list of ports that traffic is going to.`
    
    - `Elements of the list can be a single port (for example 8080), or a range of ports specified as <START>-<END>, (for example 1011-1023)` 
    
    - `Mutually exclusive with icmp_code, icmp_type, from_port and to_port.` 

  - `proto`
    
    - `The IP protocol name (tcp, udp, icmp, icmpv6) or number` 

  - `rule_desc`
    
    - `A description for the rule.`

  - `ip_prefix`

    - `The IP Prefix https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-prefix-lists.html that traffic is going to.`
    
    - `You can specify only one of cidr_ip, cidr_ipv6, ip_prefix, group_id and group_name`. 

  - `group_id`
    
    - `The ID of the Security Group that traffic is going to.` 
    
    - `You can specify only one of cidr_ip, cidr_ipv6, ip_prefix, group_id and group_name.` 

  - `group_name`
  
    - `Name of the Security Group that traffic is going to.`
    
    - `If the Security Group doesn’t exist a new Security Group will be created with group_desc as the description. `
    
    - `You can specify only one of cidr_ip, cidr_ipv6, ip_prefix, group_id and group_name.` 

  - `group_desc`
    
    - `If the group_name is set and the Security Group doesn’t exist a new Security Group will be created with group_desc as the description.`
 




