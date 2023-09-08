# <ins> Introduction to Ansible </ins> #

# <ins> Ansible </ins> #

- `Ansible` is an open source
  
  - `configuration management`
  
  - `software provisioning`
  
  - `application deployment` 
 
  `toolset` created by `Michael De Haan in 2012`

- It was later acquired by Red Hat, Inc in 2015

- `since then Red Hat, Inc and the open source community` have `further developed and improved the platform`

- `Whilst` `many refer` to `Ansible` as a `specific entity` it is a `multitude of "tools modules and software defined infrastructure" ` that `are collectively the Ansible toolset`

- In this introductory section we're going to take a look at some of the more well-known `core components of Ansible `

# <ins> Ansible Modules </ins> #

  - `A major factor in the success of Ansible is the extensive library of modules that are openly available for consumption`

  - `There are modules that cover many areas including`
    
    -  `Cloud Computing`
    -  `Networking `
    -  `Server configuration amd Management` 
    -  `Virtualisation` 
    -  `container` 
    -  many more      

- Given the size of the module catalog there may be an Ansible module already out there to support the automation requirements that you have

-  If `there isn't a module for your needs` there's also the opportunity to `create a custom module` `using` the `extensible framework` that is `native to Ansible`

# <ins> Ansible Executable </ins> #

- The `next core component` is the`Ansible Executable` `A highly versatile tool that acts as a swiss army knife for your automation requirements` 

- quite simply `typing` `ansible` on a `system where Ansible is installed` an `excellent gateway point` for
    
    -  `starting an Ansible project` 
    
    -  for `setting up your "Ansible execution " environment`  
  
    -  for `everyday usage`

- ` Ansible Executable` Great for 

    - `initially setting of the project` 
  
    - `testing Ansible configuration`

- ` Ansible Executable` help you to `interact between` 
  
    - `Ansible Module`
  
    - `Ansible Target Infrastructure` 

# <ins> Ansible Playbook </ins> #

- using the `Ansible playbook executable` it `allow` you `work with` `human readable configuration deployment and orchestration language`

- `ansible playbook` is a `book of play` `where` `play` `depicting` the `configuration and changes` we want to achieve against the `given set targets`

- the `playbook` consist of `simple set of Task` to `advance configuration` `leveraging Ansible feature` such as 
  
  - `Rolling updates`
  - `Parallel execution` 
  - `Roles`

- we will learn about in depth

    - `ansible playbook`
  
    - `ansible language`

    - `advance component that can be leveraged to fully exploit power of Ansible`

# <ins> Ansible Inventories </ins> #

- `Inventories` are nothing but the `collection of targets`

- `Inventories` are mostly comprises of `hosts` as `component` but can also relate to `other component`
  
  - `Network Switches`
  - `containers`
  - `Storage Array`
  - `other physical and virtual component`

   we want to interact using through `Ansible`

- `inventories` can `provide` `useful info` that `we can use alongside our target` `during the ansible execution`

- `inventories` can be `very simple` such as `txt file` with `selection of target`

- we can create the `dynamic inventory` where the `inventory instead of the txt file with a series of target` rather is a `executable` where the `data sourced dynamically`

- this can give a lot of flexibility to `store the data else where` and `make use of it during the runtime`

- we will create the `Dynamic inventory with AWS ` and we can also create `our own inventory`
