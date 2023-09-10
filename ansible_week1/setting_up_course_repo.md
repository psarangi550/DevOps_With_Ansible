# <ins> Setting up Ansible Code Repo </ins> #

- we can go to the `github repo` with the address as `https://github.com/spurin/diveintoansible` and clone this report into `ansible control host `using the command as `git clone https://github.com/spurin/diveintoansible.git`

- `Ansible is a single tool` which is `False` because `Ansible is a toolset,comprising of many tools modules and Ansible is also an extensible framework`

- the core component of `ansible` being as 

    - `modules`
    - `ansible executable`
    - `ansible playbook executable`
    - `inventories`
  
  many more 

- we can use `target type` as below for ansible 
  
  - `host`
  - `network switchs`
  - `storage arrays`
  - `container`

- when we re using the `SSH` during the `secure channel configuration` what `algo` used for creating the `symmetric key`
  
  - `the diffie hellman algorithm` the algoritm from the `1970` thats been published by `whitfield Diffie and Martin Hellman`


- in the `.ssh` directory `we can find below file `such as 
  
  - `private key`
  - `public key`
  - `known_hosts`
  - `authorized_keys`

- the `ssh-copy-id ` command will help in putting the `public key of the trusted host` to the `authorized_keys file of the target host`

- which `SSH-Option` automatically accept the `unknown Host Key Fingerprint`
  
  - `StrictHostKeyChecking=no ` which can be mentioned as `ssh -o` or `ssh-copy-id -o` option which will help in accepting the `inknown host key fingerprint acceptance`

- in case of `ansible -i,ubuntu1 all -m ping` what does the `-i` and `-m` command represent 

    - here the `-i` command represent the `inventory` where we can specify the `inventory file` or with the option as `-i,` we can also specify the `list of host i.e target host`
    
    - the `-m` stands for the `module` here we are using the `ping module` which will respond as `pong` on `successfull passwordless communication`






