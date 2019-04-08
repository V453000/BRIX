_resizer.py -r -d 4 -i 32bpp/train-depot/x4/train-depot-monorail_0000.png    -o 32bpp/train-depot/x1/train-depot-monorail-x1.png

RGBA-EATER.py -n train-depot/x4/train-depot-monorail        -e ALL
RGBA-EATER.py -n train-depot/x1/train-depot-monorail-x1     -e ALL

cd ..

C:\NML\nmlc -c --default-lang=english.lng --grf=BRIX.grf BRIX.nml
copy /Y BRIX.grf "C:\Users\V\Documents\OpenTTD\newgrf"
pause
