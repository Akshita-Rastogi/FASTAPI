import sqlite3
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import json
import psycopg2

class Item(BaseModel):
    name: str
    rfid: str

app = FastAPI()

def db(database_name='database.db'):
    return psycopg2.connect(database=database_name)

def query_db(query, args=(), one=False):
    cur = db().cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r

@app.post("/")
async def create_item(item: Item):
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        query = '''INSERT INTO Data (Name, RFID) VALUES ('{0}','{1}');'''.format(item.name,item.rfid)
        # Create table
        print(query)
        c.execute(query)
        my_query = query_db("select * from Data")

        json_output = json.dumps(my_query)


        conn.commit()
        #close the connection
        conn.close()

        return {"Status": json_output}
    except:
        return {"Status": "Fail"}



