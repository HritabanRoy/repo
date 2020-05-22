import os
os.system("""
echo Input ext: 
read init
echo Output ext:
read outp
for f in *.$init
do ffmpeg -i "$f" -c copy "${f%.$init}.$outp"
done
""")
