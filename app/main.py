from fastapi import FastAPI
import time
import redis
import psycopg2

app = FastAPI()

start_time = time.time()

@app.get("/")
def home():
    return {"message": "FastAPI Assignment Running"}

@app.get("/health")
def health():
    uptime = time.time() - start_time
    return {
        "status": "healthy",
        "uptime_seconds": round(uptime, 2)
    }

@app.get("/redis")
def redis_test():
    r = redis.Redis(host="redis", port=6379)
    r.set("test", "ok")
    return {"redis": r.get("test").decode()}

@app.get("/database")
def db_test():
    conn = psycopg2.connect(
        host="postgres",
        database="mydb",
        user="postgres",
        password="password123"
    )
    return {"db": "connected"}