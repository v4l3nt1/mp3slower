for %%f in (*.mp3) do (
    ffmpeg -i "%%~nf.mp3" -an -c:v copy image.jpg
    ffmpeg -r 0.1 -loop 1 -i "image.jpg" -i "%%~nf.mp3" -filter:a "lowpass=f=10000,asetrate=48000*0.9,aresample=48000" -c:v libx264 -shortest -n "..\slowedreverbedmp4\%%~nf [slowed ~ reverb].mp4"
    del image.jpg
)
pause