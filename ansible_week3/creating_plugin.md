# Creating Pugins in Ansible

- here we will `discuss` `various type of plugin available in Ansible`

- here we will also create `lookup_plugin`

- we will also create the `filter_plugin`  

- in `ansible there are lot of plugin knowningly or unknowningly` we are making the `use of plugin in ansible`

- when we use the `with_items` for `looping` which is a `ansible builtin lookup_plugin` with the name as `items.py` and the link for the lookup module given there 
  
  - [Ansible Lookup_plugin example](https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/lookup/items.py)   

- for using the `host_vars and group_vars` from the `directory loading` there is `vars_plugin` plugin as `host_group_vars.py`
  
  - [Ansible filter_plugin example](https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/vars/host_group_vars.py) 


- **Different Type of Plugin In Ansible**

- `Action Plugin` are the `front end to the modules` and `can execute actions on the controller before calling the module themselves` 

- `cache plugin` are the `used to keep a cache of facts`  `to avoid `  `costly fact gathering opertaions` 

- `callback plugin` are to `enable you` to `hook into` `Ansible events` `for display and logging` 

- `connection plugin` are to `how to communicate to the inventory hosts`

- `filter plugin` allow to `manipulate data inside the ansible play or template` , `This is a JINJA2 feature` , `Ansible ship`  `extra "filter" plugin`

- `lookup plugin` used to `pull the data from external source` , these are `implemented using the custom JINJA2 template`

- `startergy plugin` use for `control the "flow of play" and "execution logic" `

- `shell plugin` which deals with `low lavel command and formatting` for `different shell that ansible might encounter on the remote host`

- `Test Plugin` which allow you `validate the data inside the Ansible play or template` , this is a `JINJA2 feature` , `Ansible ship` `extra test plugin`      

- `vars plugin` `inject` the `additional variable into the ansible run` that did not `come from the inventory/playbook/commandline`

- **How to Work with the Ansible Plugin**

- here we are using a `with_items` for `looping` which is a `builtin lookup_plugin` that we ae using 

- here also we will have to `create a custom plugin` `name as with_sorted_items` which is a `lookup_plugin` to `sort the list provided against it`

- we have to `crate` the `list of directories` as below `for using the custom plugin` in here 

  - `action_plugins`
  
  - `lookup_plugins`
  
  - `callback_plugins`
  
  - `connection_plugins`
  
  - `filter_plugins`
  
  - `strategy_plugins`
  
  - `cache_plugins`
  
  - `test_plugins`

  - `shell_plugins`


- as here we are creating the `lookup plugin` hence we have to create the `lookup_plugins` `directory` in here 

- we will have to make use of the `[Ansible Lookup_plugin example](https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/lookup/items.py) module here`

- we will have to see the `lookup/items.py` and `lookyp/__init__.py(Where the LookUpBase class have been defined)` 

- we can modify the `lookup/items.py` file to `lookup_plugins/with_sort_items.py` as below or we can wget using it as below 

- for `wget` we can use the command as `wget https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/lookup/items.py` to get the `items.py` file

- if we want to see the `lookup/__init__.py` file thenn we have to wget that as well `wget https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/lookup/__init__.py ` over here 
  

  ```python

    lookup_plugins/with_sort_items.py
    ==================================

      
  
  
  
  
  
  
  
  
  
  
  
  
  
  ```
