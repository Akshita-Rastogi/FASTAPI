import sqlite3
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import json

class Item(BaseModel):
    name: str
    rfid: str

app = FastAPI()








@app.post("/")
async def create_item(item: Item):
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        query = '''INSERT INTO Data (Name, RFID) VALUES ('{0}','{1}');'''.format(item.name,item.rfid)
        # Create table
        print(query)
        c.execute(query)
        rows = c.execute('''
    SELECT * from Data
    ''').fetchall()
        

        conn.commit()
        #close the connection
        conn.close()

        return {"Table data":rows}
    except:
        return {"Status": "Fail"}


@app.post("/delete/")
async def Delete():
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('DELETE FROM Data;',)
        rows = c.execute('''
    SELECT * from Data
    ''').fetchall()
        

        conn.commit()
        #close the connection
        conn.close()

        return {"Table data":rows}
    except:
        return {"Status": "Fail"}
