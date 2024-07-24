from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.routes.route import router

app = FastAPI()

# Include the router without a prefix
app.include_router(router, prefix="/api")

# Serve static files from the 'front-end/static' directory
app.mount("/static", StaticFiles(directory="front-end/static"), name="static")

# Serve the main HTML file
@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("front-end/index.html", "r") as f:
        return HTMLResponse(content=f.read())
