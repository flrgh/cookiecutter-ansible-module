#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = '''
---
module: 
version_added: "{{ cookiecutter.ansible_introduced_version }}"
short_description: "{{ cookiecutter.module_description }}"
description:
     - "{{ cookiecutter.module_description }}"
requirements: [ ]
options:
{%- for arg in cookiecutter.module_spec.arguments %}
  {{ arg.name }}:
    description:
      - "{{ arg.description }}"
    required: {{ arg.required | default(false) | string | lower }}
    default: {{ arg.default | default(None) }}
    type: {{ arg.type }}
{%- endfor %}
'''

EXAMPLES = '''
# Do something
- {{ cookiecutter.module_slug }}:
    my_string: "foo"
    my_list:
       - one
       - two
       - three

# Do something else
- {{ cookiecutter.module_slug }}'
    my_string: "bar"
    my_int: 5
    my_path: /home/john/secret
    my_bool: no
'''


# import module snippets
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.pycompat24 import get_exception
from ansible.module_utils.six import b
from ansible.module_utils._text import to_bytes, to_native


# helper functions

def do_something(module):

    return 'foo'


# main entry point

def main():

    # setup
    #
    # example module instantiation
    module = AnsibleModule(
        argument_spec=dict(
{%- for arg in cookiecutter.module_spec.arguments %}
            {{ arg.name }}=dict(required={{arg.required|default('False')}}, default={{arg.default|default('None')}}, type='{{arg.type}}'){% if not loop.last %},{% endif %}
{%- endfor %}
        ),
        supports_check_mode=True
    )

    result = {
        'changed': False
    }


    # do some work

    output = do_something(module)
    result['data'] = output

   
   # exit with meaningful information

    if output == 'foo':
        module.exit_json(**result)
    else:
        module.fail_json(msg='Something went wrong...')

if __name__ == '__main__':
    main()
