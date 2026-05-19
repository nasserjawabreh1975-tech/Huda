from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def root():
    return {"HUDA":"ONLINE"}

@app.post("/execute")
def execute(cmd:str):

    result=subprocess.getoutput(cmd)

    return {"output":result}
