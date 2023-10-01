# Using Ansible in Cloud Services and Containers

* here we will look into 2 different topics
  
  - `AWS with Ansible` :- Using `AWS` and `Ansible` to `automate 20EC2 hosts with a web application deployment`
  
  - `Docker with Ansible` :- Automating `Docker using the Builtin Docker module`

* here we will look into `below topics`
  
  * how to `configure`  `Ansible for AWS Support`
  
  * `creating` `instances` through `ansible` with `AWS` and `adding/allocate IP address`
  
  * using `AWS Dynamic Inventory`
  
  * `spinup` the `nginx webapp `using the `AWS` , we will `spin` up `nginx webapp` `on scale` over `accross 20 hosts using AWS`
  
  * `terminating and removing` `AWS instances and related components`

* here we will be looking into the `how to use ansible for "automation and deployment"` of `"instances" in AWS`

* the `modules within ansible for AWS are built using the popular boto and boto3 python library` hence `there is a lot of functionality for AWS`

* we need the `amazon free tier account` , if not available  then `review associated cost and become aware about the aws Pricing` which `should not be substancial`

* if we are `leaving the instances running` then `it can incurred cost`

* `research the pricing cost` and `look how to set up a budgeting alert for the same`

<br/> <br/>

* go to the `AWS control panel` &rarr; `go to EC2 Dashboard` 

* we need to `create a Key Pair` which can be created by  `AWS control panel` &rarr; `go to EC2 Dashboard`  &rarr; `Key Pairs`

* then once we are in the `Key Pairs` &rarr; `create Key Pair` &rarr; `Enter a Pair Name`

* we need the `key-pair` in the `pem` `format` as we are using it with `ssh`

* it will `auto download the pem file` keep it safe 


- **Creating Access Key for the AWS account API Access**

* then we need to `create` the `access Key` so that we have the access to the `API Access of our AWS account`

* goto the `my account section on top right` &rarr; `select the my security credetional` option `which will open the IAM console`

* then click onto `create access key` which will create the `AWS access key` and `AWS secret access key` which can provide `API Access to AWS account`

* the `AWS access key` and `AWS secret access key` `will be shown or download only once` hence keep it safe else `download the required CSV file`  


**Creating Default AWS VPC Service**

* when we are `creating the AWS account` then we will be `getting a default AWS VPC` which we can leverage 

* if not we can also creae the `default VPC for AWS`  

- go to the `services` &rarr; `seach for VPC` &rarr; then `it will display the default VPC in this case`

- if we are not getting the `defgault VPC` then goto `actions` &rarr; `create default VPC` option 

<br/> <br/>


- **Setuo for Using AWS with Ansible**

- the `ansible module AWS` uses `boto` 

- and `environment vriable` `setup` for the `AWS info that we saw for the access key`

- we need to set the `environment variable` such as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` which can be created as below 

    ```
        export AWS_ACCESS_KEY_ID = <access key>
        export AWS_SECRET_ACCESS_KEY = <secret access key>
        # setting up the access key and secret access key for the AWS account
    
    ```

- 

