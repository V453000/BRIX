import os
import math
import re

def check_int(string):
    if string[0] in ('-', '+'):
        return string[1:].isdigit()
    else:
        return string.isdigit()

input_file = open('../../src-includes/bridges.nml', 'r')
output_file = open('../../src-includes/bridges-x2.nml', 'w')
output_file.close()
output_file = open('../../src-includes/bridges-x2.nml', 'w')

for line in input_file:
    if 'alternative_sprites' in line:
        if 'ZOOM_LEVEL_IN_4X' in line:
            a = line.replace('IN_4X', 'IN_2X')
            b = a.replace('_x4', '_x2')
            c = b.replace('gfx/32bpp/bridges', 'gfx/32bpp/bridges/x2')
            d = c.replace('gfx/8bpp/bridges', 'gfx/8bpp/bridges/x2')
            e = d.replace('bridges.png', 'bridges-x2.png')
            f = e.replace('-8bpp.png', '-x2-8bpp.png')
            replaced_text = f.replace('(', '(,')

            split_text = replaced_text.split(',')
            # count integers
            int_count = 0
            for n in split_text:
                if check_int(n) == True:
                    int_count += 1

            if int_count == 4:
                new_line = []
                int_position = 0
                for n in split_text:
                    if check_int(n) == True:
                        if int_position < 2:
                            n = str(int(math.floor(int(n)/2)))
                        int_position += 1
                    new_line.append(n)
            else:
                new_line = split_text
            
            line_recombine = ','.join(new_line)
            line_recombine_revert_hack = line_recombine.replace('(,', '(')
            
            output_file.write(line_recombine_revert_hack)


    

