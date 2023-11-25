from fastapi import APIRouter,Depends,status,HTTPException,Response
from .. import schemas,models,database
from sqlalchemy.orm import Session
from typing import List

get_db=database.get_db
router=APIRouter(
    tags=['Employee']
    #prefix='/'
)

@router.get('/getEmp',response_model=List[schemas.ShowEmployee])
def getEmp(db:Session=Depends(get_db)):
    empDetail=db.query(models.Employee).all()
    return empDetail

@router.post('/addEmp',status_code=status.HTTP_201_CREATED)
def create(details:schemas.Employee,db:Session=Depends(get_db)):
    new_emp=models.Employee(fname=details.fname,lname=details.lname,age=details.age)
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

@router.get('/getEmp/{id}',status_code=200,response_model=schemas.ShowEmployee)
def get_Emp_with_id(id,response:Response,db:Session=Depends(get_db)):
    emp=db.query(models.Employee).filter(models.Employee.id==id).first()

    if not emp:
        response.status_code=status.HTTP_404_NOT_FOUND
        
    return emp

@router.put('/update/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,details:schemas.Employee,db:Session=Depends(get_db)):
    emp=db.query(models.Employee).filter(models.Employee.id==id)
    if not emp.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'employee not found')
    
    emp.update({'fname':details.fname,'lname':details.lname,'age':details.age})
    db.commit()
    return 'updated scuccessfully'

@router.delete('/delete/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id,db:Session=Depends(get_db)):
    emp=db.query(models.Employee).filter(models.Employee.id==id)
    if not emp.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'employee not found')
    
    emp.delete(synchronize_session=False)
    db.commit()
    return 'deleted'