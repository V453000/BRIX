from PIL import Image
import os
import argparse
import shutil

def resize(options):
  input_path    = options['input']

  if 'output'        in options:
    output_path   = options['output']
  else:
    output_path   = ''

  if 'divider'       in options:
    divider       = options['divider']
  else:
    divider       = 4
  
  if 'remove_frames' in options:
    remove_frames = options['remove_frames']
  else:
    remove_frames = False

  if 'skip_resizer'  in options:
    skip_resizer  = options['skip_resizer']
  else:
    skip_resizer  = False
 
  if remove_frames == True:
    png = '.png'
    png_charcount = len(png)
    path_without_png = input_path[:-png_charcount]

    remove_char = True
    while remove_char == True:
      last_char = path_without_png[-1:]
      if   last_char == '0':
        remove_char = True
      elif last_char == '1':
        remove_char = True
      elif last_char == '2':
        remove_char = True
      elif last_char == '3':
        remove_char = True
      elif last_char == '4':
        remove_char = True
      elif last_char == '5':
        remove_char = True
      elif last_char == '6':
        remove_char = True
      elif last_char == '7':
        remove_char = True
      elif last_char == '8':
        remove_char = True
      elif last_char == '9':
        remove_char = True
      elif last_char == '_':
        remove_char = True
      elif last_char == '-':
        remove_char = True
      else:
        remove_char = False
      
      if remove_char == True:
        path_without_png = path_without_png[:-1]

    # end of removing characters

    new_input_path = path_without_png + png
    shutil.move(input_path, new_input_path)
    input_path = new_input_path
    print('Input path without frame count is:', input_path)


  if skip_resizer == False:
    if output_path == '':
      print('No output path given, no resizing done.')
    else:
      input_image = Image.open(input_path)
      output_width = int(input_image.width/divider)
      output_height = int(input_image.height/divider)

      output_image = input_image.resize((output_width, output_height), Image.Resampling.NEAREST)

      output_folder = os.path.dirname(output_path)
      os.makedirs(output_folder, exist_ok = True)
      output_image.save(output_path)

    print('Resizing finished!')


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = 'Process some arguments.')
  parser.add_argument('-i', '--input',
                      help='Path to input file.',
                      type = str,
                      required = True)
  parser.add_argument('-o', '--output',
                      help='Path for output file.',
                      type = str,
                      required = False)
  parser.add_argument('-d', '--divider',
                      help = 'Number to divide original image size with.',
                      type = int,
                      required = False
                     )
  parser.add_argument('-r', '--remove_frames',
                      help = 'Bool to remove frame numbers.',
                      action = 'store_true'
                     )
  parser.add_argument('-x', '--skip_resizer',
                      help = 'Bool to skip resizing.',
                      action = 'store_true'
                     )
  options = vars(parser.parse_args())
  default_values = [
    ('input'            , '' ),
    ('output'           , '' ),
    ('divider'          , 4  ),
  ]
  for name, def_value in default_values:
    if not options[name]:
      options[name] = def_value
  
  print(options.type)
  resize(options)