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

def clear_temp_folder():
    temp_dir = "./temp"
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Erreur lors de la suppression du fichier {file_path}: {e}")


@app.post("/convert")
async def convert(file: UploadFile = File(...)):
    clear_temp_folder()
    # Sauvegarde le MP3 temporairement
    mp3_path = f"temp/{uuid.uuid4()}.mp3"
    mp4_path = f"temp/{uuid.uuid4()}.mp4"

    with open(mp3_path, "wb") as f:
        f.write(await file.read())

    # Conversion
    product(mp3_path, mp4_path)

    # Retourne la vidéo
    return FileResponse(mp4_path, media_type="video/mp4")
