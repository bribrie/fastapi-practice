from fastapi import FastAPI
from _routers import user, item, extra, auth, file

# Create a FastAPI instance
# Main point of interaction to create all my API
app = FastAPI()

app.include_router(user.router)
app.include_router(item.router)
app.include_router(extra.router)
app.include_router(auth.router)
app.include_router(file.router)

# Define a path operation decorator, path operation function
@app.get("/")
async def root():
    return {"message": "Hello World"} 