import ffmpeg
import os

sourcePath = r'C:\Users\valen\Documents\Projets\mp3slower\musique'
destinationPath = r'C:\Users\valen\Documents\Projets\mp3slower\slowedreverbedmp3'

os.makedirs(destinationPath, exist_ok=True)

for file in os.listdir(sourcePath):
    if file.endswith('.mp3'):
        (ffmpeg.input(os.path.join(sourcePath, file))
               .output(os.path.join(destinationPath, f"{os.path.splitext(file)[0]} [slowed ~ reverb].mp3"),
                       filter_complex='lowpass=f=10000,asetrate=48000*0.92,aresample=48000')
               .run())
