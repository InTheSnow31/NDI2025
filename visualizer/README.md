### OBJECTIF 

Pour le défi de la NDI 2025, le défi CAPGEMINI était de faire un visualiser de musique intégré au site.

### Fonctionnement

Après avoir sélectionné la musique (en .mp3, nom sans espaces), une fonction python est appelée par l'intermédiaire de FASTAPI. Cette dernière adapte le rythme d'une vidéo "sans fin" (lien plus bas). Pour cela, on saute des images de la vidéo en fonction du % de basses. De la même manière la teinte est adaptée.

### Lancement 

Après avoir activer le venv, lancer le service :
uvicorn main:app --reload

Dans le dossier où il y a le html 

# Contenu utilisé : 
https://www.youtube.com/watch?v=xqtSbOLKIz4&list=PL4jjgxHdfmYYTewK-MfR4-BFLj7zE6GpN : Vidéo boucle sans fin, utilisation autorisée