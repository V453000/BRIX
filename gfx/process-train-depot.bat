_resizer.py -r -d 4 -i 32bpp/train-depot/x4/train-depot_0000.png    -o 32bpp/train-depot/x1/train-depot-x1.png

RGBA-EATER.py -n train-depot/x4/train-depot        -e ALL
RGBA-EATER.py -n train-depot/x1/train-depot-x1     -e ALL

cd ..

C:\NML\nmlc -c --default-lang=english.lng --grf=BRIX.grf BRIX.nml
copy /Y BRIX.grf "C:\Users\V\Documents\OpenTTD\newgrf"
pause
