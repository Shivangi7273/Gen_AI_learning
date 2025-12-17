from fastapi import FastAPI, Path, HTTPException
import json
app = FastAPI()

# loading patients.json file -
def load_data():
    with open('patients.json', 'r') as p:
        data = json.load(p)
    return data

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message': 'A full functional API to manage your patients's records"}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patients/{patient_id}')
def fetch_details_of_patient_id(patient_id:str):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        return {"error" : f"This {patient_id} doesn't exist"}
    
## 'PATH' is used to enhance the path parameters -
@app.get('/patient/{patient_id}')
def fetch_details_of_patient_id_and_more_parameters_using_PATH(patient_id:str = Path
                                                               (..., description="ID of the patient", 
                                                                example = 'P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        return {"error" : f"This {patient_id} doesn't exist"}
    
@app.get('/patient/{patient_id}')
def fetch_details_of_patient_id_and_more_parameters_and_use_HTTPException(patient_id:str = Path
                                                               (..., description="ID of the patient", 
                                                                example = 'P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")
## this can be seen in '/docs' where it will give 404 error after passing the
## patient_id that doesn't exist