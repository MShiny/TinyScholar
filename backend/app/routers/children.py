from typing import List, Optional

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field


router = APIRouter(
    prefix="/children",
    tags=["Children"],
)


class ChildCreate(BaseModel):
    name: str
    age: int = Field(ge=6, le=17)
    grade: str


class Child(ChildCreate):
    id: int


class ChildUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = Field(default=None, ge=6, le=17)
    grade: Optional[str] = None


children: List[Child] = []
_next_id = 1


@router.post(
    "",
    response_model=Child,
    status_code=status.HTTP_201_CREATED,
)
def create_child(child: ChildCreate) -> Child:
    global _next_id

    new_child = Child(
        id=_next_id,
        **child.model_dump(),
    )

    children.append(new_child)
    _next_id += 1

    return new_child


@router.get(
    "",
    response_model=List[Child],
)
def list_children() -> List[Child]:
    return children


@router.get(
    "/{id}",
    response_model=Child,
)
def get_child(id: int) -> Child:
    for child in children:
        if child.id == id:
            return child

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Child not found",
    )


@router.patch(
    "/{id}",
    response_model=Child,
)
def update_child(id: int, update: ChildUpdate) -> Child:
    for index, child in enumerate(children):
        if child.id == id:
            updates = update.model_dump(exclude_unset=True)
            updated_child = child.model_copy(update=updates)

            children[index] = updated_child

            return updated_child

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Child not found",
    )


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_child(id: int) -> None:
    for index, child in enumerate(children):
        if child.id == id:
            children.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Child not found",
    )