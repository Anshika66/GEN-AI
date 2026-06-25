from pydantic import BaseModel , EmailStr , Field
from typing import Optional


class Student(BaseModel):

    name : str='annu'       #default value 
    age : Optional[int] = None 
    email: EmailStr
    cgpa : float  = Field(gt = 0, lt = 10, default = 5 , description = 'A decimal value representing the cgpa of the student')      #greater that 0 and less that 10


new_student = {'name' : 'anshika'}

student=Student(**new_student)

print(type(student))