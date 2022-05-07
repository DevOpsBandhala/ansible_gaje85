#!/usr/bin/python
import json
from ansible.module_utils.basic import AnsibleModule
import sys
def main():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required=True, type='str'),
            age  = dict(required=True, type='str'),
        )
    )
    
    name = module.params['name']
    age = module.params['age']


    data = dict(
        output="your data has stored successfully :-) ",
    )
    try:
        file = open("/tmp/userdata.txt","w")
        file.write(name+ "," + age + "\n")
        module.exit_json(changed=True, success=data,msg=data)
    except Exception as e:
        module.fail_json(msg='something went wrong. :-(')


if __name__ == '__main__':
    main()
