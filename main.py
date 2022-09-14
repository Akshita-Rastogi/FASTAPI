import sqlite3
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

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
                    

        conn.commit()
        #close the connection
        conn.close()

        return {"Status": "Sucess"}
    except:
        return {"Status": "Fail"}



