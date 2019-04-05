from PIL import Image
import os

input_folder = 'x4/'
output_folder = 'x1/'

spritesheet_list = [
  'train-station_0000',
  'train-station-CC_0000',
]

for spritesheet_name in spritesheet_list:
  
  input_image = Image.open(input_folder + spritesheet_name + '.png')
  output_width = int(input_image.width/4)
  output_height = int(input_image.height/4)

  output_image = input_image.resize((output_width, output_height))

  os.makedirs(output_folder, exist_ok = True)
  output_image.save(output_folder + spritesheet_name + '-x1' + '.png')