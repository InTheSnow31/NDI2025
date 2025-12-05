FROM python:3.13

RUN apt-get update
RUN apt-get install libgl1 libglx-mesa0 -y
RUN apt-get install ffmpeg libsm6 libxext6 -y

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py visualizer.py ./

CMD [ "uvicorn", "main:app", "--reload" ]