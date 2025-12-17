## pip install pydantic
## pip install pydantic[email]

from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional, Literal

class Student(BaseModel):
    student: str
    email: EmailStr
    cgpa: float = Field(gt = 0, lt = 11, default=9, description='cgpa tells the performance of a student') # Field helps to add description

new_student = {'student':'Ajay', 'email': 'abc@gmail.com', 'cgpa': 10}
## new_student = {'student':32} # will throw the error unlike TypedDict, since the 'student' is str
## if the email is not in proper-suntax, then it will throw the error through the use of 'EmailStr
## will throw the error as the cgpa has to be in the range of 0 to 11

student = Student(**new_student)
print(student)
print(type(student))
print(student.student)

student_in_dict_format = dict(student) # in dict format
print(student_in_dict_format['email'])

student_in_json = student.model_dump_json() # in json format
print(student_in_json)