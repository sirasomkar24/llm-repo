from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Omkar' #set a default value
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt= 0, lt= 10, description='A decimal value representing the CGPA of the student') # Can also set the default parameter in the Field

new_student = {'age': 32,'email': 'abc@gamil.com', 'cgpa': 9.5}

student = Student(**new_student)

# print('type', type(student))

print('output', student.model_dump()) # To convert output into the dictionary

# To convert pydantic output into the Json

student_json = student.model_dump_json()

print("json output", student_json)