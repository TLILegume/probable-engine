from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI + Hugging Face app!"}

# translate endpoint that takes in an english string and returns the spanish translation
@app.get("/status")
def checkdata():
    data = "this is one crazy application, ain't it??"
    return {"message": data, "size": len(data)}