# <ins> Package Module in Ansible </ins> #

- **name**

- `name` :- `Package name, or package specifier with version.`

- `Syntax varies with package manager. For example name-1.0 or name=1.0.`

- `Package names also vary with package manager; this module will not “translate” them per distro. For example libyaml-dev, libyaml-devel.`

- **state**

- `Whether to install (present), or remove (absent) a package.`

- `You can use other states like latest ONLY if they are supported by the underlying package module(s) executed.`

- **Use**

- `The required package manager module to use (yum, apt, and so on). The default ‘auto’ will use existing facts or try to autodetect it.`

- `You should only use this field if the automatic selection is not working for some reason.`

- `Default: "auto"`
