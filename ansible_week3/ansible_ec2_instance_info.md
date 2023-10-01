# amazon.aws.ec2_instance_info module

- To use it in a playbook, specify: `amazon.aws.ec2_instance_info.`

- `Gather information about ec2 instances in AWS`

- **parameters**
  
  - `access_key` 
    
    - `AWS access key ID`. 

    - `The AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variables may also be used in decreasing order of preference`'
    
  - `filters`   
    
    -  `A dict of filters to apply`
    
    - `Filter names and values are case sensitive.`
    
    - `Default: {}` 

  - `minimum_uptime` 
  
    -  `Minimum running uptime in minutes of instances`
    
    -  `For example if uptime is 60 return all instances that have run more than 60 minutes`.  


  - `region` 
    
    - `The AWS region to use.`

    - The `AWS_REGION` or `EC2_REGION` `environment variables `may also be used.
    
    - `For global services such as IAM, Route53 and CloudFront, region is ignored.` 
  
  - `secret_key` :
    
    - `AWS secret access key`  
    
    - `The AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variables may also be used in decreasing order of preference.` 
    
    - `Support for the EC2_SECRET_KEY environment variable has been deprecated and will be removed in a release after 2024-12-01.`

  - `instance_ids` 
    
    - `If you specify one or more instance IDs, only instances that have the specified IDs are returned.` 
    
    - `Default: [] `


`Example:-`

- if we specify the `tags` as `Key:Name` and `Value:Value"` then while `querying we can use` as below 

    ```
    

    
    
    
    
    
    
    
    
    
    ```

- if we ahve use the `tags` directly with the `name:value` as below the query should be as `below`

    ---













    ...