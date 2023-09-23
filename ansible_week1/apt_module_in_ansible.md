# <ins> apt module with Ansible </ins> #

- **deb**
  
- `deb` :- `Path to a .deb package on the remote machine. `

- `If :// in the path`, `ansible` will `attempt to download deb before installing.` (Version added 2.1)

- `Requires` the `xz-utils` `package` `to extract the control file of the deb package to install.`


- **force_apt_get**

- `Force usage of apt-get instead of aptitude `

- `Choices`:

    - `false ← (default)`

    - `true`

- **install_recommends**

- Corresponds to the --no-install-recommends option for apt.

- true installs recommended packages.

- false does not install recommended packages. 

- By default, Ansible will use the same defaults as the operating system.
  
-  Suggested packages are never installed.

- Choices:

    - false

    - true


- **name**

- `name` :- A list of package names, like foo, or package specifier with version, like foo=1.0 or foo>=1.0

- Name wildcards (fnmatch) like apt* and version wildcards like foo=1.0* are also supported.

- **only_upgrade**

- `only_upgrade` :- `Only upgrade a package if it is already installed`

- `Choices`:

    - `false ← (default)`

    - `true`

- **purge**

- `purge` :- `Will force purging of configuration files` if the module `state is set to absent`.

- `Choices`:

    - `false ← (default)`

    - `true`


- **update_cache**

- `update_cache` :- `Run` the equivalent of `apt-get update` `before the operation`

- `Can be run as part of the package installation` or `as a separate step`

- `Default is not to update the cache.`

- `Choices`:

    - `false ← (default)`

    - `true`


- **upgrade**

	
- If `yes or safe`, performs an `aptitude safe-upgrade.`

- If `full`, performs an aptitude `full-upgrade.`

- If `dist`, performs an apt-get `dist-upgrade`.

- `Note: This does not upgrade a specific package, use state=latest for that.`

- `Note: Since 2.4, apt-get is used as a fall-back if aptitude is not present.`

Choices:

    "dist"

    "full"

    "no" ← (default)

    "safe"

    "yes"




