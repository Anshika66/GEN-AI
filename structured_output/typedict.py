from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int

new_person : Person = {'name' : 'annu' , 'age' : 56}

print(new_person)
