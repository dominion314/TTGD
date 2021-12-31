"""  Simple Cerberus Validator Script """
from cerberus import Validator
import yaml

with open('PSA_Customer_Request.yml') as f:
    DATA = yaml.load(f, Loader=yaml.FullLoader)

with open('PSA_Parameter_Template.yaml') as f:
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
