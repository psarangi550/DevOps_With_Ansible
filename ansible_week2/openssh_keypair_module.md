# <ins> openssh_keypair module </ins> #

- this module help in generate the `private and public` key using the `ssh-keygen` command 

- `This module allows one to (re)generate OpenSSH private and public keys.`

- `It uses ssh-keygen to generate keys.`

- `One can generate rsa, dsa, rsa1, ed25519 or ecdsa private keys `

- **Parameters**
  
  - **backend** :-
    
    - `Selects` between the `cryptography` library or the `OpenSSH binary` `opensshbin`.   
    
    - `auto` will `default` to `opensshbin` unless the `OpenSSH binary is not installed or when using passphrase `

    - Choices:

       `"auto" ← (default)`

        `"cryptography"`

        `"opensshbin"`


  - **comment**
    
    - Provides a new comment to the public key.

  - **force**
    
    -  Should the key be regenerated even if it already exists

    - Choices:

        false ← (default)

        true

  - **Path**
    
    - `Name of the files containing the public and private key. The file containing the public key will have the extension .pub.`

  - **size**
    
    - `Specifies the number of bits in the private key to create. ` 

  - **state**
    
    - `Whether the private and public keys should exist or not`, `taking action if the state is different from what is stated` 
    
    - Choices:

        "present" ← (default)

        "absent"

  - **type**
    
    - `The algorithm used to generate the SSH private key `
    
    - Choices:

        "rsa" ← (default)

        "dsa"

        "rsa1"

        "ecdsa"

        "ed25519"

  - **regenerate**
    
    - `Allows to configure in which situations the module is allowed to regenerate private keys.` 
    
    - `The module will always generate a new key if the destination file does not exist.`

    - `If set to never, the module will fail if the key cannot be read or the passphrase is not matching, and will never regenerate an existing key.`

    - If `set to fail`, the `module will fail if the key does not correspond to the module’s options.`

    - If `set to partial_idempotence`, 
        
        - `the key will be regenerated if it does not conform to the module’s options`. 
        
        - `The key is not regenerated if it cannot be read (broken file), the key is protected by an unknown passphrase, or when they key is not protected by a passphrase, but a passphrase is specified.`

    - If `set to full_idempotence`, 
          
          - `the key will be regenerated if it does not conform to the module’s options.` 
          
          - `This is also the case if the key cannot be read (broken file), the key is protected by an unknown passphrase, or when they key is not protected by a passphrase, but a passphrase is specified. `
          
          - `Make sure you have a backup when using this option!`

    - `If set to always, the module will always regenerate the key. This is equivalent to setting force to true. `
 
 

 
