
# <ins> unarchive Module </ins> #

- `The unarchive module unpacks an archive.` `It will not unpack a compressed file that does not contain an archive.`

- `By default, it will copy the source file from the local system to the target before unpacking.`

- Set `remote_src=yes` to `unpack an archive which already exists on the target.`

- If `checksum validation is desired`, use `ansible.builtin.get_url or ansible.builtin.uri ` `instead to fetch the file and set remote_src=yes.`

- `For Windows targets, use the community.windows.win_unzip module instead.`


- **Parameters**

- **copy**

- `copy` :- `If true, the file is copied from local controller to the managed (remote) node`, `otherwise, the plugin will look for src archive on the managed machine`.

- This `option has been deprecated` in favor of `remote_src`.

- `This option is mutually exclusive with remote_src.`

- `Choices`:

    `false`

    `true ← (default)`

- **creates**

- `If the specified absolute path (file or directory) already exists, this step will not be run.`

- `The specified absolute path (file or directory) must be below the base path given with dest:.`


- **dest**

- `Remote absolute path where the archive should be unpacked.`

- `The given path must exist`. 

- `Base directory is not created by this module.`

- **exclude**

- `List the directory and file entries` that` you would like to exclude from the unarchive action.`

- `Mutually exclusive with include.`

- `Default: []`

- **include**

- `List of directory and file entries that you would like to extract from the archive.` 

- If `include is not empty, only files listed here will be extracted.`

- `Mutually exclusive with exclude.`

- `Default: []`

- **list_files**

- `If set to True, return the list of files that are contained in the tarball.`

- Choices:

    false ← (default)

    true

- **mode**

- `The permissions the resulting filesystem object should have.`

- For those used to /usr/bin/chmod remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results,   quote octal numbers (for example, '644' or '1777') so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, 0755) works sometimes, but can fail in loops and some other circumstances.

- Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.

- `As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, u+rwx or u=rw,g=r,o=r).`

- If `mode is not specified` and the `destination filesystem object does not exist`, the d`efault umask on the system will be used` when setting the mode for the newly created filesystem object.

- If `mode is not specified `and the d`estination filesystem object does exist`, the m`ode of the existing filesystem object will be used.`

- Specifying mode is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details.


- **keep_newer**

- `Do not "replace existing files that are newer than files from the archive."`

- `Choices`:

    `false ← (default)`

    `true`

- **remote_src**

- `Set to true` to `indicate the archived file is already on the remote system and not local to the Ansible controller.`

- `This option is mutually exclusive with copy.`

- `Choices`:

    `false ← (default)`

    `true`


- **src**

- `if remote_src=no (default), local path to archive file to copy to the target server`; `can be absolute or relative.`

- `If remote_src=yes`, `path on the target server to existing archive file to unpack.`

- If `remote_src=yes` and `src contains ://`, the `remote machine will download the file from the URL first`. (version_added 2.0). 

- `This is only for simple cases, for full download support use the ansible.builtin.get_url module.`



