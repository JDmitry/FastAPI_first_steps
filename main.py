from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI"}

@app.get("/about")
def about():
    return {"message": "About"}