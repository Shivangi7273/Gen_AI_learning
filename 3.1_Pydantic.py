## Pydantic is basically used for type and data validation
## very useful for AI
## we for example specifically assign the data type to the arguments that we declare in a function

# pip install pydantic

from pydantic import BaseModel

# it is mandatory to import 'BaseModel' in your class so as to treat it as the Pydantic
# if by mistake we have passed 30 as str but ideally as int it should have been passed
# then Pydantic automatically understands it and converts it to int

## Step 1 - making a Pydantic model
class Patient(BaseModel):
    name:str
    age:int

def insert_patient_info(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

## Step 2 - creating the object of this Pydantic model
patient_info = {'name': 'John', 'age': 28}

patient1 = Patient(**patient_info) #unpacking the dictionary through the use of **

insert_patient_info(patient1)
