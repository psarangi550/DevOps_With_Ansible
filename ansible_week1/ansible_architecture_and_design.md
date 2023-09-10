# <ins> Ansible Architecture And Design </ins> #

- here we will look into the 
  
  - `ansible configuration`
  
  - `ansible inventories`
    
    - how to `appy host` and `group variables`  
    
    - `how to simplify groups with ranges`

    - how to `configure` the `inventory` to `allow` `root connectivty` 
    
    - how to use the `ansible` with different `target configuration`

  - `Ansible module`

    - `common module those are available`
    
    - how to `interact` with `common module of ansible` and use them with the `ansible command line tool`
    

- **Ansible configuration**
  
  - `ansible` can make use of the `associate config file` where `ansible` will `make reference to` config file in regards to `how ansible will operate` and `resources that ansible uses`
  
  - we can start of by using the `ansible host` in here which is the `ubuntu-c` machine over here 
  
  - we can run the command as `ansible --version` on the `ansible hostclient i.e ubuntu-c system ` which will provide the below info such as 

    ```
        # ansible --version 
        # this command will geneate info such as below in this case 

        ansible [core 2.14.2] # this will show the ansible version that we have 
        config file = None # no config file reference 
        configured module search path = ['/home/ansible/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
        ansible python module location = /usr/local/lib/python3.10/dist-packages/ansible
        ansible collection location = /home/ansible/.ansible/collections:/usr/share/ansible/collections
        executable location = /usr/local/bin/ansible
        python version = 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] (/usr/bin/python3)
        jinja version = 3.1.2
        libyaml = True
    
    
    
    ```

- the `output` of the `ansible --version` can show different output in this case which can show the `ansible-base or ansible-core` version in this case

- we can un the command as `pip freeze | grep ansible` which will show the below info such as 
  
  - `ansible==<version>`
  - `ansible-core==<version>`

- `ansible-base or ansible-core` is a `core package` that provide the `ansible binaries and contains supporting file to execute ansible`

- `ansible package` provide the `individual module and plugin` thatvwere supported in `ansible-2.9`

- the `installation of ansible` will take care for the `ansible-base or ansible core and its dependencies`

- here we have the `config file = None` means the `ansible` not making any reference to the `config file`

- we can configure the `ansible config file` location as the `environment vriable` that `ansible can able to refer`

- we can find the `lowest priority ansible config file` present in the `/etc/ansible/ansible.cfg` configuration file which `being used when the ansible being  installed` using the `system installation` 

- if we are using the command as `sudo pt install ansible` then the `ansible being installed using the system installation` for the ubuntu system

- if we are using the `RHEL/centos/amazon Linux` which can install the ansible as `sudo yum install ansible or sudo dnf install ansible`

- the `su -` means `switch user` in the `linux command line`

- after `switch user` to the `root user` then we can create a `directory` using the command as `mkdir -p /etc/ansible` and create the `ansible.cfg` file using the command as `touch /etc/ansible/ansible.cfg` file in this case 

- the `touch` command will do `2 things`
  
  - create a `zero length` file 
  
  - updating the `timestamp` of a file to `current time` value in the `system`

- when we exit from the `root user` we will fallback to the `user through which we access the root user`

- now when we do the `ansible --version` then we can see the `config file` reference to the `/etc/ansible/asible.cfg` file 

- the `next priority of ansible config file` comes to the `user home directory i.e /home/<user>` hidden file which is `~/.ansible.cfg` file 

- now when we use the `ansible --version` now we can see that its been referencing to the below file 

    - `config file = /home/<user>/.ansible.cfg` when we use the command as `ansible --version` command 

- as long as we are logged in as the `user` then `ansible` will reference to the `config file ` from wherever the `ansible` being used

- even if we go to any other directory also it will still be reference to the `config file` in the `user home directory` file only

- when we use the `cd` command only it will take us to the `user home directory only which is /home/<user> directory`

- the `next priority` will come for the `/ansible.cfg` filewhich can be placed in the `current working directory` that we are using in this case 

- remeber here we are not creating the `hidden file` as `.ansible.cfg` rather we are crreating the normal file as `ansible.cfg` file 

- this `allow` to have the `ansible configuration file `along with your a`nsible execution` itself and both of them together consider as `one entity`

- the `number one` priority will go for the `ANSIBLE_CONFIG` which is the `environment variable` which been pointing to the `ansible config file as target`

- we can use any name for the `config` file in this case 

- we can create a `ansible config file` as `example-config.cfg` and set the `environment variable` as `ANSIBLE_CONFIG` for the same 

- now when we do the `ansible --version` then we can see the `config file=home/<user>/example_config.cfg`

- we will learn about the `config that can feed to the cofg file` in the coming videos


