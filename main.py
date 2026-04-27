import re
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
import pypinyin

app = FastAPI(title="拼音田字格默写纸生成器")

# CORS
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 模板和静态文件
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


class ConvertRequest(BaseModel):
    text: str


class WordItem(BaseModel):
    word: str
    pinyin: List[str]


class ConvertResponse(BaseModel):
    words: List[WordItem]


def split_words(text: str) -> List[str]:
    """按分隔符切分词语，支持多种分隔符"""
    # 将所有分隔符统一替换为半角空格
    text = re.sub(r'[，,、\t\n]', ' ', text)
    # 替换全角空格
    text = text.replace('\u3000', ' ')
    # 按空格切分，过滤空字符串
    words = [w.strip() for w in text.split() if w.strip()]
    return words


def get_pinyin(word: str) -> List[str]:
    """获取词语中每个字的拼音（带声调）"""
    py_list = pypinyin.pinyin(word, style=pypinyin.TONE, heteronym=False, neutral_tone_with_five=True)
    return [py[0] for py in py_list]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/convert", response_model=ConvertResponse)
async def convert(req: ConvertRequest):
    words = split_words(req.text)
    result = []
    for word in words:
        pinyin = get_pinyin(word)
        result.append(WordItem(word=word, pinyin=pinyin))
    return ConvertResponse(words=result)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
