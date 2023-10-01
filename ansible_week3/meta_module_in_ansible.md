# ansible.builtin.meta module 

- `Meta tasks` `are a special kind of task` `which can influence Ansible internal execution or state.`

- `Meta tasks can be used anywhere within your playbook` 

- `This module is also supported for Windows targets`. 

- **Paramters**

  - `free_form`  :- `string` :-  `required`
    
    - `This module takes a free form command, as a string`. 
    
    - `There is not an actual option named “free form”. See the examples! `
    
    
    - `flush_handlers` 
      
        - `makes Ansible run` `any handler tasks ` `which have thus far been notified`.
        
        - `Ansible inserts these tasks internally` `at certain points` `to implicitly trigger handler runs`
        
    
    - `refresh_inventory`

        - `(added in Ansible 2.0) forces the reload of the inventory`
        
        - which `in the case of dynamic inventory` `scripts` means `they will be re-executed`
        
        - `If the dynamic inventory script is using a cache, Ansible cannot know this and has no way of refreshing it (you can disable the cache or, if available for your specific inventory datasource (e.g. aws) `
        
        - `This is mainly useful when additional hosts are created and users wish to use them instead of using the ansible.builtin.add_host module.` 

    
    - `noop`
      
      -  `This literally does ‘nothing’`. 
      
      -  `It is mainly used internally and not recommended for general use. `

    
    - `clear_facts`
      
      - `causes the gathered facts for the hosts specified in the play’s list of hosts to be cleared, including the fact cache.` 


    - `clear_host_errors`
      
      - `clears` `the` `failed state (if any)` `from hosts` `specified in the play’s list of hosts`. 

    
    - `end_play`
      
      - `causes the play to end without failing the host(s). Note that this affects all hosts.` 

    
    - `reset_connection`
      
      - `interrupts a persistent connection (i.e. ssh + control persist) `

    
    - `end_host`
      
      - `is a per-host variation of end_play`.` Causes the play to end for the current host without failing it.` 

    
    - `end_batch`:-
      
      - c`auses the current batch (see serial) to end without failing the host(s).`` Note that with serial=0 or undefined this behaves the same as end_play.`

 