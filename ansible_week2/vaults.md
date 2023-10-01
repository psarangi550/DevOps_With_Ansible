# <ins> Ansible Vault </ins> #

- we need to `account for` the `sensible info` and `secured` ,  ideally . `providing the same functionality that was preveiously provided`

- for this situation an `useful tool` will be as `ansible vault`

- `ansible vault` allow us to `vault and unvault info as desired`  

- here we will be learning 
  
  - how to `encrypt and decrypt` `variables` using the `ansible vaults`
  
  - how to `encrypt and decrypt` `files` using the `ansible vaults`
  
  - how to `re-encrypt data` 
  
  - how to use `multiple valuts`

- **Case01**
  
  - here as of now we are using the `ansible_become_password : <required root passwd>` inside the `groupvars` or `group_vars folder by defining the particular hostname`
  
  - but here we have remove the   `ansible_become_password : <required root passwd>` from the `group_vars folder by defining the particular hostname` for the `ubuntu target group`
  
  - now when we try to `ping to the ubuntu target group` we will be facing the issue as the `ansible_become_password` been missing and only have the `ansible_become:true`
  
  - now when we use the `ansible adhoc command` then we can see the below details 

    
    ```

        ansible ubuntu -m ping -o 
        
        # using the ansible adhoc command line utility then we can see the info as 
        
        ubuntu1 | FAILED! => {"msg": "Missing sudo password"}
        ubuntu2 | FAILED! => {"msg": "Missing sudo password"}
        ubuntu3 | FAILED! => {"msg": "Missing sudo password"}

    
    ```

- here we can `change this` `in favour of` the `ansible_vaults` `for this password`

- we need to create a `vault_entry` for the `ansible_become_password` for the password variables

- here while generating the `variable which we want to store to vault` using the `ansible-vault` command this can `key` will be `name thats been provided against the --name attribute while using the ansible-vault command` and `value will br encrypted value` `(look very carefully for the vault password as it can overstepped  in the terminal)` 

- we can write the below command for the same as 

    ```
        ansible-valut encrypt_string --ask-vault-pass --name 'ansible_become_pass' 'password'

        # here we are making the use of the `ansible-valut` tool in here 

        # we are using the `encrypt_string` stating we want to `encrypt the string provided`

        # also we are using the --ask-vault-pass which will prompt for the `vault password`

        # --name will provide us the `name of variable we want to save to the vault`

        # `password` is the `corresponding value` for the `variable that that we saved usign the --name attribute`

        -------------------------------------------------------------------------------------------------------------
        # when we execute this we will be getting the output value as below 
        # it will prompt for the vault password and confirm the password 
        # then we can see the message as encryption successful
        # then it will generate the variable that we provided with the vault value 
        
        New Vault password: 
        Confirm New Vault password: 
        Encryption successful
        ansible_become_password: !vault |
                $ANSIBLE_VAULT;1.1;AES256
                38623063613234383633393638323933313864366563666461666464356266323430633962346332
                3438336635396437343234616637666330363137643034660a383062353839313232623536373766
                63343566386239613739373931396664663532303234326537643364613563326437306162353165
                3139663264633734350a363263323663663563336138373833376663373630636535333831363936

        # this can be used in the `group_vars/<hostname>` file as below 

        group_vars/ubuntu
        -----------------

        ---

        ansible_become: true 
        ansible_become_password: !vault |
                $ANSIBLE_VAULT;1.1;AES256
                38623063613234383633393638323933313864366563666461666464356266323430633962346332
                3438336635396437343234616637666330363137643034660a383062353839313232623536373766
                63343566386239613739373931396664663532303234326537643364613563326437306162353165
                3139663264633734350a363263323663663563336138373833376663373630636535333831363936

        ...

    
    ```

- now as we are using the `ansible vault` for `encrypting the password i.e ansible_become_pass` hence `we need to supply`  `vault information`

- here we can `supply` the `vault information` to the `ansible adhoc command` while using the `that particular target host` by using the `--ask-valut-pass` command option

- hence now we try to ping the `same ubuntu system which is valut encrypted then we can use it as below`

    
    ```

        ansible ubuntu --ask-vallt-pass -m ping -o 
        # here we are using the --ask-valut-pass option which will prompt for the vault pass
        # also here we are pining using the ping module 
        # -o stands for the --oneline option 
        # here we are targeting the ubuntu hot where we save the valut entry 

        # the output of this will be as
        # this will ask for the password of the vault which we set while using the `ansible-vault`  command  
        Vault password: # here we need to provide the `valut password we have preveiously created`
        ubuntu3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}

    ```

- **Case02**
  
  - we can also encrypt the `file` using the `ansible-vault command line tool`

  - we can define a `file` with the `key and value pair` that can be written as below  
  
    ```
        external_vault_var.yaml
        =======================
        ---

        example_key :  example_value
        ...
    
    ``` 

- if we want to encrypt the file we can use the command as below 

    
    ```

        ansible-vault encrypt external_vault_var.yaml
        # the encrypt command will encrypt the yaml file defined in here 
        # hence the output will be as below 

        New Vault password: 
        Confirm New Vault password: 
        Encryption successful
        
    
        # few things to kee in mind that 
        # you must be having the 775 accesss to the folder containering the external_vault_var.yaml
        # you also need the 775 access to the file external_vault_var.yaml
        # we also have to define the user lavel for both the permission  
    
    ```

- now we can use this `particular encrypted file` that we `encrypt` using the command `ansible-vault encrypt <filename>` in the `ansible-playbook`

- here in the `playbook` we don't have to specify the `ansible vault related any info` ansible will automatically able to detect that

- here we can write the playbook as below 

    ```
        vault_playbook.yaml
        ===================

        ---
    
        - hosts: linux # here we are targeting the linux host in this case 

          vars_files:
            - ./external_vault_var.yaml

          tasks:   #defining the task attribute in here 
            - name: using the variable using the debug module in here  
              debug:   #usiing the debug module in this case 
                var: example_key  # here accessiung the variable using the var paramter 


        ...

        # we can execute this playbook as below 
        # here we need to make use of the --ask-vault-pass attribute
        ansible-playbook vault_playbook.yaml --ask-vault-pass
        # using the --ask-vault-pass to prompt for the vault password while executing the playbook
        # the output will be in the format of below

        Vault password:  # here it will ask for the vault password that we have set

        PLAY [linux] *************************************************************************************************************************************************************************

        TASK [Gathering Facts] ***************************************************************************************************************************************************************
        ok: [ubuntu2]
        ok: [ubuntu3]
        ok: [ubuntu1]
        ok: [centos2]
        ok: [centos3]
        ok: [centos1]

        TASK [using the variable using the debug module in here] *****************************************************************************************************************************
        ok: [centos1] => {
            "example_key": "example_value"
        }
        ok: [centos2] => {
            "example_key": "example_value"
        }
        ok: [centos3] => {
            "example_key": "example_value"
        }
        ok: [ubuntu1] => {
            "example_key": "example_value"
        }
        ok: [ubuntu2] => {
            "example_key": "example_value"
        }
        ok: [ubuntu3] => {
            "example_key": "example_value"
        }

        PLAY RECAP ***************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

    
    
    ```
  - here actually `two things` happended 
    
    - first the `ansible-vault` successfully decrypt the `ansible_become_pass` value as we have provided the `vault password` , we can validate that as we are able to connect to all the `ubuntu target hosts`
    
    -  also we have successfully get the `value of the key which being encrypted` by using the same `vault password ` as we are able to get the `vaule of the example_key` in the output

- **case03**
  
  - there are also other thing we can do with the `ansible-vault` command such as 
  
  - we can decrypt the `encrypted content` using the `ansible-vault decrypt` command 

    ```
        ansible-vault decrypt external_vault_var.yaml
    
        # using the decrypt key to decrypt the encrypte yaml file 
        # here will be the output
        Vault password: 
        Decryption successful
        # here if we go ahead and check the content then we can see that vault been decrypted as we can see other info as well
    
    ```

- we can also reencypt this as below 

    ```
        ansible-vault encrypt external_vault_var.yaml
    
        # re-encrypt the data again back to the encrypted form  in here 
        # here will be the output
        New Vault password: 
        Confirm New Vault password: 
        Encryption successful
    
    ```

- sometimes there may be the requirement of `password rotation` where might need to `decrypt and rencrypt the file back again`

- then we can use the  `rekey command along with ansible-vault` which will `decrypt the key and then re-encrypt the same`

- as it is doing the `decryption first then the encryption` hence it will ask for the `vault password first followed by the resetting the new vault pass agian for the recencyption`

- we can use it as below 

    ```
        
        ansible-vault rekey external_vault_var.yaml  

        # using the rekey command which will first decrypt and re-encrypt the file backagain 
        # here will be th output as below 
        Vault password: 
        New Vault password: 
        Confirm New Vault password: 
        Rekey successful
        # here we can see at the end th file again enctypted with a different vault password
    
    
    ```


- if we want to view the `key and value` that being encrypted then we can use the command as `ansible-vault view <encrypted filename>`

- this will prompt for the password in this case over here as below 

    ```
        ansible-vault view <encrypted filename>

        # ex:
        ansible-vault view external_vault_var.yaml
        # here this will ask for the vault password if valid then show the content 
        Vault password: 
        example_key: example_value

    ```

- **case04**

- we can save the `vault password` as to a `passwordfile` and use that password file as the `vault password` using the `--vault-password-file` option 

- here we are saving the `vault password` to a file using the echo command as `echo <vault pass> > <file name>` and using the `--vault-password-file` we can define the `vault password file loction` as `--vault-password-file <password file>`

- also we can use the use the command as below 

    ```

        echo <password> > passwordfile 
        # here we are writing the password to a password file in this case 

        ansible-vault view --vault-password-file passwordfile external_vault_var.yaml
        # here we have used the --vault-password-file which will provide the password info in this case 
        # then we don't have to provide the password in here 
    
        external_vault_var.yaml # here in this case it will not prompt for the vault password
    
    ```

- **case04**

- if we want to prompt for the `vault password` then we can use the command as `--vault-id as the paramter` and the `value will be @prompt`

- if we want to use the below command to view the `encryoted content` as below 

- we can use the command as below 

    ```
        ansible-vault view --vault-id @prompt external_vault_var.yaml 
        
        # using the ansible-vault command with the value as @prompt which will prompt for the vault password 
        # here also we are using the external_vault_var.yaml to get the encrypted content
        # the output will be as below 
        Vault password (default): 
        example_key: example_value

    ```

- `--vault-id` provide other `benefit` rather than the `input prompt password`

- we can use that with the `named vaults` and `filename` which are nothing but the `password filename`

- we can use this as below against the vaule of `--vault-id parameter`
  
  - `name of the vault@[<password filename>| prompt]` 

- here we have written the `password to a password file` by using the command as `echo "<password>" > passwordfile`

- we can use the below syntax fetch the /view the encrypted content valyue using the command as below 

    ```
        echo "<password>" > passwordfile
        # writing the password to a password file in here 

        ansible-vault --vault-id @passwordfile external_vault_var.yaml
        # here we are using the --vault-id with the option as below
            - we don't know the name of vault hence making it as empty 
            - we are also using the @passwordfile which will consider the password file in this case 
        
        # the output for the content being in here is of
        example_key: example_value
        # this command also not going to ask for the password in this case 
    
    ```

- we can also create the `named vault` using the `--vault-id` command with `ansible-vault`

- lets suppose we have the `file` as `external_var.yaml` where `we have the key value pair `

    ```
        external_var.yaml
        =================
        ---
        some_key: some_value
        ...
    
    ```

- we want to create the `named vault` for the `external_var.yaml` file using the `--vault-id` option then we can use it as below 

- we can use it as below 
  
  ```
    ansible-vault encrypt --vault-id ext@prompt external_var.yaml
    # here we re trying to encypt the external_var.yaml file 
    # also here we are using the --vault-id as the ext@prompt where the ext is the name of the vault 
    # @prompt means ask for the vault password 
    
    
    # we can see the below output for the same 
    # lets suppose  the password is `pratik` in here 
    New vault password (ext): 
    Confirm new vault password (ext): 
    Encryption successful 

    # if we have a look in the encypted file we have thebelow content as 
    $ANSIBLE_VAULT;1.2;AES256;ext
    36376466396662373232623263376562613861366464616330646532363061633036643430363437
    6662353866643966346632326536323565336532613661380a343531653935356235643732313363
    39666331313962656233353537663837646137386339323434656537666236623030353932396535
    3639376132643262620a613639396533623862653530643831626662353138343566343836663337
    32656530353362383566353435366665336337613939613836636531343232316236

   # we can see the name `ext` been there in the `enrpted string in here`
  
  ```

- **case05**

- we can use the use the same conecpt to generate the `ansible_become_pass` file here using the `name vault` as the `ssh`

- here as we are geneting for the sdtring we need to use the `encrypt_string` instead of the `encrypt` which is for the `file`

- we can use the command as below

    ```

        ansible-vault encrypt_string --vault-id ssh@prompt --name 'ansible_become_pass' 'password'
        # here we are using the encrypt_string to encrypt a particular string in here 
        # also we are usng the --vault-id as the name as ssh and for the password using the prompt 
        # also we are using as --name as `ansible_become_pass`
        # the string we want to encrypt is of `password`

        # hence the output in this case as below
        # lets suppose the password id `vaultpass` 

        New vault password (ssh): 
        Confirm new vault password (ssh): 
        Encryption successful
        ansible_become_pass: !vault |
                $ANSIBLE_VAULT;1.2;AES256;ssh
                30623238323032313636643866656139306466306534613561326333383264326161393432663832
                3263373638376533623238656238303064643032303137390a313263323864346439373464303364
                36333465383965316439346266326461316365663462626366366431363361333664386662363763
                3665633233653664640a336532646565626230633664623933366463353638626639643438323937
                6330
    
    
    
        # we can then add that to the group_vars/ubuntu tarhget host as below 

        group_vars/ubuntu
        =================
        ---

        ansible_become: true
        ansible_become_pass: !vault |
                $ANSIBLE_VAULT;1.2;AES256;ssh
                30623238323032313636643866656139306466306534613561326333383264326161393432663832
                3263373638376533623238656238303064643032303137390a313263323864346439373464303364
                36333465383965316439346266326461316365663462626366366431363361333664386662363763
                3665633233653664640a336532646565626230633664623933366463353638626639643438323937
                6330

        ...
    
    ```

- **Case6**
  
  - here we have one `external_var.yaml` file  which is `ansible_vault encrypted` with the `name vault as ext` and also we have added the `ansible_vaut` for the `ansible_become_password` as well in the `group_vars/ubuntu` file with the named vault as `ssh`
  
  - both of them having the `different different password` and if we want to use it in the same playbook  then we can use it as below 
  
  - while executing the `ansible-playbook` which contain both the `named vault with different different passsword` as below  

  - we can write the `ansible-playbook` s below

    ```
        vault_playbook.yaml
        ===================
        ---

        - hosts: linux # here we are targeting the linux host in this case 

          vars_files:
            - ./external_var.yaml

          tasks:   #defining the task attribute in here 
            - name: using the variable using the debug module in here  
              debug:   #usiing the debug module in this case 
                var: some_key  # here accessiung the variable using the var paramter 

        ...

        # here while executing this ansible_playbook we have to provide 2 different named vault with their password to be prompted as below 
        ansible-playbook --vault-id ext@prompt --vault-id ssh@prompt vault_playbook.yaml
        # here we are using the `--vault-id ext@prompt` for prompting the vault password for ext named vault 
        # here we are using the `--vault-id ext@prompt` for prompting the vault password for ssh named vault 
        
        # we can see the output as below 
    
        Vault password (ext): # asking for the ext name vault pass
        Vault password (ssh): # asking for the ssh named vault pass

        PLAY [linux] *************************************************************************************************************************************************************************

        TASK [Gathering Facts] ***************************************************************************************************************************************************************
        ok: [centos1]
        ok: [centos2]
        ok: [ubuntu3]
        ok: [centos3]
        ok: [ubuntu1]
        ok: [ubuntu2]

        TASK [using the variable using the debug module in here] *****************************************************************************************************************************
        ok: [centos1] => {
            "some_key": "some_value"
        }
        ok: [centos2] => {
            "some_key": "some_value"
        }
        ok: [centos3] => {
            "some_key": "some_value"
        }
        ok: [ubuntu1] => {
            "some_key": "some_value"
        }
        ok: [ubuntu2] => {
            "some_key": "some_value"
        }
        ok: [ubuntu3] => {
            "some_key": "some_value"
        }

        PLAY RECAP ***************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
            
    
    
    ```

- **Case07**
  
  - as a part we can also `encrypt the entire playbook script`  as well using the `ansible-vault`

  - we can use it as below if we want to encypt the `vault_playbook.yaml` file

    ```
        ansible-vault encrypt --vault-id playbook@prompt  vault_playbook.yaml
        # here we are trying to encrypt the entire the ansible playbook in here 
        # here we are using the --vault-id with the named vault as playbook
        # we cansee the output as below for this 
        # here lets suppose we are providing the password as `prateek` over here
         
        New vault password (playbook): 
        Confirm new vault password (playbook): 
        Encryption successful
    

    ```

- now  if we want to use this playbook then we need `3 things`
  
  - `--vault-id for the ext named vault`
  
  - `--vault-id for the ext named vault`

  - `--vault-id for the ext named vault`

- we can execute the playbook as below 

    ```
        ansible-playbook --vault-id ext@prompt --vault-id ssh@prompt  --vault-id playbook@prompt vault_playbook.yaml
        # here this will prompt for the ext named vault password
        # here this will prompt for the ssh named vault password
        # here this will prompt for the playbook named vault password
        # after hthat we can see the output 

        Vault password (ext): 
        Vault password (ssh): 
        Vault password (playbook): 

        PLAY [linux] *************************************************************************************************************************************************************************

        TASK [Gathering Facts] ***************************************************************************************************************************************************************
        ok: [centos1]
        ok: [centos3]
        ok: [centos2]
        ok: [ubuntu3]
        ok: [ubuntu1]
        ok: [ubuntu2]

        TASK [using the variable using the debug module in here] *****************************************************************************************************************************
        ok: [centos1] => {
            "some_key": "some_value"
        }
        ok: [centos2] => {
            "some_key": "some_value"
        }
        ok: [centos3] => {
            "some_key": "some_value"
        }
        ok: [ubuntu1] => {
            "some_key": "some_value"
        }
        ok: [ubuntu2] => {
            "some_key": "some_value"
        }
        ok: [ubuntu3] => {
            "some_key": "some_value"
        }

        PLAY RECAP ***************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        centos3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
        ubuntu3                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
    
    
    ```



