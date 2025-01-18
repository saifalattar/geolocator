from fastapi import FastAPI, Request, routing
from fastapi.responses import RedirectResponse, HTMLResponse
import requests

app = FastAPI()


@app.get("/")
def read_root(r: Request):
    content = """<script>fetch("https://ipinfo.io/json")
.then((v)=>{
    v.json().then((val)=> {fetch("http://192.168.1.12:8000/".concat(val["ip"]))});
})</script>
"""
    return HTMLResponse(content)

@app.get("/{data}")
def getData(data):
    print(data)