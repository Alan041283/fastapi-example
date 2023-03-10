from .. import models, schemas, utils, oauth2
from fastapi import FastAPI, Path, Response, status, HTTPException, Depends, APIRouter
from ..database_pg_local import get_db
from sqlalchemy.orm import Session
#per importare app_orm non fare come nel main app_orm = FastAPI() ma usare APIRouter in lib fastapi

router = APIRouter(prefix="/vote", tags=["Votes"])
#users

#user puo mettere 1 solo like e lo puo rimuovere
#ad un post puo essere associato sono un user
@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db:Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):

    post=  db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f'post n. {vote.post_id} does not exist')

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,
                                              models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    #sto votando mettendo dir 1
    if (vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'user {current_user.id} has already voted on {vote.post_id}')
        new_vote=models.Vote(post_id = vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message: successfully added vote"}
    #se metto dir= 0  cancello il voto se c'è
    else:
        if not found_vote:
        #se vuoi cancella un voto che non esiste
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message: successfully deleted vote"}

    return
    # pubblica la post per eventuale storage in un py string
    # pubblica la post per eventuale storage in un py dictionary
    #print(post.dict())
    #post_dict = post.dict()
    #post_dict['id']= randrange(0,10000000)
    #my_posts.append(post_dict)
    #raise HTTPException(status_code=status.HTTP_201_CREATED, detail={"data": post_dict})
    #response.status_code = status.HTTP_201_CREATED
    #return {"data": post_dict}

