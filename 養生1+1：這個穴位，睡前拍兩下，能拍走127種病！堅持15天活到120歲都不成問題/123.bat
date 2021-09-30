REM 6:48~8:46
ffmpeg -ss 00:06:48 -t 00:01:58 -i "videoplayback.mp4" -vcodec copy -acodec copy  "01.mp4"
ffmpeg -i 01.mp4 -s 320x240 -b:v 500k -vcodec libx264 -r 29.97 -acodec libvo_aacenc -b:a 48k -ac 2 -ar 44100 -profile:v baseline -level 3.0 -f mp4 -y output.mp4
pause