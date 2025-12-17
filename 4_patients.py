from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, computed_field
import json
from typing import Annotated, Optional, Literal
from fastapi.responses import JSONResponse

app = FastAPI()

## creating the Pydantic class in order to validate the data that we want to add in our json file
## which is making use of the 'POST' request

class Patient(BaseModel):
    id:Annotated[str, Field(..., description="Id of the patient", example='P001')]
    name:Annotated[str, Field(..., description="Name of the patient", example="John Garland")]
    city:Annotated[str, Field(...,description="City of the birth of patient", example='Jaipur')]
    age:Annotated[int, Field(...,ge=0,lt=120, description="Age of the patient")]
    gender:Annotated[Literal['male', 'female', 'others'], Field(...,description='Gender of the patient')]
    height:Annotated[float, Field(...,gt=0,description="Height of the patient in mtrs")]
    weight:Annotated[float, Field(...,gt=0,description="Wright of the patient in kgs")]

## creating our own fields through alread existing fields
## here, bmi for example -
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    @computed_field
    @property
    def verdict(self) ->str:
        if self.bmi < 18.5:
            return 'under-weight'
        elif self.bmi < 25:
            return 'normal'
        elif self.bmi < 30:
            return 'normal'
        else:
            return 'Obese'

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]

def load_data():
    with open ("patients.json") as p:
        data = json.load(p)
    return data

def save_data(data):
        with open('patients.json', 'w') as p:
            json.dump(data, p)

@app.post('/create')
def create_patient(patient:Patient):

    # loading the existing data
    data = load_data()
    # check if the patient already exists (the patient data that we have created)
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    
    # else, we will add the patient in the existing data
    # here, patient is the pydantic model format and our already existing data is in
    # json format, so we will first convert the Pydantic data into json format
    # and then we will add our newly created record
    data[patient.id] = patient.model_dump(exclude=['id']) # model_dump converts pydantic data into dictionary

    # saving this data in our already existing json file -
    save_data(data=data)

    return JSONResponse(status_code=201,content={'message': 'patient created successfully'})

@app.put('/edit/{patient_id}')
def update_patient(patient_id:str, patient_update:PatientUpdate):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    existing_patient_info = data[patient_id]

    # converting patient_update Pydantic object into a dictionary -
    updated_patient_info = patient_update.model_dump(exclude_unset=True) # this will include only updating the fields
    # that we want to and not all

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    # converting dictionary object back to Pydantic object so as to retrieve fresh values
    # of bmi and verdict
    existing_patient_info['id'] = patient_id
    patient_pydantic_object = Patient(**existing_patient_info)

    # converting pydantic object back to dictionary
    existing_patient_info = patient_pydantic_object.model_dump(exclude=['id'])

    # adding this dict to our already created data (adding updated dictionary)
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content='Patient updated')

@app.put('/editPatient/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    #existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydandic_obj = Patient(**existing_patient_info)
    #-> pydantic object -> dict
    existing_patient_info = patient_pydandic_obj.model_dump(exclude='id')

    # add this dict to data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient updated'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted'})