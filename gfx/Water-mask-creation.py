import os
from PIL import Image
from copy import deepcopy

#112-121 to 245-254
# or 144-153 to 245-254

def create_color_dictionary(indexes):
    color_dictionary = {}
    palette_rgba = Image.open('x-script-input/openttd-palette-dos-RGBA.png')
    palette_index = Image.open('x-script-input/openttd-palette-dos-index.png')

    for y in range(0, palette_rgba.height):
        for x in range(0, palette_rgba.width):
            pix_index = palette_index.getpixel((x, y))
            if pix_index in indexes:
                pix_rgba = palette_rgba.getpixel((x, y))
                pix_rgb = (pix_rgba[0], pix_rgba[1], pix_rgba[2])
                color_dictionary[str(pix_rgb)] = pix_index
                print(pix_index, pix_rgb)

    return color_dictionary


def convert_to_water_mask(input_path, color_dict):
    palette_img_indexed = Image.open('x-script-input/palette_key.png')
    palette_data = deepcopy(palette_img_indexed.palette)

    with Image.open(input_path) as img:
        output_image = Image.new('L', (img.width, img.height), color = 0)
        output_image.putpalette(palette_data)
        for y in range(0, img.height):
            for x in range(0, img.width):
                pix_rgba = img.getpixel((x, y))
                if pix_rgba[3] > 0:
                    # print('non-alpha-pixel', pix_rgba)
                    pix_rgb = (pix_rgba[0], pix_rgba[1], pix_rgba[2])
                    # compare pixel to color dictionary
                    if str(pix_rgb) in color_dict:
                        result_index = int(color_dict[str(pix_rgb)])
                        #print(result_index,'-', x, y)
                        output_image.putpixel((x,y), (result_index))
                    else:
                        print('index not found:', pix_rgb,'- at location:', x, y)
        
        output_path = input_path.replace('32bpp', '8bpp')
        output_path = output_path.replace('.png', '-8bpp.png')
        output_image.save(output_path)

def dictionary_translation(dictionary, keys):
    for entry in dictionary:
        old_index = dictionary.get(entry)
        result = keys.get(str(old_index))
        print(entry, result)
        dictionary[entry] = result
    return dictionary



color_indexes_to_read = [144, 145, 146, 147, 148, 149, 150, 151, 152, 153]
color_translations = {
    '144' : 245,
    '145' : 246,
    '146' : 247,
    '147' : 248,
    '148' : 249,
    '149' : 250,
    '150' : 251,
    '151' : 252,
    '152' : 253,
    '153' : 254,
}

color_dict = create_color_dictionary(color_indexes_to_read)
print(color_dict)
color_dict_translated = dictionary_translation(color_dict, color_translations)
print(color_dict_translated)
convert_to_water_mask('32bpp/terrain/water-mask_0000.png', color_dict_translated)
