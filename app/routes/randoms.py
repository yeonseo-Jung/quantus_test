import os
import sys

from fastapi import FastAPI, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# root(app) 절대경로 추가
sys.path.append(os.path.abspath(BASE_DIR))
from api.get_randoms import get_random


router = APIRouter(prefix="/random")
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
# router.mount("/static", StaticFiles(directory="static"), name="static")

@router.post("/", response_class=HTMLResponse)
async def post_random(request: Request, integer: str=Form(...) or None):
    
    if integer:
        _rand = get_random(int(integer))
    else:
        _rand = None
        
    html = "random.html"
    context = {
        "request": request,
        "integer": integer,
        "random_number": _rand,
    }
    # return context
    return templates.TemplateResponse(html, context=context)

@router.get("/", response_class=HTMLResponse)
async def post_random(request: Request):
    
    html = "random.html"
    context = {
        "request": request
    }
    return templates.TemplateResponse(html, context=context)