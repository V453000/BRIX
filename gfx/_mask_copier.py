import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
import argparse
from copy import deepcopy

def copy_mask(options):
  if 'mask'        in options:
    mask_path   = options['mask']
  else:
    raise Exception("mask_path must be specified")

  if 'output'        in options:
    output_path   = options['output']
  else:
    raise Exception("mask_path must be specified")

  if 'shift_x'in options:
    shift_x = int(options['shift_x'])
  else:
    shift_x = 0

  if 'shift_y'in options:
    shift_y = int(options['shift_y'])
  else:
    shift_y = 0
    
  mask_image = Image.open(mask_path)
  output_image = Image.open(output_path)

  for y in range(0, mask_image.height):
    for x in range(0, mask_image.width):
      pixel = mask_image.getpixel((x,y))
      if pixel != 0:
        if pixel in [215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226]:
          # replace pink pixel with a blue one instead
          output_image.putpixel((x + shift_x, y + shift_y), 0)
        else:
          output_image.putpixel((x + shift_x, y + shift_y), pixel)
  
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
  parser.add_argument('-x', '--shift_x',
                      help='Shift target x.',
                      type = str,
                      required = False)
  parser.add_argument('-y', '--shift_y',
                      help='Shift target y.',
                      type = str,
                      required = False)
  options = vars(parser.parse_args())
  default_values = [
    ('mask'             , '' ),
    ('output'           , '' ),
    ('shift_x'          , 0 ),
    ('shift_y'          , 0 ),
  ]
  for name, def_value in default_values:
    if not options[name]:
      options[name] = def_value
  
  copy_mask(options)