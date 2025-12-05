<script setup lang="ts">
import { useTemplateRef } from 'vue';

const fileInput = useTemplateRef("mp3File");
const loadingDiv = useTemplateRef("loading");
const videoPlayer = useTemplateRef("videoPlayer");

async function uploadAndPlay() {
  if (fileInput.value === null) return;

  if (!fileInput.value.files || fileInput.value.files.length === 0) {
    alert("Veuillez sélectionner un fichier MP3.");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.value.files[0]!);


  // Affiche le loader
  loadingDiv.value!.style.display = "block";
  videoPlayer.value!.src = ""; // vide le player

  try {
    const response = await fetch(import.meta.env.VITE_AUDIOVIZ_BACKEND_URL + "convert", {
      method: "POST",
      body: formData
    });

    if (!response.ok) {
      alert("Erreur lors de la conversion.");
      return;
    }

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);

    videoPlayer.value!.src = url;
    videoPlayer.value!.load();
    videoPlayer.value!.play();

  } catch (err) {
    console.error(err);
    alert("Une erreur est survenue lors de la requête.");
  } finally {
    loadingDiv.value!.style.display = "none";
  }
}
</script>

<template>
  <div id="floatingWindow">
    <h2>Convertir un MP3 en vidéo</h2>

    <div ref="loading" id="loading">
      <div class="spinner"></div> Conversion en cours...
    </div>

    <input class="text-[#333]" type="file" ref="mp3File" accept="audio/mp3">
    <button class="text-[#333]" @click="uploadAndPlay()">Envoyer et jouer</button>

    <video ref="videoPlayer" controls></video>
  </div>
</template>

<style scoped>
/* Fenêtre flottante */
#floatingWindow {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 300px;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  padding: 15px;
  z-index: 1000;
}

#floatingWindow h2 {
  margin: 0 0 10px 0;
  font-size: 16px;
  color: #333;
}

#floatingWindow input,
#floatingWindow button {
  width: 100%;
  margin-bottom: 10px;
}

#floatingWindow video {
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 8px;
}

/* Loader */
#loading {
  display: none;
  text-align: center;
  margin-bottom: 10px;
}

.spinner {
  width: 24px;
  height: 24px;
  border: 3px solid #ccc;
  border-top: 3px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  display: inline-block;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>