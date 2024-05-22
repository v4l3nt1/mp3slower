# mp3slower
mp3slower est un petit projet tout simple utilisant [**ffmpeg**](https://ffmpeg.org/) pour transformer (pas très simplement pour l'instant) n'importe quel fichier .mp3 en une version slowed~reverb.

## Prérequis
Pour utiliser cet outil, vous devrez évidemment posséder vos musiques au format .mp3, et les placer dans le dossier "musique" du projet, vous aller également devoir posséder ffmpeg, que vous pouvez obtenir via [ce lien](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z). 

Pour pouvoir utiliser pleinement ffmpeg et sans problème, vous devrez l'ajouter à la variable d'environnement PATH. Dézippez l'archive d'ffmpeg dans `C:\` et renommer le nouveau dossier en `ffmpeg`

Exécuter cette commande dans un cmd ouvert en mode administrateur :
```bash
setx /m PATH "C:\ffmpeg\bin;%PATH%"
```
ffmpeg est prêt !

Installer la bibliothèque `ffmpeg-python` avec la commande :
```bash
pip install ffmpeg-python
```

## Utilisation

D