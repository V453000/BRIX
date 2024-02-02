import subprocess
import shutil
import os

def compile_grf():
    print('Starting to compile GRF...')
    subprocess.run(["nmlc", "-c", "--default-lang=english.lng", "--grf=BRIX.grf", "BRIX-NML-combined.nml", "--verbosity=3"])

def copy_grf_to_game():
    game_path = "/Users/v453000/Documents/OpenTTD/newgrf"
    grf_name = "BRIX.grf"

    source = grf_name
    destination = os.path.join(game_path, grf_name)

    shutil.copy(source, destination)
    print('Copied', grf_name, 'to', game_path)

