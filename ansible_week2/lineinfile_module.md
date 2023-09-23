# <ins> lineinfile module </ins> #

- `This module ensures` a` particular line is in a file,` or `replace an existing line using a back-referenced regular expression`.

- `This is primarily useful when you want to change a single line in a file only.` 

- `See the ansible.builtin.replace module if you want to change multiple`, 

- `similar lines or check ansible.builtin.blockinfile if you want to insert/update/remove a block of lines in a file.` 

-  For other cases, see the ansible.builtin.copy or ansible.builtin.template modules.

     
- **Parameters**
  
  - **state**
      
      - `Whether the line should be there or not.`
      
      -  `Choices`:

            `"absent"`

            `"present" ← (default)`
    
  - **line**
    
    - `The line to insert/replace into the file.`     
    
    - `Required for state=present. `  , hence `must` need to be specified if we want to `inser or replace a line`
    
    - `The text or line you want to ensure is present or absent in the file.`
    
  -  **path**
     
    -   `path: The path to the file you want to modify`

  - **backrefs**
  
    - `Used with state=present. `
    
    - `if set`, `line can contain backreferences (both positional and named) that will get populated if the regexp matches. `
    
    - `Mutually exclusive with search_string.`
    
    - `If the regexp does match`,` the last matching line will be replaced by the expanded line parameter.`
    
    - `if the regexp does not match anywhere in the file, the file will be left unchanged.` 
    
    - `This parameter changes the operation of the module slightly`; `insertbefore` and `insertafter` `will be ignored `
    
    - `Choices`:

        `false ← (default)`

        `true`

    - **insertafter**
      
      - `Used with state=present. `
      
      - `If specified, the line will be inserted after the last match of specified regular expression.`
      
      - `if the first match is required, use(firstmatch=yes).` 
      
      - A `special value is available; EOF` `for inserting the line at the end of the file.` 
      
      - `If specified regular expression has no matches, EOF will be used instead. `
      
      - `If regular expressions are passed to both` `regexp and insertafter, insertafter` is `only honored if no match for regexp is found.` 
      
      - `May not be used with backrefs or insertbefore.`
      
      - Choices:

            "EOF" ← (default)

            "*regex*"
    
    - **insertbefore**
      
      - `Used with state=present.`

      -  `If specified`, t`he line will be inserted before the last match of specified regular expression.`
      
      -  `If the first match is required, use firstmatch=yes`.

      -  `A value is available; BOF for inserting the line at the beginning of the file.`

      -  `If specified regular expression has no matches, the line will be inserted at the end of the file.`

      -  `If regular expressions are passed` `to both` `regexp and insertbefore, insertbefore is only honored if no match for regexp is found.`

      -  May not be used with backrefs or insertafter.

      - Choices:

            "BOF"

            "*regex*"
    
    **mode**

      - The permissions the resulting filesystem object should have.

      - For those used to /usr/bin/chmod remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, '644' or '1777') so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, 0755) works sometimes, but can fail in loops and some other circumstances.

      - Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.

      - As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, u+rwx or u=rw,g=r,o=r).

      - If mode is not specified and the destination filesystem object does not exist, the default umask on the system will be used when setting the mode for the newly created filesystem object.

      - If mode is not specified and the destination filesystem object does exist, the mode of the existing filesystem object will be used.

      - Specifying mode is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details.

 
 
    - **regexp**
      
      - `The regular expression to look for in every line of the file.`
      
      - For `state=present,` `the pattern to replace if found.` `Only the last line found will be replaced.`
      
      - For `state=absent`, `the pattern of the line(s) to remove.`  
      
      -  `If the regular expression is not matched, the line will be added to the file in keeping with insertbefore or insertafter settings`. 
      
      - `When modifying a line the regexp should typically match both the initial state of the line as well as its state after replacement by line to ensure idempotence.` 


    - **search_string**
      
      - `The literal string to look for in every line of the file. This does not have to match the entire line.`
      
      - `Mutually exclusive with backrefs and regexp.`
      
      - For `state=present`, the `line to replace if the string is found in the file`. `Only the last line found will be replaced.`   
      
      - For `state=absent`, `the line(s) to remove if the string is in the line.` 
      
      - `If the literal expression is not matched`, `the line will be added to the file in keeping with insertbefore or insertafter settings.` 

    
    - **firstmatch**
      
      - `Used with insertafter or insertbefore. `
      
      - If set, insertafter and insertbefore will work with the first line that matches the given regular expression.
      
      - Choices:

            false ← (default)

            true

    - **backup**
      
      - `Create a backup file` `including the timestamp information` s`o you can get the original file back if you somehow clobbered it incorrectly.` 
      
      - Choices:

            false ← (default)

            true
    
    **create**

      - `Used with state=present.`
      
      - `If specified, the file will be created if it does not already exist.`

      - `By default it will fail if the file is missing.` 
      
      - Choices:

            false ← (default)

            true
 
      

    - **others**
      
      - `All arguments accepted by` the `ansible.builtin.file module` also `work here.` 
      
      -  

  