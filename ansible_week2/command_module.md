# <ins> command module </ins> #

- The `command module` `takes the command name` `followed by a list of space-delimited arguments`.

- The given command will be executed on all selected nodes.

- The `command(s) will not be processed through the shell`, so `variables like $HOSTNAME `and `operations like "*", "<", ">", "|", ";" and "&" will not work`. `Use` the `ansible.builtin.shell module if you need these features.`

- To `create command tasks that are easier to read than the ones using space-delimited arguments`, `pass parameters using the args task keyword ` or `use cmd parameter`. 

- `Either a free form command or cmd parameter is required`, see the examples.

-  `For Windows targets, use the ansible.windows.win_command module instead.`


- **Parameters**
  
  - **chdir**
    
    - `Change into this directory before running the command.`  
    
  - **cmd**
    
    - The command to run.

  - **creates**
    
    - A `filename or (since 2.0) glob pattern`. 
  
    - If a `matching file already exists, this step will not be run.`

    - `This is checked before removes is checked.`

  - **removes**
    
    - `A filename or (since 2.0) glob pattern. If a matching file exists, this step will be run.`

    - `This is checked after creates is checked.`
 

  - **stdin**
    
    - `Set the stdin of the command directly to the specified value`. 

  - **strip_empty_ends**
    
    - `Strip empty lines from the end of stdout/stderr in result.`

    -   Choices:

            false

            true ← (default)

 
  - **stdin_add_newline**
    
    - `If set to true, append a newline to stdin data.`

    -    Choices:

            false

            true ← (default)

  - **argv**
    
    - `Passes the command as a list rather than a string.`
    
    -  Use argv to avoid quoting values that would otherwise be interpreted incorrectly (for example “user name”).
    
    - `Only the string (free form) or the list (argv) form can be provided, not both. One or the other must be provided.`  

     