from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import uuid
from visualizer import product
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crée le dossier temp si nécessaire
os.makedirs("temp", exist_ok=True)

@app.post("/convert")
async def convert(file: UploadFile = File(...)):
    # Sauvegarde le MP3 temporairement
    mp3_path = f"temp/{uuid.uuid4()}.mp3"
    mp4_path = f"temp/{uuid.uuid4()}.mp4"

    with open(mp3_path, "wb") as f:
        f.write(await file.read())

    # Conversion
    product(mp3_path, mp4_path)

    # Retourne la vidéo
    return FileResponse(mp4_path, media_type="video/mp4")
