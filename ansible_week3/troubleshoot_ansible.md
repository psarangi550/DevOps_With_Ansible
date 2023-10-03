# Troubleshooting Ansible

- `Troubleshooting Ansible` is the part of `other ansible resources and Areas`

-  here we will look at the `Trick and Techniques` for `Troubleshooting Ansible`

- here also we will `looking at the best practises `

-  in the `Troubleshooting Ansible` we will look into 
   
   - `How to troubleshoot "SSH connectivity"`
   
   - `How to make use  of the "Syntax Checking Option" within ansible`  
   
   - `how to use "Step" to step over the task defined in ansible`
   
   - `how to check "Start At" in order to "start a particular task in ansible"`
   
   - `How to use the "Log Path" for logging info `
   
   - `How to use verbosity`     


- **How to check "SSH connectivity**

  - the `debug` module is one of way to `troubleshoot the ansible playbook`

  -  however the `problem` can be on the `lies much prior to that such as SSH connectvity Issue`

  - let suppose we have the `wrong_permission` on the `authorized_key` of the `Target Host`
  
  - if we set as `sudo chmod 777 ~/.ssh/authorized_keys` on the `Target Host System` system and now when we try to connect now `ssh ansible@ubuntu1` then it will ask for the `password`
  
  - the only `prerequisite of ansible` to have the `working ssh connectivity` 
  
  - **How to check "SSH connectivity**
    
    - we can use the `-v` option on the `ssh` command to see the complete `verbose`
    
    - if we are using the `ssh command with the -v option` then we can see that as below 

    - if we login using the below command as 

        ```bash
            
            # here we are using the bash command as below 
            ssh -v ansible@ubuntu1
            # trying to connect the ansible host on the target hosts
            # we can use that as below 
            # if the authorized_key having the correct permission then it will not ask for password 
            OpenSSH_8.9p1 Ubuntu-3ubuntu0.1, OpenSSL 3.0.2 15 Mar 2022
            debug1: Reading configuration data /etc/ssh/ssh_config
            debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
            debug1: /etc/ssh/ssh_config line 21: Applying options for *
            debug1: Connecting to ubuntu1 [172.18.0.5] port 22.
            debug1: Connection established.
            debug1: identity file /home/ansible/.ssh/id_rsa type 0
            debug1: identity file /home/ansible/.ssh/id_rsa-cert type -1
            debug1: identity file /home/ansible/.ssh/id_ecdsa type -1
            debug1: identity file /home/ansible/.ssh/id_ecdsa-cert type -1
            debug1: identity file /home/ansible/.ssh/id_ecdsa_sk type -1
            debug1: identity file /home/ansible/.ssh/id_ecdsa_sk-cert type -1
            debug1: identity file /home/ansible/.ssh/id_ed25519 type -1
            debug1: identity file /home/ansible/.ssh/id_ed25519-cert type -1
            debug1: identity file /home/ansible/.ssh/id_ed25519_sk type -1
            debug1: identity file /home/ansible/.ssh/id_ed25519_sk-cert type -1
            debug1: identity file /home/ansible/.ssh/id_xmss type -1
            debug1: identity file /home/ansible/.ssh/id_xmss-cert type -1
            debug1: identity file /home/ansible/.ssh/id_dsa type -1
            debug1: identity file /home/ansible/.ssh/id_dsa-cert type -1
            debug1: Local version string SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
            debug1: Remote protocol version 2.0, remote software version OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
            debug1: compat_banner: match: OpenSSH_8.9p1 Ubuntu-3ubuntu0.1 pat OpenSSH* compat 0x04000000
            debug1: Authenticating to ubuntu1:22 as 'ansible'
            debug1: load_hostkeys: fopen /home/ansible/.ssh/known_hosts2: No such file or directory
            debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
            debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
            debug1: SSH2_MSG_KEXINIT sent
            debug1: SSH2_MSG_KEXINIT received
            debug1: kex: algorithm: curve25519-sha256
            debug1: kex: host key algorithm: ssh-ed25519
            debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
            debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
            debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
            debug1: SSH2_MSG_KEX_ECDH_REPLY received
            debug1: Server host key: ssh-ed25519 SHA256:Bq0T7Bg1OWZDjSsLlhWtp7QjqtZitWuPQCgcXX+pXas
            debug1: load_hostkeys: fopen /home/ansible/.ssh/known_hosts2: No such file or directory
            debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
            debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
            debug1: Host 'ubuntu1' is known and matches the ED25519 host key.
            debug1: Found key in /home/ansible/.ssh/known_hosts:1
            debug1: rekey out after 134217728 blocks
            debug1: SSH2_MSG_NEWKEYS sent
            debug1: expecting SSH2_MSG_NEWKEYS
            debug1: SSH2_MSG_NEWKEYS received
            debug1: rekey in after 134217728 blocks
            debug1: Will attempt key: /home/ansible/.ssh/id_rsa RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac
            debug1: Will attempt key: /home/ansible/.ssh/id_ecdsa 
            debug1: Will attempt key: /home/ansible/.ssh/id_ecdsa_sk 
            debug1: Will attempt key: /home/ansible/.ssh/id_ed25519 
            debug1: Will attempt key: /home/ansible/.ssh/id_ed25519_sk 
            debug1: Will attempt key: /home/ansible/.ssh/id_xmss 
            debug1: Will attempt key: /home/ansible/.ssh/id_dsa 
            debug1: SSH2_MSG_EXT_INFO received
            debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519,sk-ssh-ed25519@openssh.com,ssh-rsa,rsa-sha2-256,rsa-sha2-512,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,sk-ecdsa-sha2-nistp256@openssh.com,webauthn-sk-ecdsa-sha2-nistp256@openssh.com>
            debug1: kex_input_ext_info: publickey-hostbound@openssh.com=<0>
            debug1: SSH2_MSG_SERVICE_ACCEPT received
            debug1: Authentications that can continue: publickey,password
            debug1: Next authentication method: publickey
            debug1: Offering public key: /home/ansible/.ssh/id_rsa RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac
            debug1: Server accepts key: /home/ansible/.ssh/id_rsa RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac
            Authenticated to ubuntu1 ([172.18.0.5]:22) using "publickey".
            debug1: channel 0: new [client-session]
            debug1: Requesting no-more-sessions@openssh.com
            debug1: Entering interactive session.
            debug1: pledge: filesystem
            debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
            debug1: client_input_hostkeys: searching /home/ansible/.ssh/known_hosts for ubuntu1 / (none)
            debug1: client_input_hostkeys: searching /home/ansible/.ssh/known_hosts2 for ubuntu1 / (none)
            debug1: client_input_hostkeys: hostkeys file /home/ansible/.ssh/known_hosts2 does not exist
            debug1: client_input_hostkeys: host key found matching a different name/address, skipping UserKnownHostsFile update
            debug1: Remote: /home/ansible/.ssh/authorized_keys:1: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
            debug1: Remote: /home/ansible/.ssh/authorized_keys:1: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
            debug1: Sending environment.
            Last login: Mon Oct  2 06:59:30 2023 from 172.18.0.2
        
            # if the authorized_keys of the `ansible Target host` being changed then we can see that by 
            ssh ansible@ubuntu1 # logging to the ubuntu1 system
            # the default permission for ~/.ssh/authorized_keys is of `600`
            sudo chmod 777 ~/.ssh/authorized_keys # changing the permission of the authorized_keys file 
            exit # exiting the target host in here
            # now when we are using the using the login again as the command as 
            ssh -v ansible@ubuntu1 # logging to the ubuntu1 system
            # then we can see that its been stopped on the `Next authentication method: password`step
            # here we can see the output as below 


            OpenSSH_8.9p1 Ubuntu-3ubuntu0.1, OpenSSL 3.0.2 15 Mar 2022
            debug1: Reading configuration data /etc/ssh/ssh_config
            debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
            debug1: /etc/ssh/ssh_config line 21: Applying options for *
            debug1: Connecting to ubuntu1 [172.18.0.5] port 22.
            debug1: Connection established.
            debug1: identity file /home/ansible/.ssh/id_rsa type 0
            debug1: identity file /home/ansible/.ssh/id_rsa-cert type -1
            debug1: identity file /home/ansible/.ssh/id_ecdsa type -1
            debug1: identity file /home/ansible/.ssh/id_ecdsa-cert type -1
            debug1: identity file /home/ansible/.ssh/id_ecdsa_sk type -1
            debug1: identity file /home/ansible/.ssh/id_ecdsa_sk-cert type -1
            debug1: identity file /home/ansible/.ssh/id_ed25519 type -1
            debug1: identity file /home/ansible/.ssh/id_ed25519-cert type -1
            debug1: identity file /home/ansible/.ssh/id_ed25519_sk type -1
            debug1: identity file /home/ansible/.ssh/id_ed25519_sk-cert type -1
            debug1: identity file /home/ansible/.ssh/id_xmss type -1
            debug1: identity file /home/ansible/.ssh/id_xmss-cert type -1
            debug1: identity file /home/ansible/.ssh/id_dsa type -1
            debug1: identity file /home/ansible/.ssh/id_dsa-cert type -1
            debug1: Local version string SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
            debug1: Remote protocol version 2.0, remote software version OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
            debug1: compat_banner: match: OpenSSH_8.9p1 Ubuntu-3ubuntu0.1 pat OpenSSH* compat 0x04000000
            debug1: Authenticating to ubuntu1:22 as 'ansible'
            debug1: load_hostkeys: fopen /home/ansible/.ssh/known_hosts2: No such file or directory
            debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
            debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
            debug1: SSH2_MSG_KEXINIT sent
            debug1: SSH2_MSG_KEXINIT received
            debug1: kex: algorithm: curve25519-sha256
            debug1: kex: host key algorithm: ssh-ed25519
            debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
            debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
            debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
            debug1: SSH2_MSG_KEX_ECDH_REPLY received
            debug1: Server host key: ssh-ed25519 SHA256:Bq0T7Bg1OWZDjSsLlhWtp7QjqtZitWuPQCgcXX+pXas
            debug1: load_hostkeys: fopen /home/ansible/.ssh/known_hosts2: No such file or directory
            debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
            debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
            debug1: Host 'ubuntu1' is known and matches the ED25519 host key.
            debug1: Found key in /home/ansible/.ssh/known_hosts:1
            debug1: rekey out after 134217728 blocks
            debug1: SSH2_MSG_NEWKEYS sent
            debug1: expecting SSH2_MSG_NEWKEYS
            debug1: SSH2_MSG_NEWKEYS received
            debug1: rekey in after 134217728 blocks
            debug1: Will attempt key: /home/ansible/.ssh/id_rsa RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac
            debug1: Will attempt key: /home/ansible/.ssh/id_ecdsa 
            debug1: Will attempt key: /home/ansible/.ssh/id_ecdsa_sk 
            debug1: Will attempt key: /home/ansible/.ssh/id_ed25519 
            debug1: Will attempt key: /home/ansible/.ssh/id_ed25519_sk 
            debug1: Will attempt key: /home/ansible/.ssh/id_xmss 
            debug1: Will attempt key: /home/ansible/.ssh/id_dsa 
            debug1: SSH2_MSG_EXT_INFO received
            debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519,sk-ssh-ed25519@openssh.com,ssh-rsa,rsa-sha2-256,rsa-sha2-512,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,sk-ecdsa-sha2-nistp256@openssh.com,webauthn-sk-ecdsa-sha2-nistp256@openssh.com>
            debug1: kex_input_ext_info: publickey-hostbound@openssh.com=<0>
            debug1: SSH2_MSG_SERVICE_ACCEPT received
            debug1: Authentications that can continue: publickey,password
            debug1: Next authentication method: publickey
            debug1: Offering public key: /home/ansible/.ssh/id_rsa RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac
            debug1: Authentications that can continue: publickey,password
            debug1: Trying private key: /home/ansible/.ssh/id_ecdsa
            debug1: Trying private key: /home/ansible/.ssh/id_ecdsa_sk
            debug1: Trying private key: /home/ansible/.ssh/id_ed25519
            debug1: Trying private key: /home/ansible/.ssh/id_ed25519_sk
            debug1: Trying private key: /home/ansible/.ssh/id_xmss
            debug1: Trying private key: /home/ansible/.ssh/id_dsa
            debug1: Next authentication method: password
            ansible@ubuntu1's password: 

        ```

    - if we want to see the same from the `server i.e Target Host point of view` then we can `login to any system as the root user`
    
    - we need to `connect to the remote Host` where we want to `see the changes` using the `sshd` i.e `ssh daemon service` as below 

        ```bash
            # here we first login to the rrot user of the target host as 
            ssh root@ubuntu1 # login to the ubuntu1 system in here using the password 
            #now here we need to start the sshd service with `debug mode` and `port` as `1234`
            # hence in here we can use this as below 
            /usr/sbin/sshd -d -p 1234
            # here wr using the ssh daemon utility and starting the port at 1234 with debug mode
            # now when wrr try to connect using the ansible client ubuntu-c then we can see it as below 
            # on the ansible host or client system
            ssh -v ansible@ubuntu -p 1234
            # here as the ssh connection being open on 1234 so hence we want to connect there 
            # now when we observe the connection we get the `various logsn in client and serverside`
            # if we look into the `server side log` then we will be getting the error as `Bad file permission or mode`

            # if we see the below output

            debug1: sshd version OpenSSH_8.9, OpenSSL 3.0.2 15 Mar 2022
            debug1: private host key #0: ssh-rsa SHA256:EI6vsdHY46JCSxZ3V6MsHwu35GTZwXaoQd/KGeFZOG0
            debug1: private host key #1: ecdsa-sha2-nistp256 SHA256:X7zYzNv1yap+4M+B8HyX3LJCl5+D0RLeP8XM331gLwk
            debug1: private host key #2: ssh-ed25519 SHA256:Bq0T7Bg1OWZDjSsLlhWtp7QjqtZitWuPQCgcXX+pXas
            debug1: rexec_argv[0]='/usr/sbin/sshd'
            debug1: rexec_argv[1]='-d'
            debug1: rexec_argv[2]='-p'
            debug1: rexec_argv[3]='1234'
            debug1: Set /proc/self/oom_score_adj from 0 to -1000
            debug1: Bind to port 1234 on 0.0.0.0.
            Server listening on 0.0.0.0 port 1234.
            debug1: Bind to port 1234 on ::.
            Server listening on :: port 1234.
            debug1: Server will not fork when running in debugging mode.
            debug1: rexec start in 5 out 5 newsock 5 pipe -1 sock 8
            debug1: sshd version OpenSSH_8.9, OpenSSL 3.0.2 15 Mar 2022
            debug1: private host key #0: ssh-rsa SHA256:EI6vsdHY46JCSxZ3V6MsHwu35GTZwXaoQd/KGeFZOG0
            debug1: private host key #1: ecdsa-sha2-nistp256 SHA256:X7zYzNv1yap+4M+B8HyX3LJCl5+D0RLeP8XM331gLwk
            debug1: private host key #2: ssh-ed25519 SHA256:Bq0T7Bg1OWZDjSsLlhWtp7QjqtZitWuPQCgcXX+pXas
            debug1: inetd sockets after dupping: 3, 3
            Connection from 172.18.0.2 port 40012 on 172.18.0.5 port 1234 rdomain ""
            debug1: Local version string SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
            debug1: Remote protocol version 2.0, remote software version OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
            debug1: compat_banner: match: OpenSSH_8.9p1 Ubuntu-3ubuntu0.1 pat OpenSSH* compat 0x04000000
            debug1: permanently_set_uid: 105/65534 [preauth]
            debug1: list_hostkey_types: rsa-sha2-512,rsa-sha2-256,ecdsa-sha2-nistp256,ssh-ed25519 [preauth]
            debug1: SSH2_MSG_KEXINIT sent [preauth]
            debug1: SSH2_MSG_KEXINIT received [preauth]
            debug1: kex: algorithm: curve25519-sha256 [preauth]
            debug1: kex: host key algorithm: ssh-ed25519 [preauth]
            debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none [preauth]
            debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none [preauth]
            debug1: expecting SSH2_MSG_KEX_ECDH_INIT [preauth]
            debug1: SSH2_MSG_KEX_ECDH_INIT received [preauth]
            debug1: rekey out after 134217728 blocks [preauth]
            debug1: SSH2_MSG_NEWKEYS sent [preauth]
            debug1: Sending SSH2_MSG_EXT_INFO [preauth]
            debug1: expecting SSH2_MSG_NEWKEYS [preauth]
            debug1: SSH2_MSG_NEWKEYS received [preauth]
            debug1: rekey in after 134217728 blocks [preauth]
            debug1: KEX done [preauth]
            debug1: userauth-request for user ansible service ssh-connection method none [preauth]
            debug1: attempt 0 failures 0 [preauth]
            debug1: userauth-request for user ansible service ssh-connection method publickey [preauth]
            debug1: attempt 1 failures 0 [preauth]
            debug1: userauth_pubkey: publickey test pkalg rsa-sha2-512 pkblob RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac [preauth]
            debug1: temporarily_use_uid: 1000/1000 (e=0/0)
            debug1: trying public key file /home/ansible/.ssh/authorized_keys
            debug1: fd 4 clearing O_NONBLOCK
            #Authentication refused: bad ownership or modes for file /home/ansible/.ssh/authorized_keys --- this is the error
            debug1: restore_uid: 0/0
            debug1: temporarily_use_uid: 1000/1000 (e=0/0)
            debug1: trying public key file /home/ansible/.ssh/authorized_keys2
            debug1: Could not open authorized keys '/home/ansible/.ssh/authorized_keys2': No such file or directory
            debug1: restore_uid: 0/0
            Failed publickey for ansible from 172.18.0.2 port 40012 ssh2: RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac

            # if we want to revert back to the original
            ssh root@ubuntu1 # login to the ubuntu1 system in here using the password 
            sudo chmod 600 ~/.ssh/authorized_keys # setting th correct permission 
            exit
            # then when we exit and reconnect we cn see the info as below 
            ssh -v ansible@ubuntu
            # here we are able to connect
            OpenSSH_8.9p1 Ubuntu-3ubuntu0.1, OpenSSL 3.0.2 15 Mar 2022
            debug1: Reading configuration data /etc/ssh/ssh_config
            debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
            debug1: /etc/ssh/ssh_config line 21: Applying options for *
            debug1: Connecting to ubuntu1 [172.18.0.5] port 22.
            debug1: Connection established.
            debug1: identity file /home/ansible/.ssh/id_rsa type 0
            debug1: identity file /home/ansible/.ssh/id_rsa-cert type -1
            debug1: identity file /home/ansible/.ssh/id_ecdsa type -1
            debug1: identity file /home/ansible/.ssh/id_ecdsa-cert type -1
            debug1: identity file /home/ansible/.ssh/id_ecdsa_sk type -1
            debug1: identity file /home/ansible/.ssh/id_ecdsa_sk-cert type -1
            debug1: identity file /home/ansible/.ssh/id_ed25519 type -1
            debug1: identity file /home/ansible/.ssh/id_ed25519-cert type -1
            debug1: identity file /home/ansible/.ssh/id_ed25519_sk type -1
            debug1: identity file /home/ansible/.ssh/id_ed25519_sk-cert type -1
            debug1: identity file /home/ansible/.ssh/id_xmss type -1
            debug1: identity file /home/ansible/.ssh/id_xmss-cert type -1
            debug1: identity file /home/ansible/.ssh/id_dsa type -1
            debug1: identity file /home/ansible/.ssh/id_dsa-cert type -1
            debug1: Local version string SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
            debug1: Remote protocol version 2.0, remote software version OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
            debug1: compat_banner: match: OpenSSH_8.9p1 Ubuntu-3ubuntu0.1 pat OpenSSH* compat 0x04000000
            debug1: Authenticating to ubuntu1:22 as 'ansible'
            debug1: load_hostkeys: fopen /home/ansible/.ssh/known_hosts2: No such file or directory
            debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
            debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
            debug1: SSH2_MSG_KEXINIT sent
            debug1: SSH2_MSG_KEXINIT received
            debug1: kex: algorithm: curve25519-sha256
            debug1: kex: host key algorithm: ssh-ed25519
            debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
            debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
            debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
            debug1: SSH2_MSG_KEX_ECDH_REPLY received
            debug1: Server host key: ssh-ed25519 SHA256:Bq0T7Bg1OWZDjSsLlhWtp7QjqtZitWuPQCgcXX+pXas
            debug1: load_hostkeys: fopen /home/ansible/.ssh/known_hosts2: No such file or directory
            debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory
            debug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory
            debug1: Host 'ubuntu1' is known and matches the ED25519 host key.
            debug1: Found key in /home/ansible/.ssh/known_hosts:1
            debug1: rekey out after 134217728 blocks
            debug1: SSH2_MSG_NEWKEYS sent
            debug1: expecting SSH2_MSG_NEWKEYS
            debug1: SSH2_MSG_NEWKEYS received
            debug1: rekey in after 134217728 blocks
            debug1: Will attempt key: /home/ansible/.ssh/id_rsa RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac
            debug1: Will attempt key: /home/ansible/.ssh/id_ecdsa 
            debug1: Will attempt key: /home/ansible/.ssh/id_ecdsa_sk 
            debug1: Will attempt key: /home/ansible/.ssh/id_ed25519 
            debug1: Will attempt key: /home/ansible/.ssh/id_ed25519_sk 
            debug1: Will attempt key: /home/ansible/.ssh/id_xmss 
            debug1: Will attempt key: /home/ansible/.ssh/id_dsa 
            debug1: SSH2_MSG_EXT_INFO received
            debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519,sk-ssh-ed25519@openssh.com,ssh-rsa,rsa-sha2-256,rsa-sha2-512,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,sk-ecdsa-sha2-nistp256@openssh.com,webauthn-sk-ecdsa-sha2-nistp256@openssh.com>
            debug1: kex_input_ext_info: publickey-hostbound@openssh.com=<0>
            debug1: SSH2_MSG_SERVICE_ACCEPT received
            debug1: Authentications that can continue: publickey,password
            debug1: Next authentication method: publickey
            debug1: Offering public key: /home/ansible/.ssh/id_rsa RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac
            debug1: Server accepts key: /home/ansible/.ssh/id_rsa RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac
            Authenticated to ubuntu1 ([172.18.0.5]:22) using "publickey".
            debug1: channel 0: new [client-session]
            debug1: Requesting no-more-sessions@openssh.com
            debug1: Entering interactive session.
            debug1: pledge: filesystem
            debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
            debug1: client_input_hostkeys: searching /home/ansible/.ssh/known_hosts for ubuntu1 / (none)
            debug1: client_input_hostkeys: searching /home/ansible/.ssh/known_hosts2 for ubuntu1 / (none)
            debug1: client_input_hostkeys: hostkeys file /home/ansible/.ssh/known_hosts2 does not exist
            debug1: client_input_hostkeys: host key found matching a different name/address, skipping UserKnownHostsFile update
            debug1: Remote: /home/ansible/.ssh/authorized_keys:1: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
            debug1: Remote: /home/ansible/.ssh/authorized_keys:1: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
            debug1: Sending environment.
            Last login: Tue Oct  3 03:47:12 2023 from 172.18.0.2
                    
        
        ```

- we can run the `ansible-playbook` with the `syntax checking option` as well by using the option as `ansible-playbook <playbook-name>.yaml --syntax-checking`

- this will return `playbook:<playbook-name>.yaml` if the `syntax checking` is `valid` 

- here also we have to use the `--step` if we want to `execute the ansible-playbook` by `stepping ovr each task` 

- this will be useful when we are not using the `tags` and mentioned with `--tags` option 

- if we execute the playbook as below 

    ```yaml

        troubleshoot_playbook.yaml
        ==========================

        ---

        - hosts: centos1 # targeting the centos target host

          tasks:

            - name : executing the debug module 01
              debug:  # using the debug mnodule in here
                msg: Playbook Executed-Step 1

            - name : executing the debug module 02
              debug:  # using the debug mnodule in here
                msg: Playbook Executed-Step 2

        ...

        # if we execute the playbook using the option as below 
        ansible-playbook troubleshoot_playbook.yaml --syntax-checking
        # here we are using the syntax checking option
        # the output will be as below 
        [WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under
        development. This is a rapidly changing source of code and can become unstable at any point.
        playbook: troubleshoot_playbook.yaml
       
        
        # if we want to execute the command as 
        ansible-playbook troubleshoot_playbook.yaml --step 
        # below will be the outcome of that
        [WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under
        development. This is a rapidly changing source of code and can become unstable at any point.

        PLAY [centos1] ***********************************************************************************************************************************************************************
        Perform task: TASK: Gathering Facts (N)o/(y)es/(c)ontinue: y

        Perform task: TASK: Gathering Facts (N)o/(y)es/(c)ontinue: ***************************************************************************************************************************

        TASK [Gathering Facts] ***************************************************************************************************************************************************************
        ok: [centos1]
        Perform task: TASK: executing the debug module 01 (N)o/(y)es/(c)ontinue: y

        Perform task: TASK: executing the debug module 01 (N)o/(y)es/(c)ontinue: *************************************************************************************************************

        TASK [executing the debug module 01] *************************************************************************************************************************************************
        ok: [centos1] => {
            "msg": "Playbook Executed-Step 1"
        }
        Perform task: TASK: executing the debug module 02 (N)o/(y)es/(c)ontinue: n

        Perform task: TASK: executing the debug module 02 (N)o/(y)es/(c)ontinue: *************************************************************************************************************

        PLAY RECAP ***************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
    
    
    ```

  -  if we have the `start-at-task` args which we can provide to the `named task` to particularly `execut the command over here`
    
  -  if we want to `execute a named ansible task` we can provide the `task name`  against the `--start-at-task` params while using it with the `ansible-playbook command`
  
  - when we use the `start-at-task` from that task the `playbook start executing the ansible tasks`  
  
  - here we can use this as below 

    ```bash
        ansible-playbook troubleshoot_playbook.yaml --start-at-task='executing the debug module 01'
        # here we are exicuting the troubleshoot_playbook first task then we can define as above the the output will be as below 
        # then the both task will be executed 
        [WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under
        development. This is a rapidly changing source of code and can become unstable at any point.

        PLAY [centos1] ***********************************************************************************************************************************************************************

        TASK [Gathering Facts] ***************************************************************************************************************************************************************
        ok: [centos1]

        TASK [executing the debug module 01] *************************************************************************************************************************************************
        ok: [centos1] => {
            "msg": "Playbook Executed-Step 1"
        }

        TASK [executing the debug module 02] *************************************************************************************************************************************************
        ok: [centos1] => {
            "msg": "Playbook Executed-Step 2"
        }

        PLAY RECAP ***************************************************************************************************************************************************************************
        centos1                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


        # but if mentioned as 
        ansible-playbook troubleshoot_playbook.yaml --start-at-task='executing the debug module 02'
        # then only the 2nd task exected as it starts from there 
    
        [WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under
        development. This is a rapidly changing source of code and can become unstable at any point.

        PLAY [centos1] ***********************************************************************************************************************************************************************

        TASK [Gathering Facts] ***************************************************************************************************************************************************************
        ok: [centos1]

        TASK [executing the debug module 02] *************************************************************************************************************************************************
        ok: [centos1] => {
            "msg": "Playbook Executed-Step 2"
        }

        PLAY RECAP ***************************************************************************************************************************************************************************
        centos1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    
    
    ```

- ansible `by default` will not prvide the `log for the task executed`

- but we can mention the `log_path` variable to the `ansible.cfg` file as below then we can see the `same console output in the file`

- we can write the `ansible.cfg` file in here as below 

    ```
        ansible.cfg
        ===========
        inventory=hosts
        host_key_checking=False
        fork=6
        jinja2_extension=jinja2.ext.loopcontrols
        log_path=mylogger.log

    ```

- now when we execut  the `playbook` we can see the output in the `log_path located file`

- here we can also use the `verbosity` option in ansible

- ansible has an `incresing number of verbosity` which starts from `1-4`
  
  - the `1 i.e v` option will provide the `output log`
  - the `2 i.e vv` option will provide `both the input and output log`
  - the `3 i.e vvv` option provide the `connection info the managed target host`
  - the `4 i,e vvvv` option will provide the additional info for `connection plugin` and `script` and `user context`

- if we execute the `above playbook with 4 vvvv option` then the `output` will be as below 

    ```bash
        ansible-playbook vvvv troubleshoot_playbook.yaml
        # running the yaml file in the 4 verbosity mode 
        # the output will be as below 
        [WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under
        development. This is a rapidly changing source of code and can become unstable at any point.
        ansible-playbook [core 2.17.0.dev0] (devel 4d4c50f856) last updated 2023/10/01 05:48:27 (GMT +000)
        config file = /home/ansible/diveintoansible/Creating Modules and Plugins/Creating Plugins/template/ansible.cfg
        configured module search path = ['/home/ansible/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
        ansible python module location = /home/ansible/ansible/lib/ansible
        ansible collection location = /home/ansible/.ansible/collections:/usr/share/ansible/collections
        executable location = /home/ansible/ansible/bin/ansible-playbook
        python version = 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] (/usr/bin/python)
        jinja version = 3.1.2
        libyaml = True
        Using /home/ansible/diveintoansible/Creating Modules and Plugins/Creating Plugins/template/ansible.cfg as config file
        setting up inventory plugins
        Loading collection ansible.builtin from 
        host_list declined parsing /home/ansible/diveintoansible/Creating Modules and Plugins/Creating Plugins/template/hosts as it did not pass its verify_file() method
        auto declined parsing /home/ansible/diveintoansible/Creating Modules and Plugins/Creating Plugins/template/hosts as it did not pass its verify_file() method
        Parsed /home/ansible/diveintoansible/Creating Modules and Plugins/Creating Plugins/template/hosts inventory source with ini plugin
        Loading callback plugin default of type stdout, v2.0 from /home/ansible/ansible/lib/ansible/plugins/callback/default.py
        Skipping callback 'default', as we already have a stdout callback.
        Skipping callback 'minimal', as we already have a stdout callback.
        Skipping callback 'oneline', as we already have a stdout callback.

        PLAYBOOK: troubleshoot_playbook.yaml *************************************************************************************************************************************************
        Positional arguments: troubleshoot_playbook.yaml
        verbosity: 4
        connection: ssh
        become_method: sudo
        tags: ('all',)
        inventory: ('/home/ansible/diveintoansible/Creating Modules and Plugins/Creating Plugins/template/hosts',)
        forks: 6
        1 plays in troubleshoot_playbook.yaml

        PLAY [centos1] ***********************************************************************************************************************************************************************

        TASK [Gathering Facts] ***************************************************************************************************************************************************************
        task path: /home/ansible/diveintoansible/Creating Modules and Plugins/Creating Plugins/template/troubleshoot_playbook.yaml:3
        <centos1> ESTABLISH SSH CONNECTION FOR USER: root
        <centos1> SSH: EXEC ssh -vvv -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o 'User="root"' -o ConnectTimeout=10 -o 'ControlPath="/home/ansible/.ansible/cp/d0b36aa9b1"' centos1 '/bin/sh -c '"'"'echo ~root && sleep 0'"'"''
        <centos1> (0, b'/root\n', b'OpenSSH_8.9p1 Ubuntu-3ubuntu0.1, OpenSSL 3.0.2 15 Mar 2022\r\ndebug1: Reading configuration data /etc/ssh/ssh_config\r\ndebug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files\r\ndebug1: /etc/ssh/ssh_config line 21: Applying options for *\r\ndebug3: expanded UserKnownHostsFile \'~/.ssh/known_hosts\' -> \'/home/ansible/.ssh/known_hosts\'\r\ndebug3: expanded UserKnownHostsFile \'~/.ssh/known_hosts2\' -> \'/home/ansible/.ssh/known_hosts2\'\r\ndebug1: auto-mux: Trying existing master\r\ndebug1: Control socket "/home/ansible/.ansible/cp/d0b36aa9b1" does not exist\r\ndebug2: resolving "centos1" port 2222\r\ndebug3: resolve_host: lookup centos1:2222\r\ndebug3: ssh_connect_direct: entering\r\ndebug1: Connecting to centos1 [172.18.0.7] port 2222.\r\ndebug3: set_sock_tos: set socket 3 IP_TOS 0x10\r\ndebug2: fd 3 setting O_NONBLOCK\r\ndebug1: fd 3 clearing O_NONBLOCK\r\ndebug1: Connection established.\r\ndebug3: timeout: 10000 ms remain after connect\r\ndebug1: identity file /home/ansible/.ssh/id_rsa type 0\r\ndebug1: identity file /home/ansible/.ssh/id_rsa-cert type -1\r\ndebug1: identity file /home/ansible/.ssh/id_ecdsa type -1\r\ndebug1: identity file /home/ansible/.ssh/id_ecdsa-cert type -1\r\ndebug1: identity file /home/ansible/.ssh/id_ecdsa_sk type -1\r\ndebug1: identity file /home/ansible/.ssh/id_ecdsa_sk-cert type -1\r\ndebug1: identity file /home/ansible/.ssh/id_ed25519 type -1\r\ndebug1: identity file /home/ansible/.ssh/id_ed25519-cert type -1\r\ndebug1: identity file /home/ansible/.ssh/id_ed25519_sk type -1\r\ndebug1: identity file /home/ansible/.ssh/id_ed25519_sk-cert type -1\r\ndebug1: identity file /home/ansible/.ssh/id_xmss type -1\r\ndebug1: identity file /home/ansible/.ssh/id_xmss-cert type -1\r\ndebug1: identity file /home/ansible/.ssh/id_dsa type -1\r\ndebug1: identity file /home/ansible/.ssh/id_dsa-cert type -1\r\ndebug1: Local version string SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1\r\ndebug1: Remote protocol version 2.0, remote software version OpenSSH_8.0\r\ndebug1: compat_banner: match: OpenSSH_8.0 pat OpenSSH* compat 0x04000000\r\ndebug2: fd 3 setting O_NONBLOCK\r\ndebug1: Authenticating to centos1:2222 as \'root\'\r\ndebug3: put_host_port: [centos1]:2222\r\ndebug1: load_hostkeys: fopen /home/ansible/.ssh/known_hosts2: No such file or directory\r\ndebug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory\r\ndebug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory\r\ndebug3: order_hostkeyalgs: no algorithms matched; accept original\r\ndebug3: send packet: type 20\r\ndebug1: SSH2_MSG_KEXINIT sent\r\ndebug3: receive packet: type 20\r\ndebug1: SSH2_MSG_KEXINIT received\r\ndebug2: local client KEXINIT proposal\r\ndebug2: KEX algorithms: curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,sntrup761x25519-sha512@openssh.com,diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group14-sha256,ext-info-c\r\ndebug2: host key algorithms: ssh-ed25519-cert-v01@openssh.com,ecdsa-sha2-nistp256-cert-v01@openssh.com,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp521-cert-v01@openssh.com,sk-ssh-ed25519-cert-v01@openssh.com,sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,rsa-sha2-512-cert-v01@openssh.com,rsa-sha2-256-cert-v01@openssh.com,ssh-ed25519,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,sk-ssh-ed25519@openssh.com,sk-ecdsa-sha2-nistp256@openssh.com,rsa-sha2-512,rsa-sha2-256\r\ndebug2: ciphers ctos: chacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctr,aes128-gcm@openssh.com,aes256-gcm@openssh.com\r\ndebug2: ciphers stoc: chacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctr,aes128-gcm@openssh.com,aes256-gcm@openssh.com\r\ndebug2: MACs ctos: umac-64-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-64@openssh.com,umac-128@openssh.com,hmac-sha2-256,hmac-sha2-512,hmac-sha1\r\ndebug2: MACs stoc: umac-64-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-64@openssh.com,umac-128@openssh.com,hmac-sha2-256,hmac-sha2-512,hmac-sha1\r\ndebug2: compression ctos: zlib@openssh.com,zlib,none\r\ndebug2: compression stoc: zlib@openssh.com,zlib,none\r\ndebug2: languages ctos: \r\ndebug2: languages stoc: \r\ndebug2: first_kex_follows 0 \r\ndebug2: reserved 0 \r\ndebug2: peer server KEXINIT proposal\r\ndebug2: KEX algorithms: curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group14-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1\r\ndebug2: host key algorithms: rsa-sha2-512,rsa-sha2-256,ssh-rsa,ecdsa-sha2-nistp256,ssh-ed25519\r\ndebug2: ciphers ctos: aes256-gcm@openssh.com,chacha20-poly1305@openssh.com,aes256-ctr,aes256-cbc,aes128-gcm@openssh.com,aes128-ctr,aes128-cbc\r\ndebug2: ciphers stoc: aes256-gcm@openssh.com,chacha20-poly1305@openssh.com,aes256-ctr,aes256-cbc,aes128-gcm@openssh.com,aes128-ctr,aes128-cbc\r\ndebug2: MACs ctos: hmac-sha2-256-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha1,umac-128@openssh.com,hmac-sha2-512\r\ndebug2: MACs stoc: hmac-sha2-256-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha1,umac-128@openssh.com,hmac-sha2-512\r\ndebug2: compression ctos: none,zlib@openssh.com\r\ndebug2: compression stoc: none,zlib@openssh.com\r\ndebug2: languages ctos: \r\ndebug2: languages stoc: \r\ndebug2: first_kex_follows 0 \r\ndebug2: reserved 0 \r\ndebug1: kex: algorithm: curve25519-sha256\r\ndebug1: kex: host key algorithm: ssh-ed25519\r\ndebug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: zlib@openssh.com\r\ndebug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: zlib@openssh.com\r\ndebug3: send packet: type 30\r\ndebug1: expecting SSH2_MSG_KEX_ECDH_REPLY\r\ndebug3: receive packet: type 31\r\ndebug1: SSH2_MSG_KEX_ECDH_REPLY received\r\ndebug1: Server host key: ssh-ed25519 SHA256:o0/SqFd3nZFiWf/wvAoCMh2UIk8ZEf8p3yyOLb952s8\r\ndebug3: put_host_port: [172.18.0.7]:2222\r\ndebug3: put_host_port: [centos1]:2222\r\ndebug1: load_hostkeys: fopen /home/ansible/.ssh/known_hosts2: No such file or directory\r\ndebug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory\r\ndebug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory\r\ndebug1: checking without port identifier\r\ndebug3: record_hostkey: found key type ED25519 in file /home/ansible/.ssh/known_hosts:5\r\ndebug3: load_hostkeys_file: loaded 1 keys from centos1\r\ndebug1: load_hostkeys: fopen /home/ansible/.ssh/known_hosts2: No such file or directory\r\ndebug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts: No such file or directory\r\ndebug1: load_hostkeys: fopen /etc/ssh/ssh_known_hosts2: No such file or directory\r\ndebug1: Host \'centos1\' is known and matches the ED25519 host key.\r\ndebug1: Found key in /home/ansible/.ssh/known_hosts:5\r\ndebug1: found matching key w/out port\r\ndebug1: check_host_key: hostkey not known or explicitly trusted: disabling UpdateHostkeys\r\ndebug3: send packet: type 21\r\ndebug2: ssh_set_newkeys: mode 1\r\ndebug1: rekey out after 134217728 blocks\r\ndebug1: SSH2_MSG_NEWKEYS sent\r\ndebug1: expecting SSH2_MSG_NEWKEYS\r\ndebug3: receive packet: type 21\r\ndebug1: SSH2_MSG_NEWKEYS received\r\ndebug2: ssh_set_newkeys: mode 0\r\ndebug1: rekey in after 134217728 blocks\r\ndebug1: Will attempt key: /home/ansible/.ssh/id_rsa RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac\r\ndebug1: Will attempt key: /home/ansible/.ssh/id_ecdsa \r\ndebug1: Will attempt key: /home/ansible/.ssh/id_ecdsa_sk \r\ndebug1: Will attempt key: /home/ansible/.ssh/id_ed25519 \r\ndebug1: Will attempt key: /home/ansible/.ssh/id_ed25519_sk \r\ndebug1: Will attempt key: /home/ansible/.ssh/id_xmss \r\ndebug1: Will attempt key: /home/ansible/.ssh/id_dsa \r\ndebug2: pubkey_prepare: done\r\ndebug3: send packet: type 5\r\ndebug3: receive packet: type 7\r\ndebug1: SSH2_MSG_EXT_INFO received\r\ndebug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519,ssh-rsa,rsa-sha2-256,rsa-sha2-512,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521>\r\ndebug3: receive packet: type 6\r\ndebug2: service_accept: ssh-userauth\r\ndebug1: SSH2_MSG_SERVICE_ACCEPT received\r\ndebug3: send packet: type 50\r\ndebug3: receive packet: type 51\r\ndebug1: Authentications that can continue: publickey,gssapi-keyex,gssapi-with-mic,password\r\ndebug3: start over, passed a different list publickey,gssapi-keyex,gssapi-with-mic,password\r\ndebug3: preferred gssapi-with-mic,gssapi-keyex,hostbased,publickey\r\ndebug3: authmethod_lookup gssapi-with-mic\r\ndebug3: remaining preferred: gssapi-keyex,hostbased,publickey\r\ndebug3: authmethod_is_enabled gssapi-with-mic\r\ndebug1: Next authentication method: gssapi-with-mic\r\ndebug1: No credentials were supplied, or the credentials were unavailable or inaccessible\nNo Kerberos credentials available (default cache: FILE:/tmp/krb5cc_1000)\n\n\r\ndebug1: No credentials were supplied, or the credentials were unavailable or inaccessible\nNo Kerberos credentials available (default cache: FILE:/tmp/krb5cc_1000)\n\n\r\ndebug2: we did not send a packet, disable method\r\ndebug3: authmethod_lookup gssapi-keyex\r\ndebug3: remaining preferred: hostbased,publickey\r\ndebug3: authmethod_lookup publickey\r\ndebug3: remaining preferred: ,publickey\r\ndebug3: authmethod_is_enabled publickey\r\ndebug1: Next authentication method: publickey\r\ndebug1: Offering public key: /home/ansible/.ssh/id_rsa RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac\r\ndebug3: send packet: type 50\r\ndebug2: we sent a publickey packet, wait for reply\r\ndebug3: receive packet: type 60\r\ndebug1: Server accepts key: /home/ansible/.ssh/id_rsa RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac\r\ndebug3: sign_and_send_pubkey: using publickey with RSA SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac\r\ndebug3: sign_and_send_pubkey: signing using rsa-sha2-512 SHA256:WMWqFAVrFOxVU75/9gqICFCcQykRJoTuxP7Y8Ez5Iac\r\ndebug3: send packet: type 50\r\ndebug3: receive packet: type 52\r\ndebug1: Enabling compression at level 6.\r\nAuthenticated to centos1 ([172.18.0.7]:2222) using "publickey".\r\ndebug1: setting up multiplex master socket\r\ndebug3: muxserver_listen: temporary control path /home/ansible/.ansible/cp/d0b36aa9b1.ZmqQyqeOn5DHRtKm\r\ndebug2: fd 4 setting O_NONBLOCK\r\ndebug3: fd 4 is O_NONBLOCK\r\ndebug3: fd 4 is O_NONBLOCK\r\ndebug1: channel 0: new [/home/ansible/.ansible/cp/d0b36aa9b1]\r\ndebug3: muxserver_listen: mux listener channel 0 fd 4\r\ndebug2: fd 3 setting TCP_NODELAY\r\ndebug3: set_sock_tos: set socket 3 IP_TOS 0x08\r\ndebug1: control_persist_detach: backgrounding master process\r\ndebug2: control_persist_detach: background process is 1166958\r\ndebug2: fd 4 setting O_NONBLOCK\r\ndebug1: forking to background\r\ndebug1: Entering interactive session.\r\ndebug1: pledge: id\r\ndebug2: set_control_persist_exit_time: schedule exit in 60 seconds\r\ndebug1: multiplexing control connection\r\ndebug2: fd 5 setting O_NONBLOCK\r\ndebug3: fd 5 is O_NONBLOCK\r\ndebug1: channel 1: new [mux-control]\r\ndebug3: channel_post_mux_listener: new mux channel 1 fd 5\r\ndebug3: mux_master_read_cb: channel 1: hello sent\r\ndebug2: set_control_persist_exit_time: cancel scheduled exit\r\ndebug3: mux_master_read_cb: channel 1 packet type 0x00000001 len 4\r\ndebug2: mux_master_process_hello: channel 1 client version 4\r\ndebug2: mux_client_hello_exchange: master version 4\r\ndebug3: mux_client_forwards: request forwardings: 0 local, 0 remote\r\ndebug3: mux_client_request_session: entering\r\ndebug3: mux_client_request_alive: entering\r\ndebug3: mux_master_read_cb: channel 1 packet type 0x10000004 len 4\r\ndebug2: mux_master_process_alive_check: channel 1: alive check\r\ndebug3: mux_client_request_alive: done pid = 1166960\r\ndebug3: mux_client_request_session: session request sent\r\ndebug3: mux_master_read_cb: channel 1 packet type 0x10000002 len 104\r\ndebug2: mux_master_process_new_session: channel 1: request tty 0, X 0, agent 0, subsys 0, term "xterm-256color", cmd "/bin/sh -c \'echo ~root && sleep 0\'", env 1\r\ndebug3: mux_master_process_new_session: got fds stdin 6, stdout 7, stderr 8\r\ndebug1: channel 2: new [client-session]\r\ndebug2: mux_master_process_new_session: channel_new: 2 linked to control channel 1\r\ndebug2: channel 2: send open\r\ndebug3: send packet: type 90\r\ndebug3: receive packet: type 80\r\ndebug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0\r\ndebug3: receive packet: type 4\r\ndebug1: Remote: /root/.ssh/authorized_keys:1: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding\r\ndebug3: receive packet: type 4\r\ndebug1: Remote: /root/.ssh/authorized_keys:1: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding\r\ndebug3: receive packet: type 91\r\ndebug2: channel_input_open_confirmation: channel 2: callback start\r\ndebug2: client_session2_setup: id 2\r\ndebug1: Sending environment.\r\ndebug1: channel 2: setting env LC_CTYPE = "C.UTF-8"\r\ndebug2: channel 2: request env confirm 0\r\ndebug3: send packet: type 98\r\ndebug1: Sending command: /bin/sh -c \'echo ~root && sleep 0\'\r\ndebug2: channel 2: request exec confirm 1\r\ndebug3: send packet: type 98\r\ndebug3: mux_session_confirm: sending success reply\r\ndebug2: channel_input_open_confirmation: channel 2: callback done\r\ndebug2: channel 2: open confirm rwindow 0 rmax 32768\r\ndebug1: mux_client_request_session: master session id: 2\r\ndebug2: channel 2: rcvd adjust 2097152\r\ndebug3: receive packet: type 99\r\ndebug2: channel_input_status_confirm: type 99 id 2\r\ndebug2: exec request accepted on channel 2\r\ndebug3: receive packet: type 96\r\ndebug2: channel 2: rcvd eof\r\ndebug2: channel 2: output open -> drain\r\ndebug2: channel 2: obuf empty\r\ndebug2: chan_shutdown_write: channel 2: (i0 o1 sock -1 wfd 7 efd 8 [write])\r\ndebug2: channel 2: output drain -> closed\r\ndebug3: receive packet: type 98\r\ndebug1: client_input_channel_req: channel 2 rtype exit-status reply 0\r\ndebug3: mux_exit_message: channel 2: exit message, exitval 0\r\ndebug3: receive packet: type 98\r\ndebug1: client_input_channel_req: channel 2 rtype eow@openssh.com reply 0\r\ndebug2: channel 2: rcvd eow\r\ndebug2: chan_shutdown_read: channel 2: (i0 o3 sock -1 wfd 6 efd 8 [write])\r\ndebug2: channel 2: input open -> closed\r\ndebug3: receive packet: type 97\r\ndebug2: channel 2: rcvd close\r\ndebug3: channel 2: will not send data after close\r\ndebug2: channel 2: send close\r\ndebug3: send packet: type 97\r\ndebug2: channel 2: is dead\r\ndebug2: channel 2: gc: notify user\r\ndebug3: mux_master_session_cleanup_cb: entering for channel 2\r\ndebug2: channel 1: rcvd close\r\ndebug2: channel 1: output open -> drain\r\ndebug2: chan_shutdown_read: channel 1: (i0 o1 sock 5 wfd 5 efd -1 [closed])\r\ndebug2: channel 1: input open -> closed\r\ndebug2: channel 2: gc: user detached\r\ndebug2: channel 2: is dead\r\ndebug2: channel 2: garbage collecting\r\ndebug1: channel 2: free: client-session, nchannels 3\r\ndebug3: channel 2: status: The following connections are open:\r\n  #1 mux-control (t16 nr0 i3/0 o1/16 e[closed]/0 fd 5/5/-1 sock 5 cc -1 io 0x03/0x00)\r\n  #2 client-session (t4 r0 i3/0 o3/0 e[write]/0 fd -1/-1/8 sock -1 cc -1 io 0x00/0x00)\r\n\r\ndebug2: channel 1: obuf empty\r\ndebug2: chan_shutdown_write: channel 1: (i3 o1 sock 5 wfd 5 efd -1 [closed])\r\ndebug2: channel 1: output drain -> closed\r\ndebug2: channel 1: is dead (local)\r\ndebug2: channel 1: gc: notify user\r\ndebug3: mux_master_control_cleanup_cb: entering for channel 1\r\ndebug2: channel 1: gc: user detached\r\ndebug2: channel 1: is dead (local)\r\ndebug2: channel 1: garbage collecting\r\ndebug1: channel 1: free: mux-control, nchannels 2\r\ndebug3: channel 1: status: The following connections are open:\r\n  #1 mux-control (t16 nr0 i3/0 o3/0 e[closed]/0 fd 5/5/-1 sock 5 cc -1 io 0x00/0x03)\r\n\r\ndebug2: set_control_persist_exit_time: schedule exit in 60 seconds\r\ndebug3: mux_client_read_packet: read header failed: Broken pipe\r\ndebug2: Received exit status from master 0\r\n')
        <centos1> ESTABLISH SSH CONNECTION FOR USER: root
        <centos1> SSH: EXEC ssh -vvv -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o 'User="root"' -o ConnectTimeout=10 -o 'ControlPath="/home/ansible/.ansible/cp/d0b36aa9b1"' centos1 '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo /root/.ansible/tmp `"&& mkdir "` echo /root/.ansible/tmp/ansible-tmp-1696306419.2986948-1166956-221148555562704 `" && echo ansible-tmp-1696306419.2986948-1166956-221148555562704="` echo /root/.ansible/tmp/ansible-tmp-1696306419.2986948-1166956-221148555562704 `" ) && sleep 0'"'"''
        <centos1> (0, b'ansible-tmp-1696306419.2986948-1166956-221148555562704=/root/.ansible/tmp/ansible-tmp-1696306419.2986948-1166956-221148555562704\n', b"OpenSSH_8.9p1 Ubuntu-3ubuntu0.1, OpenSSL 3.0.2 15 Mar 2022\r\ndebug1: Reading configuration data /etc/ssh/ssh_config\r\ndebug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files\r\ndebug1: /etc/ssh/ssh_config line 21: Applying options for *\r\ndebug3: expanded UserKnownHostsFile '~/.ssh/known_hosts' -> '/home/ansible/.ssh/known_hosts'\r\ndebug3: expanded UserKnownHostsFile '~/.ssh/known_hosts2' -> '/home/ansible/.ssh/known_hosts2'\r\ndebug1: auto-mux: Trying existing master\r\ndebug2: fd 3 setting O_NONBLOCK\r\ndebug2: mux_client_hello_exchange: master version 4\r\ndebug3: mux_client_forwards: request forwardings: 0 local, 0 remote\r\ndebug3: mux_client_request_session: entering\r\ndebug3: mux_client_request_alive: entering\r\ndebug3: mux_client_request_alive: done pid = 1166960\r\ndebug3: mux_client_request_session: session request sent\r\ndebug1: mux_client_request_session: master session id: 2\r\ndebug3: mux_client_read_packet: read header failed: Broken pipe\r\ndebug2: Received exit status from master 0\r\n")
        <centos1> Attempting python interpreter discovery
        <centos1> ESTABLISH SSH CONNECTION FOR USER: root
        <centos1> SSH: EXEC ssh -vvv -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o 'User="root"' -o ConnectTimeout=10 -o 'ControlPath="/home/ansible/.ansible/cp/d0b36aa9b1"' centos1 '/bin/sh -c '"'"'echo PLATFORM; uname; echo FOUND; command -v '"'"'"'"'"'"'"'"'python3.12'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.11'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.10'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.9'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.8'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.6'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python3'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/libexec/platform-python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python2.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python'"'"'"'"'"'"'"'"'; echo ENDFOUND && sleep 0'"'"''
        <centos1> (0, b'PLATFORM\nLinux\nFOUND\n/usr/bin/python3.6\n/usr/bin/python3\n/usr/libexec/platform-python\nENDFOUND\n', b"OpenSSH_8.9p1 Ubuntu-3ubuntu0.1, OpenSSL 3.0.2 15 Mar 2022\r\ndebug1: Reading configuration data /etc/ssh/ssh_config\r\ndebug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files\r\ndebug1: /etc/ssh/ssh_config line 21: Applying options for *\r\ndebug3: expanded UserKnownHostsFile '~/.ssh/known_hosts' -> '/home/ansible/.ssh/known_hosts'\r\ndebug3: expanded UserKnownHostsFile '~/.ssh/known_hosts2' -> '/home/ansible/.ssh/known_hosts2'\r\ndebug1: auto-mux: Trying existing master\r\ndebug2: fd 3 setting O_NONBLOCK\r\ndebug2: mux_client_hello_exchange: master version 4\r\ndebug3: mux_client_forwards: request forwardings: 0 local, 0 remote\r\ndebug3: mux_client_request_session: entering\r\ndebug3: mux_client_request_alive: entering\r\ndebug3: mux_client_request_alive: done pid = 1166960\r\ndebug3: mux_client_request_session: session request sent\r\ndebug1: mux_client_request_session: master session id: 2\r\ndebug3: mux_client_read_packet: read header failed: Broken pipe\r\ndebug2: Received exit status from master 0\r\n")
        <centos1> ESTABLISH SSH CONNECTION FOR USER: root
        <centos1> SSH: EXEC ssh -vvv -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o 'User="root"' -o ConnectTimeout=10 -o 'ControlPath="/home/ansible/.ansible/cp/d0b36aa9b1"' centos1 '/bin/sh -c '"'"'/usr/bin/python3.6 && sleep 0'"'"''
        <centos1> (0, b'{"platform_dist_result": ["centos", "8.4.2105", ""], "osrelease_content": "NAME=\\"CentOS Linux\\"\\nVERSION=\\"8\\"\\nID=\\"centos\\"\\nID_LIKE=\\"rhel fedora\\"\\nVERSION_ID=\\"8\\"\\nPLATFORM_ID=\\"platform:el8\\"\\nPRETTY_NAME=\\"CentOS Linux 8\\"\\nANSI_COLOR=\\"0;31\\"\\nCPE_NAME=\\"cpe:/o:centos:centos:8\\"\\nHOME_URL=\\"https://centos.org/\\"\\nBUG_REPORT_URL=\\"https://bugs.centos.org/\\"\\nCENTOS_MANTISBT_PROJECT=\\"CentOS-8\\"\\nCENTOS_MANTISBT_PROJECT_VERSION=\\"8\\"\\n"}\n', b"OpenSSH_8.9p1 Ubuntu-3ubuntu0.1, OpenSSL 3.0.2 15 Mar 2022\r\ndebug1: Reading configuration data /etc/ssh/ssh_config\r\ndebug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files\r\ndebug1: /etc/ssh/ssh_config line 21: Applying options for *\r\ndebug3: expanded UserKnownHostsFile '~/.ssh/known_hosts' -> '/home/ansible/.ssh/known_hosts'\r\ndebug3: expanded UserKnownHostsFile '~/.ssh/known_hosts2' -> '/home/ansible/.ssh/known_hosts2'\r\ndebug1: auto-mux: Trying existing master\r\ndebug2: fd 3 setting O_NONBLOCK\r\ndebug2: mux_client_hello_exchange: master version 4\r\ndebug3: mux_client_forwards: request forwardings: 0 local, 0 remote\r\ndebug3: mux_client_request_session: entering\r\ndebug3: mux_client_request_alive: entering\r\ndebug3: mux_client_request_alive: done pid = 1166960\r\ndebug3: mux_client_request_session: session request sent\r\ndebug1: mux_client_request_session: master session id: 2\r\ndebug3: mux_client_read_packet: read header failed: Broken pipe\r\ndebug2: Received exit status from master 0\r\n")
        Using module file /home/ansible/ansible/lib/ansible/modules/setup.py
        <centos1> PUT /home/ansible/.ansible/tmp/ansible-local-1166945mx_vonno/tmpda5t_9qd TO /root/.ansible/tmp/ansible-tmp-1696306419.2986948-1166956-221148555562704/AnsiballZ_setup.py
        <centos1> SSH: EXEC sftp -b - -vvv -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o 'User="root"' -o ConnectTimeout=10 -o 'ControlPath="/home/ansible/.ansible/cp/d0b36aa9b1"' '[centos1]'
        <centos1> (0, b'sftp> put /home/ansible/.ansible/tmp/ansible-local-1166945mx_vonno/tmpda5t_9qd /root/.ansible/tmp/ansible-tmp-1696306419.2986948-1166956-221148555562704/AnsiballZ_setup.py\n', b'OpenSSH_8.9p1 Ubuntu-3ubuntu0.1, OpenSSL 3.0.2 15 Mar 2022\r\ndebug1: Reading configuration data /etc/ssh/ssh_config\r\ndebug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files\r\ndebug1: /etc/ssh/ssh_config line 21: Applying options for *\r\ndebug3: expanded UserKnownHostsFile \'~/.ssh/known_hosts\' -> \'/home/ansible/.ssh/known_hosts\'\r\ndebug3: expanded UserKnownHostsFile \'~/.ssh/known_hosts2\' -> \'/home/ansible/.ssh/known_hosts2\'\r\ndebug1: auto-mux: Trying existing master\r\ndebug2: fd 3 setting O_NONBLOCK\r\ndebug2: mux_client_hello_exchange: master version 4\r\ndebug3: mux_client_forwards: request forwardings: 0 local, 0 remote\r\ndebug3: mux_client_request_session: entering\r\ndebug3: mux_client_request_alive: entering\r\ndebug3: mux_client_request_alive: done pid = 1166960\r\ndebug3: mux_client_request_session: session request sent\r\ndebug1: mux_client_request_session: master session id: 2\r\ndebug2: Remote version: 3\r\ndebug2: Server supports extension "posix-rename@openssh.com" revision 1\r\ndebug2: Server supports extension "statvfs@openssh.com" revision 2\r\ndebug2: Server supports extension "fstatvfs@openssh.com" revision 2\r\ndebug2: Server supports extension "hardlink@openssh.com" revision 1\r\ndebug2: Server supports extension "fsync@openssh.com" revision 1\r\ndebug2: Server supports extension "lsetstat@openssh.com" revision 1\r\ndebug2: Sending SSH2_FXP_REALPATH "."\r\ndebug3: Sent message fd 3 T:16 I:1\r\ndebug3: SSH2_FXP_REALPATH . -> /root\r\ndebug3: Looking up /home/ansible/.ansible/tmp/ansible-local-1166945mx_vonno/tmpda5t_9qd\r\ndebug2: Sending SSH2_FXP_STAT "/root/.ansible/tmp/ansible-tmp-1696306419.2986948-1166956-221148555562704/AnsiballZ_setup.py"\r\ndebug3: Sent message fd 3 T:17 I:2\r\ndebug1: stat remote: No such file or directory\r\ndebug2: do_upload: upload local "/home/ansible/.ansible/tmp/ansible-local-1166945mx_vonno/tmpda5t_9qd" to remote "/root/.ansible/tmp/ansible-tmp-1696306419.2986948-1166956-221148555562704/AnsiballZ_setup.py"\r\ndebug2: Sending SSH2_FXP_OPEN "/root/.ansible/tmp/ansible-tmp-1696306419.2986948-1166956-221148555562704/AnsiballZ_setup.py"\r\ndebug3: Sent dest message SSH2_FXP_OPEN I:3 P:/root/.ansible/tmp/ansible-tmp-1696306419.2986948-1166956-221148555562704/AnsiballZ_setup.py M:0x001a\r\ndebug3: Sent message SSH2_FXP_WRITE I:5 O:0 S:32768\r\ndebug3: SSH2_FXP_STATUS 0\r\ndebug3: In write loop, ack for 5 32768 bytes at 0\r\ndebug3: Sent message SSH2_FXP_WRITE I:6 O:32768 S:32768\r\ndebug3: Sent message SSH2_FXP_WRITE I:7 O:65536 S:32768\r\ndebug3: Sent message SSH2_FXP_WRITE I:8 O:98304 S:32768\r\ndebug3: Sent message SSH2_FXP_WRITE I:9 O:131072 S:32768\r\ndebug3: Sent message SSH2_FXP_WRITE I:10 O:163840 S:32768\r\ndebug3: Sent message SSH2_FXP_WRITE I:11 O:196608 S:32768\r\ndebug3: Sent message SSH2_FXP_WRITE I:12 O:229376 S:32768\r\ndebug3: Sent message SSH2_FXP_WRITE I:13 O:262144 S:32768\r\ndebug3: Sent message SSH2_FXP_WRITE I:14 O:294912 S:1291\r\ndebug3: SSH2_FXP_STATUS 0\r\ndebug3: In write loop, ack for 6 32768 bytes at 32768\r\ndebug3: SSH2_FXP_STATUS 0\r\ndebug3: In write loop, ack for 7 32768 bytes at 65536\r\ndebug3: SSH2_FXP_STATUS 0\r\ndebug3: In write loop, ack for 8 32768 bytes at 98304\r\ndebug3: SSH2_FXP_STATUS 0\r\ndebug3: In write loop, ack for 9 32768 bytes at 131072\r\ndebug3: SSH2_FXP_STATUS 0\r\ndebug3: In write loop, ack for 10 32768 bytes at 163840\r\ndebug3: SSH2_FXP_STATUS 0\r\ndebug3: In write loop, ack for 11 32768 bytes at 196608\r\ndebug3: SSH2_FXP_STATUS 0\r\ndebug3: In write loop, ack for 12 32768 bytes at 229376\r\ndebug3: SSH2_FXP_STATUS 0\r\ndebug3: In write loop, ack for 13 32768 bytes at 262144\r\ndebug3: SSH2_FXP_STATUS 0\r\ndebug3: In write loop, ack for 14 1291 bytes at 294912\r\ndebug3: Sent message SSH2_FXP_CLOSE I:4\r\ndebug3: SSH2_FXP_STATUS 0\r\ndebug3: mux_client_read_packet: read header failed: Broken pipe\r\ndebug2: Received exit status from master 0\r\n')
        <centos1> ESTABLISH SSH CONNECTION FOR USER: root
        <centos1> SSH: EXEC ssh -vvv -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o 'User="root"' -o ConnectTimeout=10 -o 'ControlPath="/home/ansible/.ansible/cp/d0b36aa9b1"' centos1 '/bin/sh -c '"'"'chmod u+x /root/.ansible/tmp/ansible-tmp-1696306419.2986948-1166956-221148555562704/ /root/.ansible/tmp/ansible-tmp-1696306419.2986948-1166956-221148555562704/AnsiballZ_setup.py && sleep 0'"'"''
        <centos1> (0, b'', b"OpenSSH_8.9p1 Ubuntu-3ubuntu0.1, OpenSSL 3.0.2 15 Mar 2022\r\ndebug1: Reading configuration data /etc/ssh/ssh_config\r\ndebug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files\r\ndebug1: /etc/ssh/ssh_config line 21: Applying options for *\r\ndebug3: expanded UserKnownHostsFile '~/.ssh/known_hosts' -> '/home/ansible/.ssh/known_hosts'\r\ndebug3: expanded UserKnownHostsFile '~/.ssh/known_hosts2' -> '/home/ansible/.ssh/known_hosts2'\r\ndebug1: auto-mux: Trying existing master\r\ndebug2: fd 3 setting O_NONBLOCK\r\ndebug2: mux_client_hello_exchange: master version 4\r\ndebug3: mux_client_forwards: request forwardings: 0 local, 0 remote\r\ndebug3: mux_client_request_session: entering\r\ndebug3: mux_client_request_alive: entering\r\ndebug3: mux_client_request_alive: done pid = 1166960\r\ndebug3: mux_client_request_session: session request sent\r\ndebug1: mux_client_request_session: master session id: 2\r\ndebug3: mux_client_read_packet: read header failed: Broken pipe\r\ndebug2: Received exit status from master 0\r\n")
        <centos1> ESTABLISH SSH CONNECTION FOR USER: root
        <centos1> SSH: EXEC ssh -vvv -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o 'User="root"' -o ConnectTimeout=10 -o 'ControlPath="/home/ansible/.ansible/cp/d0b36aa9b1"' -tt centos1 '/bin/sh -c '"'"'/usr/libexec/platform-python /root/.ansible/tmp/ansible-tmp-1696306419.2986948-1166956-221148555562704/AnsiballZ_setup.py && sleep 0'"'"''
        <centos1> (0, b'\r\n{"ansible_facts": {"ansible_env": {"SSH_CONNECTION": "172.18.0.2 42078 172.18.0.7 2222", "_": "/usr/libexec/platform-python", "USER": "root", "PWD": "/root", "HOME": "/root", "LC_CTYPE": "C.UTF-8", "SSH_CLIENT": "172.18.0.2 42078 2222", "SSH_TTY": "/dev/pts/0", "MAIL": "/var/mail/root", "SHELL": "/bin/bash", "TERM": "xterm-256color", "SHLVL": "2", "LOGNAME": "root", "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin"}, "ansible_fips": false, "ansible_ssh_host_key_dsa_public": "AAAAB3NzaC1kc3MAAACBAMc+MKJeZkz3I/q7yCBxkZMMDiAV4nkfSBlqYspz0hnUb69zWr5edGpBQmCyeXOWu6uGB1gsupSmmkSCIm4H5KK4sUtQWoFBs974rd9N+QA/ch/njNMOdZ0v/xmZeEEUovmvCgfCkXZbFAPltQXEgRGL46PGwf8XwY4Kyf24Fg/TAAAAFQDOLGnoj9z6Cz9dj5XRWvo/hdzc5QAAAIBWHBdhH4EXBi31nNPHePUVZuzXolDWbfM1EKMvNkviitqBavi7zeXhWsXYyFmqukWFiZDKqSHpJpnD+QEzVONdVNkPrzPsLhLVqCILJFrxvurjOP2F+z5iFw1HB7Qxxf8A7nbhLImXvJM4WdH6QFd/z7JIu9n+u5HzeClcrcBxuwAAAIEAkRihglWIRMRh8Eed1MenDbmn1M4VEsB7oUi0qqaixwCC2KBGaWGoDFtTkzUYd2GwHV77tVIsh1AjaYV3oJwRXFYyR36fvVzY7JlJVuFI2ClejvSJgEywSUCkkzVpve29QsQustmIS4HhyCkOTyRS3zw//IqvyYQxXT1UpWfGzVo=", "ansible_ssh_host_key_dsa_public_keytype": "ssh-dss", "ansible_ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABgQDb9CfJ9QLVATsHCW/DErk6Q+/xSVWedO4zW/RS9YMRYc/+RpYoTVnxspI+PssmbDvNNKD8p+ohdlcsfktp9ktP029R3F3PJb2worMCaX6jAALL+oiY1Qu5x5ou2i2W7pA/pU1GdknPoC3qqQTv8Mflozewyk//2X3aRzkNlIPGgOzQ21BhYAA780kcPXIIZi0kfFLG8R6vyCIdlANG0HqR/2jeUMboiWHZWp3gNqu7PP0KlbD9BxJEYh8Is7MTIgWjrd9/AZku9R4RJN288n46UYQ4wBjSnDE+TWJwY4LvUvJ5a5sPpejAFX/PUSAKjHvVJszAVmDUTBk2N3FY6mkKcKZyGSMLs3j9mFKnqmKC+JBK/YUleDFoo+y3uX6ybugEuhUTICpCVSKGYgMMmCbJQ/EqyQ/ND49aMaHTyQ6BPA9xZfkkucMF9CA4iJPQINc4i7VFyS0YuWOvP/c12JNFu6s9RujzCnLLt52mGESZovfmVRL/cOGJllaxrgvoaxs=", "ansible_ssh_host_key_rsa_public_keytype": "ssh-rsa", "ansible_ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJP9kXOAoc9yoimx5K2eNtDFVD3kumTA6u41CqWrK0ijLJsj2sccX6fITgRjSrQS4jyts/tt1ucXsLayZ0I0l3g=", "ansible_ssh_host_key_ecdsa_public_keytype": "ecdsa-sha2-nistp256", "ansible_ssh_host_key_ed25519_public": "AAAAC3NzaC1lZDI1NTE5AAAAINd52rW3hcDwuIHgNgiO8qHQKWosHzFvYnAgXsmVvUUX", "ansible_ssh_host_key_ed25519_public_keytype": "ssh-ed25519", "ansible_date_time": {"year": "2023", "month": "10", "weekday": "Tuesday", "weekday_number": "2", "weeknumber": "40", "day": "03", "hour": "04", "minute": "13", "second": "39", "epoch": "1696306419", "epoch_int": "1696306419", "date": "2023-10-03", "time": "04:13:39", "iso8601_micro": "2023-10-03T04:13:39.974190Z", "iso8601": "2023-10-03T04:13:39Z", "iso8601_basic": "20231003T041339974190", "iso8601_basic_short": "20231003T041339", "tz": "UTC", "tz_dst": "UTC", "tz_offset": "+0000"}, "ansible_is_chroot": false, "ansible_system": "Linux", "ansible_kernel": "6.2.0-33-generic", "ansible_kernel_version": "#33~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep  7 10:33:52 UTC 2", "ansible_machine": "x86_64", "ansible_python_version": "3.6.8", "ansible_fqdn": "centos1", "ansible_hostname": "centos1", "ansible_nodename": "centos1", "ansible_domain": "", "ansible_userspace_bits": "64", "ansible_architecture": "x86_64", "ansible_userspace_architecture": "x86_64", "ansible_machine_id": "1110b27f44434a0bbab14d189d23d62d", "ansible_dns": {"search": ["localdomain"], "nameservers": ["127.0.0.11"], "options": {"edns0": true, "trust-ad": true, "ndots": "0"}}, "ansible_system_capabilities_enforced": "True", "ansible_system_capabilities": ["cap_chown", "cap_dac_override", "cap_dac_read_search", "cap_fowner", "cap_fsetid", "cap_kill", "cap_setgid", "cap_setuid", "cap_setpcap", "cap_linux_immutable", "cap_net_bind_service", "cap_net_broadcast", "cap_net_admin", "cap_net_raw", "cap_ipc_lock", "cap_ipc_owner", "cap_sys_module", "cap_sys_rawio", "cap_sys_chroot", "cap_sys_ptrace", "cap_sys_pacct", "cap_sys_admin", "cap_sys_boot", "cap_sys_nice", "cap_sys_resource", "cap_sys_time", "cap_sys_tty_config", "cap_mknod", "cap_lease", "cap_audit_write", "cap_audit_control", "cap_setfcap", "cap_mac_override", "cap_mac_admin", "cap_syslog", "cap_wake_alarm", "cap_block_suspend", "cap_audit_read", "38", "39", "40+ep"], "ansible_user_id": "root", "ansible_user_uid": 0, "ansible_user_gid": 0, "ansible_user_gecos": "root", "ansible_user_dir": "/root", "ansible_user_shell": "/bin/bash", "ansible_real_user_id": 0, "ansible_effective_user_id": 0, "ansible_real_group_id": 0, "ansible_effective_group_id": 0, "ansible_distribution": "CentOS", "ansible_distribution_release": "NA", "ansible_distribution_version": "8.4", "ansible_distribution_major_version": "8", "ansible_distribution_file_path": "/etc/redhat-release", "ansible_distribution_file_variety": "RedHat", "ansible_distribution_file_parsed": true, "ansible_os_family": "RedHat", "ansible_local": {}, "ansible_processor": ["0", "GenuineIntel", "11th Gen Intel(R) Core(TM) i7-11850H @ 2.50GHz", "1", "GenuineIntel", "11th Gen Intel(R) Core(TM) i7-11850H @ 2.50GHz", "2", "GenuineIntel", "11th Gen Intel(R) Core(TM) i7-11850H @ 2.50GHz", "3", "GenuineIntel", "11th Gen Intel(R) Core(TM) i7-11850H @ 2.50GHz", "4", "GenuineIntel", "11th Gen Intel(R) Core(TM) i7-11850H @ 2.50GHz", "5", "GenuineIntel", "11th Gen Intel(R) Core(TM) i7-11850H @ 2.50GHz", "6", "GenuineIntel", "11th Gen Intel(R) Core(TM) i7-11850H @ 2.50GHz", "7", "GenuineIntel", "11th Gen Intel(R) Core(TM) i7-11850H @ 2.50GHz"], "ansible_processor_count": 4, "ansible_processor_cores": 2, "ansible_processor_threads_per_core": 1, "ansible_processor_vcpus": 8, "ansible_processor_nproc": 8, "ansible_memtotal_mb": 7897, "ansible_memfree_mb": 144, "ansible_swaptotal_mb": 2047, "ansible_swapfree_mb": 0, "ansible_memory_mb": {"real": {"total": 7897, "used": 7753, "free": 144}, "nocache": {"free": 991, "used": 6906}, "swap": {"total": 2047, "free": 0, "used": 2047, "cached": 77}}, "ansible_bios_date": "11/12/2020", "ansible_bios_vendor": "Phoenix Technologies LTD", "ansible_bios_version": "6.00", "ansible_board_asset_tag": "NA", "ansible_board_name": "440BX Desktop Reference Platform", "ansible_board_serial": "None", "ansible_board_vendor": "Intel Corporation", "ansible_board_version": "None", "ansible_chassis_asset_tag": "No Asset Tag", "ansible_chassis_serial": "None", "ansible_chassis_vendor": "No Enclosure", "ansible_chassis_version": "N/A", "ansible_form_factor": "Other", "ansible_product_name": "VMware Virtual Platform", "ansible_product_serial": "VMware-56 4d 38 8b b1 fc b9 da-c3 be 8c 41 f0 63 d3 d1", "ansible_product_uuid": "8b384d56-fcb1-dab9-c3be-8c41f063d3d1", "ansible_product_version": "None", "ansible_system_vendor": "VMware, Inc.", "ansible_devices": {"loop1": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "620640", "sectorsize": "512", "size": "303.05 MB", "host": "", "holders": []}, "loop19": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "1265184", "sectorsize": "512", "size": "617.77 MB", "host": "", "holders": []}, "loop17": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "83648", "sectorsize": "512", "size": "40.84 MB", "host": "", "holders": []}, "loop8": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "485064", "sectorsize": "512", "size": "236.85 MB", "host": "", "holders": []}, "loop15": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "25240", "sectorsize": "512", "size": "12.32 MB", "host": "", "holders": []}, "loop6": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "151296", "sectorsize": "512", "size": "73.88 MB", "host": "", "holders": []}, "loop13": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "187776", "sectorsize": "512", "size": "91.69 MB", "host": "", "holders": []}, "loop4": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "129944", "sectorsize": "512", "size": "63.45 MB", "host": "", "holders": []}, "loop11": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "1017608", "sectorsize": "512", "size": "496.88 MB", "host": "", "holders": []}, "sr0": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": "NECVMWar", "model": "VMware SATA CD01", "sas_address": null, "sas_device_handle": null, "removable": "1", "support_discard": "0", "partitions": {}, "rotational": "1", "scheduler_mode": "mq-deadline", "sectors": "9839184", "sectorsize": "2048", "size": "4.69 GB", "host": "SATA controller: VMware SATA AHCI controller", "holders": []}, "loop2": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "620632", "sectorsize": "512", "size": "303.04 MB", "host": "", "holders": []}, "loop0": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "8", "sectorsize": "512", "size": "4.00 KB", "host": "", "holders": []}, "loop18": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "904", "sectorsize": "512", "size": "452.00 KB", "host": "", "holders": []}, "loop9": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "485192", "sectorsize": "512", "size": "236.91 MB", "host": "", "holders": []}, "loop16": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "109072", "sectorsize": "512", "size": "53.26 MB", "host": "", "holders": []}, "loop7": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "151352", "sectorsize": "512", "size": "73.90 MB", "host": "", "holders": []}, "sda": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": "VMware,", "model": "VMware Virtual S", "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "0", "partitions": {"sda2": {"links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "start": "4096", "sectors": "1050624", "sectorsize": 512, "size": "513.00 MB", "uuid": null, "holders": []}, "sda3": {"links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "start": "1054720", "sectors": "208658432", "sectorsize": 512, "size": "99.50 GB", "uuid": null, "holders": []}, "sda1": {"links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "start": "2048", "sectors": "2048", "sectorsize": 512, "size": "1.00 MB", "uuid": null, "holders": []}}, "rotational": "1", "scheduler_mode": "mq-deadline", "sectors": "209715200", "sectorsize": "512", "size": "100.00 GB", "host": "SCSI storage controller: Broadcom / LSI 53c1030 PCI-X Fusion-MPT Dual Ultra320 SCSI (rev 01)", "holders": []}, "loop14": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "1263816", "sectorsize": "512", "size": "617.10 MB", "host": "", "holders": []}, "loop5": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "129976", "sectorsize": "512", "size": "63.46 MB", "host": "", "holders": []}, "loop12": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "1017816", "sectorsize": "512", "size": "496.98 MB", "host": "", "holders": []}, "loop3": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "113992", "sectorsize": "512", "size": "55.66 MB", "host": "", "holders": []}, "loop10": {"virtual": 1, "links": {"ids": [], "uuids": [], "labels": [], "masters": []}, "vendor": null, "model": null, "sas_address": null, "sas_device_handle": null, "removable": "0", "support_discard": "4096", "partitions": {}, "rotational": "1", "scheduler_mode": "none", "sectors": "716176", "sectorsize": "512", "size": "349.70 MB", "host": "", "holders": []}}, "ansible_device_links": {"ids": {}, "uuids": {}, "labels": {}, "masters": {}}, "ansible_uptime_seconds": 115387, "ansible_lvm": "N/A", "ansible_mounts": [{"mount": "/config", "device": "/dev/sda3", "fstype": "ext4", "options": "rw,relatime,errors=remount-ro,bind", "dump": 0, "passno": 0, "size_total": 104556617728, "size_available": 68988067840, "block_size": 4096, "block_total": 25526518, "block_available": 16842790, "block_used": 8683728, "inode_total": 6520832, "inode_available": 5892690, "inode_used": 628142, "uuid": "N/A"}, {"mount": "/root", "device": "/dev/sda3", "fstype": "ext4", "options": "rw,relatime,errors=remount-ro,bind", "dump": 0, "passno": 0, "size_total": 104556617728, "size_available": 68988067840, "block_size": 4096, "block_total": 25526518, "block_available": 16842790, "block_used": 8683728, "inode_total": 6520832, "inode_available": 5892690, "inode_used": 628142, "uuid": "N/A"}, {"mount": "/shared", "device": "/dev/sda3", "fstype": "ext4", "options": "rw,relatime,errors=remount-ro,bind", "dump": 0, "passno": 0, "size_total": 104556617728, "size_available": 68988067840, "block_size": 4096, "block_total": 25526518, "block_available": 16842790, "block_used": 8683728, "inode_total": 6520832, "inode_available": 5892690, "inode_used": 628142, "uuid": "N/A"}, {"mount": "/home/ansible", "device": "/dev/sda3", "fstype": "ext4", "options": "rw,relatime,errors=remount-ro,bind", "dump": 0, "passno": 0, "size_total": 104556617728, "size_available": 68988067840, "block_size": 4096, "block_total": 25526518, "block_available": 16842790, "block_used": 8683728, "inode_total": 6520832, "inode_available": 5892690, "inode_used": 628142, "uuid": "N/A"}, {"mount": "/etc/resolv.conf", "device": "/dev/sda3", "fstype": "ext4", "options": "rw,relatime,errors=remount-ro,bind", "dump": 0, "passno": 0, "size_total": 104556617728, "size_available": 68988067840, "block_size": 4096, "block_total": 25526518, "block_available": 16842790, "block_used": 8683728, "inode_total": 6520832, "inode_available": 5892690, "inode_used": 628142, "uuid": "N/A"}, {"mount": "/etc/hostname", "device": "/dev/sda3", "fstype": "ext4", "options": "rw,relatime,errors=remount-ro,bind", "dump": 0, "passno": 0, "size_total": 104556617728, "size_available": 68988067840, "block_size": 4096, "block_total": 25526518, "block_available": 16842790, "block_used": 8683728, "inode_total": 6520832, "inode_available": 5892690, "inode_used": 628142, "uuid": "N/A"}, {"mount": "/etc/hosts", "device": "/dev/sda3", "fstype": "ext4", "options": "rw,relatime,errors=remount-ro,bind", "dump": 0, "passno": 0, "size_total": 104556617728, "size_available": 68988067840, "block_size": 4096, "block_total": 25526518, "block_available": 16842790, "block_used": 8683728, "inode_total": 6520832, "inode_available": 5892690, "inode_used": 628142, "uuid": "N/A"}], "ansible_virtualization_type": "container", "ansible_virtualization_role": "guest", "ansible_virtualization_tech_guest": ["docker", "container", "VMware"], "ansible_virtualization_tech_host": [], "ansible_lsb": {}, "ansible_cmdline": {"BOOT_IMAGE": "/boot/vmlinuz-6.2.0-33-generic", "root": "UUID=59f920ea-3233-4507-a353-7b4e56872cc1", "ro": true, "quiet": true, "splash": true}, "ansible_proc_cmdline": {"BOOT_IMAGE": "/boot/vmlinuz-6.2.0-33-generic", "root": "UUID=59f920ea-3233-4507-a353-7b4e56872cc1", "ro": true, "quiet": true, "splash": true}, "ansible_selinux_python_present": true, "ansible_selinux": {"status": "disabled"}, "ansible_loadavg": {"1m": 0.91, "5m": 1.11, "15m": 1.03}, "ansible_apparmor": {"status": "disabled"}, "ansible_hostnqn": "", "ansible_iscsi_iqn": "", "ansible_fibre_channel_wwn": [], "ansible_interfaces": ["lo", "eth0"], "ansible_eth0": {"device": "eth0", "macaddress": "02:42:ac:12:00:07", "mtu": 1500, "active": true, "type": "ether", "speed": 10000, "promisc": false, "ipv4": {"address": "172.18.0.7", "broadcast": "172.18.255.255", "netmask": "255.255.0.0", "network": "172.18.0.0", "prefix": "16"}, "features": {"rx_checksumming": "on", "tx_checksumming": "on", "tx_checksum_ipv4": "off [fixed]", "tx_checksum_ip_generic": "on", "tx_checksum_ipv6": "off [fixed]", "tx_checksum_fcoe_crc": "off [fixed]", "tx_checksum_sctp": "on", "scatter_gather": "on", "tx_scatter_gather": "on", "tx_scatter_gather_fraglist": "on", "tcp_segmentation_offload": "on", "tx_tcp_segmentation": "on", "tx_tcp_ecn_segmentation": "on", "tx_tcp_mangleid_segmentation": "on", "tx_tcp6_segmentation": "on", "generic_segmentation_offload": "on", "generic_receive_offload": "off", "large_receive_offload": "off [fixed]", "rx_vlan_offload": "on", "tx_vlan_offload": "on", "ntuple_filters": "off [fixed]", "receive_hashing": "off [fixed]", "highdma": "on", "rx_vlan_filter": "off [fixed]", "vlan_challenged": "off [fixed]", "tx_lockless": "on [fixed]", "netns_local": "off [fixed]", "tx_gso_robust": "off [fixed]", "tx_fcoe_segmentation": "off [fixed]", "tx_gre_segmentation": "on", "tx_gre_csum_segmentation": "on", "tx_ipxip4_segmentation": "on", "tx_ipxip6_segmentation": "on", "tx_udp_tnl_segmentation": "on", "tx_udp_tnl_csum_segmentation": "on", "tx_gso_partial": "off [fixed]", "tx_tunnel_remcsum_segmentation": "off [fixed]", "tx_sctp_segmentation": "on", "tx_esp_segmentation": "off [fixed]", "tx_udp_segmentation": "on", "tx_gso_list": "on", "fcoe_mtu": "off [fixed]", "tx_nocache_copy": "off", "loopback": "off [fixed]", "rx_fcs": "off [fixed]", "rx_all": "off [fixed]", "tx_vlan_stag_hw_insert": "on", "rx_vlan_stag_hw_parse": "on", "rx_vlan_stag_filter": "off [fixed]", "l2_fwd_offload": "off [fixed]", "hw_tc_offload": "off [fixed]", "esp_hw_offload": "off [fixed]", "esp_tx_csum_hw_offload": "off [fixed]", "rx_udp_tunnel_port_offload": "off [fixed]", "tls_hw_tx_offload": "off [fixed]", "tls_hw_rx_offload": "off [fixed]", "rx_gro_hw": "off [fixed]", "tls_hw_record": "off [fixed]", "rx_gro_list": "off", "macsec_hw_offload": "off [fixed]", "rx_udp_gro_forwarding": "off", "hsr_tag_ins_offload": "off [fixed]", "hsr_tag_rm_offload": "off [fixed]", "hsr_fwd_offload": "off [fixed]", "hsr_dup_offload": "off [fixed]"}, "timestamping": [], "hw_timestamp_filters": []}, "ansible_lo": {"device": "lo", "mtu": 65536, "active": true, "type": "loopback", "promisc": false, "ipv4": {"address": "127.0.0.1", "broadcast": "", "netmask": "255.0.0.0", "network": "127.0.0.0", "prefix": "8"}, "features": {"rx_checksumming": "on [fixed]", "tx_checksumming": "on", "tx_checksum_ipv4": "off [fixed]", "tx_checksum_ip_generic": "on [fixed]", "tx_checksum_ipv6": "off [fixed]", "tx_checksum_fcoe_crc": "off [fixed]", "tx_checksum_sctp": "on [fixed]", "scatter_gather": "on", "tx_scatter_gather": "on [fixed]", "tx_scatter_gather_fraglist": "on [fixed]", "tcp_segmentation_offload": "on", "tx_tcp_segmentation": "on", "tx_tcp_ecn_segmentation": "on", "tx_tcp_mangleid_segmentation": "on", "tx_tcp6_segmentation": "on", "generic_segmentation_offload": "on", "generic_receive_offload": "on", "large_receive_offload": "off [fixed]", "rx_vlan_offload": "off [fixed]", "tx_vlan_offload": "off [fixed]", "ntuple_filters": "off [fixed]", "receive_hashing": "off [fixed]", "highdma": "on [fixed]", "rx_vlan_filter": "off [fixed]", "vlan_challenged": "on [fixed]", "tx_lockless": "on [fixed]", "netns_local": "on [fixed]", "tx_gso_robust": "off [fixed]", "tx_fcoe_segmentation": "off [fixed]", "tx_gre_segmentation": "off [fixed]", "tx_gre_csum_segmentation": "off [fixed]", "tx_ipxip4_segmentation": "off [fixed]", "tx_ipxip6_segmentation": "off [fixed]", "tx_udp_tnl_segmentation": "off [fixed]", "tx_udp_tnl_csum_segmentation": "off [fixed]", "tx_gso_partial": "off [fixed]", "tx_tunnel_remcsum_segmentation": "off [fixed]", "tx_sctp_segmentation": "on", "tx_esp_segmentation": "off [fixed]", "tx_udp_segmentation": "on", "tx_gso_list": "on", "fcoe_mtu": "off [fixed]", "tx_nocache_copy": "off [fixed]", "loopback": "on [fixed]", "rx_fcs": "off [fixed]", "rx_all": "off [fixed]", "tx_vlan_stag_hw_insert": "off [fixed]", "rx_vlan_stag_hw_parse": "off [fixed]", "rx_vlan_stag_filter": "off [fixed]", "l2_fwd_offload": "off [fixed]", "hw_tc_offload": "off [fixed]", "esp_hw_offload": "off [fixed]", "esp_tx_csum_hw_offload": "off [fixed]", "rx_udp_tunnel_port_offload": "off [fixed]", "tls_hw_tx_offload": "off [fixed]", "tls_hw_rx_offload": "off [fixed]", "rx_gro_hw": "off [fixed]", "tls_hw_record": "off [fixed]", "rx_gro_list": "off", "macsec_hw_offload": "off [fixed]", "rx_udp_gro_forwarding": "off", "hsr_tag_ins_offload": "off [fixed]", "hsr_tag_rm_offload": "off [fixed]", "hsr_fwd_offload": "off [fixed]", "hsr_dup_offload": "off [fixed]"}, "timestamping": [], "hw_timestamp_filters": []}, "ansible_default_ipv4": {"gateway": "172.18.0.1", "interface": "eth0", "address": "172.18.0.7", "broadcast": "172.18.255.255", "netmask": "255.255.0.0", "network": "172.18.0.0", "prefix": "16", "macaddress": "02:42:ac:12:00:07", "mtu": 1500, "type": "ether", "alias": "eth0"}, "ansible_default_ipv6": {}, "ansible_all_ipv4_addresses": ["172.18.0.7"], "ansible_all_ipv6_addresses": [], "ansible_locally_reachable_ips": {"ipv4": ["127.0.0.0/8", "127.0.0.1", "172.18.0.7"], "ipv6": []}, "ansible_python": {"version": {"major": 3, "minor": 6, "micro": 8, "releaselevel": "final", "serial": 0}, "version_info": [3, 6, 8, "final", 0], "executable": "/usr/libexec/platform-python", "has_sslcontext": true, "type": "cpython"}, "ansible_pkg_mgr": "dnf", "ansible_service_mgr": "systemd", "gather_subset": ["all"], "module_setup": true}, "invocation": {"module_args": {"gather_subset": ["all"], "gather_timeout": 10, "filter": [], "fact_path": "/etc/ansible/facts.d"}}}\r\n', b"OpenSSH_8.9p1 Ubuntu-3ubuntu0.1, OpenSSL 3.0.2 15 Mar 2022\r\ndebug1: Reading configuration data /etc/ssh/ssh_config\r\ndebug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files\r\ndebug1: /etc/ssh/ssh_config line 21: Applying options for *\r\ndebug3: expanded UserKnownHostsFile '~/.ssh/known_hosts' -> '/home/ansible/.ssh/known_hosts'\r\ndebug3: expanded UserKnownHostsFile '~/.ssh/known_hosts2' -> '/home/ansible/.ssh/known_hosts2'\r\ndebug1: auto-mux: Trying existing master\r\ndebug2: fd 3 setting O_NONBLOCK\r\ndebug2: mux_client_hello_exchange: master version 4\r\ndebug3: mux_client_forwards: request forwardings: 0 local, 0 remote\r\ndebug3: mux_client_request_session: entering\r\ndebug3: mux_client_request_alive: entering\r\ndebug3: mux_client_request_alive: done pid = 1166960\r\ndebug3: mux_client_request_session: session request sent\r\ndebug1: mux_client_request_session: master session id: 2\r\ndebug3: mux_client_read_packet: read header failed: Broken pipe\r\ndebug2: Received exit status from master 0\r\nShared connection to centos1 closed.\r\n")
        <centos1> ESTABLISH SSH CONNECTION FOR USER: root
        <centos1> SSH: EXEC ssh -vvv -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o 'User="root"' -o ConnectTimeout=10 -o 'ControlPath="/home/ansible/.ansible/cp/d0b36aa9b1"' centos1 '/bin/sh -c '"'"'rm -f -r /root/.ansible/tmp/ansible-tmp-1696306419.2986948-1166956-221148555562704/ > /dev/null 2>&1 && sleep 0'"'"''
        <centos1> (0, b'', b"OpenSSH_8.9p1 Ubuntu-3ubuntu0.1, OpenSSL 3.0.2 15 Mar 2022\r\ndebug1: Reading configuration data /etc/ssh/ssh_config\r\ndebug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files\r\ndebug1: /etc/ssh/ssh_config line 21: Applying options for *\r\ndebug3: expanded UserKnownHostsFile '~/.ssh/known_hosts' -> '/home/ansible/.ssh/known_hosts'\r\ndebug3: expanded UserKnownHostsFile '~/.ssh/known_hosts2' -> '/home/ansible/.ssh/known_hosts2'\r\ndebug1: auto-mux: Trying existing master\r\ndebug2: fd 3 setting O_NONBLOCK\r\ndebug2: mux_client_hello_exchange: master version 4\r\ndebug3: mux_client_forwards: request forwardings: 0 local, 0 remote\r\ndebug3: mux_client_request_session: entering\r\ndebug3: mux_client_request_alive: entering\r\ndebug3: mux_client_request_alive: done pid = 1166960\r\ndebug3: mux_client_request_session: session request sent\r\ndebug1: mux_client_request_session: master session id: 2\r\ndebug3: mux_client_read_packet: read header failed: Broken pipe\r\ndebug2: Received exit status from master 0\r\n")
        ok: [centos1]

        TASK [executing the debug module 01] *************************************************************************************************************************************************
        task path: /home/ansible/diveintoansible/Creating Modules and Plugins/Creating Plugins/template/troubleshoot_playbook.yaml:7
        ok: [centos1] => {
            "msg": "Playbook Executed-Step 1"
        }

        TASK [executing the debug module 02] *************************************************************************************************************************************************
        task path: /home/ansible/diveintoansible/Creating Modules and Plugins/Creating Plugins/template/troubleshoot_playbook.yaml:11
        ok: [centos1] => {
            "msg": "Playbook Executed-Step 2"
        }

        PLAY RECAP ***************************************************************************************************************************************************************************
        centos1                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


    ```








