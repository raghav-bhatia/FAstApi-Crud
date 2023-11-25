from fastapi import APIRouter,Depends,status,HTTPException,Response
from .. import schemas,models,database
from ..hashing import Hash
from sqlalchemy.orm import Session

router=APIRouter(
    tags=['Employee_Login_Details']
)
get_db=database.get_db

@router.post('/Emp_login',response_model=schemas.ShowEmployee_Login)
def employee_login(details:schemas.Employee_Login,db:Session=Depends(get_db)):
   
    emp_login=models.Employee_Login(username=details.username,password=Hash.bcrypt(details.password))
    db.add(emp_login)
    db.commit()
    db.refresh(emp_login)
    return emp_login

@router.get('/getEmplogin/{id}',status_code=200,response_model=schemas.ShowEmployee_Login)
def get_EmpLogin_with_id(id,response:Response,db:Session=Depends(get_db)):
    emp_login=db.query(models.Employee_Login).filter(models.Employee_Login.id==id).first()

    if not emp_login:
        response.status_code=status.HTTP_404_NOT_FOUND
        
    return emp_login
