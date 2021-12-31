"""  Simple Cerberus Validator Script """
from cerberus import Validator
import yaml

with open('PSA_PR_Format.yml') as f:
    DATA = yaml.load(f, Loader=yaml.FullLoader)

with open('PSA_Schema.yaml') as f:
    SCHEMA = yaml.load(f, Loader=yaml.FullLoader)

V = Validator()
V.allow_unknown = True

if V.validate(DATA, SCHEMA):
    print('Pass')
    print(V.document)
else:
    print('Fail')
    ERR = V.errors
    print(ERR)

#1. 