from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{name}")
def users(name:str = Path(min_length=3, max_length=20)):
    return {"user_id": name}

