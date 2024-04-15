from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
