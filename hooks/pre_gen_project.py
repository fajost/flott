# Copied from: https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/hooks/pre_gen_project.py
import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.package_name }}'

if not re.match(MODULE_REGEX, module_name):
    print(
        f"ERROR: The project slug {module_name} is not a valid Python module name. "
        "Please do not use a - and use _ instead"
    )

    sys.exit(1)