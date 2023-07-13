from typing import Union
from . import etl_trafico

from fastapi import FastAPI
import psycopg2

app = FastAPI()

connection = psycopg2.connect(
    host="postgresql",
    database="postgres",
    user="postgres",
    password="postgres"
)
with connection.cursor() as cur:
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL
                )""")
    connection.commit()

@app.get("/select_users")
async def get_users():
    with connection.cursor() as cur:
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
    return rows

@app.post("/insert_users")
async def create_user(user: dict):
    with connection.cursor() as cur:
        cur.execute(f"INSERT INTO users (name, email) VALUES ('{user['name']}', '{user['email']}')")
        connection.commit()
    return {"message": "User created successfully"}

@app.get("/")
def read_root():
    return {"Hello": "World Juan Manuel Restrepo"}

@app.get("/etl")
def func_etl_trafico():
    e = ""
    try:    
        variable = str(etl_trafico.etl_trafico_prueba())
        e = variable
        etl_trafico.etl_trafico()
        return {"Hello": str(e)}
    except Exception as e:
        return {"Hello": str(e)}

@app.get("/etl1")
def func_etl_trafico1():
    etl_trafico.etl_trafico()
    return {"Hello": "juan"}

@app.get("/etl2")
def func_etl_trafico1():
    for i in range(6):
        return {"Hello": str(i)}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
