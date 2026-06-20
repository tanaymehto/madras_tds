from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

df = pd.read_csv("q-fastapi.csv")

students = [
    {"studentId": int(row.studentId), "class": row["class"]}
    for _, row in df.iterrows()
]

@app.get("/api")
def get_students(class_: list[str] | None = Query(None, alias="class")):
    if not class_:
        return {"students": students}

    return {
        "students": [
            s for s in students
            if s["class"] in class_
        ]
    }

@app.get("/")
def root():
    return {"status": "ok"}