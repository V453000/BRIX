cls

@REM call run-RGBA-EATER_bridges.bat
@REM call run-RGBA-EATER_bridges-mask.bat
@REM call run-RGBA-EATER_bridges-transparency.bat

@REM _mask-copier.py -m 8bpp/bridges/bridges-transparency-x1-8bpp.png -f 8bpp/bridges/bridges-8bpp.png
@REM _mask-copier.py -m 8bpp/bridges/bridges-transparency-x4-8bpp.png -f 8bpp/bridges/bridges-8bpp.png
@REM _mask-copier.py -m 8bpp/bridges/bridges-mask-full-color-8bpp.png -f 8bpp/bridges/bridges-8bpp.png

_resizer.py -d 2 -i 32bpp/bridges/bridges.png                 -o 32bpp/bridges/x2/bridges-x2.png
_resizer.py -d 2 -i 32bpp/bridges/bridges-mask-full.png       -o 32bpp/bridges/x2/bridges-mask-full-x2.png
_resizer.py -d 2 -i 32bpp/bridges/bridges-mask-full-color.png -o 32bpp/bridges/x2/bridges-mask-full-color-x2.png
_resizer.py -d 2 -i 32bpp/bridges/bridges-transparency-x4.png    -o 32bpp/bridges/x2/bridges-transparency-x2.png

RGBA-EATER.py -t 32 -n bridges/x2/bridges-x2 -e ALL CC1 CC2
RGBA-EATER.py -t 32 -n bridges/x2/bridges-mask-full-x2 -e BROWN_1
RGBA-EATER.py -t 32 -n bridges/x2/bridges-mask-full-color-x2 -e BROWN_1 -
RGBA-EATER.py -t 32 -n bridges/x2/bridges-transparency-x2 -e GRAYSCALE -i 215 -j 1 -a 128 -c -l

_mask-copier.py -m 8bpp/bridges/x2/bridges-transparency-x2-8bpp.png -f 8bpp/bridges/x2/bridges-x2-8bpp.png
_mask-copier.py -m 8bpp/bridges/x2/bridges-mask-full-color-x2-8bpp.png -f 8bpp/bridges/x2/bridges-x2-8bpp.png

cd ..
@REM call _SHIT-BRIX_.bat

pause