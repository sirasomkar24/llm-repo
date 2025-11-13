from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str = 'Omkar' #set a default value
    age: Optional[int] = None

new_student = {'age': 32}

student = Student(**new_student)

# print('type', type(student))

print('output', student)