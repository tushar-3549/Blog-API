from fastapi import status, HTTPException, Depends, APIRouter
from .. import schemas, database, oauth2, models
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/vote',
    tags=['Vote']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(
    vote: schemas.Vote,
    db: Session = Depends(database.get_db),
    cur_user: int = Depends(oauth2.get_current_user)
):
    # Check if the post exists
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {vote.post_id} does not exist!"
        )
    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id,
        models.Vote.user_id == cur_user.id
    )
    found_vote = vote_query.first()

    if found_vote:
        found_vote.ratings = vote.ratings
        db.commit()
        return {"message": f"Rating updated for post {vote.post_id}."}
    new_vote = models.Vote(
        post_id=vote.post_id,
        user_id=cur_user.id,
        ratings=vote.ratings
    )
    db.add(new_vote)
    db.commit()
    return {"message": "Rating successfully added."}

@router.delete('/', status_code=status.HTTP_200_OK)
def delete_vote(
    vote: schemas.Vote,
    db: Session = Depends(database.get_db),
    cur_user: int = Depends(oauth2.get_current_user)
):
    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id,
        models.Vote.user_id == cur_user.id
    )
    found_vote = vote_query.first()

    if not found_vote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rating doesn't exist!"
        )

    vote_query.delete(synchronize_session=False)
    db.commit()
    return {"message": "Rating successfully deleted."}
