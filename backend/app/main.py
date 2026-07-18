from fastapi import FastAPI

from .routers.children import router as children_router


app = FastAPI(
    title="TinyScholar API",
    description="AI-powered game-based learning platform for children.",
    version="0.1.0",
)


@app.get(
    "/",
    tags=["General"],
)
def root():
    return {"message": "Welcome to TinyScholar"}


@app.get(
    "/health",
    tags=["General"],
)
def health():
    return {"status": "ok"}


app.include_router(children_router)