cls

call run-RGBA-EATER_bridges.bat
call run-RGBA-EATER_bridges-mask.bat
call run-RGBA-EATER_bridges-transparency.bat

_mask-copier.py -m 8bpp/bridges/bridges-transparency-x1-8bpp.png -f 8bpp/bridges/bridges-8bpp.png
_mask-copier.py -m 8bpp/bridges/bridges-transparency-x4-8bpp.png -f 8bpp/bridges/bridges-8bpp.png
_mask-copier.py -m 8bpp/bridges/bridges-mask-full-color-8bpp.png -f 8bpp/bridges/bridges-8bpp.png

cd ..
call _SHIT-BRIX_.bat

pause