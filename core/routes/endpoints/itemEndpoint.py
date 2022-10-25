from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from core.routes.endpoints.itemEndpoints import list_
import core.db.itemDb as ID
import core.db.userDb as UD
from core.schemas.itemSchema import ItemSchema
from .. import get_db_session, Session

router = APIRouter()

router.include_router(list_.router)


@router.get("/{itemId}")
def get_item_by_id(itemId: int, Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    Authorize.jwt_required()

    try:
        item = ID.get_by_id(session, itemId)
    except AttributeError:
        raise HTTPException(status_code=404, detail="Item with that id not found")

    return item


@router.delete("/{itemId}")
def delete_item_by_id(itemId: int, Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    Authorize.jwt_required()

    try:
        ID.delete(session, itemId)
    except AttributeError:
        raise HTTPException(status_code=404, detail="Item with that id not found")

    return {
        "message": "success",
    }


@router.post("/")
def add_item(item: ItemSchema, Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    Authorize.jwt_required()

    currentUser = Authorize.get_jwt_subject()

    userSchema = UD.get_by_lowercase_username(session, currentUser)

    try:
        ID.add(session, item, userSchema.id)
    except AttributeError:
        raise HTTPException(status_code=422, detail="Jest jakiś zły warehouse albo kategoria albo coś nie wiem bo"
                                                    "jeszcze nie zrobiłem customowych błędów peepoBlush")

    return {
        "message": "success",
    }


@router.put("/")
def edit_item(itemSchema: ItemSchema, Authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)):
    Authorize.jwt_required()

    try:
        assert itemSchema.id is not None
    except AssertionError:
        raise HTTPException(status_code=422, detail="Item id required")

    currentUser = Authorize.get_jwt_subject()

    userSchema = UD.get_by_lowercase_username(session, currentUser)

    itemSchema.user_id = userSchema.id

    try:
        ID.edit(session, itemSchema)
    except AttributeError:
        raise HTTPException(status_code=422, detail="Jest jakiś zły warehouse albo kategoria albo coś nie wiem bo"
                                                    "jeszcze nie zrobiłem customowych błędów peepoBlush")

    return {
        "message": "success",
    }
