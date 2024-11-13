from fastapi import FastAPI,Depends,status,Response,HTTPException
from .import schemas,models
from .database import engine,get_db
# from sqlalchemy.orm import Session
# from typing import List
# from passlib.context import CryptContext
# from .hashing import Hash
# from .import database
from .router import blog,user

app = FastAPI()
app .include_router(blog.router)
app .include_router(user.router)
models.Base.metadata.create_all(engine)
# get_db = database.get_db()
# def get_db():
#     db = SessionLocal()
#     try: 
#         yield db
#     finally:
#         db.close()

# @app.get('/blog',response_model=List[schemas.ShowBlog],tags=['blog'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blog'])
# def create_post(request:schemas.Blog,db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog



# @app.get('/blog/{id}',response_model=schemas.ShowBlog,tags=['blog'])
# def show(id,db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog id:{id} is not available')
#     return blog

# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blog'])
# def destroy(id,db : Session=Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog id:{id} does not exists')
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return f'Blog with {id} is deleted'

# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['blog'])
# def update(id,request:schemas.Blog,db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog id:{id} does not exists')
#     blog.update(request)
#     db.commit()
#     return 'The blog is updated'



# @app.post('/user',response_model = schemas.ShowUser,tags=['user'])
# def create_user(request:schemas.User,db : Session = Depends(get_db)):
#     new_user = models.User(name=request.name,emaill=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}',response_model=schemas.ShowUser,tags=['user'])
# def get_user(id:int,db:Session=Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id==id)
#     if not user.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"There exists no user with id:{id}")
#     return user