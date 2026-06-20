from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from io import StringIO
import sys
import traceback
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/healthz")
def healthz():
    return {"ok": True}

def execute_python_code(code: str):
    old_stdout = sys.stdout
    captured = StringIO()
    sys.stdout = captured

    try:
        exec(code)
        output = captured.getvalue()
        return {"success": True, "output": output}
    except Exception:
        return {"success": False, "output": traceback.format_exc()}
    finally:
        sys.stdout = old_stdout

@app.post("/code-interpreter")
def code_interpreter(req: CodeRequest):
    result = execute_python_code(req.code)

    if result["success"]:
        return {
            "error": [],
            "result": result["output"]
        }

    tb = result["output"]

    # Only extract line numbers from the user's code
    matches = re.findall(r'File "<string>", line (\d+)', tb)

    return {
        "error": [int(matches[-1])] if matches else [],
        "result": tb
    }