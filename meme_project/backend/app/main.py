from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine, Base
from models import Meme
from schemas import Meme, MemeCreate, MemeUpdate
from crud import get_meme, get_memes, create_meme, update_meme, delete_meme
from media_service import upload_file
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Измените на список разрешенных источников
    allow_credentials=True,
    allow_methods=["*"],  # Позволить все методы (GET, POST, PUT, DELETE, OPTIONS и т.д.)
    allow_headers=["*"],  # Позволить все заголовки
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="C:/Users/roman/meme_project/backend/app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("C:/Users/roman/meme_project/backend/app/static/index.html") as f:
        return HTMLResponse(content=f.read())

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/memes", response_model=List[Meme])
async def read_memes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    memes = get_memes(db, skip=skip, limit=limit)
    return memes

@app.get("/memes/{id}", response_model=Meme)
async def read_meme(id: int, db: Session = Depends(get_db)):
    db_meme = get_meme(db, meme_id=id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme

@app.post("/memes", response_model=Meme)
async def create_new_meme(text: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_url = upload_file(file.filename, file.file)
    meme = MemeCreate(text=text)
    return create_meme(db=db, meme=meme, image_url=file_url)

@app.put("/memes/{id}", response_model=Meme)
async def update_existing_meme(id: int, meme_update: MemeUpdate, db: Session = Depends(get_db)):
    db_meme = get_meme(db, meme_id=id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return update_meme(db=db, db_meme=db_meme, meme_update=meme_update)

@app.delete("/memes/{id}", response_model=Meme)
async def delete_existing_meme(id: int, db: Session = Depends(get_db)):
    db_meme = get_meme(db, meme_id=id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return delete_meme(db=db, meme_id=id)
