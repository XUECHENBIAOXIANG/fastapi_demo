from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import sys
sys.path.append("..")
import crud
import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@app.get("/students/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    updated_student = crud.update_student(db, student_id=student_id, student=student)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted_student = crud.delete_student(db, student_id=student_id)
    if deleted_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted"}