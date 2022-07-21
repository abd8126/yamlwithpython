# import yaml
# from yaml import Loader
# yaml_file =open('company.yml', 'r')
# data = yaml.load(yaml_file, Loader=Loader)
# print(data)

import yaml
# from yaml import Loader
with open('company.yml') as f:
    result = yaml.safe_load(f)
    print(result)