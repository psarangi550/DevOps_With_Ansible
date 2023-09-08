# <ins> Installing the Ansible Lab </ins> #

- this will allow you access the `ansible` and `number of guests` either in `web browser` or by using `SSH`

- the `entire environment` been `hosted on github`

- if after starting the `lab` `if we still have the problem` then we can visit the `users and username` section in the `README.md` file 

- when we styart the `docker-compose` using the command as `docker compose up -d` then we can see the port `http://localhost:1000` getting updated there

- we can use the `docker compose rm` inorder to `remove the already installed images` so on the `next time it will try to pull the image again`

- as here we are using the `volume mapping` hence the `data within the same will be persistant`

- we have the `.env` file where we have the `.sshd` ports that our `lab guest` going to `listen on`

- we can also nativelt connect to the `lab guest` using the `ssh` as `ssh <username>@localhost -p <portnumber>`

- we also have the `ttyd` which is the `web terminal` that we are using it over here 

- the `ttyd` web terminal has `specifc port` `associated` `with them`

- if not able to login then `there is problem with the configuration` when the docker compose image starts they made reference to the `directory` mentioned in the `docker-compose` for `volume mapping`

- if we have the problem then we can do the `docker compose rm` and then reinstall the `docker compose up -d`

# <ins> Installing the Ansible Lab on Google cloud Shell </ins> #

- we have to `switch off the ephemeral mode` in the `google cloud shell` in this case over here 

- By default the `cloud shell` will run with the `ephemeral mode` by default , so as soon as the `connection lost` the `corresponding data will be lost too in the google cloud shell`

- then we have to `clone the repo of the diveintoansible-lab git repo` and also we can set the `ssh-key` for the same as well 

- this `ssh-keygen` command will help in setting `ssh relationship between ansible user and root user`

- then we can use the `docker compiose up -d` which will run the `docker container for the same` 

- we can access the `port` by clicking on the `<preview>` option on the `right hand top corner` and select the `port to preview on 8080`

- we can generate the `readme.md` or any `md file` as the `tutorial on the right hand side using the command` as `teachme <filename>.md`


