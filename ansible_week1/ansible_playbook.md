# <ins>Ansible Playbook and YAML</ins> #

- in this section we will learn about the `YAML` 

- `YAML` is the `ansible playbook language` and `how to use this effieciently`

- `ansible plybook` `review section  which constitute` a `ansible playbook` i.e `review section which makes up a playbook`

- `various way` in which we can use `variables can be used in ansible playbook`

-  more closely look into `Ansible facts` provided by the `setup module` during the `execution of the  playbook`

- how we can create `custom defined ansible facts`

- we will use the `jinja2` for the `templating purpose`

- `creating and executing` the `ansible playbook`

- we will `configure` the `nginx webserver` on the `on ubuntu and centos` 
  
- `template the deployment of the web  application`

# <ins> YAML </ins>

- `YAML` is a `data-oriented` language

- we will `look into the structure of the YAML files`

- `indentation` 
  
  - how the `indentation` `applies/works` with the `YAML Documents` and `rules for the indentation `

- `quotes,advantages and disadvantages`
  
  - try out `different way of using` the `quotes` and the `advantages and disadvantages for the same` 

- multiline values 

  - how `YAML` `accomodate different option `for the `multiline values`

- boolean (True/False)
  
  - how the `true/false` represented in YAML

- lists and dictionary 

<br/><br/>

# <ins> Ansible Playbook </ins> #

- the `ansible command` that we uses untill now `which will be useful for the adhoc command`

- the `ansible command` will be very helpful for the `inventory with multiple hosts` when we use the `ansible command with inventory with multiple hosts`

- `ansible` has the `scripting functionality` which is known as `ansible playbook`

- An `ansible playbook` allow us to `perform many action` accross `multitude of system` using the `module what we have discussed earlier in ansible module`

- `Ansible Playbook` can be written in `both YAML or JSON` language

- whilst the `ansible playbook` has the `compatibilty to support both the markup language(YAML/JSON)` but the `YAML is the predominant standard`

# <ins> What is YAML </ins> #

- `Ansible playbook`, utilise `YAML` as `humn readable` `data-serialisation language`

- `YAML` is 
  
  - `easy to use`

  - `easy to read `

  - `great for collaberation`

- `Reading and Writing of YAML` supported by `major programming language`

- often seen with `.yml/.yaml` extension , where the `.yaml` is officially recomended extension since `2006`

# <ins> Practicing YAML </ins> #

- go to the `Ansible Playbook,Introduction` &rarr; `YAML` &rarr; `01`/`Teamplate` based on how we want to use it 

- on the folder `01` of the `YAML Folder` we have the `bash file` as `show_yaml_python.sh` and `temp.yaml` file 

- on the `show_yaml_python.sh` we have the sceript as below 

    ```
        show_yaml_python.sh
        --------------------

        #! /bin/bash

        python3 -c 'import yaml,pprint;pprint.pprint(yaml.load(open("test.yaml").read(),loader=yaml.FullLoader))'

        # using the python3 with the `-c` option which stands for the `command`

        # also using the pprint module pprint method to display the python dict that we got from the yaml.loads() which uses the test.yml file with the `read() on the file object` as `open("test.yaml").read()`    
    
    ```

- here we re using the `python` or `indirectly ansible` will `read/interprete` the `tests.yaml` file and represent the `details` onto the `terminal`

- this will provide the `python dict` as the `output` which show how `python or indirectly ansible will read the tests.yaml file`

- the `YAML` file `optionally` `starts with 3 dashes(---)` and `ends with 3 dots(...)`

- this is not a `prerequisite` we can also have the `YAML` file without the `3 dashes(---) and 3 dots(...)`

- but `these 3 dashes(---) and 3 dots(...) at the start and end respectively` will display the `yaml section for the single file`

- when we use the `# for comment inside the YAML` file which will be `ignored` by the `YAML interpreter`

- but if we have deined the `test.yaml` file as below then we can see the output as `None` as there were `no content` in it s per `python or indirect ansible` will interprete as `None Type`

- **Case1**

- we can mention the the test.yaml as below 

    ```
        test.yaml
        ---------
        --- # defining the 3 dashes for the start 

        # here we can define the comment in here 
        # this will help the user to understand more rather than the YAML interpreter

        ... #defining the 3 dashes for the end 
    
        # now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output a None value as there are no content in the yaml file 

    
    ```

- **Case2**

- if we hve define the test.yaml as below where we have `define the key(as str) and values(as str)` in here in the `tests.yaml` as 

- when we define the 
    
    ```
        test.yaml
        ----------
    
        # Every YAML file should start with three dashes
        ---

        example_key_1: this is a string
        example_key_2: this is another string
        
        # Every YAML file should end with three dots
        ...

        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict 
        {'example_key_1': 'this is a string', 'example_key_2': 'this is another string'}
    
    
    ```

- we can use the `ctrl+d` to come out of the  `python interpreter that we have opened using the python3` command 

- **case3**

- if we define the `test.yaml` with the `key as preveious example but the values as in quotes (single or double quotes)` then we can use it as below 

- in all these scenarios we will be getting the `output` as the `str key and str values` from the `python dict view point`

- we don't have to provide the `quotes in YAML` , if we want we can eaither provide `single or double quotes` without any issue

- for python `whether we are using the single quote or double quote` both will be `appeared as the single quoted string only inside the python dict`

- all the `no quote or single quote or double quote inside the YAML` will be treated same through python `single quoted string inside the python dict`


- below is the example for the same 

    ```
        
        tests.yaml
        ----------
        # Every YAML file should start with three dashes
        ---

        example_key_0:this is  a str
        example_key_1: 'this is a string'
        example_key_2: "this is another string"
        
        # Every YAML file should end with three dots
        ...

        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as 
        {'example_key_0': 'this is  a str',
        'example_key_1': 'this is a string',
        'example_key_2': 'this is another string'}

    
    ```

- **Case:-4**

- here we are using the `control character` such as `New line by using the \n`

- here also we can use the `control character represented by escape character \n`

- `\n` is the `newline control character` indicating that `string should included a newline`

- when we are using the `escape character aliong with string in the YAML file` then the `double quoted string behave properly as per the escape character by adding a newline`

- when we are using the `ecape character with the single quote or no quote` then it will try to `escape the backslash i.e \ by providing another backslash as \\`

- in case of the `escape character` in the `YAML` the `single quote and no quote will try to escpe the backslash(\) as (\\)` as it think the `\n` is a part of the string 

- we need to use the `double quotes` while using the `string with escape character / control character in YAML file` in 

- when we are using the below `tests.yaml ` file as

    ```
        tests.yaml
        ----------
        # Every YAML file should start with three dashes
        ---

        no_quote:this is  a str\n
        single_quote: 'this is a string\n'
        double_quote: "this is another string\n"
        
        # Every YAML file should end with three dots
        ...
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as 
        {'double_quote': 'this is another string\n',
        'no_quote': 'this is  a str\\n',
        'single_quote': 'this is a string\\n'}

        # here in this case `double quote been behaving properly` where as the `single and no quotes`will try to `escape the \ with \\` considering the `\n` as the part of the string not as an `new line escape code`
    
    ```

- **Case5**

- if we want to `define the string in multiple line` aginst the `defined keys` then we can use `|` against the `key value`

- in `YAML` there is always a `space gap between the <key>: and <value against it>`

- when we define the `value of key with the | symbol ` then we can see that `each new line character are being mentioned as \n`

- below the example reference for the same 

    ```
       tests.yaml
       ---------- 
       tests.yaml
        ----------
        # Every YAML file should start with three dashes
        ---

        multi_line_str: |
                        this is a string
                        that goes over 
                        multiple lines
        
        # here we have define the multiline string in this case with the `|` symbol
        
        # Every YAML file should end with three dots
        ...
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as 
        {'multi_line_comment': 'this is a string\nthat goes over\nmultiple lines\n'}
        # here if print() then those line will be displayed as the multiline comment and escape character will not be displayed 


    ```

- **Case6**

- suppose we have a `very long string` and for the sake of `neatness` we have decided to `use it as the multiline`

- but as it is a `single string` we can define the `single line string as multiline for neatness`

- then in that case we can use the `>` symbol to represent the `values`

- here we can sonsider below example for reference 

    ```
        tests.yaml
        ----------

        # Every YAML file should start with three dashes
        ---

        single_line_as_multi_line_str: >
                        this is a string
                        that goes over 
                        multiple lines but consider as one line
        
        # here we have define the multiline string for neatness but which will be actually a single line in this case with the `>` symbol
        
        # Every YAML file should end with three dots
        ...
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as 
        {'single_line_as_multi_line_str': 'this is a string that goes over multiple '
                                  'lines but consider as one line\n'}

        # here by the use of `>` we can consider the `single line distributed over multiple lines`
        # but when we conside then we can seee that `at the end \n` which is being added implicitly

    ```

- but when we consider the `>` option then we can seee that `at the end \n` which is being added implicitly

- the `>` specifies the `single string` that can be formatted as multiple line in `YAML`

- but at the end we cn see the `\n` will be appending to `single line string` that we see from the `python utility`

- **Case7**

- if we want to remove the `additional \n while represeting the single line over multiple line` for neatness purpose then we can use the `-` symbol with the `>` symbol and use it as `>-` symbol

- we can represent the preveious `tests.yaml` file as 

    ```
        tests.yaml
        ----------

        # Every YAML file should start with three dashes
        ---

        single_line_as_multi_line_str: >-
                        this is a string
                        that goes over 
                        multiple lines but consider as one line
        
        # here we have define the multiline string for neatness but which will be actually a single line in this case with the `>-` symbol to remove the `\n` at the end
        # this (-) can also be used with the `|` as to remove the `\n` from the multiline command as well
        
        # Every YAML file should end with three dots
        ...
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as
        {'single_line_as_multi_line_str': 'this is a string that goes over multiple '
                                  'lines but consider as one line'}

        # here we can see that the line does not goes over the with the `\n` symbol at the end 
        # hence we can specify that as below
        

    
    
    ```

- `-` can also be used with the `|` as to remove the `\n` from the multiline command as well

- we can see that the line does not goes over the with the `\n` symbol at the end

- the `-` symbol strip the `last character(new line)` from a string

-**Case8**

- with `YAML` the `integer`can be automatically `interpreted`

- hence we can see the response as below 

    ```
        tests.yaml
        ----------
        # Every YAML file should start with three dashes
        ---

        example_interget_key: 1
        
        # Every YAML file should end with three dots
        ...
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as
        {'example_interget_key': 1}
    
    ```

- **Case9**

- but we can represent the `integer` as `string` by providing the `quotes around the integer`

- hence we can specify that as `single or double quotes`

- we can see the below example for reference 

    ```
        tests.yaml
        ----------
        # Every YAML file should start with three dashes
        ---

        example_interget_key_str1: '1'
        example_interget_key_str2: "1"
        
        # Every YAML file should end with three dots
        ...  
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as
        {'example_interget_key': '1'}
    
    
    ```

- it does not matter whether we provide the `single or double quote` around the `integer` to make it as `string` but we will strill be getting the `outcome python dict with single quote only` which will be `interpreted` by `python or alternatively by ansible`

- **Case10**

- `boolean` in `programming language` or `YAML` represent as `true/false` value 

- `YAML` is very `versitile` while dealing with the `boolean value`

- we can repsent the boolean value as  below 

    ```
        #false False FALSE no No NO off Off OFF
        # this will represent  the false value in here 
        
        #true True TRUE yes Yes YES on On ON
        # this will be represent the true value in versitile manner

        # we can even mention the `true and false` as `y and n` in this case 
    
    ```

- we can represent the `test.yaml` as below 

    ```
        tests.yaml
        ----------
        # Every YAML file should start with three dashes
        ---
        is_false_01: false
        is_false_02: False
        is_false_03: FALSE
        is_false_04: no
        is_false_05: No
        is_false_06: NO
        is_false_07: off
        is_false_08: Off
        is_false_09: OFF
        is_false_10: n
        is_true_01: true
        is_true_02: True
        is_true_03: TRUE
        is_true_04: yes
        is_true_05: Yes
        is_true_06: YES
        is_true_07: on
        is_true_08: On
        is_true_09: ON
        is_true_10: y

        # Every YAML file should end with three dots
        ...  
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as
        # here in this case python interpreter will treat everything as `boolean` i.e `True/False`
        # but in case of the `y/n` even though these as `valid ansible expression` python will treat then as string alternative ansible might
        # for the case of confusion try avoid using the `y/n`
        # rather we can use the `False/True` as this is the exact representation of `boolean` in python 
        # the output in here is as 
        {'is_false_01': False,
        'is_false_02': False,
        'is_false_03': False,
        'is_false_04': False,
        'is_false_05': False,
        'is_false_06': False,
        'is_false_07': False,
        'is_false_08': False,
        'is_false_09': False,
        'is_false_10': 'n',
        'is_true_01': True,
        'is_true_02': True,
        'is_true_03': True,
        'is_true_04': True,
        'is_true_05': True,
        'is_true_06': True,
        'is_true_07': True,
        'is_true_08': True,
        'is_true_09': True,
        'is_true_10': 'y'}
    
    ```

- when we use the `y/n` for the `boolean value as true/false` then even though its `valid in YAML prospect` but the `python utility` will treat it as the `string` in this case 

- but when using from the `ansible prospect and YAML one` we can use the`y/n` , but for the `confusion/ambiguity` its recomended to `avoid such behaviour`

- rather we can use the `False/True` as this is the exact representation of `boolean` in python as `one to one` mapping 

- **Case11**

- when we represent the `YAML` with the `key and value` pair then that will be represented as the `python dict` from the `python utility that we are using`

- but we can use the `list of item in YAML` without havving any `key`

- the `list of item` represented as `-` appended to each of the `item`

- if we are using the `python utility` then we can see that `those will be translated to python list instead of python dict in that case`

- we can represent the `test.yaml` as below

    ```
        tests.yaml
        ----------
        # Every YAML file should start with three dashes
        ---

        - item1
        - item2
        - item3
        - item4
        
        # Every YAML file should end with three dots
        ...  
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python list as
        ['item1', 'item2', 'item3', 'item4']
        # here as we are not using the `key andf vlue in yaml` rather using the list of item using the `-` hence that can be treated as `list of item` which being represented by the python interpreter
    
    ```

- if we see that from the `python/ansible` prospect we can see that `it will be in the form of python list rather than the dict when we mwntioned the list of item with the dashes`

- but here the `list` will be `string of item` which can be considered as `if we are not mentioning the integer or boolean then it consider the value as string`

- **Case12**

- if we are `representing anything ` as `key:value` pair in `YAML` then it will create an `equivalent of python dictionary` from the `python utility`

- whatever `comes after the key:` will be treated as the `value`

- if we have `subsequent entries of key-value pair in YAML` are considered as the `part of the same dictinary`

- we can represent the `dict` in ansible by using the `key1:value1 \n key2:value2` format which is very common 

- we can see the `python inline dict` inside the `YAML` as well 

- we can represent the `inline block of python dict` in `3 ways`

- we can represent the dict in `YAML` which is most common as below

    ```
        tests.yaml
        ----------
        # Every YAML file should start with three dashes
        ---

        example_key_1:example_value1
        example_key_2: example_value2

        # Every YAML file should end with three dots
        ...  
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as
        {'example_key_1': 'example_value1', 'example_key_2': 'example_value2'}
    
    
    ```

- **Case13**

- but we can reporesent the `dict in YAML` as `python inline dict` in `2 format`

- which can be represented as below 


    ```
        tests.yaml
        ----------
        # Every YAML file should start with three dashes
        ---

        {example_key_1: example_value_1 , example_key_2: example_value_2 }
        # here can represent the python inline dict to represent the dict inside the YAML

        # alternatively we can use the quotes as well while defining the inline block dict of python in YAML
        {'example_key_1': 'example_value_1' , 'example_key_2': 'example_value_2'}


        # Every YAML file should end with three dots
        ...  

        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as
        {'example_key_1': 'example_value_1', 'example_key_2': 'example_value_2'}
        # in both the case we will getting the same output in python
        # but the recomended approach will be case 12 represntation 


    ```

- here we can see `some of developer might write the YAML dict as python inline dict` which can be `interpreted as well` as `python dict`

- but `recomended` to use the `approach that we have decided in case 12`

- **Case14**

- we can define the `list inside the ansible` as the `python ibline block format`

- when executing by the `python utility` then we will betting the response as `list of string` as `every entry if not boolean or integer` consider as `string`

- we can use the below example for reference 

    ```
        tests.yaml
        ----------
        # Every YAML file should start with three dashes
        ---

        [example_list1,example_list2] #defining the list not with the `list of item with -'s` rather using the python inline block to definethe same 
        
        # Every YAML file should end with three dots
        ...  
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python list as
        ['example_list1', 'example_list2']
        # this will be represented as the list of string in this case 


    ```

- but recomended to use the format of `- with list of item` rather than the `python inline block which consitute list`

- **Case15 and 16**

- we can't define the `key and value and list of item` inside the `same block of the YAML`

- if we are going to define then thats not a `valid YAML Signature`

- we can't evben define the same `if we are using the python inline block representation of defining the dict and list` it will also not going to work 

- we can write the `tests.yaml` file as below 

    ```
        tests.yaml
        ----------
         # Every YAML file should start with three dashes
        ---
        {example_key_1: example_value_1 , example_key_2: example_value_2 } # here using the inline block of representing the dict in YAML
        [example_list1,example_list2] #defining the list not with the `list of item with -'s` rather using the python inline block to definethe same 
        
        # Every YAML file should end with three dots
        ...  

        Or 
        tests.yaml
        ----------
         # Every YAML file should start with three dashes
        ---
        example_key_1:example_value_1
        example_key_2:example_value_2
        # here defining the regular expression for the dict 

        - item1
        - item2
        - item3
        - item4

        # Every YAML file should end with three dots
        ...  

        # here in both the case whether the `inline block or regular expression` we define the `key and value pair` and the `list of item` under the `same block`
        # which is not a valid YAML Signature 
        # when we execute the python utility then in that case we will be getting error as below 
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # when we execute thenm we will end up getting the error as the YAML is not a valid Signature
    
    ```

- we can't have the `kye-value` and the `list item` inside the `in the same block inside the YAML`

- **Case17**

- we can also define the `dictionary of dictionary` inside the `YAML` file using the `recommended approach` as well as the `inline approach`

- when we are using the `recomended approach` then we have to provide `indentation` of `2 character` to define the `inner key and value pair`

- indentaion is the part of the `YAML language` and `Two character indentation` is common practise for `Ansible and other usage of YAML`

- we can define the `dictionary of dictionary as below`

    ```
       tests.yaml
        ----------
         # Every YAML file should start with three dashes
        ---
        
        # the dictinary of dictionary in recomended approachcan be as 

        dict_key_1:
            example_key_1:example_value_1

        dict_key_2:
            example_key_2:example_value_2

        # Every YAML file should end with three dots
        ...   

        # here we are defining the recomended approach with indentation of 2 character 



        #Or
        #but we can also define using the python inline block as below 
        tests.yaml
        ----------
         # Every YAML file should start with three dashes
        ---
        
        # the dictinary of dictionary in inlinbe block be as
        dict_key_1: {example_key_1: example_value_1}
        dict_key_2: {example_key_2: example_value_2}

        # or we can defined with the quotes as below 
        'dict_key_1': {'example_key_1': 'example_value_1'}
        'dict_key_2': {'example_key_2': 'example_value_2'}

        # Every YAML file should end with three dots
        ...  

        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as 
        {'dict_key_1': {'example_key_1': 'example_value_1'},
        'dict_key_2': {'example_key_2': 'example_value_2'}}

    
    ```

- when we execute the `python utility` then on the `outcome` we will see the resullt as `dictionary of dictionary`

- if the `corresonnding entries` will do under the `part of the same dictionary`

- **Case18**

- A `dictionary key in YAML` can have a `list of values`

- we can see the blow example for reference 

    ```
        tests.yaml
        -----------
        # Every YAML file should start with three dashes
        ---
        
        # the dictinary key can have list of values
        example_1: # here defined the key with key:
            - item1 # here the list of item defined as `-` symbol
            - item2
            - item3

        example_2:
            - item4
            - item5
            - item6

        # Every YAML file should end with three dots
        ... 
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as 
        {'example_1': ['item1', 'item2', 'item3'],
        'example_2': ['item4', 'item5', 'item6']}
    
    ```

- **Case19**

- `YAML` is a `data-oriented language`

- we can take the `combination of the same` that we have `discussesd earlier`

- we can define the `test.yaml` as

    ```
        tests.yaml
        -----------
        # Every YAML file should start with three dashes
        ---
        
        # the dictinary key can have list of values
        example_dict_1: #defining the key which contains the List of dictionary as value 
            - example_dict2: #defining the dictionary whose values as list of value which is inside a list
                - 1 # defining the list of values in here 
                - 2 # defining the list of values in here 
                - 3 # defining the list of values in here 
            -  example_dict_3:##defining the dictionary whose values as list of value which is inside a list
                - 4 # defining the list of values in here 
                - 5 # defining the list of values in here 
                - 6 # defining the list of values in here 
            - example_dict_4: # defining the example_dict_4 which will container the list of values which is inside the list
                - 7 # defining the list of values in here 
                - 8 # defining the list of values in here 
                - 9 # defining the list of values in here 


        # Every YAML file should end with three dots
        ... 
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as 
        {
            example_dict1:[
                {
                    example_dict2:[1,2,3]
                },
                {
                    example_dict2:[4,5,6]
                },
                {
                    example_dict3:[7,8,9]
                }
            ]
        }
    
    
    
    
    ```

- we can also define the `tests.yaml`as below 

    ```
        tests.yaml
        -----------
        # Every YAML file should start with three dashes
        ---
        
        dict_key_1:
            - example_key_1:
                - 1
                - 2
                - 3

            dict_key_2:
            - example_key_2:
                - 4
                - 5
                - 6

            dict_key_3:
            - example_key_3:
                - 7
                - 8
                - 9


        # Every YAML file should end with three dots
        ... 
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as 
        {
            dict_key_1:[{example_key_1:[1,2,3]}],
            dict_key_2:[{example_key_2:[4,5,6]}],
            dict_key_3:[{example_key_1:[7,8,9]}]
        }
    
    
    
    ```

- we can also define this as below  in the `tests.yaml` file as 

    ```
        tests.yaml
        -----------
        # Every YAML file should start with three dashes
        ---
        
        dict_key_1:
            example_key_1:
                - 1
                - 2
                - 3

        dict_key_2:
            example_key_2:
                - 4
                - 5
                - 6

        dict_key_3:
            example_key_3:
                - 7
                - 8
                - 9


        # Every YAML file should end with three dots
        ... 
        now when execute the command as 
        bash/sh  show_yaml_python.sh
        # this will output the below outcome as the python dict as 
        {
            dict_key_1:{example_key_1:[1,2,3]},
            dict_key_2:{example_key_2:[4,5,6]}
            dict_key_3:{example_key_3:[7,8,9]}

        }
    
    
    ```

- having the `understanding of YAML` and `how it related to python as (python dict) which indirectly related to ansible` gives you more understanding of `what type of data we want to use inside the YAML`

- we can read the `thinking how the YAML data converted as python dict` will `give us more understanding how ansible will behave or how the output of ansible amodule will behave`

# <ins> challenge </ins> #

- when we use the `tests.yaml` file with `start and stop marker by using the (3-dashes) ans (3-dots)` then we can see that `python utility will return None`

- we can create a list of `car manufcture` inside the `YAML` as 

    - Aston Martin

    - Fiat

    - Ford

    - Vauxhall

- we can represent the `tests.yaml` as list as below

    ```
        tests.yaml
        -----------

        ---
        # 3 dashes for the starter marker

        -  Aston Martin

        - Fiat

        - Ford

        - Vauxhall

        # 3 dots for the end marker
        ...

        # now when we run the utility with as 
        bash/sh show_yaml_python.sh
        # then below will be the output
        ['Aston Martin','Fiat','Ford','Vauxhall']
    
    
    ```

- now if we want to convert thwat klist to the sdictionary then we can use it as below

- but while converting to the dict we can see thtat the value will be as `key:None` as we are not mentioning the `value` while utilizing the `python utility`

    ```
        tests.yaml
        -----------

        ---
        # 3 dashes for the starter marker

        Aston Martin:
        Fiat:
        Ford:
        Vauxhall:

        # 3 dots for the end marker
        ...
        # now when we run the utility with as 
        bash/sh show_yaml_python.sh
        # then below will be the output
        {
            'Aston Martin':None,
            'Fiat':None,
            'Ford':None,
            'Vauxhall':None
        }
    
    
    
    ```

- now for each manufacture we want to `implement` `year_fiounded` as the `key` and `correcponding year founded as value` and the `website` key `with website value`

- we can write it as 

    ```
        tests.yaml
        -----------
        ---
        # 3 dashes for the starter marker
        Aston Martin: 
            year_founded: 1913
            website: https://www.astonmartin.com/

        Fiat:
            year_founded: 1899
            website: https://www.fiat.com/

        Ford:
            year_founded: 1903
            website: https://www.ford.com/

        Vauxhall:
            year_founded: 1857
            website: https://www.vauxhall.co.uk/
    
        # 3 dots for the end marker
        ...
    
    ```

- now if we have the defione the `founder` or `list of founder` as a `list` to the `founded_by` key then we can define it as for `each manufacture`

    ```
        tests.yaml
        -----------
        ---
        # 3 dashes for the starter marker
        Aston Martin: 
            year_founded: 1913
            website: https://www.astonmartin.com/
            founded_by:
                - Lionel Martin
                - Robert Bamford

        Fiat:
            year_founded: 1899
            website: https://www.fiat.com/
            founded_by:
                - Giovanni Agnelli

        Ford:
            year_founded: 1903
            website: https://www.ford.com/
            founded_by:
                - Henry Ford

        Vauxhall:
            year_founded: 1857
            website: https://www.vauxhall.co.uk/
            founded_by:
                - Alexander Wilson
    
        # 3 dots for the end marker
        ...
    

    
    ```

# <ins> Important Resource </ins> #

![Resources](image-2.png)