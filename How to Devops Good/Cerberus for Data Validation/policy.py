"""  Simple Cerberus Validator Script """
from cerberus import Validator #import the Cerberus library
import yaml                    #import the yaml library 

with open('PSA_Customer_Request.yaml') as f: #open the customers PSA request
    DATA = yaml.load(f, Loader=yaml.FullLoader) #We will call this info DATA

with open('PSA_Template_Schema.yaml') as f: #open the PSA template
    SCHEMA = yaml.load(f, Loader=yaml.FullLoader) #We will call this info SCHEMA

V = Validator() #This variable will use the function that compares the Customer Request to the Tempalate we create.
V.allow_unknown = True #This will allow unknown document key pairs.

if V.validate(DATA, SCHEMA): #This will validate the DATA info against the Template Schema.
    print('Pass') #If the DATA passes the Template, we will print pass.
    print(V.document)
else:
    print('Fail') #If the DATA does not pass the schema check, we will print fail. 
    ERR = V.errors
    print(ERR)
