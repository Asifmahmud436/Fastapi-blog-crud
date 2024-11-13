from fastapi import APIRouter,Depends,HTTPException,status
from ..import schemas,database,models
from typing import List
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post('/',response_model = schemas.ShowUser)
def create_user(request:schemas.User,db : Session = Depends(database.get_db)):
    new_user = models.User(name=request.name,emaill=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id==id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"There exists no user with id:{id}")
    return user