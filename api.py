from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    """com"""
    return "Hello World!"
@app.get("/test")

async def test():
    """com"""
    return "test"
