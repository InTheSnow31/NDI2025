### OBJECTIF 

Pour le défi de la NDI 2025, le défi CAPGEMINI était de faire un visualiser de musique intégré au site.

### Utilisation

Cliquer sur le widget flottant en bas à droite de l'écran et sélectionner un fichier .mp3 (sans espace dans le nom).
Après un petit peu d'attente, la vidéo devrait se lancer avec la musique automatiquement.
Les tests fonctionnels ont été réalisés sur Firefox.

Pour avoir un mp3 de votre musique préférée, il est possible d'aller sur https://notube.net/en/youtube-app-281, mettre le lien dans le champs de saisie et sélectionner le format mp3.

### Fonctionnement

Après avoir sélectionné la musique (en .mp3, nom sans espaces), une fonction python est appelée par l'intermédiaire de FASTAPI. Cette dernière adapte le rythme d'une vidéo "sans fin" (lien plus bas). Pour cela, on saute des images de la vidéo en fonction du % de basses. De la même manière la teinte est adaptée.

# Contenu utilisé : 
https://www.youtube.com/watch?v=xqtSbOLKIz4&list=PL4jjgxHdfmYYTewK-MfR4-BFLj7zE6GpN : Vidéo boucle sans fin, utilisation autorisée