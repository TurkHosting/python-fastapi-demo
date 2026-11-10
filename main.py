import sys

from fastapi import FastAPI

app = FastAPI(title="python-fastapi-demo")


@app.get("/")
async def index():
    return {"framework": "FastAPI", "python": sys.version.split()[0]}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/items/{item_id}")
async def item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
