from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from core.routes.endpoints.categoryEndpoints import all
import core.db.categoryDb as CD
from core.schemas.categorySchema import CategorySchema
from sqlalchemy.exc import IntegrityError

router = APIRouter()

router.include_router(all.router)


@router.get("/{categoryAttribute}")
def get_category_by_id_or_name(categoryAttribute: int | str, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    if isinstance(categoryAttribute, int):
        try:
            categorySchema = CD.get_by_id(categoryAttribute)
        except AttributeError:
            raise HTTPException(status_code=404, detail="Category with that id not found")
    else:
        try:
            categorySchema = CD.get_by_name(categoryAttribute)
        except AttributeError:
            raise HTTPException(status_code=404, detail="Category with that name not found")

    return categorySchema


@router.delete("/{categoryId}")
def delete_category_by_id(categoryId: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    try:
        CD.delete(categoryId)
    except AttributeError:
        raise HTTPException(status_code=404, detail="Category with that id not found")
    except IntegrityError:
        raise HTTPException(status_code=422, detail="Some item is assigned to that category (probably :P)")

    return {
        "message": "success",
    }


@router.post("/")
def add_category(categorySchema: CategorySchema, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    try:
        CD.add(categorySchema)
    except AssertionError:
        raise HTTPException(status_code=422, detail="Category with that name already exists (probably :P)")

    return {
        "message": "success",
    }


@router.put("/")
def edit_category(categorySchema: CategorySchema, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    try:
        assert categorySchema.id is not None
    except AssertionError:
        raise HTTPException(status_code=422, detail="Category id required")

    try:
        CD.edit(categorySchema)
    except (AttributeError, AssertionError):
        raise HTTPException(status_code=422, detail="Category with that name already exists (probably :P)")

    return {
        "message": "success",
    }
