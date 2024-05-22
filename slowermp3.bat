for %%f in (musique\*.mp3) do (
    ffmpeg -i "musique\%%~nf.mp3" -filter_complex "lowpass=f=10000,asetrate=48000*0.9,aresample=48000,aecho=0.8:0.9:1000:0.3" ".\slowedreverbedmp3\%%~nf [slowed ~ reverb].mp3"
)
pause
