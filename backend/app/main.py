from typing import List

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="TinyScholar API",
    description="AI-powered game-based learning platform for children.",
    version="0.1.0"
)


@app.get(
    "/",
    tags=["General"]
)
def root():
    return {"message": "Welcome to TinyScholar"}


@app.get("/health", tags=["General"])
def health():
    return {"status": "ok"}


# --- Child profiles (in-memory for now) ---

class ChildCreate(BaseModel):
    name: str
    age: int = Field(ge=6, le=17)  # Pydantic validates before the endpoint runs
    grade: str


class Child(ChildCreate):
    id: int


children: List[Child] = []
_next_id = 1


@app.post(
    "/children",
    tags=["Children"],
    response_model=Child,
    status_code=status.HTTP_201_CREATED
)

def create_child(child: ChildCreate) -> Child:
    global _next_id
    new_child = Child(id=_next_id, **child.model_dump())
    children.append(new_child)
    _next_id += 1
    return new_child


@app.get(
    "/children",
    tags=["Children"],
    response_model=List[Child]
)
def list_children() -> List[Child]:
    return children

@app.get("/children/{id}", tags=["Children"], response_model=Child)
def get_child(id: int):
    for child in children:
        if child.id == id:
            return child
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Child not found")
