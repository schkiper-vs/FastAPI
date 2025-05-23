from fastapi import FastAPI
import  uvicorn

app= FastAPI()

@app.get("/ping")
async def get_pong():
    return  {"status":"ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)