from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Omkar' #set a default value
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt= 0, lt= 10) # Can also set the default parameter in the Field

new_student = {'age': 32,'email': 'abc@gamil.com', 'cgpa': 9.5}

student = Student(**new_student)

# print('type', type(student))

print('output', student)