import librosa
import numpy as np
import cv2
import subprocess

def product(mp3_path, mp4_path):

    ############################################
    # Vidéo d'entrée
    ############################################

    input_video = "loop_cut.mp4"
    cap = cv2.VideoCapture(input_video)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # Redimension
    width, height = 720, 480

    # On précharge les frames pour relacher la lecture
    frames = []
    i = 0
    while True:
        i += 1
        print("Chargement du BG : ", i, "/", frame_count )
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(cv2.resize(frame, (width, height)))
    cap.release()

    ############################################
    # Vidéo de sortie
    ############################################

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('visualizer_temp.mp4', fourcc, fps, (width, height))

    ############################################
    # Audio
    ############################################

    audio_file = mp3_path
    y, sr = librosa.load(audio_file, sr=22050)
    frame_size = 2048
    hop = int(sr / fps)

    stft = np.abs(librosa.stft(y, n_fft=frame_size, hop_length=hop))
    freqs = librosa.fft_frequencies(sr=sr, n_fft=frame_size)
    times = librosa.frames_to_time(np.arange(stft.shape[1]), sr=sr, hop_length=hop)

    # Bandes
    bass_idx   = np.where((freqs >= 20) & (freqs < 150))[0]
    mid_idx    = np.where((freqs >= 250) & (freqs < 4000))[0]
    treble_idx = np.where((freqs >= 4000))[0]

    bass_energy   = stft[bass_idx].mean(axis=0)
    mid_energy    = stft[mid_idx].mean(axis=0)
    treble_energy = stft[treble_idx].mean(axis=0)

    # Décimation pour accélérer (optionnel)
    step = 1

    bass_energy = bass_energy[::step]
    mid_energy = mid_energy[::step]
    treble_energy = treble_energy[::step]
    times = times[::step]

    bass_max = np.max(bass_energy)
    mid_max = np.max(mid_energy)
    treble_max = np.max(treble_energy)

    # Normaliser
    bass_energy /= bass_max
    mid_energy /= mid_max
    treble_energy /= treble_max

    # Boucle principale

    t = 0
    current_frame = 0
    prev_hue, prev_val = 0, 0

    while t < len(bass_energy):

        # Vitesse
        speed_factor = int(1 + 6*bass_energy[t])
        current_frame += speed_factor
        current_frame = int(current_frame) % frame_count
        frame = frames[current_frame]

        # Teinte

        if bass_energy[t] > 0.3:  # Déterminer la teinte cible
            target_hue = 0          # rouge pour les basses
        else:
            target_hue = int(treble_energy[t] * 60) + 30  # jaune → cyan

        hue = int(prev_hue * 0.8 + target_hue * 0.2)
        prev_hue = hue

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype(np.float32)
        hsv[:, :, 0] = (hsv[:, :, 0] + hue) % 180  # teinte
        frame_mod = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

        out.write(frame_mod)

        # avancer audio
        t += 1

        print("Préparation du rendu :", t,"/",len(bass_energy))

    out.release()
    cap.release()
    cv2.destroyAllWindows()

    ############################################
    # Ajouter l'audio à la vidéo finale avec ffmpeg
    ############################################

    final_output = mp4_path
    import librosa
import numpy as np
import cv2
import subprocess

def product(mp3_path, mp4_path):

    ############################################
    # Vidéo d'entrée
    ############################################

    input_video = "loop_cut.mp4"
    cap = cv2.VideoCapture(input_video)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # Redimension
    width, height = 720, 480

    # On précharge les frames pour relacher la lecture
    frames = []
    i = 0
    while True:
        i += 1
        print("Chargement du BG : ", i, "/", frame_count )
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(cv2.resize(frame, (width, height)))
    cap.release()

    ############################################
    # Vidéo de sortie
    ############################################

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('visualizer_temp.mp4', fourcc, fps, (width, height))

    ############################################
    # Audio
    ############################################

    audio_file = mp3_path
    y, sr = librosa.load(audio_file, sr=22050)
    frame_size = 2048
    hop = int(sr / fps)

    stft = np.abs(librosa.stft(y, n_fft=frame_size, hop_length=hop))
    freqs = librosa.fft_frequencies(sr=sr, n_fft=frame_size)
    times = librosa.frames_to_time(np.arange(stft.shape[1]), sr=sr, hop_length=hop)

    # Bandes
    bass_idx   = np.where((freqs >= 20) & (freqs < 150))[0]
    mid_idx    = np.where((freqs >= 250) & (freqs < 4000))[0]
    treble_idx = np.where((freqs >= 4000))[0]

    bass_energy   = stft[bass_idx].mean(axis=0)
    mid_energy    = stft[mid_idx].mean(axis=0)
    treble_energy = stft[treble_idx].mean(axis=0)

    # Décimation pour accélérer (optionnel)
    step = 1

    bass_energy = bass_energy[::step]
    mid_energy = mid_energy[::step]
    treble_energy = treble_energy[::step]
    times = times[::step]

    bass_max = np.max(bass_energy)
    mid_max = np.max(mid_energy)
    treble_max = np.max(treble_energy)

    # Normaliser
    bass_energy /= bass_max
    mid_energy /= mid_max
    treble_energy /= treble_max

    # Boucle principale

    t = 0
    current_frame = 0
    prev_hue, prev_val = 0, 0

    while t < len(bass_energy):

        # Vitesse
        speed_factor = int(1 + 6*bass_energy[t])
        current_frame += speed_factor
        current_frame = int(current_frame) % frame_count
        frame = frames[current_frame]

        # Teinte

        if bass_energy[t] > 0.3:  # Déterminer la teinte cible
            target_hue = 0          # rouge pour les basses
        else:
            target_hue = int(treble_energy[t] * 60) + 30  # jaune → cyan

        hue = int(prev_hue * 0.8 + target_hue * 0.2)
        prev_hue = hue

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype(np.float32)
        hsv[:, :, 0] = (hsv[:, :, 0] + hue) % 180  # teinte
        frame_mod = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

        out.write(frame_mod)

        # avancer audio
        t += 1

        print("Préparation du rendu :", t,"/",len(bass_energy))

    out.release()
    cap.release()
    cv2.destroyAllWindows()

    ############################################
    # Ajouter l'audio à la vidéo finale avec ffmpeg
    ############################################

    final_output = mp4_path
    cmd = f'ffmpeg -y -i visualizer_temp.mp4 -i "{audio_file}" -c:v libx264 -pix_fmt yuv420p -c:a aac -b:a 192k "{final_output}"'
    subprocess.call(cmd, shell=True)

    print("Vidéo finale enregistrée :", final_output)
    