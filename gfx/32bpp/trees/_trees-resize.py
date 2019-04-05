from PIL import Image
import os

input_folder = 'x4/'
output_folder = 'x1/'

for n in range(0, 62):
  n_2d = format(n, '02d')

  tree_name = 'Tree-' + n_2d

  input_image = Image.open(input_folder + tree_name + '.png')
  output_width = int(input_image.width/4)
  output_height = int(input_image.height/4)

  output_image = input_image.resize((output_width, output_height))

  os.makedirs(output_folder, exist_ok = True)
  output_image.save(output_folder + tree_name + '-x1' + '.png')