import os
from PIL import Image
import argparse
from copy import deepcopy

def run():
  mask_path   = options['mask']
  output_path = options['output']

  mask_image = Image.open(mask_path)
  output_image = Image.open(output_path)

  for y in range(0, mask_image.height):
    for x in range(0, mask_image.width):
      pixel = mask_image.getpixel((x,y))
      if pixel != 0:
        output_image.putpixel((x,y), pixel)
  
  output_image.save(output_path)
  print('Mask copying finished!')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = 'Process some arguments.')
  parser.add_argument('-m', '--mask',
                      help='Path to mask file to copy from.',
                      type = str,
                      required = True)
  parser.add_argument('-f', '--output',
                      help='Path to file to put mask to.',
                      type = str,
                      required = True)
  options = vars(parser.parse_args())
  default_values = [
    ('mask'             , '' ),
    ('output'           , '' ),
  ]
  for name, def_value in default_values:
    if not options[name]:
      options[name] = def_value
  
  run()