# <ins> User Module in Ansible </ins> #

- `Manage user accounts and user attributes.`

- `For Windows targets, use the ansible.windows.win_user module instead.`

# Paramter
----------

- **append**

  - `If true`, `add the user to the groups specified in groups`
  
  - `If false`, `user will only be added to the groups specified in groups`, `removing them from all other groups`. 
  
  - `Choices`:

    - `false ← (default)`

    - `true`


- **authorization**
  
  - Sets the authorization of the user.

  - Does nothing when used with other platforms.

  - Can set multiple authorizations using comma separation.

  - To delete all authorizations, use authorization=''.

  - Currently supported on Illumos/Solaris.

- **comment**

  - `Optionally sets the description (aka GECOS) of user account.`

- **create_home**
  
  - `Unless set to false`, `a home directory will be made for the user when the account is created` or `if the home directory does not exist`. 
  
  - Changed from `createhome` to `create_home` in `Ansible 2.5.`

  - `Choices`:

        - `false`

        - `true ← (default)`

  - **expires**
  
    - `An expiry time for the user in epoch, it will be ignored on platforms that do not support this.`

    - Currently supported on `GNU/Linux, FreeBSD, and DragonFlyBSD`.

    - `Since Ansible 2.6 you can remove the expiry time by specifying a negative value`. 
    
    - `Currently supported on GNU/Linux and FreeBSD`.

  - **force**
    
    - `This only affects` `state=absent `
    
    - it forces `removal of the user` and `associated directories on supported platforms`. 
    
    - `The behavior is the same` as `userdel --force`, check the `man page for userdel on your system for details and support`. 
    
    - When used with `generate_ssh_key=yes ` and `force=True` this `forces an existing key to be overwritten`. 
    
    - `Choice`s:

        `false ← (default)`

        `true`

- **generate_ssh_key**
  
  - `Whether to generate a SSH key` `for the user` in question.  

  - `This will not overwrite an existing SSH key` `unless used with force=yes`
  
  - `Choices`:

    - `false ← (default)`

    - `true`


- **group**
  
  - `Optionally sets the user’s primary group (takes a group name).`

- **groups**

  - `List of groups user will be added to.`

  - `By default, the user is removed from all other group`
  
  - Configure append to modify this.
  
  - When `set to an empty string ''`, the `user is removed from all groups except the primary group`
  
  - `Before Ansible 2.3`, the only `input format allowed was a comma separated string.`


- **home** 
  
  - `Optionally set the user’s home directory. `

- **local**

  -  `Forces` the `use of “local” ` command `alternatives on platforms that implement it.`
    
- **move_home**
  
  - `If set to true` when `used with home`: , attempt to `move the user’s old home directory to the specified directory` if `it isn’t there already` and `the old home exists.`
  
  - Choices:

        `false ← (default)`

        `true`

- **name**
  
  -  `Name of the user` `to create, remove or modify.`

- **password**
  
  - `If provided`, `set` the `user’s password to the provided encrypted hash (Linux)` or `plain text password (macOS)`.

  - `Linux/Unix/POSIX: Enter the hashed password as the value.`

  - See FAQ entry[link](https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-generate-encrypted-passwords-for-the-user-module) fo`r details on various ways to generate the hash of a password.`

  - To `create an account with` a `locked/disabled password` on `Linux` systems, `set this to '!' or '*'.`

  - To cr`eate an account with` a `locked/disabled password `on `OpenBSD`, `set this to '*************'`.

  - `OS X/macOS: Enter the cleartext password as the value. Be sure to take relevant security precautions.`


- **password_expire_max**
  
  - `Maximum number of days between password change.`

  - `Supported on Linux only.`

- **password_expire_min**
  
  - `Minimum number of days between password change.`

  - `Supported on Linux only.`

- **password_lock**
  
  - `Lock the password (usermod -L, usermod -U, pw lock)`.

  - `Implementation differs by platform.` `This option does not always mean the user cannot login using other methods.`

  - `This option does not disable the user, only lock the password.`

  - `This must be set to False in order to unlock a currently locked password`. 
  
  - `The absence of this parameter will not unlock a password.`

  - Currently supported on Linux, FreeBSD, DragonFlyBSD, NetBSD, OpenBSD.

  - Choices:

        `false` :- `remove the password lock in GNU/Linux`

        `true` :- `provide the locl on the password in GNU/Linux `


  
  -  **shell**
     
    - `Optionally set the user’s shell. ` 
    
    - On macOS, before Ansible 2.5, the default shell for non-system users was /usr/bin/false. Since Ansible 2.5, the default shell for non-system users on macOS is /bin/bash

    - See notes for details on how other operating systems determine the default shell by the underlying tool.

  -  **ssh_key_file**
      

  - **state**
    
    -  `Whether the account should exist or not`, `taking action if the state is different from what is stated.`
    
    -  Choices:

        "absent"

        "present" ← (default)

  - **system**

    - When creating an account state=present, setting this to true makes the user a system account.

    - This setting cannot be changed on existing users.

    - Choices:

          false ← (default)

          true

  - **uid**
    
    - Optionally sets the UID of the user.
   
  - **update_password**
    
    - `always will update passwords if they differ.`
    
    - on_create will only set the password for newly created users.

    - Choices:

        "always" ← (default)

        "on_create"






 
 
 
   




 

 
 
 
