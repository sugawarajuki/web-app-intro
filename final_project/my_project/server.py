from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, PlainTextResponse
from pydantic import BaseModel
from typing import List, Optional

import sqlite3
import os
import uvicorn

app = FastAPI()

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "data.db")


class Training(BaseModel):
    id: Optional[int] = None
    exercise: str
    sets: int
    reps: int


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS trainings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise TEXT NOT NULL,
            sets INTEGER NOT NULL,
            reps INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


@app.get("/trainings", response_model=List[Training])
def read_trainings():
    conn = get_db_connection()
    items = conn.execute("SELECT * FROM trainings").fetchall()
    conn.close()
    return [Training(**dict(item)) for item in items]


@app.post("/trainings", response_model=Training, status_code=201)
def create_training(item: Training):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO trainings (exercise, sets, reps) VALUES (?, ?, ?)",
        (item.exercise, item.sets, item.reps),
    )
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()
    return Training(
        id=item_id,
        exercise=item.exercise,
        sets=item.sets,
        reps=item.reps,
    )


# ここから下は書き換えない
@app.get("/", response_class=HTMLResponse)
async def read_html():
    html_file_path = os.path.join(BASE_DIR, "client.html")
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/style.css")
def read_css():
    css_file_path = os.path.join(BASE_DIR, "style.css")
    with open(css_file_path, "r", encoding="utf-8") as f:
        css_content = f.read()
    return Response(content=css_content, media_type="text/css")


@app.get("/script.js", response_class=PlainTextResponse)
def read_js():
    js_file_path = os.path.join(BASE_DIR, "script.js")
    with open(js_file_path, "r", encoding="utf-8") as f:
        js_content = f.read()
    return PlainTextResponse(
        content=js_content, status_code=200, media_type="application/javascript"
    )


@app.get("/favicon.ico")
def read_favicon():
    favicon_path = os.path.join(BASE_DIR, "favicon.ico")
    with open(favicon_path, "rb") as f:
        favicon_content = f.read()
    return Response(content=favicon_content, media_type="image/x-icon")


if __name__ == "__main__":
    initialize_db()
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)