from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Version 3 - add uv"}


@app.get("/health")
def health():
    return {"status": "healthy"}