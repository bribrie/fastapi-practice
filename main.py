from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from _routers import user, item, extra, auth, file

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

# Create a FastAPI instance
# Main point of interaction to create all my API
app = FastAPI()

# Custom exception handlers
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )

# Override the default exception handlers
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

# Define a path operation decorator, path operation function
@app.get("/")
async def root():
    return {"message": "Hello World"} 

@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}

@app.get("/exc-test/{test_id}")
async def read_item(test_id: int):
    if test_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"test_id": test_id}

app.include_router(user.router)
app.include_router(item.router)
app.include_router(extra.router)
app.include_router(auth.router)
app.include_router(file.router)