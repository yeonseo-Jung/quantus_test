from typing import Union
import uvicorn

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routes import randoms
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

# from config import conf

def create_app():
    """
    앱 함수 실행
    :return:
    """
    # _conf = conf()
    app = FastAPI()

    # 데이터 베이스 이니셜라이즈

    # 레디스 이니셜라이즈

    # 미들웨어 정의

    # 라우터 정의
    app.include_router(randoms.router, tags=["Randoms"], prefix="/api")

    return app

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.post("/random/", response_class=HTMLResponse)
# async def post_random(request: Request, integer: str=Form(...) or None):
    
#     if integer:
#         _rand = get_random(int(integer))
#     else:
#         _rand = None
        
#     html = "random.html"
#     context = {
#         "request": request,
#         "integer": integer,
#         "random_number": _rand,
#     }
#     # return context
#     return templates.TemplateResponse(html, context=context)

# @app.get("/random/", response_class=HTMLResponse)
# async def post_random(request: Request):
    
#     html = "random.html"
#     context = {
#         "request": request
#     }
#     return templates.TemplateResponse(html, context=context)

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)