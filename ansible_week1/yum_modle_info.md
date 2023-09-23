# <ins> YUM Module info </ins> #

- **update_cache**

- `update_cache` :- `Force yum to check if cache is out of date and redownload if needed. Has an effect only if state is present or latest.`

- `Choices:`

    - `false ← (default)`

    - `true`

- **update_only**

-  `update_only` :- `When using state --> latest, only update installed packages. Do not install packages.`

- `Has an effect only if state is latest`

- `Choices:`

    - `false ← (default)`

    - `true`

- **state**
  
- `state` :- `Whether to install (present or installed, latest), or remove (absent or removed) a package`.

- `present` and `installed` will `simply ensure that a desired package is installed.`

- `latest` will `update the specified package` if `it’s not of the latest available version`.

- `absent` and `removed` will `remove the specified package`.

- `Default` is `None`, `however in effect the default action is present` `unless` `the autoremove option is enabled` for this module, `then absent is inferred.`

- `Choices`:

    - `"absent"`

    - `"installed"`

    - `"latest"`

    - `"present"`

    - `"removed"`

- **name**
  
- `name` :- A` package name or package specifier with version, like name-1.0.`

- `Comparison operators for package version are valid here >, <, >=, <=. Example - name>=1.0`

- `If a previous version is specified, the task also needs to turn allow_downgrade on. See the allow_downgrade documentation for caveats with downgrading packages.`

- When using `state=latest`, `this can be '*'` `which` means `run` `yum -y update.`

- `You can also pass a url or a local path to a rpm file (using state=present).`

- `To operate on several packages this can accept a comma separated string of packages or (as of 2.0) a list of packages.`
