from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int

class StudentUpdate(BaseModel):
    name: str = None
    age: int = None

class Student(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        orm_mode = True