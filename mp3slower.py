import ffmpeg
import os

sourcePath = r'musique'
destinationPath = r'slowedreverbedmp3'

os.makedirs(destinationPath, exist_ok=True)

for file in os.listdir(sourcePath):
    if file.endswith('.mp3'):
        (ffmpeg.input(os.path.join(sourcePath, file))
               .output(os.path.join(destinationPath, f"{os.path.splitext(file)[0]} [slowed ~ reverb].mp3"),
                       lowpass=f=10000,asetrate=48000*0.9,aresample=48000,aecho=0.8:0.9:1000:0.3')
               .run())
