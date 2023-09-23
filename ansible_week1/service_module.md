# <ins> Service Module </ins> #

- `Controls services on remote hosts. Supported init systems include BSD init, OpenRC, SysV, Solaris SMF, systemd, upstart.`

- `This module acts as a proxy to the underlying service manager module.`

- `While all arguments will be passed to the underlying module, not all modules support the same arguments.` 

- `This documentation only covers the minimum intersection of module arguments that all service manager modules support.`

- `This module is a proxy for multiple more specific service manager modules (such as ansible.builtin.systemd and ansible.builtin.sysvinit). `

- `This allows management of a heterogeneous environment of machines without creating a specific task for each service manager. `

- `The module to be executed` is `determined by the use option`, `which defaults to the service manager discovered by ansible.builtin.setup`. 

- `If setup was not yet run, this module may run it.`

- **enabled**

- `enabled`:- `Whether the service should start on boot.`

- `At least ` `one of state `and `enabled` are required.

- `Choices`:

    `false`

    `true`

- **name**

- `Name of the service.  `

- **arguments**

- `Additional arguments provided on the command line.` 

- `While using remote hosts with systemd this setting will be ignored.`

- `Default: ""`

- **sleep**

- `If the service is being restarted` then `sleep this many seconds between the stop and start command.`

- `This helps to work around badly-behaving init scripts that exit immediately after signaling a process to stop.`

- `Not all service managers support sleep, i.e when using systemd this setting will be ignored.`

- **state**

- `started/stopped are idempotent actions that will not run commands unless necessary.`

- `restarted will always bounce the service.`

- `reloaded will always reload.`

- `At least one of state and enabled are required.`

- Note that `reloaded will start the service if it is not already started`, `even if your chosen init system wouldn’t normally.`

- Choices:

    "reloaded"

    "restarted"

    "started"

    "stopped"

