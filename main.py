from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse
 
app = FastAPI()

@app.get("/old")
def old():
    return RedirectResponse("https://metanit.com/python/fastapi")

@app.get("/new")
def new():
    return PlainTextResponse("Новая страница")