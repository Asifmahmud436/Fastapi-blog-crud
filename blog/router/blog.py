from fastapi import APIRouter,Depends,HTTPException,status
from ..import schemas,database,models
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blog'],
)

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db)):
    return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db: Session = Depends(database.get_db)):
    # new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    return blog.create(request,db)



@router.get('/{id}',response_model=schemas.ShowBlog)
def show(id,db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog id:{id} is not available')
    return blog

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db : Session=Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog id:{id} does not exists')
    blog.delete(synchronize_session=False)
    db.commit()
    return f'Blog with {id} is deleted'

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog id:{id} does not exists')
    blog.update(request)
    db.commit()
    return 'The blog is updated'