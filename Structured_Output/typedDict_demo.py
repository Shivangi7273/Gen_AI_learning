from typing import TypedDict

class Person(TypedDict):
    name : str
    age: int

new_person = Person(name='Ajay', age=27)

print(new_person)
