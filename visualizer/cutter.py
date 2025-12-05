import cv2

input_video = "loop.mp4"
output_video = "loop_cut.mp4"
seconds_to_remove = 15

# Ouvrir la vidéo
cap = cv2.VideoCapture(input_video)
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Calculer le nombre de frames à sauter
frames_to_skip = int(fps * seconds_to_remove)

# Initialiser VideoWriter pour la vidéo finale
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# Lire et ignorer les premières frames
for _ in range(frames_to_skip):
    ret, _ = cap.read()
    if not ret:
        break  # si la vidéo est plus courte que 15s

# Lire le reste et écrire dans la nouvelle vidéo
while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()

print("Vidéo créée :", output_video)