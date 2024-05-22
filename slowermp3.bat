for %%f in (musique\*.mp3) do (
    ffmpeg -i "musique\%%~nf.mp3" -filter:a "lowpass=f=10000,asetrate=48000*0.9,aresample=48000" ".\slowedreverbedmp3\%%~nf [slowed ~ reverb].mp3"
)
pause
