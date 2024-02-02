# _resizer.py -r -d 4 -i 32bpp/train-station/x4/train-station_0000.png    -o 32bpp/train-station/x1/train-station-x1.png
# _resizer.py -r -d 4 -i 32bpp/train-station/x4/train-station-CC_0000.png -o 32bpp/train-station/x1/train-station-CC-x1.png

# RGBA-EATER.py -n train-station/x4/train-station        -e ALL
# RGBA-EATER.py -n train-station/x4/train-station-CC     -e CC1

# RGBA-EATER.py -n train-station/x1/train-station-x1     -e ALL
# RGBA-EATER.py -n train-station/x1/train-station-CC-x1  -e CC1

# _mask-copier.py -m 8bpp/train-station/x1/train-station-CC-x1-8bpp.png -f 8bpp/train-station/x1/train-station-x1-8bpp.png
# _mask-copier.py -m 8bpp/train-station/x4/train-station-CC-8bpp.png    -f 8bpp/train-station/x4/train-station-8bpp.png

# cd ..

# C:\NML\nmlc -c --default-lang=english.lng --grf=BRIX.grf BRIX.nml
# copy /Y BRIX.grf "C:\Users\V\Documents\OpenTTD\newgrf"
# pause


# Resizing x4 to x1
from _resizer import resize
resize(
    {
        'input' : '32bpp/train-station/x4/train-station.png',
        'output' : '32bpp/train-station/x1/train-station-x1.png',
        'divider' : 4
    }
)
resize(
    {
    'input' : '32bpp/train-station/x4/train-station-CC.png',
    'output' : '32bpp/train-station/x1/train-station-CC-x1.png',
    'divider' : 4
    }
)

# RGBA Eater
import subprocess
subprocess.run(['python', 'RGBA-EATER.py', '-n', 'train-station/x4/train-station',    '-e', 'ALL'])
subprocess.run(['python', 'RGBA-EATER.py', '-n', 'train-station/x4/train-station-CC', '-e', 'CC1'])

subprocess.run(['python', 'RGBA-EATER.py', '-n', 'train-station/x1/train-station-x1',    '-e', 'ALL'])
subprocess.run(['python', 'RGBA-EATER.py', '-n', 'train-station/x1/train-station-CC-x1', '-e', 'CC1'])

# Copying masks over converted 8bpp
from _mask_copier import copy_mask
copy_mask(
    {
        'mask'    : '8bpp/train-station/x1/train-station-CC-x1-8bpp.png',
        'output'  : '8bpp/train-station/x1/train-station-x1-8bpp.png',
        'shift_x' : 0,
        'shift_y' : 0
    }
)
copy_mask(
    {
        'mask'    : '8bpp/train-station/x4/train-station-CC-8bpp.png',
        'output'  : '8bpp/train-station/x4/train-station-8bpp.png',
        'shift_x' : 0,
        'shift_y' : 0
    }
)

# compile the grf etc
import os
os.chdir('..')
subprocess.run(['python', '_SHIT-BRIX_.py'])
