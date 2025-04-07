from fastapi import FastAPI
import  uvicorn
import redis

app= FastAPI()

red_app = redis.StrictRedis(
    host='redis',
    port=6379,
)
red_app.set('count', '0')

@app.get("/ping")
async def get_status():
    return  {"status":"ok"}

@app.get("/count")
async def get_count():
    red_app.incr('count', '1')
    print(red_app.get('count'))
    return red_app.get('count')

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)