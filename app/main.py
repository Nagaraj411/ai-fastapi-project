from fastapi import FastAPI
import redis
import psycopg2
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI Assignment Running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/redis")
def redis_test():
    try:
        r = redis.Redis(host="redis", port=6379)
        r.set("test", "working")
        return {"redis": r.get("test").decode()}
    except Exception as e:
        return {"error": str(e)}

@app.get("/database")
def db_test():
    try:
        conn = psycopg2.connect(
            host="postgres",
            database="mydb",
            user="postgres",
            password="password123"
        )
        return {"database": "connected"}
    except Exception as e:
        return {"error": str(e)}