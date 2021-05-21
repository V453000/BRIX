import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

def split_spritesheet(input_path, rows, columns):
    with Image.open(input_path) as input_image:
        valid = True
        validation_width = input_image.width % columns
        if validation_width != 0:
            valid = False
            print('!!! Image Width could not be divided evenly. Use different Column count. % was', validation_width)

        validation_height = input_image.height % rows != 0
        if validation_height != 0:
            valid = False
            print('!!! Image Height could not be divided evenly. Use different Column count. % was', validation_height)
        
        if valid == True:
            print('Splitting', os.path.basename(input_path), 'into', rows, 'rows and', columns, 'columns.')
            piece_x = int(input_image.width / columns)
            piece_y = int(input_image.height / rows)

            crop_corner_1_x = 0
            crop_corner_1_y = 0
            crop_corner_2_x = piece_x
            crop_corner_2_y = piece_y
            for column in range(0, columns):
                # update crop corner X
                crop_corner_1_x = column * piece_x
                crop_corner_2_x = crop_corner_1_x + piece_x
                #print('Starting column', column, 'corners', crop_corner_1_x, crop_corner_1_y, crop_corner_2_x, crop_corner_2_y)

                for row in range (0, rows):
                    # update crop corner Y
                    crop_corner_1_y = row * piece_y
                    crop_corner_2_y = crop_corner_1_y + piece_y

                    #print('Starting row', row, 'corners', crop_corner_1_x, crop_corner_1_y, crop_corner_2_x, crop_corner_2_y)

                    output_image = input_image.crop( ( crop_corner_1_x, crop_corner_1_y, crop_corner_2_x, crop_corner_2_y ) )

                    # get filename without dirpath
                    output_basename = os.path.basename(input_path)
                    # remove .png
                    output_filename_no_extension = os.path.splitext(output_basename)[0]
                    # combine new file name
                    output_filename = str(output_filename_no_extension) + '_row' + str(row).zfill(2) + '_col' + str(column).zfill(2) + '.png'

                    # combine into new folder
                    output_folder = os.path.join('split-spritesheets', os.path.dirname(input_path) )
                    os.makedirs( output_folder, exist_ok = True)
                    
                    # combine into new file path
                    output_filepath = os.path.join(output_folder, output_filename)

                    output_image.save(output_filepath)

split_spritesheet( '8bpp/terrain/terrain-8bpp.png' , 1, 3)
split_spritesheet('32bpp/terrain/terrain.png'      , 1, 3)
