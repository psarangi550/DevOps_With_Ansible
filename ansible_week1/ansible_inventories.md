# <ins> Ansible Inventories </ins> #

- `Ansible Inventories` :- 
  
  - `what they are ?`

  - `how they are used ?`


- different type of `ansible inventories`

- we will be seeing `how to provide connectivity as root` to our `centos target host`

- provide `ansible connectivity` to out `ubutu target host` using `sudo`

- `inventory host variables` also known as `hostvars`

- how to `simplify our inventory with the help of host ranges `

- how to `applying` the `group variables` also known as `groupvars` to `improve` the `inventory` further 

- what is `inventory children group` and how `these can be of use`


# <ins> Ansible Inventory </ins> #

- we need to check that the `centos1` is `pingable` by using the command `ping centos1`

- here if we are going to the folder `01` then we can see the `ansible.cfg` which is the `configuration file that ansible refer`

- in that `ansible.cfg` file we have the section as below 


    ```
        ansible.cfg
        ------------

        [defaults]
        inventory = hosts

        # here the inventory refer to the `hosts` which will be filename relevant to the path mentioned against the inventory path 
    
    ```

- the `hosts` file been formated by using the `INI` format 

- here we can see that the content of the `hosts` file is as below 

    ```
        hosts
        -----

        [all]
        centos1 # target host we want to connect can be mentioned in here 

        # here we should not specify the `[all]` because all the `host mentioned in hosts file` will going to add to the `"all" target group`
        # all the hosts mentioned in the hosts file will be added to the `all target group` regardsless which group they are in 

    
    ```

- all the `hosts` mentioned in the `hosts file` will be added to the `all target group` in `ansible` regardsless which group they are in 

- if we have the `known_hosts` file in `/home/<user>/.ssh/known_hosts` file containing the `details about the centos1 target host`

- now if we try to ping to that `centos1` then we can see the below command and output 

    ```
        # go to the folder where the hosts and ansible.cfg file being present 
        
        # then we can use the command as below
        ansible all -m ping
        # here all being the target group that we mentioned in the `hosts` file with the value of `centos1`
    
    ```

- if remove the `known_hosts` file present in the `/home/<user>/.ssh/known_hosts` file using the `rm /home/<user>/.ssh/known_hosts`

- now when we are trying to connect to the `ansible all group` then it will try to `established a secure connection and ask for the fingerp[rint validation`

- if we deny the ` target fingerprint match` then in that  case we will be getting the error as `User interupted execution` when we use the command as `ansible all -m ping`

- but we can ignore the `StrictHostKeyChecking=no` using the command as `ANSIBLE_HOST_KEY_CHECKING=False` environment variable 

- if we are doing this and we don't have the `known_hosts file` in the `/home/<user>/.ssh/known_hosts` ,eben though the `ansible host` trying to connect to the `target host using the ssh secure connection` it will not be prompted to verify the `target fingerprint` option out in here 

- we can also `create this env variable` which is of `ANSIBLE_HOST_KEY_CHECKING=False` and exeute the `ansible command` using the `linux system` using the command as 


    ```
        ANSIBLE_HOST_KEY_CHECKING=False ansible all -m ping
        
        # this will provide the successful pong response because on the background the known_hosts file again be recreated where the fingerprint been auto accepted       
        # we can place the variable before the command we want to execute and use those variable that variable will be used for the single command before where we specify the command 
    
    ```

- even though this `ANSIBLE_HOST_KEY_CHECKING` is convinient but we don't want to specify the same in every command where we want to connect to a host

- to make this permanent we can add an entry to the `ansible configuration file` which is the `ansible.cfg` file in this case 

- we can add an additional entry to the `ansible config file i.e ansible.cfg file` with a command as `host_key_checking=False`

- we can refine the `ansible.cfg file` as below 

    ```
        ansible.cfg
        -----------

        [defaults]
        inventory=host
        host_key_checking=False
    
    ```

- if we remove the `known_host` file from the location of `/home/<user>/.ssh/known_hosts` using the command as `rm -rf /home/<user>/.ssh/known_hosts` and trying to connect to `all group` using the `ansible ping module` then we can see the `known_hosts` file will be created on the `background` as we have put the `host_key_checking=False` to the `ansible.cfg file`

- when we use the command as `ansible all -m ping` then we can see the `pong` response as we are `successfully connect to the target group host with fingerprint accepted automatically`

- we can also define the `multiple target hosts` as `inventory` in the `hosts` file which been stating the `host file` as below 

- here we are trying to connect to multiple `target host` which can be defined in the `hosts file` which being referenced by the `ansible.cfg` by putting the `inventory=hosts`

    ```
        hosts
        ------

        [ubuntu] #defining the ubuntu group in here 
        ubuntu1 # defining the host ubuntu1 over here
        ubuntu2 # defining the host ubuntu2 over here
        ubuntu3 # defining the host ubuntu3 over here

        [centos] #defining the centos group in here 
        centos1 # defining the host centos1 over here
        centos2 # defining the host centos2 over here
        centos3 # defining the host centos3 over here
    

    ```

- here the `key thing to remeber` is that `all host` mentioned in `any group` will be added to the `all tartget group`

- also we need to keep in mind that we can ping on bais of the `individual group` as well using the command as `ansible <individual group> -m ping`

- here we can use it as `ansible ubuntu/centos -m ping` if we want to check the particular `target group` connection using the `ansible` command using the module as `ping`

- its `worth noting that this can also be referred` to with the `wildcard symbol` as well like below 

    ```
        ansible u*/c* -m ping 

        # here we are using the individual group as the wildcard inorder to ping to target group
        # we can also use the `al*` to ping to the `all group as wild card`
    
    
    ```

- but its recomended to `provide quotes` while using the `wildcard` aos we can also it as below , otherwise it will be seen as `listing of files`


    ```
        ansible "u*"/"c*" -m ping 

        # here we are using the individual group as the wildcard inorder to ping to target group
        # we can also use the `"a*"` to ping to the `all group as wild card`

        # we can also do such as below 
        ansible "*" -m ping

    
    ```

- if we are using the `-o` option which can provide the `one line condensed view which will be useful`

- we can use the command as `ansible -o "*" -m ping / ansible "*" -m ping -o ` which will give the `one line condensed view of the output `

# <ins> How to Query Inventory Details using the Ansible Terminal </ins> #

- the `inventory or target host` that we have can be queries using the `ansible command line`

- we can list all the `target host` present inside the `centos target group` using the command as below 


    ```

        ansible <group name> --list-hosts
        # this command will group all the target host present in the host file which comes under the particular target group 
        
        Ex:-
        # we can use the comand such as below
        ansible ubuntu/centos/all --list-hosts
        # this command will give all the host reside under the specific target group or all if we provided all as the target group


        # the output will be off as below if we are using the command against the all target group

        hosts (6):
        ubuntu1
        ubuntu2
        ubuntu3
        centos1
        centos2
        centos3

    
    ```

- we don't have to specify the `target group` rather we can use the `target host` over here as below  

    ```
        #syntax
        ansible <target host> --list-host

        #ex:-
        ansible ubuntu1 --list-hosts

        # which can provide the output as below
         hosts (1):
            ubuntu1
    
    ```

- we can also use the `individual host` can be also applied to the `module we are using the -m option` , on the preveious example it will be off `ping module`

- we can use the command as `ansible <target host> -m ping -o ` this will be ble to help us in fetching the `whether we are able to reach to the target host or not`

    ```
        # here we can use the individual target host as below 
        ansible <target host> -m ping -o
        #ex:-
        ansible centos1 -m ping -o

        # the output will be as below 
        centos1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
    
    ```

- we can also use the `ping module` with the `wild card pattern` using the `~` symbol in here which can be used for the `pattern matching`

- we can use this command with the `regular expression` as below in this case over here

    ```
        #syntax
        ansible ~ <regular expression> -m ping -o

        #ex
        ansible ~.*1$ -m ping -o
        ansible ~cent.*1$ -m ping -o
        ansible ~^cent.*1$ -m ping -o
    
    ```

- here in the `regular expression` the `.` means any `character alphanumeric or non alphanumeric`

- here in the `regular expression` the `*` means `Any nummber of preveious including 0` i.e `any number of any character `

- here we can mention the `regular expression` the `$` means `endswith` and `^` means starts with

- we can also utilize this in order to fetch the `host as well from a target group or target host`

    ```
        #syntax
        ansible ~ <regular expression> --list-hosts

        #ex
        ansible ~^ce.*3$ --list-hosts

    ```

- here at this point our `ansible host client` can connect to `set of target host spread on implicit target group as well as explicit target group as well as specific target host`

- but `ansible` will not be able to `do much based on lavel of access it has over the remote server or target host`

- ideally we need  `ansible to have escalated access i.e root privileges`

- earlier we have configure the `both ansible and root user access` while setting up the `ssh key` in the `ssh key instruction using the for loop`

- so that we can connect the `ansible host` to the `remote system/ target host` using the `root privileges or root user`

# <ins> Connecting the Ansible Host to Target Host using the Root Privileges </ins> #

- in order to connect the `ansible host client` to connect to the `remote system / target host` as the `root user` we need to use the `ansible host variable or hostvars`

- we can specify the `ansible_user=<user that we want to login>` alongside the `target host` in the `hosts` file as below 

- here in this case the `ansible_user` is the `anbsible host variable or hostvars` alongside the `target host`

- here the `ansible_user` the `hostvars` specify the `user we will use to login` will be off `root/ansible user based on what specified against it`

    ```

        hosts
        -----
        
        [centos]
        centos1 ansible_user=root # here we are using the hostvars as ansible_host alongside the target host
        centos2 ansible_user=root # here we are using the hostvars as ansible_host alongside the target host
        centos3 ansible_user=root # here we are using the hostvars as ansible_host alongside the target host

        [ubuntu]
        ubuntu1
        ubuntu2
        ubuntu3
    
    
    ```

- on the `preveious version of the ansible` we will have to use the `ansible_ssh_user=<user that we want to login>` alongside the `target host`

- now if we run the `ping module with one line option` as below then we can see the output as 

    ```
        # here we are using it against the centos explicit group that we specified as below 
        ansible centos -m ping -o

        # the o/p will be off 
        centos2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
    
    
    ```

- but this `ping module` that we are using the `ansible module` will not be `suffice`  to provide the `option which user been loggin in`

- hence we need to switch it to a different `module` and cheeck the `UID` thats been used  while checking in (for the root user the `UID` will be -0 and for other it can be verified by doing `echo $UID`)

- or we can see the `id` command on the `command line` which will provide the `UID and GID` info along with that it will provide the info about the `groups` and `sudo` info along with the `user info in bracket`

- for the `ansible and root user` the value can come as below 

    ```
        id # if we run the id command then we can see the below info for root user of ansible host client 
        # uid=0(root) gid=0(root) groups=0(root)

        # but if ruin the same command for the ansible user then we can see the info as below
        id
        #uid=1000(ansible) gid=1000(ansible) groups=1000(ansible),27(sudo)

    ```

# <ins> Using the Ansible command module to verify ansible able connect to the remote server or target host using the root UID rather than ansible UID </ins> #

- here we will use the `another module` as the `command module` which will provide the info such as below with the `args` as the `id`

- we the command we can use is as 

    ```
        ansible <target group/all/target host> -m command -a <args as command we want to use>
        
        # here we are using the command as `id` in this case 
        # hence the command constitute as below 

        ansible centos -m command -a id
        # here we are using the `command module` with the `-m` option 
        # here we are using the args as `-a` option in here 
        # on the centos target group we are applying 
        
        # we can also use the `-o` option to see the one line result 
        ansible centos -m command -a id -o 

        # hence the result will show the result as below
        centos1 | CHANGED | rc=0 | (stdout) uid=0(root) gid=0(root) groups=0(root)
        centos3 | CHANGED | rc=0 | (stdout) uid=0(root) gid=0(root) groups=0(root)
        centos2 | CHANGED | rc=0 | (stdout) uid=0(root) gid=0(root) groups=0(root)

        # but if we run the same command for the ubuntu target grouo where we have not specified the ansible_user hostvars then the output will be as below 
        ansible ubuntu -m command -a id -o 

        # the o/pp will be as below
        ubuntu1 | CHANGED | rc=0 | (stdout) uid=1000(ansible) gid=1000(ansible) groups=1000(ansible),27(sudo)
        ubuntu3 | CHANGED | rc=0 | (stdout) uid=1000(ansible) gid=1000(ansible) groups=1000(ansible),27(sudo)
        ubuntu2 | CHANGED | rc=0 | (stdout) uid=1000(ansible) gid=1000(ansible) groups=1000(ansible),27(sudo)
    
    ```

- we here use the `ansible command` using `ansible` command with the `command module` to check the `user we logged in the remote server/target host` using the command args as `id`

- the command args provided  against the `command module` wiull be executed against the `remote server / target host` where we want to connect using the `ansible` command 

- its recomend to provide the `quotes` while providing the command args as below

    ```
        ansible <target group/all/target host> -m command -a "<args as command we want to use>"
        # here we are providing the command args as within the `quotes` symbol over here
        
        # here we are using the command as `"id"` in this case 
        # hence the command constitute as below 

        ansible centos -m command -a "id"
        # here we are using the `command module` with the `-m` option 
        # here we are using the args as `-a` option in here 
        # on the centos target group we are applying
        # here we are defining the command args as `quotes in here`  
        
        # we can also use the `-o` option to see the one line result 
        ansible centos -m command -a "id" -o 
        # # here it with the quotes where we are providing the command line args

        # hence the result will show the result as below
        centos1 | CHANGED | rc=0 | (stdout) uid=0(root) gid=0(root) groups=0(root)
        centos3 | CHANGED | rc=0 | (stdout) uid=0(root) gid=0(root) groups=0(root)
        centos2 | CHANGED | rc=0 | (stdout) uid=0(root) gid=0(root) groups=0(root)

        # but if we run the same command for the ubuntu target grouo where we have not specified the ansible_user hostvars then the output will be as below 
        ansible ubuntu -m command -a "id" -o 
        # here it with the quotes where we are providing the command line args

        # the o/pp will be as below
        ubuntu1 | CHANGED | rc=0 | (stdout) uid=1000(ansible) gid=1000(ansible) groups=1000(ansible),27(sudo)
        ubuntu3 | CHANGED | rc=0 | (stdout) uid=1000(ansible) gid=1000(ansible) groups=1000(ansible),27(sudo)
        ubuntu2 | CHANGED | rc=0 | (stdout) uid=1000(ansible) gid=1000(ansible) groups=1000(ansible),27(sudo)
    
    
    ```

- the `ansible command module` will run the `command` on the `remote host` using the `ansible` executable with the `inventory` we have provided against it 

- when we use the `command` module we can provide the `args as command args with quote` which will be executed on the `remote host` using the `ansible command` with specific `inventory info` we mentioned against it 

- `command` is a `default module` in `ansible` so we can use it without the `-m command` option while using it with `ansible executable`

- Although in the `Ansinble Lab Env` that we setup we can have the `direct access to the root of the target system` , But in the real world its ideal to `restrict direct root access` and login as `mortal user` to the `remote system`

- once we able to login as the `mortal user / normal user` then we can escaled then to the `super user privileges`

- ansible also able to cover this aspect as well , we can use the `hostvars` as `ansible_become=true` and `ansible_become_password=<password>` alongside the `target host` in the `hosts` file 

- this will then help in `using the sudo command as the ansible user` when `ansible` try to connect to the `remote host` and then use the `sudo` command for which the `password` being required 

- we can define the hosts file as below 

    ```
        hosts
        -----

        [centos] # this is the centos target group that we have specified  
        centos1 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection 
        centos2 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection 
        centos3 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection 

        [ubuntu] # this is the ubuntu target group that we have specified 
        ubuntu1 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 
        ubuntu2 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 
        ubuntu3 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 
    
    ```

- now when we use the command as `ansible all -a "id" -o` as the `command module` is the `default module inside the ansible` this can check by running the command `id` as the `ansinble user` using the `sudo` command as `sudo id` for which password being required on the `remote system or target hosts`

# <ins> connecting to the Target Hosts from Ansible Host Using different ssh ports </ins> #

- here in the picture all the system(`including the ansible host and target hosts`) being using and running the `ssh daemon` on the port `22` as standard 

- however the `system` can run the `sshd service` on alternate port as well 

- whatif one of the `target host (lets say centos1)` running the `sshd service` on port `2222` as below  and the `image` to `#image: spurin/diveintoansible:centos-sshd-2222`

- we can do that by editing the `docker-compose.yml` file as below 

    ```
    
        centos1:
            hostname: centos1
            container_name: centos1
            # image: spurin/diveintoansible:centos
            image: spurin/diveintoansible:centos-sshd-2222
            ports: 
            #  - ${CENTOS1_PORT_SSHD}:22
            - ${CENTOS1_PORT_SSHD}:2222
            - ${CENTOS1_PORT_TTYD}:7681
            privileged: true
            volumes:
            - ${CONFIG}:/config
            - ${ANSIBLE_HOME}/shared:/shared
            - ${ANSIBLE_HOME}/centos1/ansible:/home/ansible
            - ${ANSIBLE_HOME}/centos1/root:/root
            networks:
            - diveinto.io
    
    ```


- now when we try to connecct to the `centos1` `target-host or remote-system` then we will end up getting the error as below 

    ```
        ansible centos1 -a "id" -o
        # using the centos1target host using the command module which is the default module with the args to execute as `"id"`
        
        # when we are using this then we will get the out put as below 
        centos1 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host centos1 port 22: Connection refused
    
    ```

- here the `ansible` try to communicate to the `target host` using the port `22` which is the `default port for SSH`

- but we can add a `hostvars` named as `ansible_port=<sshd port of the remote server or target host>` alongside the `target host` in the `hosts` file which is an `inventory file`

- here we can write the `hosts/inventory` file as below 

    ```
        hosts
        -----

        [centos] # this is the centos target group that we have specified  
        centos1 ansible_user=root ansible_port=2222 # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection and using the `ansible_ports` hostvars which can be utilized as the `sshd port that is configured for the remote server` on which the `ansible host client` try to connect 
        centos2 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection 
        centos3 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection 

        [ubuntu] # this is the ubuntu target group that we have specified 
        ubuntu1 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 
        ubuntu2 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 
        ubuntu3 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 

    
    ```

- now when we run the command as `ansible all -m ping -o` in order to `ping` to `remote server` which been `running over a different sshd port` then `also we are able to connect to the same`

- we can also able to specify the `port` alongsside the `hosts` that we uses as below 

    ```
        hosts
        -----

        [centos] # this is the centos target group that we have specified  
        centos1:2222 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection  and using the sshd port against the target host directly which can help in connectiong to the required sshd ports 
        centos2 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection 
        centos3 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection 

        [ubuntu] # this is the ubuntu target group that we have specified 
        ubuntu1 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 
        ubuntu2 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 
        ubuntu3 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 
    
    
    
    ```

- now also when we try to connect to the `remote host where the sshd service been running over port 2222` then we can also amend the `hosts/inventory` file as below where we specify the `sshd port` the `target host` been using the format as `<target host>:<sshd port>` in the `hosts/inventory file`

- we can add the `control` group as the `target group` and we specified the `ubuntu-c ansible_connection=local` where the `ubuntu-c` is the `ansible client host` and using the `hostsvars` as `ansible_connection=local`

- when we write the `control group` with the info about the `ansible_connection=local` against the `ansible host` then there is `no transport meachanism (like SSH)` required for the same

- now when we write the hosts file as below 

    ```
        hosts
        ------
        
        [control] # here using the control group
        ubuntu-c ansible_connection=local # defining the ansible_connection=local hostvars against the ansible host which can make sure no `transport mechanism like ssh connection` will be applied


        [centos] # this is the centos target group that we have specified  
        centos1:2222 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection  and using the sshd port against the target host directly which can help in connectiong to the required sshd ports 
        centos2 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection 
        centos3 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection 

        [ubuntu] # this is the ubuntu target group that we have specified 
        ubuntu1 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 
        ubuntu2 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 
        ubuntu3 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 
    
    
    ```

- noww when we use the command as `ansible all -m ping -o` then that will show the info with the info of the `ubuntu-c` machine as well which was not preveiously displaying 

- we can use the command as 

    ```
        ansible all -m ping -o # using the ansible command as to ping to the target host

        # but as we have mentioned the ansible_connection=local hence no transport going to happen hence the output will be as 
        # here it also show the result for the ansible_hosts as the ansible_connection=local and ubuntu-c will be displayed as inventory

        ubuntu-c | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        centos1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        ubuntu1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}

    ```

# <ins> How to Use the Hosts ranges in order to Simplify the inventory/hosts file in Ansible </ins> #

- we can see some commanalities between the `target host` belong `same target group` i.e `commonalities can be fetched between the trget host(ubuntu1,uuntu2,ubuntu3) in the ubuntu(target group)`

- we can see the same commonalties beterrn the `centos target host present in the centos target group` which can be seen as below 

- here we can use the `host ranges` to simplify the `host/inventory file` as below 

    ```
        hosts
        -----

        hosts
        ------
        
        [control] # here using the control group
        ubuntu-c ansible_connection=local # defining the ansible_connection=local hostvars against the ansible host which can make sure no `transport mechanism like ssh connection` will be applied


        [centos] # this is the centos target group that we have specified  
        centos1:2222 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection  and using the sshd port against the target host directly which can help in connectiong to the required sshd ports 
        centos2 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection 
        centos3 ansible_user=root # here using the hostsvars as the `ansible_user` which will help in loggin in as root at the start of the connection 

        [ubuntu] # this is the ubuntu target group that we have specified 
        ubuntu1 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 
        ubuntu2 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 
        ubuntu3 ansible_become=true ansible_become_password=password # using the ansible_become and ansible_become_password as the hostvars which will help in getting the username and password where we login as the normal user later elevet to the root user using the sudo command 

        # but we can simplify the  inventory / hosts file as below 

        hosts
        -----

        [control] # here using the control group
        ubuntu-c ansible_connection=local # defining the ansible_connection=local hostvars against the ansible host which can make sure no `transport mechanism like ssh connection` will be applied

        [centos] # here using the centos target group in here 
        centos1:2222 ansible_user=root # defining the centos target host which can connect to sshd port 2222 and directly login as the root user while connecting 
        centos[2:3] ansible_user = root # connecting ro centos target host with port 22 and directly login as the root user while connecting 

        [ubuntu] # using the ubuntu target group in here 
        ubuntu[1:3] ansible_beome=true ansible_become_password=password # here using the ansible_beccome and ansible_become_password as the hostvars to connect it as the ansible user and later turned to the root user

        #Or we can write without comment as belowe 

        hosts
        -----
        [control] # here using the control group
        ubuntu-c ansible_connection=local


        [centos] # here using the centos target group in here 
        centos1:2222 ansible_user=root
        centos[2:3] ansible_user=root

        [ubuntu] # using the ubuntu target group in here 
        ubuntu[1:3] ansible_beome=true ansible_become_password=password

    
    ```


- here we are using the `hosts ranges` in order to make simple changes for the `inventory/hosts file` which can make easier to the `inventory file` where we can define it in ranges 

- but keep in mind that the `index of the hosts  ranges` starts from `1` not from `0`

- even if we want to `list` all the `target hosts` for a particular `target group` we can see the info as `ansible <target group/ target host> --list-hosts ` this will show all the required info as we have seen ealier 

- if we want to list host under the `all/ubuntu/centos` target group or `ubuntu1/centos1` target host the output will be as below 

    ```
    
        ansible <target group / target hosts> --list-hosts

        # here the value can be as below 
        ansible all/ubuntu/centos/ubuntu1/centos1 --list-hosts

        # example 
        ansible centos --list-hosts

        # the output will be as 
         hosts (3):
            centos1
            centos2
            centos3


    ```

- but as we have mentioned the `ansible_connection=local` when we list out the `all group target host` we can see the info about the `ubuntu-c` which been mentioned in the `control section`

    ```
        ansible all --list-hosts
        # here we can see the output as below including the control group
        # as all the group target host were added to the target group
        
          hosts (7):
            ubuntu-c
            centos1
            centos2
            centos3
            ubuntu1
            ubuntu2
            ubuntu3
    
    
    ```

- here we need to make an `exception` and have to define the `centos1` separately as weare using the `different ansible_port` for the `centos1 target hosts`

- but we can define the `ansible_port` as the `separate hostvars` or we can define with the `<target host>:<ansible ssh port>` as an alternatives


# <ins> Usage of groupvars for the Inventory files in Ansible </ins> #

- here we can see that the `ansible_user` being used multiple time in the earlier `hosts/inventory files` under the `centos` target group

- if we want remove the `duplicated ansible_user hostvars` then we can define the `groupvars` in this particular case 

- for this we can define the `host or inventory file as below`

    ```
        hosts
        -----

        [control] # using the control group here 
        ubuntu-c ansible_connection=local # here define the ansible_connection=local so that no transmission protocol will be allowed for the same 

        [centos]
        centos1:2222 # defining the target host with the ports thats been provided 
        centos[2:3] # defining the other host with the default ssh port as 22 

        [centos:vars] # here we are defining the group variable in this case 
        ansible_user=root # here defining the ansible_user host variable as group variable which will be used as the host variable against all the target host 

        [ubuntu]
        ubuntu[1:3] # defining the ubuntu target host over the ubuntu target group

        [ubuntu:vars] # defining the group vars for the ubuntu group over here 
        ansible_become=true # defining the group varaible which will be applied to each of the host under the specific host against which the variable being defined 
        ansible_become_password=password # defining the group varaible which will be applied to each of the host under the specific host against which the variable being defined 

        #Or without the comment we can write it as 

        hosts
        -----

        [control]
        ubuntu-c ansible_connection=local


        [centos]
        centos1:2222
        centos[2:3]

        [centos:vars]
        ansible_user=root

        [ubuntu]
        ubuntu[1:3]

        [ubuntu:vars] 
        ansible_become=true
        ansible_become_password=password
    
    
    ```


- here when we try to connect to the `ansible target host` using the command as `ansible all -m ping -o` then we can see the same response over here as well 

    ```
        ansible all -m ping -o
        # here defining the ping over here in this case 

        # the output of the file being 
        ubuntu-c | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        centos3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        ubuntu1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
    
    ```

- here `every host` under the `target group` will receive the `variable which been provided under the groupvars related to that group`

- we can define the `groupvars` as the `[<target group>:vars]` in the `inventory host ini file`

- here the `ansible_user` variable will be provided to `every host present in the centos target group` and `ansible_become and ansible_become_password` to be provided to the `every host in the ubuntu group`


# <ins> How to Define the Inventory child in Ansible </ins> #

- here if we are looking into the `hosts/inventory` files then we can see an `mixture of Linux OS (ubuntu and centos target hosts)` and in those target group we have the `target host such as (ubuntu1,ubuntu2,ubuntu3)(centos1,centos2,centos3)`

- it will be better if we distinguish them i.e. `ubuntu and centos` target group  into a `collective group` as both of them are the `variation of the Linux group`

- fortunately `ansible has the children declaration` which is useful to `define the parent linux  target group` which contains the `children declarative` as the `target group of ubuntu and centos`

- we can define that as below 

    ```
        hosts
        -----

        [control] # using the control group here 
        ubuntu-c ansible_connection=local # here define the ansible_connection=local so that no transmission protocol will be allowed for the same 

        [centos]
        centos1:2222 # defining the target host with the ports thats been provided 
        centos[2:3] # defining the other host with the default ssh port as 22 

        [centos:vars] # here we are defining the group variable in this case 
        ansible_user=root # here defining the ansible_user host variable as group variable which will be used as the host variable against all the target host 

        [ubuntu]
        ubuntu[1:3] # defining the ubuntu target host over the ubuntu target group

        [ubuntu:vars] # defining the group vars for the ubuntu group over here 
        ansible_become=true # defining the group varaible which will be applied to each of the host under the specific host against which the variable being defined 
        ansible_become_password=password # defining the group varaible which will be applied to each of the host under the specific host against which the variable being defined 

        [linux:children] # defining the children declarative for linux target group
        ubuntu #defining the child target group
        centos #defining the child target group

        #OR the child can be written as below without comment

        hosts
        -----
        [control]
        ubuntu-c ansible_connection=local


        [centos]
        centos1:2222
        centos[2:3]

        [centos:vars]
        ansible_user=root

        [ubuntu]
        ubuntu[1:3]

        [ubuntu:vars] 
        ansible_become=true
        ansible_become_password=password

        [linux:children]
        ubuntu
        centos

    ```

- here we can ping to the `parent target group` and `as the child target group are the part of it` hence we will be getting the `output for all the target host which is under the child target group`

- hence we can define this as below 

    ```
        ansible linux -m ping -o
        # defining the ping module for the linux parent group with one line option 
        # as linux is the parent hence we will be getting the output from the target child 
        # on the target child we have the ubuntu and centos child target group which contains the target host which will provide all the ping for the target hosts

        #hence the output for th same will be as 
        ubuntu-c | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        centos1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        ubuntu1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        centos2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}        
    
    
    ```

- we know that when we add the `host to the hosts/inventory file` that will be added to the `all target group`

- hence we can also define the `groupvars` on the `[all:vars]` level as well which will be applied to `all the host` in the `hosts or inventory file`

- we can define the `hostvars` as the `groupvars` inside the `[all:vars]` section which will be applied to the `all the hosts inside the hosts file`

- but if we define the `hostvars`  against the `target hosts` then that will get the `more preference` than the `hostvars which defined as groupvrs under the [all:vars] target group`

- then we can see that below example for the same 

    ```

        hosts
        ------
        [control] # here defining the control group over here
        ubuntu-c ansible_connection=local #definign the control group with ansible_connection=local to avoid the `transport call` rather doing the `local call in this case`


        [centos] #defining the centos target group
        centos1 ansible_port=2222 # definging the centos1 target host with ansible_port host variable=2222 which will preceed over the [all:vars] ansible_port=22 that define
        centos[2:3] # here defining the rest of the centos host in here

        [centos:vars] # here we need to define the group vars for the centos target group which will be applied as the hostvars for all the target host
        ansible_user=root # here also we define the ansible_user =root which will be applied to the all the target host as hostvars

        [ubuntu] #defining the ubuntu target group
        ubuntu[1:3] #deining thall the target host over here

        [ubuntu:vars] # here we need to define the groupvars for the ubuntu target group
        ansible_become=true # using the ansible_become which will be applied to all the target host as the hostvars
        ansible_become_password=password # using the ansible_become_password which will be applied to all the target host as the hostvars

        [linux:children] #definign the parent group having the children declarative
        ubuntu # defining the child target group ubuntu
        centos # defining the child target group centos

        [all:vars] # defining the groupvars for the [all:vars] target group
        ansible_port=22 # defining the groupvars which will be used as hostvars against all the host even in the `control group` here

    
    ```

-  if we define the `ansible_port=1234` which is a `invalid config` as the `target host were running on port 22 only the centos1 target host will be running on port 2222` then we can see that those config will be applied to all the `hosts` but if the `hosts` have the `native hostvars` then that will be preceeded over the `[all:vars]` group variable 

- if we ping the `linux` target group `having the ansible_port=1234` on the `[all:vars]` then all `ping connection` will going to fail but only the `centos1` going to be `success` becuse we have explicitly define the `ansible_port hostvars` against the `centos1` host

- we can see that `when we are pining to thr all group` then in that case `centos1 will be successful` because the `centos1` define the `hostvars ansible_port explicitly` , but we can also see the `ubuntu-c` will also be successful as we are not making any `ssh connection` rather we are making the `local connection by putting the anisble_connection=local` against it 

- below are the observation in regards to the same 

    ```
        ansible linux -m ping -o 
        # pinging to the linux parent group which in turn ping the children target group 
        # as we are pinging to the children target group then we can see that all the target host get pinged by it 
        # but as we are providing the [all:vars] groupvars with the value as `ansible_port=1234` which will be applied to all the host inside the child target group
        # hence everything fails to get the pong in response to the ping module but only centos1 will be successful
        # as we have discussed the centos1 define the `ansible_port=2222` explicitly then those will be overide the [all:vars] group variable 

        # the output can be disolayed as below 
        ubuntu1 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host ubuntu1 port 1234: Connection refused
        ubuntu2 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host ubuntu2 port 1234: Connection refused
        ubuntu3 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host ubuntu3 port 1234: Connection refused
        centos2 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host centos2 port 1234: Connection refused
        centos3 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host centos3 port 1234: Connection refused
        centos1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}


        ansible all -m ping -o 
        # pining the all host in this case both the ubuntu-c and all the rest of the hosts inside the `ubuntu and centos` target group specified 
        # here we try to ping as the centos1 has the `ansible_port` defined the that will overide the `[all:vars]` groupvars
        # then we can define the ubuntu-c in the control group with the `ansible_connection` hostvars hence that connection will be come as success as well 

        # the output in this case will be as 
        ubuntu1 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host ubuntu1 port 1234: Connection refused
        ubuntu2 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host ubuntu2 port 1234: Connection refused
        ubuntu3 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host ubuntu3 port 1234: Connection refused
        centos2 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host centos2 port 1234: Connection refused
        centos3 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host centos3 port 1234: Connection refused
        ubuntu-c | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        centos1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
    
    
    ```

# <ins> Applying GroupVars to Parent which will impact all of its children </ins> #

- we can also define the `groupvars` for the `custom target group` which we have declared as the `parent` for `some other target group`

- if we apply the `groupvars` to the `custom parent target group` then all its children also get the `groupvars as hostvars` if not specified `explicitly`

- if defined `explicitly` then that `hostvars` will take `precedence` over the declared `groupvars`

- we can define the `incentory/hosts` file as below 

    ```
        
        hosts
        ------
        [control] # here defining the control group over here
        ubuntu-c ansible_connection=local #definign the control group with ansible_connection=local to avoid the `transport call` rather doing the `local call in this case`


        [centos] #defining the centos target group
        centos1 ansible_port=2222 # definging the centos1 target host with ansible_port host variable=2222 which will preceed over the [all:vars] ansible_port=22 that define
        centos[2:3] # here defining the rest of the centos host in here

        [centos:vars] # here we need to define the group vars for the centos target group which will be applied as the hostvars for all the target host
        ansible_user=root # here also we define the ansible_user =root which will be applied to the all the target host as hostvars

        [ubuntu] #defining the ubuntu target group
        ubuntu[1:3] #deining thall the target host over here

        [ubuntu:vars] # here we need to define the groupvars for the ubuntu target group
        ansible_become=true # using the ansible_become which will be applied to all the target host as the hostvars
        ansible_become_password=password # using the ansible_become_password which will be applied to all the target host as the hostvars

        [linux:children] #definign the parent group having the children declarative
        ubuntu # defining the child target group ubuntu
        centos # defining the child target group centos

        [linux:vars] # defining the groupvars for the [linux:vars] target group which is  a `custom target group`
        ansible_port=22 # defining the groupvars which will be used as hostvars against all the child target group, if defined explicitly then will be ignored 


    ```

- we have defined the `ansible linux -m ping -o` then we can get the output as 

    ```
        
        ansible linux -m ping -o 
        # pinging to the linux parent group which in turn ping the children target group 
        # here as the vars been applied to the [linux:vars] then it will be applied to the `all the child target group and their host` if not defined explicitly
        # if defined explicitly then those will overide the groupvars defined in the [linux:vars] group

        # the output can be disolayed as below 
        ubuntu1 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host ubuntu1 port 1234: Connection refused
        ubuntu2 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host ubuntu2 port 1234: Connection refused
        ubuntu3 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host ubuntu3 port 1234: Connection refused
        centos2 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host centos2 port 1234: Connection refused
        centos3 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host centos3 port 1234: Connection refused
        centos1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}

    
    ```


# <ins> Defining the inventory hosts as YAMLS and JSON File </ins> #

- untill now we see the `inventory` files are in the `ini` format 

- but the `inventory` can be in the format of `YAML or JSON` as well , but we need to reference that `in the ansible.cfg` file which present alongside of that 

- we can see the `ansible.cfg` file as 

    ```
        ansible.cfg
        ------------

        [defaults]
        inventory=hosts.yaml / hosts.json
        host_key_checking=False
    
    ```

- we can define the `hosts.yml` file which is the `inventory` file as below 

    ```
        hosts.yaml
        -----------

        --- # we need to define the start with the `---` i.e `3 dashes`
        
        control: # here these are the target group which should be on the first
            hosts: # here we need to define the declarative keyword suchas hosts
                ununtu-c: # defining the ubuntu-c as the target-host and every target host should end with `:` although they don't have any hostvars or not 
                    ansible_connection: local #defining the hostvars in here which will be in key:value format

        centos: # here these are the target group which should be on the first which is centos
            hosts: # defining the hosts declarative keyword in here 
                centos1: # defining the centos1 target hosts in here with the `:` 
                ansible_port : 2222 # defining the hostvars in here which will be in key:value pair
                centos2: # defining the other target host with `:`
                centos3: # defining the other target host with `:`
            vars: # here we can define the `groupvars` which will applied as `hostvars` to all the `host` if not specified explicitly
                ansible_user=root # defining the groupvars in the key:value format

        ubuntu:  here these are the target group which should be on the first which is ubuntu
        hosts: # defining the hosts declarative keyword in here 
            ubuntu1: # defining the other target host with `:`
            ubuntu2: # defining the other target host with `:`
            ubuntu3: # defining the other target host with `:`
        vars: # definign the groupvars over the vars keyword declarative 
            ansible_become: true #defining the groupvars in the key:value format
            ansible_become_password: password # defining the groupvars in the key:value format

        linux: # defining the linux target group which is the parent target group
            children: #defining the children keyword declarative
                ubuntu: #defining the ` child target group` with the `:` symbol
                centos: #defining the ` child target group` with the `:` symbol

        all: #defining the target group as all 
        vars: #defining the groupvars declarative directives over here
            ansible_port: 22 # defining the group vars as hosts vars which will be applied to all the hosts 

        ... # we need to define the end with the `...` i.e `3 dots`
    
    
    ```

- we need to start the `hosts.yaml` with the `3 dash(---)` and end it with `3 dots(...)` for the `yaml inventory file`

- these `--- and ...` are `not mandetory` for the `yaml inventory file` recomended to put that through

- we need to define all the `target-group` as the `root of the indent declaration`

- these should contains the `keyword declartive` which can contains the `target host` with `: symbol` which can contain the `hostsvars` as the `key:value` pair

- then we can also provide the `group vars` as the `vars` which is a  `keyword declarative directive` which can be utilized with to specify the `groupvars` in `key:value` format which can be used as the `hostvars` if we don't specify the `hostvars explicitly`

- individual `hostvars` can declared under the `target host` individually explicitly as well 

- now when we ping the `ansible all -m ping -o` we can get the repsonse as below which is same as earlier

    ```
        ansible linux -m ping -o
        # here we are pinging to the linux custom target group which has child target group and their target hosts
        # here we will get th response as below in this case 
        ubuntu3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        centos1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}

        #or here we can define the all target hosts as well where it will include the ubuntu-c target machine as well 
        ansible all -m ping -o
        ununtu-c | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        centos1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
    
    
    ```

- we can also define the `inventory file` as the `JSON file` as well , for which we can conver the `yaml file into the json file using python` in command line or writing the script 

    ```
        yaml_to_json_convertor.py
        --------------------------
        import yaml #importing the yaml module
        import json #importing the json module

        with open("hosts.yaml") as yml_file: # opening the yaml file
            with open("hosts.json","w") as json_file: # opening the json file
                json.dump(yaml.load(yml_file,Loader=yaml.FullLoader),json_file,indent=4) # converting the yaml to the dict and then to json usiong the json and yaml module
                # here the FullLoader as an loader we are using for the yaml file too provide the quotes to the json file

        
        # or we can exeute a simple python command as below 
        # python command
        python3 -c 'import sys,json,yaml;json.dump(yaml.load(sys.stdin,yaml.FullLoader),sys.stdout,indent=4)' < hosts.yaml > host1.json
        # here the `-c` option will run the command from the python interpreter 
        # here we are using the sys module to get the input from the stdin of the yaml file and rediecting the stdout of the stream to the json file 

        # but we need to make sure in the ansible.cfg file the reference should made to the json file 
        
        ansible.cfg
        -----------  
        [defaults]
        inventory=hosts.json
        host_key_checking=False


    ```

- now we ping the `all hosts` we will get the output as be of same 

    ```
        #or here we can define the all target hosts as well where it will include the ubuntu-c target machine as well 
        ansible all -m ping -o
        ununtu-c | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        centos1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
    
    
    ```

- but remember as we are using the `JSON` which is a lottle bit `Scrict` hence we need to define the `target host with : null value` if there is `hostvars there or not` and same goes for the `target child group` as well we need to define by `:null` if no value are there 

- same like `yaml` the `hostvars and groupvars` mentioned with the `<key>:<value>` format

- and the json file will be in the format of 

    ```
        hosts.json
        -----------
        {
        "control": {
            "hosts": {
                "ununtu-c": {
                    "ansible_connection": "local"
                }
            }
        },
        "centos": {
            "hosts": {
                "centos1": {
                    "ansible_port": 2222
                },
                "centos2": null,
                "centos3": null
            },
            "vars": "ansible_user=root"
        },
        "ubuntu": {
            "hosts": {
                "ubuntu1": null, // defining the target host with the :null value as there are no values  
                "ubuntu2": null,
                "ubuntu3": null
            },
            "vars": {
                "ansible_become": true,
                "ansible_become_password": "password"
            }
        },
        "linux": {
            "children": {
                "ubuntu": null, // defining the target group with the :null value as there are no values
                "centos": null
            }
        },
        "all": {
            "vars": {
                "ansible_port": 22
            }
        }
    }
    
    ```

- in the `preveious example we changed the hosts file` on the `ansible.cfg` file but we can do the same changes on the `ansible command line` using the `-i or inventory option`

- when we define the `-i or inventory` command then takes `precedence over wht we have defined on the ansible.cfg` file 

- even though we have the `ansible.cfg` as the `inventory=hosts.json` but we can execute the `ansible command with -i option as below`

    ```

        ansible.cfg
        -----------  
        [defaults]
        inventory=hosts.json # here the inventoey will be of hosts.json
        host_key_checking=False
        # here defining the target fingerprint will happen  automatically

        # while executing the ansible command we can change the `inventory file` with the `-i` option which will overide what defined in the `ansible.cfg` file 
        ansible all -i hosts.yaml -m ping -o
        # here we are using the -i option and mentioning the incentoey as hosts.yml which will overide the incentory in the `ansible,cfg` file 
        # we need to make sue that file location priviusded against the -i or inventory option is right
        
        # hence we can define the output value as below 
        ununtu-c | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        centos1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}

        # we can eveb list the host using the command as 
        ansible all -i hosts.yaml --list-hosts
        #this willdefine the all the host belog to the all target group present in the hosts/.yaml rather than hosts.json define in ansible.cfg file
          hosts (7):
            ununtu-c
            ubuntu1
            ubuntu2
            ubuntu3
            centos1
            centos2
            centos3
    
    ```

- another command line option that we must need to know is the `-e` command which stands for the `extra variable`

- if we do the `ansible --help | grep more` the we can see the details 

- this `extra variable or -e` option will take the `extra args with the format for key=value format` or we can also provcide the `YAML or JSON file` with the `file name prepended as @ symbol`

- we can use the `extra variable or -e` option as below 

    ```
        ansible all -m ping -o -e ansible_host=12345
        # or 
        ansible all -m ping -o -e 'ansible_hosts=12345' # her e we are using the quotes
        # when we provide the extra variable tht will preceed over the `hostvars` whether they have defined in the  `groupvars or individually explicitly`
        # now when we execute the command we can get the output as below 
        ununtu-c | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu1 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host 0.0.48.57 port 22: Connection timed out
        ubuntu3 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host 0.0.48.57 port 22: Connection timed out
        ubuntu2 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host 0.0.48.57 port 22: Connection timed out
        centos1 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host 0.0.48.57 port 2222: Connection timed out
        centos2 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host 0.0.48.57 port 22: Connection timed out
        centos3 | UNREACHABLE!: Failed to connect to the host via ssh: ssh: connect to host 0.0.48.57 port 22: Connection timed out
    
    ```

- this `extra vars` can be able to overide the `variables` declared in the `inventory file`

- when we provide the extra variable tht will preceed over the `hostvars` whether they have defined in the  `groupvars or individually explicitly`

- we have defined the `ansible_port=2222`  explicitly for the `centos` target host , buyt if we deine the `-e ansible_port=12345` that will preceed over the `explicitly defined ansible_port=2222 under the target hosts`

- this `extra vars` if provided `against the all /specific target parent/child group` then that will apply to `all host(in case of all)/ specific target hosts(in case of parent /child target group  hosts variable )` 

- we can define thge `-e key=value` with thwe quotes as well as `-e "key=value"` which is recomended


#### TIP:-

- if other users were able to connect then we need to check the `known_hosts` file might be present on the `root user` then we can delete in order to see the `ansible` making `ssh connection` for the same
