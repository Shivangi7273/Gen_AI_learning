# use of query parameters -
## query parameters are used for performing operations like sorting, pagination, filtering, searching,
## without altering the endpoint path itself
## but query parameters are optional
## each parameter is a key-value pair (in the form of key-value) and with the use of '?'
## if there are multiple query parameters then we separate them through '&'

from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

# loading patients.json file -
def load_data():
    with open('patients.json', 'r') as p:
        data = json.load(p)
    return data

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data