from pydantic import BaseModel

class Student(BaseModel):
    name: str = 'Omkar' #set a default value

new_student = {}

student = Student(**new_student)

print('type', type(student))

print('output', student)