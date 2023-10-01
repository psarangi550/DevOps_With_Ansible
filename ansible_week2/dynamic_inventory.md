# <ins> Dynamic Inventories </ins> #

- we will look into the `requirement` of `dynamic inventories`

- `how to create` `dynamic inventory` `with minimal scripting `

- `how to interrogate` a `Dynamic inventory`

- `performance enhancement` that could be `achieved` `using` `_meta` `within` the `dynamic inventory`

- the use of `ansible python framework` for `dynamic inventory`


- up until now we are using the `inventory of hosts` `defined` in the `ansible.cfg` file

- we can `associate` the `inventories` with both `inline groupvars and hostvars` defined in the `same inventory file`

- we can `associate` the `inventories` with the `hostvars and groupvars` defined in the repective `host_vars/<host> and group_vars/<host>` file as well

- we can also use the `-i` option define the `inventory files` while using the `adsible adhoc command`

- if that `inventory file` is `executable script(shell script/python script)` `ansible` will `use that as` the `Dynamic Inventory`

-  if that `inventory file` is `executable script(shell script/python script)` ansible will `execute the file` and use the `return content of the executable script` as the `inventory`

- `ansible has the ability` to `execute` the `dynamic inventory i.e executable script which been provided return content as the inventory` and `use the return content based on the context of the executable script,  as the inventory`


# <ins> Key Requiement for the Ansible Dynamic Inventory </ins> #

- the `key requirement` for the `dynamic inventory file` need to be `executable script file` , can be `written in any language` if `that can be executed from the command line`

- `Accept the command line option` of 

    - `--list `
  
    - `-- host <hostname>`

- `return` a `JSON encoded` `dictionary of inventory content` when used wit the `--list` option

- `return` a `JSON encoded` `dictionary structure` for the `--host <hostaname>` option 

# <ins> Writing the Dynamic Inventory Script </ins> #

- here `we have `the `example template of the dynamic inventory` which is `stored as inventory.py` which is a `python script`

- we have `removed all the references` from the `ansible.cfg` `regarding the info about` the `inventory host`

- here the `dynamic inventory which is the python script here` will `recreate` the `inventory` that we are `preveiously using`

- we can define the `example template of python executable script as below `

    ```
        inventory.py
        ------------

        #! /usr/bin/env python3 # using the shabang code over here

        from __future__ import print_function
        # this will make the script backward compatible with the python2 as well as the python3

        import argsparse # importing the argsparse module in here 
        import logging # importing the logging module in here 

        try:
            import json # importing the json module 
        except ImportError: # incase of ImportError which will be based on the python2
            import simplejson as json # importing the simplejosn as using it as json 

        
        class Inventory(object): #creating the Inventory class which is subclass of the object class 

            def __init__(self,include_list_hostvars) : # defining the constructor out in here 

                self.include_list_hostvars=include_list_hostvars # using the self to redeine the include_list_hostvars as the instance varible 

                self.command_option() #activating the logging functionality
                
                paeser=argsparse.ArgumentParser() # creating the ArgumentParser object to accept the command line option 
                
                #defining the argument as default argument that we are going to accept in here 
                parse.add_arguments("--list,action="store_true",help="list of inventories") # defining the list of inventories which we can get using the `--list` option

                # here defining the command line option as the --host in here 
                parser.add_arguments("--host",action="store", help="showing the hostvars from the hostname")

                self.args=parser.parse_args() # fetching the vlid argument using the self.args variable 

                if not (self.args.list,self.args.host): # if an invalid default command line args been provided 
                    parser.print_usage() # printing the invalid usage option in here 
                    return SystemExit # exiting the system in here 

                self.define_group_hostvar_arguments() # calling the instance method to initialize the self.group and self.hostvars i.e the groupvars and hostvars for both --list and --host option
                
                if self.args.list: # if the self.args provided as --list then we can see the below

                    self.print_json(self.list())

                    # here calling the self.print_json() to convert the dictionary to the JSON encoded dictionary 

                    # also we are calling the self.list() which will return the dictionary with and without hostvars based on the value of self.include_list_hostvars

                elif self.args.host: # if the self.args provided as --host then we can see the below

                    self.print_json(self.host())

                    # here calling the self.print_json() to convert the dictionary to the JSON encoded dictionary

                    # also we are calling the self.host() which will return the hostvars if the corresponding host been matched else return the empty dict as {}

            
            def define_group_hostvar_arguments(self): # this method will define the group of host as well as the hostvars for both --list and --host option

                # defining the groupvars in this case over here

                self.group={
                    "centos":{ #defining the centos target group in here
                        "hosts":["centos1","centos2","centos3"],
                        "vars":{
                            "ansible_user":"root" #defining the ansible_user groupvars as root
                        }
                    },
                    "ubuntu":{ #defining the ubuntu target group in here
                        "hosts":["ubuntu1","ubuntu2","ubuntu3"],
                        "vars":{
                            "ansible_become":True,
                            "ansible_become_password":"password"
                        }
                    },
                    "control":{ # defining the control host over here 
                        "hosts":["ubuntu-c"]
                    },
                    "linux":{
                        "control":["ubuntu","centos"]
                    }
                }

                # defining the hostvars in here which will help in defining the hostvars based on the target host

                self.hostvars={
                    "centos1":{ # defining the centos1 host here0
                        "ansible_port": 2222 #defining the hostvars as ansible_port in here
                    },
                    "ubuntu-c":{
                        "ansible_connection":"local" # defining the ansible_connection as local in here 
                    }
                }

            def print_json(self,content): #defining the method which convert the dict content to JSON

                # printing the json in nice pretty print format

                print(json.dumps(content,indent=4,sort_keys=4))


            def list(self) # defining the list method in here 

                self.logger.info("List Executed")

                if self.include_list_hostvars:

                    merged= self.group # assinging the dictionary to the merged dictionary in here 

                    merged["_meta"]={} # defining the _meta key which will contain the hostvars

                    return merged # returning the dictionary 

                else:

                    return self.group # returning the group of without the _meta info here 

            def host(self) # defining the host instance method in here 

                self.logger.info(f"Execueted for the Host {self.args.host}") #definingthe logger statement in here 

                if self.args.host in self.hostvars: # if the host ecist in the hostvars

                    return self.hostvars[self.args.host] # returning the hostvrs value for the spoecific host

                else:

                    return {} # returning the emptyu dict in here if the hostname not matched in the self.hostvars

            
            def command_option(self): #activating the log to the file in here 

                self.logger=logging.getLogger("ansible_dynamic_inventory") #defining the custom logger inn here

                self.hndlr=logging.FileHandler("/var/tmp/ansible_dynamic_inventory.log")

                # defining the file handler as the location of /var/tmp/ansible_dynamic_inventory.log value 

                # her we can't return to the StreamHandler as the return JSON being used by the ansible to get the inventory info

                self.formatter=logging.Formatter("%(asctime)s %(level)s %(message)s")

                # setting up the formatter in here 

                self.hndlr.setFormatter(self.formatter) # settng the formatter to the FileHandler 

                self.logger.addHandler(self.hndler) # here adding the handler to the logger

                self.logger.setLevel(level=logging.DEBUG) # defining the logger level as DEBUG in here 

        # now we can call the Inventory class with include_list_hostvars as below
        
        Inventory(include_list_hostvars=False) # using the Inventory class in here with the include_list_hostvars as False which will not provide the _meta key in the group of host

    ```

- the `dynamic inventory script` here `inventory.py` will going to `dynamically recreate the inventory` which we are `using preveiously`

- if we are running without the option as `--list or --host <hostname>` we will get the `usage message in return`

- but we run that with the `--list` option and the `include_list_hostvars` been set to `False` in  that case we will be getting the `groups containing the list of host as the JSON encrypted dictionary`

- if we run the command as `./inventory.py --list` here using the `--list` option then it will output the `group of host as the JSON encrypted dictionary`

- if we run as below 

    ```
        # if we run the inventory.py python script then we will get the output 
        ./inventory.py --list # here using the inventory.py file in here 

        # the output will be in the form of JSON encoded dict of self.group
        # here we can see the target group and their corresponding host and also the groupvars
        # also we have the linux parent of centos and ubuntu and those info also we can able to see 

        {
            "centos": {
                "hosts": [
                    "centos1",
                    "centos2",
                    "centos3"
                ],
                "vars": {
                    "ansible_user": "root"
                }
            },
            "control": {
                "hosts": [
                    "ubuntu-c"
                ]
            },
            "linux": {
                "children": [
                    "ubuntu",
                    "centos"
                ]
            },
            "ubuntu": {
                "hosts": [
                    "ubuntu1",
                    "ubuntu2",
                    "ubuntu3"
                ],
                "vars": {
                    "ansible_become": true,
                    "ansible_become_password": "password"
                }
            }
        }
    
    
    
    ```

- if we have the `hostvars` for the `particular host` then we can provide the `host against the --host option` with the `hostnme` as `host <hostname>`

- if the `hostvars` for the `particular host exist` then we can see the `corresponding hostvars` else we will be getting the `{} i.e empty dict` as the `response`

- for eample we know we have the `hostvars` of `centos1 target host` as `ansible_port` we can see the `infopp as below`

    ```
        # if we execute the script as below 
        ./inventory.py --host centos1

        # then we can see the corresponding hostvar JSON encrypted dict in here 
        {
            "ansible_port": 2222
        }


        # if we provided a host where don't have the host in the hostvars then we can see it as below 
        /inventory.py --host centos2

        # as the host doe not ecists in self.hostvars then we will get the empty dict as the return value 
        {}

    ```

- as long as the `executable script or dynamic inventory` as long as it accept the  `command line input with --list and --host <hostname>` then  `return` the `JSON encrypted inventory content or JSON encrypted data structure respectively` as the outcome then we can use that as the `dynamic inventory` with `ansible`

- we can specify the `-i option` and `inventory file` with the `ansible adhoc command` then we can use the `dynamic inventory` as below from the `ansible front`

    ```
        ansible all -i inventory --list-hosts
        # this will be run against all the target hosts
        # using the --lists host which will show all the host in the inventory.py file
        # here we are providing the inventory with the -i option out in here 

        # the output will be as 
         hosts (7):
            ubuntu-c
            ubuntu1
            ubuntu2
            ubuntu3
            centos1
            centos2
            centos3
    

    ```

- we can also use the `dynamic inventory script with the ping module to ping to all the target host` as below 

    ```
        # we can use  the dynamic host as below 
        ansible all -i inventory -m ping -o
        # here we are using the --one-line or -o option in here 
        # here also we are using the ping module against the -m option 
        # here we are targeting all the host 

        # the output JSON will be same as preveious 
        
        ubuntu-c | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        ubuntu3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        centos1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        ubuntu1 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"},"changed": false,"ping": "pong"}
        centos2 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
        centos3 | SUCCESS => {"ansible_facts": {"discovered_interpreter_python": "/usr/libexec/platform-python"},"changed": false,"ping": "pong"}
    
    ```

- we can `temporayly` disable the `logging` by commenting `over it and use it while debugging`

- the `action=strore_true` will store `True/False` based on the `--list option been provided or not`

- but for the `action=store` which will store the `value provided against the optional args` in here 

- when we use the `define_group_hostvrs` will actually define the `entirely inventory`

- we are `storing the group of host` and the `hostvars` `with the help of self` which will be a part of the `Inventory class only` and exist for each `Inventory object`

- the `print_json()` will output the `JSON enctypted dict which can help in troubleshooting and debugging` as well 

- we can't write the `logging message to the stdout` as the `stdout display the JSON which the ansible uses` and the `StyreamHandler can distort that the code will not run` , hence we are outputing to a `logger file`

- if we are  looking into the  `logging file` which been managed by the `FileHandler` then we can see that 




- even though we are using the `--list` option for `each of the host in the inventory.py` the `every host has been checked for the hostvars`

- when we use the `dynamic inventory with --list` option then we will getting the below output in the `logfile`

    ```
        # when we execute the command as below 
        ansible all -i inventory --list-hosts
        # then we can see the logger file s below 

        /var/tmp/ansible_dynamic_inventory.log
        ---------------------------------------
        2023-09-18 19:57:19,249 INFO list executed
        2023-09-18 19:57:19,291 INFO host executed for centos2
        2023-09-18 19:57:19,327 INFO host executed for ubuntu3
        2023-09-18 19:57:19,365 INFO host executed for ubuntu2
        2023-09-18 19:57:19,401 INFO host executed for centos1
        2023-09-18 19:57:19,435 INFO host executed for centos3
        2023-09-18 19:57:19,461 INFO host executed for ubuntu-c
        2023-09-18 19:57:19,488 INFO host executed for ubuntu1
    

    ```

- we can see the `even though we just provided the --list option` for `each of the host present in th inventory.py file hostvars host() will get executed` which takes `significant time`

- when we use the `--list` option then `ansible called dynamic inventory --list` which provide the `list of host` option then for each of the `target host in the inventory file` it ran the `--host` with `each of the hostname that we get from the inventor.py file`

- hence lets suppose we have `1000 of target host` then `each will go through the hostvars` check and time will be high 

- if we lets suppose added `1000 fake host` and check the time taken we can do as below 

    ```
        # we can generate the 1000 fake host as below shell command 

        for i in {1..1000}
        do
            echo \"fake{i}\" 
        done | tr "\n" ""

        # using the forloop to create the 1000 fake target hosts in here
        # here the tr command will replace the `\n` with the ''
        # and forgetting the "" we need to escape using it as `\"\"` 

        # now we can run the tail command in backgound to see the latest output of the file 
        tail -f /var/tmp/ansible_dynamic_inventory.log &
        # using the & to run on the background 

        # this also gives us the pid it is running on

        inventory.py
        -------------
        #! /usr/bin/env python3 # using the shabang code over here

        from __future__ import print_function
        # this will make the script backward compatible with the python2 as well as the python3

        import argsparse # importing the argsparse module in here 
        import logging # importing the logging module in here 

        try:
            import json # importing the json module 
        except ImportError: # incase of ImportError which will be based on the python2
            import simplejson as json # importing the simplejosn as using it as json 

        
        class Inventory(object): #creating the Inventory class which is subclass of the object class 

            def __init__(self,include_list_hostvars) : # defining the constructor out in here 

                self.include_list_hostvars=include_list_hostvars # using the self to redeine the include_list_hostvars as the instance varible 

                self.command_option() #activating the logging functionality
                
                paeser=argsparse.ArgumentParser() # creating the ArgumentParser object to accept the command line option 
                
                #defining the argument as default argument that we are going to accept in here 
                parse.add_arguments("--list,action="store_true",help="list of inventories") # defining the list of inventories which we can get using the `--list` option

                # here defining the command line option as the --host in here 
                parser.add_arguments("--host",action="store", help="showing the hostvars from the hostname")

                self.args=parser.parse_args() # fetching the vlid argument using the self.args variable 

                if not (self.args.list,self.args.host): # if an invalid default command line args been provided 
                    parser.print_usage() # printing the invalid usage option in here 
                    return SystemExit # exiting the system in here 

                self.define_group_hostvar_arguments() # calling the instance method to initialize the self.group and self.hostvars i.e the groupvars and hostvars for both --list and --host option
                
                if self.args.list: # if the self.args provided as --list then we can see the below

                    self.print_json(self.list())

                    # here calling the self.print_json() to convert the dictionary to the JSON encoded dictionary 

                    # also we are calling the self.list() which will return the dictionary with and without hostvars based on the value of self.include_list_hostvars

                elif self.args.host: # if the self.args provided as --host then we can see the below

                    self.print_json(self.host())

                    # here calling the self.print_json() to convert the dictionary to the JSON encoded dictionary

                    # also we are calling the self.host() which will return the hostvars if the corresponding host been matched else return the empty dict as {}

            
            def define_group_hostvar_arguments(self): # this method will define the group of host as well as the hostvars for both --list and --host option

                # defining the groupvars in this case over here

                self.group={
                    "centos":{ #defining the centos target group in here
                        "hosts":["centos1","centos2","centos3"],
                        "vars":{
                            "ansible_user":"root" #defining the ansible_user groupvars as root
                        }
                    },
                    "ubuntu":{ #defining the ubuntu target group in here
                        "hosts":["ubuntu1","ubuntu2","ubuntu3"],
                        "vars":{
                            "ansible_become":True,
                            "ansible_become_password":"password"
                        }
                    },
                    "control":{ # defining the control host over here 
                        "hosts":["ubuntu-c"]
                    },
                    "linux":{
                        "control":["ubuntu","centos"]
                    }
                    "fake":{
                        "hosts":['fake1', 'fake2', 'fake3', 'fake4', 'fake5', 'fake6', 'fake7', 'fake8', 'fake9', 'fake10', 'fake11', 'fake12', 'fake13', 'fake14', 'fake15', 'fake16', 'fake17', 'fake18', 'fake19', 'fake20', 'fake21', 'fake22', 'fake23', 'fake24', 'fake25', 'fake26', 'fake27', 'fake28', 'fake29', 'fake30', 'fake31', 'fake32', 'fake33', 'fake34', 'fake35', 'fake36', 'fake37', 'fake38', 'fake39', 'fake40', 'fake41', 'fake42', 'fake43', 'fake44', 'fake45', 'fake46', 'fake47', 'fake48', 'fake49', 'fake50', 'fake51', 'fake52', 'fake53', 'fake54', 'fake55', 'fake56', 'fake57', 'fake58', 'fake59', 'fake60', 'fake61', 'fake62', 'fake63', 'fake64', 'fake65', 'fake66', 'fake67', 'fake68', 'fake69', 'fake70', 'fake71', 'fake72', 'fake73', 'fake74', 'fake75', 'fake76', 'fake77', 'fake78', 'fake79', 'fake80', 'fake81', 'fake82', 'fake83', 'fake84', 'fake85', 'fake86', 'fake87', 'fake88', 'fake89', 'fake90', 'fake91', 'fake92', 'fake93', 'fake94', 'fake95', 'fake96', 'fake97', 'fake98', 'fake99', 'fake100', 'fake101', 'fake102', 'fake103', 'fake104', 'fake105', 'fake106', 'fake107', 'fake108', 'fake109', 'fake110', 'fake111', 'fake112', 'fake113', 'fake114', 'fake115', 'fake116', 'fake117', 'fake118', 'fake119', 'fake120', 'fake121', 'fake122', 'fake123', 'fake124', 'fake125', 'fake126', 'fake127', 'fake128', 'fake129', 'fake130', 'fake131', 'fake132', 'fake133', 'fake134', 'fake135', 'fake136', 'fake137', 'fake138', 'fake139', 'fake140', 'fake141', 'fake142', 'fake143', 'fake144', 'fake145', 'fake146', 'fake147', 'fake148', 'fake149', 'fake150', 'fake151', 'fake152', 'fake153', 'fake154', 'fake155', 'fake156', 'fake157', 'fake158', 'fake159', 'fake160', 'fake161', 'fake162', 'fake163', 'fake164', 'fake165', 'fake166', 'fake167', 'fake168', 'fake169', 'fake170', 'fake171', 'fake172', 'fake173', 'fake174', 'fake175', 'fake176', 'fake177', 'fake178', 'fake179', 'fake180', 'fake181', 'fake182', 'fake183', 'fake184', 'fake185', 'fake186', 'fake187', 'fake188', 'fake189', 'fake190', 'fake191', 'fake192', 'fake193', 'fake194', 'fake195', 'fake196', 'fake197', 'fake198', 'fake199', 'fake200', 'fake201', 'fake202', 'fake203', 'fake204', 'fake205', 'fake206', 'fake207', 'fake208', 'fake209', 'fake210', 'fake211', 'fake212', 'fake213', 'fake214', 'fake215', 'fake216', 'fake217', 'fake218', 'fake219', 'fake220', 'fake221', 'fake222', 'fake223', 'fake224', 'fake225', 'fake226', 'fake227', 'fake228', 'fake229', 'fake230', 'fake231', 'fake232', 'fake233', 'fake234', 'fake235', 'fake236', 'fake237', 'fake238', 'fake239', 'fake240', 'fake241', 'fake242', 'fake243', 'fake244', 'fake245', 'fake246', 'fake247', 'fake248', 'fake249', 'fake250', 'fake251', 'fake252', 'fake253', 'fake254', 'fake255', 'fake256', 'fake257', 'fake258', 'fake259', 'fake260', 'fake261', 'fake262', 'fake263', 'fake264', 'fake265', 'fake266', 'fake267', 'fake268', 'fake269', 'fake270', 'fake271', 'fake272', 'fake273', 'fake274', 'fake275', 'fake276', 'fake277', 'fake278', 'fake279', 'fake280', 'fake281', 'fake282', 'fake283', 'fake284', 'fake285', 'fake286', 'fake287', 'fake288', 'fake289', 'fake290', 'fake291', 'fake292', 'fake293', 'fake294', 'fake295', 'fake296', 'fake297', 'fake298', 'fake299', 'fake300', 'fake301', 'fake302', 'fake303', 'fake304', 'fake305', 'fake306', 'fake307', 'fake308', 'fake309', 'fake310', 'fake311', 'fake312', 'fake313', 'fake314', 'fake315', 'fake316', 'fake317', 'fake318', 'fake319', 'fake320', 'fake321', 'fake322', 'fake323', 'fake324', 'fake325', 'fake326', 'fake327', 'fake328', 'fake329', 'fake330', 'fake331', 'fake332', 'fake333', 'fake334', 'fake335', 'fake336', 'fake337', 'fake338', 'fake339', 'fake340', 'fake341', 'fake342', 'fake343', 'fake344', 'fake345', 'fake346', 'fake347', 'fake348', 'fake349', 'fake350', 'fake351', 'fake352', 'fake353', 'fake354', 'fake355', 'fake356', 'fake357', 'fake358', 'fake359', 'fake360', 'fake361', 'fake362', 'fake363', 'fake364', 'fake365', 'fake366', 'fake367', 'fake368', 'fake369', 'fake370', 'fake371', 'fake372', 'fake373', 'fake374', 'fake375', 'fake376', 'fake377', 'fake378', 'fake379', 'fake380', 'fake381', 'fake382', 'fake383', 'fake384', 'fake385', 'fake386', 'fake387', 'fake388', 'fake389', 'fake390', 'fake391', 'fake392', 'fake393', 'fake394', 'fake395', 'fake396', 'fake397', 'fake398', 'fake399', 'fake400', 'fake401', 'fake402', 'fake403', 'fake404', 'fake405', 'fake406', 'fake407', 'fake408', 'fake409', 'fake410', 'fake411', 'fake412', 'fake413', 'fake414', 'fake415', 'fake416', 'fake417', 'fake418', 'fake419', 'fake420', 'fake421', 'fake422', 'fake423', 'fake424', 'fake425', 'fake426', 'fake427', 'fake428', 'fake429', 'fake430', 'fake431', 'fake432', 'fake433', 'fake434', 'fake435', 'fake436', 'fake437', 'fake438', 'fake439', 'fake440', 'fake441', 'fake442', 'fake443', 'fake444', 'fake445', 'fake446', 'fake447', 'fake448', 'fake449', 'fake450', 'fake451', 'fake452', 'fake453', 'fake454', 'fake455', 'fake456', 'fake457', 'fake458', 'fake459', 'fake460', 'fake461', 'fake462', 'fake463', 'fake464', 'fake465', 'fake466', 'fake467', 'fake468', 'fake469', 'fake470', 'fake471', 'fake472', 'fake473', 'fake474', 'fake475', 'fake476', 'fake477', 'fake478', 'fake479', 'fake480', 'fake481', 'fake482', 'fake483', 'fake484', 'fake485', 'fake486', 'fake487', 'fake488', 'fake489', 'fake490', 'fake491', 'fake492', 'fake493', 'fake494', 'fake495', 'fake496', 'fake497', 'fake498', 'fake499', 'fake500', 'fake501', 'fake502', 'fake503', 'fake504', 'fake505', 'fake506', 'fake507', 'fake508', 'fake509', 'fake510', 'fake511', 'fake512', 'fake513', 'fake514', 'fake515', 'fake516', 'fake517', 'fake518', 'fake519', 'fake520', 'fake521', 'fake522', 'fake523', 'fake524', 'fake525', 'fake526', 'fake527', 'fake528', 'fake529', 'fake530', 'fake531', 'fake532', 'fake533', 'fake534', 'fake535', 'fake536', 'fake537', 'fake538', 'fake539', 'fake540', 'fake541', 'fake542', 'fake543', 'fake544', 'fake545', 'fake546', 'fake547', 'fake548', 'fake549', 'fake550', 'fake551', 'fake552', 'fake553', 'fake554', 'fake555', 'fake556', 'fake557', 'fake558', 'fake559', 'fake560', 'fake561', 'fake562', 'fake563', 'fake564', 'fake565', 'fake566', 'fake567', 'fake568', 'fake569', 'fake570', 'fake571', 'fake572', 'fake573', 'fake574', 'fake575', 'fake576', 'fake577', 'fake578', 'fake579', 'fake580', 'fake581', 'fake582', 'fake583', 'fake584', 'fake585', 'fake586', 'fake587', 'fake588', 'fake589', 'fake590', 'fake591', 'fake592', 'fake593', 'fake594', 'fake595', 'fake596', 'fake597', 'fake598', 'fake599', 'fake600', 'fake601', 'fake602', 'fake603', 'fake604', 'fake605', 'fake606', 'fake607', 'fake608', 'fake609', 'fake610', 'fake611', 'fake612', 'fake613', 'fake614', 'fake615', 'fake616', 'fake617', 'fake618', 'fake619', 'fake620', 'fake621', 'fake622', 'fake623', 'fake624', 'fake625', 'fake626', 'fake627', 'fake628', 'fake629', 'fake630', 'fake631', 'fake632', 'fake633', 'fake634', 'fake635', 'fake636', 'fake637', 'fake638', 'fake639', 'fake640', 'fake641', 'fake642', 'fake643', 'fake644', 'fake645', 'fake646', 'fake647', 'fake648', 'fake649', 'fake650', 'fake651', 'fake652', 'fake653', 'fake654', 'fake655', 'fake656', 'fake657', 'fake658', 'fake659', 'fake660', 'fake661', 'fake662', 'fake663', 'fake664', 'fake665', 'fake666', 'fake667', 'fake668', 'fake669', 'fake670', 'fake671', 'fake672', 'fake673', 'fake674', 'fake675', 'fake676', 'fake677', 'fake678', 'fake679', 'fake680', 'fake681', 'fake682', 'fake683', 'fake684', 'fake685', 'fake686', 'fake687', 'fake688', 'fake689', 'fake690', 'fake691', 'fake692', 'fake693', 'fake694', 'fake695', 'fake696', 'fake697', 'fake698', 'fake699', 'fake700', 'fake701', 'fake702', 'fake703', 'fake704', 'fake705', 'fake706', 'fake707', 'fake708', 'fake709', 'fake710', 'fake711', 'fake712', 'fake713', 'fake714', 'fake715', 'fake716', 'fake717', 'fake718', 'fake719', 'fake720', 'fake721', 'fake722', 'fake723', 'fake724', 'fake725', 'fake726', 'fake727', 'fake728', 'fake729', 'fake730', 'fake731', 'fake732', 'fake733', 'fake734', 'fake735', 'fake736', 'fake737', 'fake738', 'fake739', 'fake740', 'fake741', 'fake742', 'fake743', 'fake744', 'fake745', 'fake746', 'fake747', 'fake748', 'fake749', 'fake750', 'fake751', 'fake752', 'fake753', 'fake754', 'fake755', 'fake756', 'fake757', 'fake758', 'fake759', 'fake760', 'fake761', 'fake762', 'fake763', 'fake764', 'fake765', 'fake766', 'fake767', 'fake768', 'fake769', 'fake770', 'fake771', 'fake772', 'fake773', 'fake774', 'fake775', 'fake776', 'fake777', 'fake778', 'fake779', 'fake780', 'fake781', 'fake782', 'fake783', 'fake784', 'fake785', 'fake786', 'fake787', 'fake788', 'fake789', 'fake790', 'fake791', 'fake792', 'fake793', 'fake794', 'fake795', 'fake796', 'fake797', 'fake798', 'fake799', 'fake800', 'fake801', 'fake802', 'fake803', 'fake804', 'fake805', 'fake806', 'fake807', 'fake808', 'fake809', 'fake810', 'fake811', 'fake812', 'fake813', 'fake814', 'fake815', 'fake816', 'fake817', 'fake818', 'fake819', 'fake820', 'fake821', 'fake822', 'fake823', 'fake824', 'fake825', 'fake826', 'fake827', 'fake828', 'fake829', 'fake830', 'fake831', 'fake832', 'fake833', 'fake834', 'fake835', 'fake836', 'fake837', 'fake838', 'fake839', 'fake840', 'fake841', 'fake842', 'fake843', 'fake844', 'fake845', 'fake846', 'fake847', 'fake848', 'fake849', 'fake850', 'fake851', 'fake852', 'fake853', 'fake854', 'fake855', 'fake856', 'fake857', 'fake858', 'fake859', 'fake860', 'fake861', 'fake862', 'fake863', 'fake864', 'fake865', 'fake866', 'fake867', 'fake868', 'fake869', 'fake870', 'fake871', 'fake872', 'fake873', 'fake874', 'fake875', 'fake876', 'fake877', 'fake878', 'fake879', 'fake880', 'fake881', 'fake882', 'fake883', 'fake884', 'fake885', 'fake886', 'fake887', 'fake888', 'fake889', 'fake890', 'fake891', 'fake892', 'fake893', 'fake894', 'fake895', 'fake896', 'fake897', 'fake898', 'fake899', 'fake900', 'fake901', 'fake902', 'fake903', 'fake904', 'fake905', 'fake906', 'fake907', 'fake908', 'fake909', 'fake910', 'fake911', 'fake912', 'fake913', 'fake914', 'fake915', 'fake916', 'fake917', 'fake918', 'fake919', 'fake920', 'fake921', 'fake922', 'fake923', 'fake924', 'fake925', 'fake926', 'fake927', 'fake928', 'fake929', 'fake930', 'fake931', 'fake932', 'fake933', 'fake934', 'fake935', 'fake936', 'fake937', 'fake938', 'fake939', 'fake940', 'fake941', 'fake942', 'fake943', 'fake944', 'fake945', 'fake946', 'fake947', 'fake948', 'fake949', 'fake950', 'fake951', 'fake952', 'fake953', 'fake954', 'fake955', 'fake956', 'fake957', 'fake958', 'fake959', 'fake960', 'fake961', 'fake962', 'fake963', 'fake964', 'fake965', 'fake966', 'fake967', 'fake968', 'fake969', 'fake970', 'fake971', 'fake972', 'fake973', 'fake974', 'fake975', 'fake976', 'fake977', 'fake978', 'fake979', 'fake980', 'fake981', 'fake982', 'fake983', 'fake984', 'fake985', 'fake986', 'fake987', 'fake988', 'fake989', 'fake990', 'fake991', 'fake992', 'fake993', 'fake994', 'fake995', 'fake996', 'fake997', 'fake998', 'fake999', 'fake1000']
                    }
                }

                # defining the hostvars in here which will help in defining the hostvars based on the target host

                self.hostvars={
                    "centos1":{ # defining the centos1 host here0
                        "ansible_port": 2222 #defining the hostvars as ansible_port in here
                    },
                    "ubuntu-c":{
                        "ansible_connection":"local" # defining the ansible_connection as local in here 
                    }
                }

            def print_json(self,content): #defining the method which convert the dict content to JSON

                # printing the json in nice pretty print format

                print(json.dumps(content,indent=4,sort_keys=4))


            def list(self) # defining the list method in here 

                self.logger.info("List Executed")

                if self.include_list_hostvars:

                    merged= self.group # assinging the dictionary to the merged dictionary in here 

                    merged["_meta"]={} # defining the _meta key which will contain the hostvars

                    return merged # returning the dictionary 

                else:

                    return self.group # returning the group of without the _meta info here 

            def host(self) # defining the host instance method in here 

                self.logger.info(f"Execueted for the Host {self.args.host}") #definingthe logger statement in here 

                if self.args.host in self.hostvars: # if the host ecist in the hostvars

                    return self.hostvars[self.args.host] # returning the hostvrs value for the spoecific host

                else:

                    return {} # returning the emptyu dict in here if the hostname not matched in the self.hostvars

            
            def command_option(self): #activating the log to the file in here 

                self.logger=logging.getLogger("ansible_dynamic_inventory") #defining the custom logger inn here

                self.hndlr=logging.FileHandler("/var/tmp/ansible_dynamic_inventory.log")

                # defining the file handler as the location of /var/tmp/ansible_dynamic_inventory.log value 

                # her we can't return to the StreamHandler as the return JSON being used by the ansible to get the inventory info

                self.formatter=logging.Formatter("%(asctime)s %(level)s %(message)s")

                # setting up the formatter in here 

                self.hndlr.setFormatter(self.formatter) # settng the formatter to the FileHandler 

                self.logger.addHandler(self.hndler) # here adding the handler to the logger

                self.logger.setLevel(level=logging.DEBUG) # defining the logger level as DEBUG in here 

        # now we can call the Inventory class with include_list_hostvars as below
        
        Inventory(include_list_hostvars=False) # using the Inventory class in here with the include_list_hostvars as False which will not provide the _meta key in the group of host
    
    
        # now when run the command as 
        time ansible all -i inventory --list-hosts

        # we can see the tail which is running on the background output
        # at the end we can see that it take signifant time to be execued 
    
    ```

- if `we want to provide thousand of host` ansible need to `mitigate this problem`

- in `Ansible 1.3` we are not adding the `hostvars info for each host that we get back from --list option` `rather` we are `using the _meta key with the hostvars info embeded into the group of host itsef so that each host will not called with the hostvars`

- hence we will be getting the `Ansible 1.3` we can set the `include_list_hostvars=True` then which will add the `_meta` key to the `group of host with hostvars` as the value 

- if we are using the `Ansible < 1.3` we need to referene tht with the `--list and --host option`

- we can execute the `if the group of host contains the _meta key` then for every host `checking the hostvars` `will not be performed` 

- hene when we use the `include_list_hostvars=True` which make the `_meta info` and `hostvars is the part of it` and hence ansible will not prform the `every host hostvar checking` which can imporve the `time sifgnifantly`

- we can write the code as below 

    ```
    
        inventory.py
        -------------
        #! /usr/bin/env python3 # using the shabang code over here

        from __future__ import print_function
        # this will make the script backward compatible with the python2 as well as the python3

        import argsparse # importing the argsparse module in here 
        import logging # importing the logging module in here 

        try:
            import json # importing the json module 
        except ImportError: # incase of ImportError which will be based on the python2
            import simplejson as json # importing the simplejosn as using it as json 

        
        class Inventory(object): #creating the Inventory class which is subclass of the object class 

            def __init__(self,include_list_hostvars) : # defining the constructor out in here 

                self.include_list_hostvars=include_list_hostvars # using the self to redeine the include_list_hostvars as the instance varible 

                self.command_option() #activating the logging functionality
                
                paeser=argsparse.ArgumentParser() # creating the ArgumentParser object to accept the command line option 
                
                #defining the argument as default argument that we are going to accept in here 
                parse.add_arguments("--list,action="store_true",help="list of inventories") # defining the list of inventories which we can get using the `--list` option

                # here defining the command line option as the --host in here 
                parser.add_arguments("--host",action="store", help="showing the hostvars from the hostname")

                self.args=parser.parse_args() # fetching the vlid argument using the self.args variable 

                if not (self.args.list,self.args.host): # if an invalid default command line args been provided 
                    parser.print_usage() # printing the invalid usage option in here 
                    return SystemExit # exiting the system in here 

                self.define_group_hostvar_arguments() # calling the instance method to initialize the self.group and self.hostvars i.e the groupvars and hostvars for both --list and --host option
                
                if self.args.list: # if the self.args provided as --list then we can see the below

                    self.print_json(self.list())

                    # here calling the self.print_json() to convert the dictionary to the JSON encoded dictionary 

                    # also we are calling the self.list() which will return the dictionary with and without hostvars based on the value of self.include_list_hostvars

                elif self.args.host: # if the self.args provided as --host then we can see the below

                    self.print_json(self.host())

                    # here calling the self.print_json() to convert the dictionary to the JSON encoded dictionary

                    # also we are calling the self.host() which will return the hostvars if the corresponding host been matched else return the empty dict as {}

            
            def define_group_hostvar_arguments(self): # this method will define the group of host as well as the hostvars for both --list and --host option

                # defining the groupvars in this case over here

                self.group={
                    "centos":{ #defining the centos target group in here
                        "hosts":["centos1","centos2","centos3"],
                        "vars":{
                            "ansible_user":"root" #defining the ansible_user groupvars as root
                        }
                    },
                    "ubuntu":{ #defining the ubuntu target group in here
                        "hosts":["ubuntu1","ubuntu2","ubuntu3"],
                        "vars":{
                            "ansible_become":True,
                            "ansible_become_password":"password"
                        }
                    },
                    "control":{ # defining the control host over here 
                        "hosts":["ubuntu-c"]
                    },
                    "linux":{
                        "control":["ubuntu","centos"]
                    }
                    "fake":{
                        "hosts":['fake1', 'fake2', 'fake3', 'fake4', 'fake5', 'fake6', 'fake7', 'fake8', 'fake9', 'fake10', 'fake11', 'fake12', 'fake13', 'fake14', 'fake15', 'fake16', 'fake17', 'fake18', 'fake19', 'fake20', 'fake21', 'fake22', 'fake23', 'fake24', 'fake25', 'fake26', 'fake27', 'fake28', 'fake29', 'fake30', 'fake31', 'fake32', 'fake33', 'fake34', 'fake35', 'fake36', 'fake37', 'fake38', 'fake39', 'fake40', 'fake41', 'fake42', 'fake43', 'fake44', 'fake45', 'fake46', 'fake47', 'fake48', 'fake49', 'fake50', 'fake51', 'fake52', 'fake53', 'fake54', 'fake55', 'fake56', 'fake57', 'fake58', 'fake59', 'fake60', 'fake61', 'fake62', 'fake63', 'fake64', 'fake65', 'fake66', 'fake67', 'fake68', 'fake69', 'fake70', 'fake71', 'fake72', 'fake73', 'fake74', 'fake75', 'fake76', 'fake77', 'fake78', 'fake79', 'fake80', 'fake81', 'fake82', 'fake83', 'fake84', 'fake85', 'fake86', 'fake87', 'fake88', 'fake89', 'fake90', 'fake91', 'fake92', 'fake93', 'fake94', 'fake95', 'fake96', 'fake97', 'fake98', 'fake99', 'fake100', 'fake101', 'fake102', 'fake103', 'fake104', 'fake105', 'fake106', 'fake107', 'fake108', 'fake109', 'fake110', 'fake111', 'fake112', 'fake113', 'fake114', 'fake115', 'fake116', 'fake117', 'fake118', 'fake119', 'fake120', 'fake121', 'fake122', 'fake123', 'fake124', 'fake125', 'fake126', 'fake127', 'fake128', 'fake129', 'fake130', 'fake131', 'fake132', 'fake133', 'fake134', 'fake135', 'fake136', 'fake137', 'fake138', 'fake139', 'fake140', 'fake141', 'fake142', 'fake143', 'fake144', 'fake145', 'fake146', 'fake147', 'fake148', 'fake149', 'fake150', 'fake151', 'fake152', 'fake153', 'fake154', 'fake155', 'fake156', 'fake157', 'fake158', 'fake159', 'fake160', 'fake161', 'fake162', 'fake163', 'fake164', 'fake165', 'fake166', 'fake167', 'fake168', 'fake169', 'fake170', 'fake171', 'fake172', 'fake173', 'fake174', 'fake175', 'fake176', 'fake177', 'fake178', 'fake179', 'fake180', 'fake181', 'fake182', 'fake183', 'fake184', 'fake185', 'fake186', 'fake187', 'fake188', 'fake189', 'fake190', 'fake191', 'fake192', 'fake193', 'fake194', 'fake195', 'fake196', 'fake197', 'fake198', 'fake199', 'fake200', 'fake201', 'fake202', 'fake203', 'fake204', 'fake205', 'fake206', 'fake207', 'fake208', 'fake209', 'fake210', 'fake211', 'fake212', 'fake213', 'fake214', 'fake215', 'fake216', 'fake217', 'fake218', 'fake219', 'fake220', 'fake221', 'fake222', 'fake223', 'fake224', 'fake225', 'fake226', 'fake227', 'fake228', 'fake229', 'fake230', 'fake231', 'fake232', 'fake233', 'fake234', 'fake235', 'fake236', 'fake237', 'fake238', 'fake239', 'fake240', 'fake241', 'fake242', 'fake243', 'fake244', 'fake245', 'fake246', 'fake247', 'fake248', 'fake249', 'fake250', 'fake251', 'fake252', 'fake253', 'fake254', 'fake255', 'fake256', 'fake257', 'fake258', 'fake259', 'fake260', 'fake261', 'fake262', 'fake263', 'fake264', 'fake265', 'fake266', 'fake267', 'fake268', 'fake269', 'fake270', 'fake271', 'fake272', 'fake273', 'fake274', 'fake275', 'fake276', 'fake277', 'fake278', 'fake279', 'fake280', 'fake281', 'fake282', 'fake283', 'fake284', 'fake285', 'fake286', 'fake287', 'fake288', 'fake289', 'fake290', 'fake291', 'fake292', 'fake293', 'fake294', 'fake295', 'fake296', 'fake297', 'fake298', 'fake299', 'fake300', 'fake301', 'fake302', 'fake303', 'fake304', 'fake305', 'fake306', 'fake307', 'fake308', 'fake309', 'fake310', 'fake311', 'fake312', 'fake313', 'fake314', 'fake315', 'fake316', 'fake317', 'fake318', 'fake319', 'fake320', 'fake321', 'fake322', 'fake323', 'fake324', 'fake325', 'fake326', 'fake327', 'fake328', 'fake329', 'fake330', 'fake331', 'fake332', 'fake333', 'fake334', 'fake335', 'fake336', 'fake337', 'fake338', 'fake339', 'fake340', 'fake341', 'fake342', 'fake343', 'fake344', 'fake345', 'fake346', 'fake347', 'fake348', 'fake349', 'fake350', 'fake351', 'fake352', 'fake353', 'fake354', 'fake355', 'fake356', 'fake357', 'fake358', 'fake359', 'fake360', 'fake361', 'fake362', 'fake363', 'fake364', 'fake365', 'fake366', 'fake367', 'fake368', 'fake369', 'fake370', 'fake371', 'fake372', 'fake373', 'fake374', 'fake375', 'fake376', 'fake377', 'fake378', 'fake379', 'fake380', 'fake381', 'fake382', 'fake383', 'fake384', 'fake385', 'fake386', 'fake387', 'fake388', 'fake389', 'fake390', 'fake391', 'fake392', 'fake393', 'fake394', 'fake395', 'fake396', 'fake397', 'fake398', 'fake399', 'fake400', 'fake401', 'fake402', 'fake403', 'fake404', 'fake405', 'fake406', 'fake407', 'fake408', 'fake409', 'fake410', 'fake411', 'fake412', 'fake413', 'fake414', 'fake415', 'fake416', 'fake417', 'fake418', 'fake419', 'fake420', 'fake421', 'fake422', 'fake423', 'fake424', 'fake425', 'fake426', 'fake427', 'fake428', 'fake429', 'fake430', 'fake431', 'fake432', 'fake433', 'fake434', 'fake435', 'fake436', 'fake437', 'fake438', 'fake439', 'fake440', 'fake441', 'fake442', 'fake443', 'fake444', 'fake445', 'fake446', 'fake447', 'fake448', 'fake449', 'fake450', 'fake451', 'fake452', 'fake453', 'fake454', 'fake455', 'fake456', 'fake457', 'fake458', 'fake459', 'fake460', 'fake461', 'fake462', 'fake463', 'fake464', 'fake465', 'fake466', 'fake467', 'fake468', 'fake469', 'fake470', 'fake471', 'fake472', 'fake473', 'fake474', 'fake475', 'fake476', 'fake477', 'fake478', 'fake479', 'fake480', 'fake481', 'fake482', 'fake483', 'fake484', 'fake485', 'fake486', 'fake487', 'fake488', 'fake489', 'fake490', 'fake491', 'fake492', 'fake493', 'fake494', 'fake495', 'fake496', 'fake497', 'fake498', 'fake499', 'fake500', 'fake501', 'fake502', 'fake503', 'fake504', 'fake505', 'fake506', 'fake507', 'fake508', 'fake509', 'fake510', 'fake511', 'fake512', 'fake513', 'fake514', 'fake515', 'fake516', 'fake517', 'fake518', 'fake519', 'fake520', 'fake521', 'fake522', 'fake523', 'fake524', 'fake525', 'fake526', 'fake527', 'fake528', 'fake529', 'fake530', 'fake531', 'fake532', 'fake533', 'fake534', 'fake535', 'fake536', 'fake537', 'fake538', 'fake539', 'fake540', 'fake541', 'fake542', 'fake543', 'fake544', 'fake545', 'fake546', 'fake547', 'fake548', 'fake549', 'fake550', 'fake551', 'fake552', 'fake553', 'fake554', 'fake555', 'fake556', 'fake557', 'fake558', 'fake559', 'fake560', 'fake561', 'fake562', 'fake563', 'fake564', 'fake565', 'fake566', 'fake567', 'fake568', 'fake569', 'fake570', 'fake571', 'fake572', 'fake573', 'fake574', 'fake575', 'fake576', 'fake577', 'fake578', 'fake579', 'fake580', 'fake581', 'fake582', 'fake583', 'fake584', 'fake585', 'fake586', 'fake587', 'fake588', 'fake589', 'fake590', 'fake591', 'fake592', 'fake593', 'fake594', 'fake595', 'fake596', 'fake597', 'fake598', 'fake599', 'fake600', 'fake601', 'fake602', 'fake603', 'fake604', 'fake605', 'fake606', 'fake607', 'fake608', 'fake609', 'fake610', 'fake611', 'fake612', 'fake613', 'fake614', 'fake615', 'fake616', 'fake617', 'fake618', 'fake619', 'fake620', 'fake621', 'fake622', 'fake623', 'fake624', 'fake625', 'fake626', 'fake627', 'fake628', 'fake629', 'fake630', 'fake631', 'fake632', 'fake633', 'fake634', 'fake635', 'fake636', 'fake637', 'fake638', 'fake639', 'fake640', 'fake641', 'fake642', 'fake643', 'fake644', 'fake645', 'fake646', 'fake647', 'fake648', 'fake649', 'fake650', 'fake651', 'fake652', 'fake653', 'fake654', 'fake655', 'fake656', 'fake657', 'fake658', 'fake659', 'fake660', 'fake661', 'fake662', 'fake663', 'fake664', 'fake665', 'fake666', 'fake667', 'fake668', 'fake669', 'fake670', 'fake671', 'fake672', 'fake673', 'fake674', 'fake675', 'fake676', 'fake677', 'fake678', 'fake679', 'fake680', 'fake681', 'fake682', 'fake683', 'fake684', 'fake685', 'fake686', 'fake687', 'fake688', 'fake689', 'fake690', 'fake691', 'fake692', 'fake693', 'fake694', 'fake695', 'fake696', 'fake697', 'fake698', 'fake699', 'fake700', 'fake701', 'fake702', 'fake703', 'fake704', 'fake705', 'fake706', 'fake707', 'fake708', 'fake709', 'fake710', 'fake711', 'fake712', 'fake713', 'fake714', 'fake715', 'fake716', 'fake717', 'fake718', 'fake719', 'fake720', 'fake721', 'fake722', 'fake723', 'fake724', 'fake725', 'fake726', 'fake727', 'fake728', 'fake729', 'fake730', 'fake731', 'fake732', 'fake733', 'fake734', 'fake735', 'fake736', 'fake737', 'fake738', 'fake739', 'fake740', 'fake741', 'fake742', 'fake743', 'fake744', 'fake745', 'fake746', 'fake747', 'fake748', 'fake749', 'fake750', 'fake751', 'fake752', 'fake753', 'fake754', 'fake755', 'fake756', 'fake757', 'fake758', 'fake759', 'fake760', 'fake761', 'fake762', 'fake763', 'fake764', 'fake765', 'fake766', 'fake767', 'fake768', 'fake769', 'fake770', 'fake771', 'fake772', 'fake773', 'fake774', 'fake775', 'fake776', 'fake777', 'fake778', 'fake779', 'fake780', 'fake781', 'fake782', 'fake783', 'fake784', 'fake785', 'fake786', 'fake787', 'fake788', 'fake789', 'fake790', 'fake791', 'fake792', 'fake793', 'fake794', 'fake795', 'fake796', 'fake797', 'fake798', 'fake799', 'fake800', 'fake801', 'fake802', 'fake803', 'fake804', 'fake805', 'fake806', 'fake807', 'fake808', 'fake809', 'fake810', 'fake811', 'fake812', 'fake813', 'fake814', 'fake815', 'fake816', 'fake817', 'fake818', 'fake819', 'fake820', 'fake821', 'fake822', 'fake823', 'fake824', 'fake825', 'fake826', 'fake827', 'fake828', 'fake829', 'fake830', 'fake831', 'fake832', 'fake833', 'fake834', 'fake835', 'fake836', 'fake837', 'fake838', 'fake839', 'fake840', 'fake841', 'fake842', 'fake843', 'fake844', 'fake845', 'fake846', 'fake847', 'fake848', 'fake849', 'fake850', 'fake851', 'fake852', 'fake853', 'fake854', 'fake855', 'fake856', 'fake857', 'fake858', 'fake859', 'fake860', 'fake861', 'fake862', 'fake863', 'fake864', 'fake865', 'fake866', 'fake867', 'fake868', 'fake869', 'fake870', 'fake871', 'fake872', 'fake873', 'fake874', 'fake875', 'fake876', 'fake877', 'fake878', 'fake879', 'fake880', 'fake881', 'fake882', 'fake883', 'fake884', 'fake885', 'fake886', 'fake887', 'fake888', 'fake889', 'fake890', 'fake891', 'fake892', 'fake893', 'fake894', 'fake895', 'fake896', 'fake897', 'fake898', 'fake899', 'fake900', 'fake901', 'fake902', 'fake903', 'fake904', 'fake905', 'fake906', 'fake907', 'fake908', 'fake909', 'fake910', 'fake911', 'fake912', 'fake913', 'fake914', 'fake915', 'fake916', 'fake917', 'fake918', 'fake919', 'fake920', 'fake921', 'fake922', 'fake923', 'fake924', 'fake925', 'fake926', 'fake927', 'fake928', 'fake929', 'fake930', 'fake931', 'fake932', 'fake933', 'fake934', 'fake935', 'fake936', 'fake937', 'fake938', 'fake939', 'fake940', 'fake941', 'fake942', 'fake943', 'fake944', 'fake945', 'fake946', 'fake947', 'fake948', 'fake949', 'fake950', 'fake951', 'fake952', 'fake953', 'fake954', 'fake955', 'fake956', 'fake957', 'fake958', 'fake959', 'fake960', 'fake961', 'fake962', 'fake963', 'fake964', 'fake965', 'fake966', 'fake967', 'fake968', 'fake969', 'fake970', 'fake971', 'fake972', 'fake973', 'fake974', 'fake975', 'fake976', 'fake977', 'fake978', 'fake979', 'fake980', 'fake981', 'fake982', 'fake983', 'fake984', 'fake985', 'fake986', 'fake987', 'fake988', 'fake989', 'fake990', 'fake991', 'fake992', 'fake993', 'fake994', 'fake995', 'fake996', 'fake997', 'fake998', 'fake999', 'fake1000']
                    }
                }

                # defining the hostvars in here which will help in defining the hostvars based on the target host

                self.hostvars={
                    "centos1":{ # defining the centos1 host here0
                        "ansible_port": 2222 #defining the hostvars as ansible_port in here
                    },
                    "ubuntu-c":{
                        "ansible_connection":"local" # defining the ansible_connection as local in here 
                    }
                }

            def print_json(self,content): #defining the method which convert the dict content to JSON

                # printing the json in nice pretty print format

                print(json.dumps(content,indent=4,sort_keys=4))


            def list(self) # defining the list method in here 

                self.logger.info("List Executed")

                if self.include_list_hostvars:

                    merged= self.group # assinging the dictionary to the merged dictionary in here 

                    merged["_meta"]={} # defining the _meta key which will contain the hostvars

                    return merged # returning the dictionary 

                else:

                    return self.group # returning the group of without the _meta info here 

            def host(self) # defining the host instance method in here 

                self.logger.info(f"Execueted for the Host {self.args.host}") #definingthe logger statement in here 

                if self.args.host in self.hostvars: # if the host ecist in the hostvars

                    return self.hostvars[self.args.host] # returning the hostvrs value for the spoecific host

                else:

                    return {} # returning the emptyu dict in here if the hostname not matched in the self.hostvars

            
            def command_option(self): #activating the log to the file in here 

                self.logger=logging.getLogger("ansible_dynamic_inventory") #defining the custom logger inn here

                self.hndlr=logging.FileHandler("/var/tmp/ansible_dynamic_inventory.log")

                # defining the file handler as the location of /var/tmp/ansible_dynamic_inventory.log value 

                # her we can't return to the StreamHandler as the return JSON being used by the ansible to get the inventory info

                self.formatter=logging.Formatter("%(asctime)s %(level)s %(message)s")

                # setting up the formatter in here 

                self.hndlr.setFormatter(self.formatter) # settng the formatter to the FileHandler 

                self.logger.addHandler(self.hndler) # here adding the handler to the logger

                self.logger.setLevel(level=logging.DEBUG) # defining the logger level as DEBUG in here 

        # now we can call the Inventory class with include_list_hostvars as below
        
        Inventory(include_list_hostvars=True) # using the Inventory class in here with the include_list_hostvars as True which will not provide the _meta key in the group of host
    
    
    
    ```

- also when we execute the `dynamic inventory --list` then we can see that `_meta key hostvars` which will be part of it 

- we can see the below code for the same 

    ```
        # we can eecute the inventory file with the list info and get the output as below
        ./inventory.py --list
        # then we can see the _meta key with hostvars value added as part of it 
        # as this being added to the _meta key hence for each host the hostvars checking not happenning 

        {
            "_meta": {
                "hostvars": {
                    "centos1": {
                        "ansible_port": 2222
                    },
                    "ubuntu-c": {
                        "ansible_connection": "local"
                    }
                }
            },
            "centos": {
                "hosts": [
                    "centos1",
                    "centos2",
                    "centos3"
                ],
                "vars": {
                    "ansible_user": "root"
                }
            },
            "control": {
                "hosts": [
                    "ubuntu-c"
                ]
            },
            "linux": {
                "children": [
                    "ubuntu",
                    "centos"
                ]
            },
            "ubuntu": {
                "hosts": [
                    "ubuntu1",
                    "ubuntu2",
                    "ubuntu3"
                ],
                "vars": {
                    "ansible_become": true,
                    "ansible_become_password": "password"
                }
            }
        }
    
    
    ```

- now when we check the `logger file with the same command we can ssee multiple hostvrs vcall foreach host been made`

    ```
        # when we execute the command as below 
        ansible all -i inventory --list-hosts
        # then we can see the logger file s below 

        /var/tmp/ansible_dynamic_inventory.log
        ---------------------------------------
        2023-09-18 19:57:19,249 INFO list executed
    
    ```


- we can remove the `background task` by the folllowing `approach`

    
    ```
        # if we run the jobs then it will show the background running task with the status=running and PID
        jobs
        # we have the kill command to terminate it with the PID
        kill <pid>
        # now when we see the jobs then it will be status as Terminated and PID
        jobs

    ```

- when will be using the `ansible with AWS` we can create `AWS Dynamic inventory` which is best `design practise `

- we can use that `AWS Dynamic inventory` to  manage the `content management system` that will be best





