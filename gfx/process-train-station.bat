_resizer.py -r -d 4 -i 32bpp/train-station/x4/train-station_0000.png    -o 32bpp/train-station/x1/train-station-x1.png
_resizer.py -r -d 4 -i 32bpp/train-station/x4/train-station-CC_0000.png -o 32bpp/train-station/x1/train-station-CC-x1.png

RGBA-EATER.py -n train-station/x4/train-station        -e ALL
RGBA-EATER.py -n train-station/x4/train-station-CC     -e CC1

RGBA-EATER.py -n train-station/x1/train-station-x1     -e ALL
RGBA-EATER.py -n train-station/x1/train-station-CC-x1  -e CC1

_mask-copier.py -m 8bpp/train-station/x1/train-station-CC-x1-8bpp.png -f 8bpp/train-station/x1/train-station-x1-8bpp.png
_mask-copier.py -m 8bpp/train-station/x4/train-station-CC-8bpp.png    -f 8bpp/train-station/x4/train-station-8bpp.png

cd ..

C:\NML\nmlc -c --default-lang=english.lng --grf=BRIX.grf BRIX.nml
copy /Y BRIX.grf "C:\Users\V\Documents\OpenTTD\newgrf"
pause
