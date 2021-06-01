call run-RGBA-EATER_terrain.bat

_mask-copier.py -m 8bpp/terrain/terrain-mask-8bpp.png -f 8bpp/terrain/terrain-8bpp.png -x 0
_mask-copier.py -m 8bpp/terrain/terrain-mask-8bpp.png -f 8bpp/terrain/terrain-8bpp.png -x 4864
_mask-copier.py -m 8bpp/terrain/terrain-mask-8bpp.png -f 8bpp/terrain/terrain-8bpp.png -x 9728

Split-Spritesheets.py -- terrain

cd ..
call _SHIT-BRIX_.bat

pause