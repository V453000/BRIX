# _resizer.py -r -d 4 -i 32bpp/train-depot/x4/train-depot_0000.png    -o 32bpp/train-depot/x1/train-depot-x1.png

# RGBA-EATER.py -n train-depot/x4/train-depot        -e ALL
# RGBA-EATER.py -n train-depot/x1/train-depot-x1     -e ALL

# cd ..

# C:\NML\nmlc -c --default-lang=english.lng --grf=BRIX.grf BRIX.nml
# copy /Y BRIX.grf "C:\Users\V\Documents\OpenTTD\newgrf"
# pause


# Resizing x4 to x1
from _resizer import resize
resize(
    {
        'input' : '32bpp/train-depot/x4/train-depot.png',
        'output' : '32bpp/train-depot/x1/train-depot-x1.png',
        'divider' : 4
    }
)

# RGBA Eater
import subprocess
subprocess.run(['python', 'RGBA-EATER.py', '-n', 'train-depot/x4/train-depot',    '-e', 'ALL'])
subprocess.run(['python', 'RGBA-EATER.py', '-n', 'train-depot/x1/train-depot-x1',    '-e', 'ALL'])

# compile the grf etc
import os
os.chdir('..')
subprocess.run(['python', '_SHIT-BRIX_.py'])
