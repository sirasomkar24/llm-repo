# Way to define a dictionary and its keys and values
from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'Omkar', 'age':32}

print(new_person)
