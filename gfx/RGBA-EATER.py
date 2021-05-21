import math
import time
import datetime
import os
from os import remove
from PIL import Image
from multiprocessing import Pool
import multiprocessing
from copy import deepcopy
import argparse
from random import randint

Image.MAX_IMAGE_PIXELS = None

# print functions for control from debug_level parameter
def print_start(bool, string):
  if bool == True:
    print(str(string))
def print_lvl_0(debug_level, string):
  print(str(string))
def print_lvl_1(debug_level, string):
  if debug_level > 0:
    print(str(string))
def print_lvl_2(debug_level, string):
  if debug_level > 1:
    print(str(string))
def print_lvl_3(debug_level, string):
  if debug_level > 2:
    print(str(string))
def print_lvl_4(debug_level, string):
  if debug_level > 3:
    print(str(string))
def print_lvl_5(debug_level, string):
  if debug_level > 4:
    print(str(string))
def print_lvl_6(debug_level, string):
  if debug_level > 5:
    print(str(string))
def print_lvl_7(debug_level, string):
  if debug_level > 6:
    print(str(string))

# centralized way to turn off messages at the start of the script
show_starting_messages = False
# starting message
print_start(show_starting_messages, '-'*79)
print_start(show_starting_messages, 'Starting...')

# path definition
diskPath = ''# only fill if you want it to work in some absolute path
inputFolder_palette = diskPath + 'x-script-input/'
inputFolder = diskPath + '32bpp/'
outputFolder = diskPath + '8bpp/'
tempFolder = diskPath + 'x-script-temp/'#don't change this
# make sure the output folders exist
os.makedirs(outputFolder, exist_ok = True)
os.makedirs(tempFolder, exist_ok = True)

# making sure the output exists - !!!!! NEEDS TO BE MANUALLY ADDED HERE, CAN'T FEED BY ARGUMENT !!!!!
os.makedirs('8bpp/', exist_ok = True)

# printing path just to check
print_start(show_starting_messages, 'inputFolder is ' + inputFolder)
print_start(show_starting_messages, 'outputFolder is ' + outputFolder)

# starting timer
tt = time.time()
# format the time. I forgot how this works but it does.
startedTime = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')

# open palette images
# -----------------------------------------------------------------------------------------------------------------
# image for palette data
palette_img_indexed = Image.open(inputFolder_palette + 'palette_key.png')
palette_data = deepcopy(palette_img_indexed.palette)
print_start(show_starting_messages, 'Opening and loading palette: ' + 'openttd-palette-dos-RGBA.png')  
# image for colour comparing
palette_img = Image.open(inputFolder_palette + 'openttd-palette-dos-RGBA.png')
# creating palette list of RGB pixels
p=[]
for b in range(0,palette_img.height):
  for a in range(0, palette_img.width):
    p.append(palette_img.getpixel((a,b)))
print_start(show_starting_messages, 'Palette loaded.')

# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
#                                   D E F I N I N G   O F   F U N C T I O N S
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------

def rgb2palette(args):
  # extract the arguments from the big args list
  thread_id = args[0]
  input_image = args[1]
  x_start = args[2]
  x_end = args[3]
  allowed_colour_types = args[4]
  disallowed_colour_types = args[5]
  allowed_colour_indexes = args[6]
  disallowed_colour_indexes = args[7]
  alpha_ignore = args[8]
  alpha_offset_2 = args[9]
  alpha_offset_1 = args[10]
  red_weight = args[11]
  green_weight = args[12]
  blue_weight = args[13]
  arg_colour_shift = args[14]
  arg_debug_level = args[15]
  offset_list = args[16]
  arg_individual_temp = args[17]
  arg_checker_alpha = args[18]
  arg_probability_alpha = args[19]
  arg_checker_alpha_pink = args[20]
  print_lvl_5(arg_debug_level, 'rgb2palette args: ' + str(args))

  # create allowed colours list
  colours_to_filter = []
  for coltype in allowed_colour_types:
    if coltype == 'ALL':
      for n in range(1, 80):
        colours_to_filter.append(n)
      for n in range(88, 197):
        colours_to_filter.append(n)
      for n in range(205, 215):
        colours_to_filter.append(n)
    if coltype == 'GRAYSCALE':
      for n in range(1, 16):
        colours_to_filter.append(n)
    if coltype == 'METAL': 
      for n in range(16, 24):
        colours_to_filter.append(n)
    if coltype == 'LIME_GREEN': 
      for n in range(24, 32):
        colours_to_filter.append(n)
    if coltype == 'BEIGE': 
      for n in range(32, 40):
        colours_to_filter.append(n)
    if coltype == 'DARK_PINK': 
      for n in range(40, 48):
        colours_to_filter.append(n)
    if coltype == 'YELLOW': 
      for n in range(50, 53):
        colours_to_filter.append(n)
    if coltype == 'DARK_BEIGE': 
      for n in range(53, 60):
        colours_to_filter.append(n)
    if coltype == 'YELLOW': 
      for n in range(60, 70):
        colours_to_filter.append(n)
    if coltype == 'BROWN_1': 
      for n in range(70, 80):
        colours_to_filter.append(n)
    if coltype == 'CC2': 
      for n in range(80, 88):
        colours_to_filter.append(n)
    if coltype == 'DARK_GREEN': 
      for n in range(88, 96):
        colours_to_filter.append(n)
    if coltype == 'PALE_GREEN': 
      for n in range(96, 104):
        colours_to_filter.append(n)
    if coltype == 'BROWN_2': 
      for n in range(104, 112):
        colours_to_filter.append(n)
    if coltype == 'BROWN_3': 
      for n in range(112, 122):
        colours_to_filter.append(n)
    if coltype == 'BROWN_4': 
      for n in range(122, 128):
        colours_to_filter.append(n)
    if coltype == 'MAUVE': 
      for n in range(128, 136):
        colours_to_filter.append(n)
    if coltype == 'PURPLE': 
      for n in range(136, 144):
        colours_to_filter.append(n)
    if coltype == 'BLUE': 
      for n in range(144, 154):
        colours_to_filter.append(n)
    if coltype == 'LIGHT_BLUE': 
      for n in range(154, 162):
        colours_to_filter.append(n)
    if coltype == 'PINK': 
      for n in range(162, 170):
        colours_to_filter.append(n)
    if coltype == 'LIGHT_PURPLE': 
      for n in range(170, 178):
        colours_to_filter.append(n)
    if coltype == 'RED_1': 
      for n in range(178, 185):
        colours_to_filter.append(n)
    if coltype == 'RED_2': 
      for n in range(185, 192):
        colours_to_filter.append(n)
    if coltype == 'ORANGE': 
      for n in range(192, 198):
        colours_to_filter.append(n)
    if coltype == 'CC1': 
      for n in range(198, 206):
        colours_to_filter.append(n)
    if coltype == 'GREEN': 
      for n in range(206, 210):
        colours_to_filter.append(n)
    if coltype =='CYAN':
      for n in range(210, 215):
        colours_to_filter.append(n)
    if coltype == 'COLA': 
      for n in range(227, 232):
        colours_to_filter.append(n)
    if coltype == 'FIRE': 
      for n in range(232, 239):
        colours_to_filter.append(n)
    if coltype == 'LED_RED': 
      for n in range(239, 241):
        colours_to_filter.append(n)
    if coltype == 'LED_YELLOW': 
      for n in range(241, 245):
        colours_to_filter.append(n)
    if coltype == 'WATER': 
      for n in range(245, 255):
        colours_to_filter.append(n)
    if coltype == 'WHITE':
      for n in range(255, 256):
        colours_to_filter.append(n)
  
  # create disallowed colours list
  disallowed_colours = []
  for coltype in disallowed_colour_types:
    if coltype == 'ALL':
      for n in range(1, 80):
        disallowed_colours.append(n)
      for n in range(88, 197):
        disallowed_colours.append(n)
      for n in range(205, 215):
        disallowed_colours.append(n)
    if coltype == 'GRAYSCALE':
      for n in range(1, 16):
        disallowed_colours.append(n)
    if coltype == 'METAL': 
      for n in range(16, 24):
        disallowed_colours.append(n)
    if coltype == 'LIME_GREEN': 
      for n in range(24, 32):
        disallowed_colours.append(n)
    if coltype == 'BEIGE': 
      for n in range(32, 40):
        disallowed_colours.append(n)
    if coltype == 'DARK_PINK': 
      for n in range(40, 48):
        disallowed_colours.append(n)
    if coltype == 'YELLOW': 
      for n in range(50, 53):
        disallowed_colours.append(n)
    if coltype == 'DARK_BEIGE': 
      for n in range(53, 60):
        disallowed_colours.append(n)
    if coltype == 'YELLOW': 
      for n in range(60, 70):
        disallowed_colours.append(n)
    if coltype == 'BROWN_1': 
      for n in range(70, 80):
        disallowed_colours.append(n)
    if coltype == 'CC2': 
      for n in range(80, 88):
        disallowed_colours.append(n)
    if coltype == 'DARK_GREEN': 
      for n in range(88, 96):
        disallowed_colours.append(n)
    if coltype == 'PALE_GREEN': 
      for n in range(96, 104):
        disallowed_colours.append(n)
    if coltype == 'BROWN_2': 
      for n in range(104, 112):
        disallowed_colours.append(n)
    if coltype == 'BROWN_3': 
      for n in range(112, 122):
        disallowed_colours.append(n)
    if coltype == 'BROWN_4': 
      for n in range(122, 128):
        disallowed_colours.append(n)
    if coltype == 'MAUVE': 
      for n in range(128, 136):
        disallowed_colours.append(n)
    if coltype == 'PURPLE': 
      for n in range(136, 144):
        disallowed_colours.append(n)
    if coltype == 'BLUE': 
      for n in range(144, 154):
        disallowed_colours.append(n)
    if coltype == 'LIGHT_BLUE': 
      for n in range(154, 162):
        disallowed_colours.append(n)
    if coltype == 'PINK': 
      for n in range(162, 170):
        disallowed_colours.append(n)
    if coltype == 'LIGHT_PURPLE': 
      for n in range(170, 178):
        disallowed_colours.append(n)
    if coltype == 'RED_1': 
      for n in range(178, 185):
        disallowed_colours.append(n)
    if coltype == 'RED_2': 
      for n in range(185, 192):
        disallowed_colours.append(n)
    if coltype == 'ORANGE': 
      for n in range(192, 198):
        disallowed_colours.append(n)
    if coltype == 'CC1': 
      for n in range(198, 206):
        disallowed_colours.append(n)
    if coltype == 'GREEN': 
      for n in range(206, 210):
        disallowed_colours.append(n)
    if coltype =='CYAN':
      for n in range(210, 215):
        disallowed_colours.append(n)
    if coltype == 'COLA': 
      for n in range(227, 232):
        disallowed_colours.append(n)
    if coltype == 'FIRE': 
      for n in range(232, 239):
        disallowed_colours.append(n)
    if coltype == 'LED_RED': 
      for n in range(239, 241):
        disallowed_colours.append(n)
    if coltype == 'LED_YELLOW': 
      for n in range(241, 245):
        disallowed_colours.append(n)
    if coltype == 'WATER': 
      for n in range(245, 255):
        disallowed_colours.append(n)
    if coltype == 'WHITE':
      for n in range(255, 256):
        disallowed_colours.append(n)

  # add individual disallowed colours
  for n in disallowed_colour_indexes:
    disallowed_colours.append(n)

  # move non-disallowed colours to a new list
  filtered_colours_to_filter = []
  for c in colours_to_filter:
    skip = 0
    for d in disallowed_colours:
      if c == d:
        skip = 1
    if skip == 0:
      filtered_colours_to_filter.append(c)
  
  # add individual allowed colours
  for n in allowed_colour_indexes:
    filtered_colours_to_filter.append(n)

  print_lvl_4(arg_debug_level, 'Colours to filter: ' + str(filtered_colours_to_filter))

  # open input image
  i = Image.open(inputFolder + input_image + '.png')
  print_lvl_2(arg_debug_level, 'Thread ' + str(thread_id) + ' Opening: ' + input_image + '.png')  
  
  # create new empty indexed image for output
  imageOutput = Image.new('L', (i.width,i.height), color = 0)
  
  # go through the input image - y axis
  for y in range (0, i.height):
    # timestamp for debug
    ts = time.time()
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    if y%32 == 0:
      print_lvl_5(arg_debug_level, 'Thread ' + str(thread_id) + ' ' + timeStamp + ' - ' + input_image + ' row {}'.format(y))

    # go through the input image - x axis, limited by threaded strips
    for x in range (x_start, x_end):
      # defining winner variables just so they exist
      winnerDistance = 100000000
      winnerID = 0
      # loading pixel from image and separating RGBA
      pixelNumber = x + (y * i.width)
      pix = i.getpixel((x,y))
      pixRed = pix[0]
      pixGreen = pix[1]
      pixBlue = pix[2]
      pixAlpha = pix[3]

      # check Alpha in pixel, and output alpha/color offset
      if pixAlpha < alpha_ignore:
        finalAlpha = 0
        colorOffset = 0
      if pixAlpha >= alpha_ignore and pixAlpha < 178:
        finalAlpha = 255
        colorOffset = 2
      if pixAlpha >= alpha_offset_1 and pixAlpha < alpha_offset_2:
        finalAlpha = 255
        colorOffset = 1
      if pixAlpha >= alpha_offset_2:
        finalAlpha = 255
        colorOffset = 0

      # checker alpha
      if arg_checker_alpha > 0:
        if pixAlpha >= alpha_ignore:
          checker_coord = math.floor(x/arg_checker_alpha) + math.floor(y/arg_checker_alpha)
          if arg_checker_alpha_pink == False:
            if checker_coord % 2 == 0:
              pixAlpha = 255
            else:
              pixAlpha = 0
          elif arg_checker_alpha_pink == True:
            if checker_coord % 2 == 0:
              pixAlpha = 255
            else:
              pixAlpha = 255
              pixRed = 255
              pixGreen = 0
              pixBlue = 255
      # random alpha
      elif arg_probability_alpha == True:
        random_alpha_decider = randint(0, 255)
        if pixAlpha > random_alpha_decider:
          pixAlpha = 255
        else:
          pixAlpha = 0

          
      # if alpha above 50%, do colour comparing to palette
      if pixAlpha >= alpha_ignore:
        # go through all of the specified colours to filter
        for colour_id in filtered_colours_to_filter:
          rgb1 = p[colour_id]
          r1 = rgb1[0]
          g1 = rgb1[1]
          b1 = rgb1[2]

          l1 = (r1*red_weight + g1*green_weight + b1*blue_weight) / 255000
          l2 = (pixRed*red_weight + pixGreen*green_weight + pixBlue*blue_weight) / 255000
          dL = l1-l2
          dR = (r1-pixRed)/255
          dG = (g1-pixGreen)/255
          dB = (b1-pixBlue)/255
          distance = (dR*dR*red_weight*0.001 + dG*dG*blue_weight*0.001 + dB*dB*blue_weight*0.001)*0.75 + dL*dL
          # if it's better match than the previous tries, save it as the new winner
          if distance < winnerDistance:
            winnerDistance = distance
            winnerID = colour_id

      # final color changed by colorOffset
      finalID = offset_list[winnerID][colorOffset] #winnerID - colorOffset
      # finalAlpha taken from the if output above palette colour comparing

      # making sure that disallowed colours don't appear even by color offset.
      # if the disallowed colour appears with color offset = 2, try with color offset = 1.
      # if the problem persists, remove color offset
      if colorOffset == 2:
        for g in disallowed_colours:
          if g == finalID:
            colorOffset = 1
            finalID = offset_list[winnerID][colorOffset]
      if colorOffset == 1:
        for g in disallowed_colours:
          if g == finalID:
            colorOffset = 0
            finalID = offset_list[winnerID][colorOffset]
         
      # argument to ignore colorOffset
      if arg_colour_shift == False:
        finalID = winnerID

      # put the final pixel into the output picture
      imageOutput.putpixel((x,y),(finalID))
  
  # crop the output image based on the threaded strip values
  # because indexed images don't have alpha, this makes it easier to combine them later
  cropped_imageOutput = imageOutput.crop((x_start, 0,x_end,i.height))
  # put the palette data into the output
  cropped_imageOutput.putpalette(palette_data)
  # save the output image to temp folder (with individual parameter or without)
  if arg_individual_temp == True:
    cropped_imageOutput.save(diskPath + 'x-scrtipt-temp/' + str(input_image) + '_'  + str(thread_id) + '-8bpp.png')
  elif arg_individual_temp == False:
    cropped_imageOutput.save(diskPath + 'x-script-temp/' + 'temp' + '_'  + str(thread_id) + '-8bpp.png') 
  # close the images
  # we won't need i anymore, and output will need to be loaded again later
  i.close()
  cropped_imageOutput.close()    
    
# function for combining the outputs of different threads
def combineResults(args, thread_count, palette_data, arg_debug_level, arg_individual_temp, arg_auto_clean_temp):
  # extract arguments from the big args list
  thread_id = args[0]
  combine_input_image = args[0]
  #x_start = args[2]
  #x_end = args[3]

  # get the final output resolution based on input image
  image_for_resolution = Image.open(inputFolder + str(combine_input_image[1]) + '.png')
  # create new empty input image with indexed colour
  final_image = Image.new('L', (image_for_resolution.width, image_for_resolution.height), color = 0)
  # put palette in the final output image
  final_image.putpalette(palette_data)
  # print the height of the output
  print_lvl_3(arg_debug_level, 'img_resolution.height = ' + str(image_for_resolution.height))
  
  # args is a list of commands for the combiner
  for combine_order in args:
    # take the image we want to paste into the final output image
    if arg_individual_temp == True:
      image_to_paste = Image.open(diskPath + 'x-script-temp/' + str(combine_order[1]) + '_'  + str(combine_order[0]) + '-8bpp.png')
    elif arg_individual_temp == False:
      image_to_paste = Image.open(diskPath + 'x-script-temp/' + 'temp' + '_'  + str(combine_order[0]) + '-8bpp.png')
    # print which strip we are pasting
    print_lvl_3(arg_debug_level, 'Combine strip with x start = ' + str(combine_order[2]))
    # paste the strip into the correct position of x
    final_image.paste(image_to_paste, box = (combine_order[2], 0))

  # put the palette data in there again just to make sure (not sure which one is necessary, it works now)
  final_image.putpalette(palette_data)
  # save the final output image
  final_image.save(outputFolder + str(combine_input_image[1]) + '-8bpp.png')

  # optionally remove the temp files
  if arg_auto_clean_temp == True:
    for combine_order in args:
      if arg_individual_temp == True:
        os.remove(diskPath + 'x-script-temp/' + str(combine_order[1]) + '_'  + str(combine_order[0]) + '_8bpp.png')
      elif arg_individual_temp == False:
        os.remove(diskPath + 'x-script-temp/' + 'temp' + '_'  + str(combine_order[0]) + '-8bpp.png')

# function for easy debug of constructing the long and rather unreadable offset list
def check_list_count(arg_debug_level, list_to_check, n):
  #define some variable
  w = 0
  for stuff in list_to_check:
    # add +1 to w for every item in the list
    w += 1
  # print amount of items in the list(w), and n for easy comparison. They should be equal.
  print_lvl_5(arg_debug_level, 'Offset list item count: ' + str(w) + ' , last n is: ' + str(n))

# function to append only sub-lists instead of appending the whole list
def append_offset_list(offset_list, temp_list):
  for t in temp_list:
    offset_list.append(t)

# function to make a template for 6-index colours for index offset list
def add_6_index_list(offset_list, n):
    temp_list = [
        [   n,  n+1,  n+2],#1
        [ n+1,  n+2,  n+3],#2
        [ n+2,  n+3,  n+3],#3--
        [ n+3,  n+3,  n+2],#4--
        [ n+4,  n+3,  n+2],#5
        [ n+5,  n+4,  n+3]# 6
      ]
    append_offset_list(offset_list,temp_list)

# function to make a template for 8-index colours for index offset list
def add_8_index_list(offset_list, n):
    temp_list = [
        [   n,  n+1,  n+2],#1
        [ n+1,  n+2,  n+3],#2
        [ n+2,  n+3,  n+4],#3
        [ n+3,  n+4,  n+4],#4--
        [ n+4,  n+4,  n+3],#5--
        [ n+5,  n+4,  n+3],#6
        [ n+6,  n+5,  n+4],#7
        [ n+7,  n+6,  n+5]# 8
      ]
    append_offset_list(offset_list,temp_list)

# function to make a template for 10-index colours for index offset list
def add_10_index_list(offset_list, n):
    temp_list = [
        [   n,  n+1,  n+2],#1
        [ n+1,  n+2,  n+3],#2
        [ n+2,  n+3,  n+4],#3
        [ n+3,  n+4,  n+5],#4
        [ n+4,  n+5,  n+5],#5--
        [ n+5,  n+5,  n+4],#6--
        [ n+6,  n+5,  n+4],#7
        [ n+7,  n+6,  n+5],#8
        [ n+8,  n+7,  n+6],#9
        [ n+9,  n+8,  n+7]#10
      ]
    append_offset_list(offset_list,temp_list)
      
def run():
  # define thread count
  thread_count = options['thread_count']

  # define what should the queue for rgb2palette include
  job_list = [  
      [
      options['input_name'],        
      options['allowed_colour_types'],#allowed colour types (string list)
      options['disallowed_colour_types'],#disallowed colour types (string list)
      options['allowed_colour_indexes'],#allowed colour indexes (number list)
      options['disallowed_colour_indexes'],#disallowed colour indexes (number list)
      options['alpha_ignore'],
      options['alpha_offset_2'],
      options['alpha_offset_1'],
      options['red_weight'],#red weight (number, default = 1)
      options['green_weight'],#green weight (number, default = 1)
      options['blue_weight'],#blue weight (number, default = 1)
      options['colour_shift'],
      options['debug_level'],
      options['individual_temp'],
      options['checker_alpha'],
      options['probability_alpha'],
      options['checker_alpha_pink'],
      ]
    ]
  # job_list-related stuff to be continued later down after creating offset list...

  #--------------------------------------------------------------------------------
  #creating offset list -----------------------------------------------------------
  #--------------------------------------------------------------------------------
  offset_list = []

  #TRANSPARENCY BLUE
  n = 0
  check_list_count(options['debug_level'], offset_list, n)
  temp_list = [
    [n,n,n]
  ]
  append_offset_list(offset_list,temp_list)
  
  #GRAYSCALE
  n = 1
  check_list_count(options['debug_level'], offset_list, n)
  temp_list = [
      [   n,  n+1,  n+2],#1
      [ n+1,  n+2,  n+3],#2
      [ n+2,  n+3,  n+4],#3
      [ n+3,  n+4,  n+5],#4
      [ n+4,  n+5,  n+6],#5
      [ n+5,  n+6,  n+7],#6
      [ n+6,  n+7,  n+7],#7--
      [ n+7,  n+8,  n+8],#8--
      [ n+8,  n+8,  n+7],#9--
      [ n+9,  n+8,  n+7],#10
      [n+10,  n+9,  n+8],#11
      [n+11, n+10,  n+9],#12
      [n+12, n+11, n+10],#13
      [n+13, n+12, n+11],#14
      [n+14, n+13, n+12],#15
  ]
  append_offset_list(offset_list, temp_list)
  
  #METAL
  n = 16
  check_list_count(options['debug_level'], offset_list, n)
  add_8_index_list(offset_list, n)
  
  #LIME_GREEN
  n = 24
  check_list_count(options['debug_level'], offset_list, n)
  add_8_index_list(offset_list, n)
  
  #BEIGE
  n = 32
  check_list_count(options['debug_level'], offset_list, n)
  add_8_index_list(offset_list, n)
  
  #DARK_PINK
  n = 40
  check_list_count(options['debug_level'], offset_list, n)
  add_10_index_list(offset_list, n)
  
  #YELLOW
  n = 50
  check_list_count(options['debug_level'], offset_list, n)
  temp_list = [
    [   n,  189,  188],#1
    [ n+1,  n+0,  188],#2
    [ n+2,  n+1,  n+0]# 3
  ]
  append_offset_list(offset_list, temp_list)
  
  #DARK_BEIGE
  n = 53
  check_list_count(options['debug_level'], offset_list, n)
  temp_list = [
    [   n,  n+1,  n+2],#1
    [ n+1,  n+2,  n+3],#2
    [ n+2,  n+3,  n+3],#3--
    [ n+3,  n+3,  n+4],#4--
    [ n+4,  n+3,  n+3],#5--
    [ n+5,  n+4,  n+3],#6
    [ n+6,  n+5,  n+4]# 7
  ]
  append_offset_list(offset_list, temp_list)
  
  #YELLOW
  n = 60
  check_list_count(options['debug_level'], offset_list, n)
  add_10_index_list(offset_list, n)
  
  #BROWN_1
  n = 70
  check_list_count(options['debug_level'], offset_list, n)
  add_10_index_list(offset_list, n)
  
  #CC2,
  n = 80
  check_list_count(options['debug_level'], offset_list, n)
  add_8_index_list(offset_list, n)
  
  #DARK_GREEN
  n = 88
  check_list_count(options['debug_level'], offset_list, n)
  add_8_index_list(offset_list, n)
  
  #PALE_GREEN
  n = 96
  check_list_count(options['debug_level'], offset_list, n)
  add_8_index_list(offset_list, n)
  
  #BROWN_2
  n = 104
  check_list_count(options['debug_level'], offset_list, n)
  add_8_index_list(offset_list, n)
  
  #BROWN_3
  n = 112
  check_list_count(options['debug_level'], offset_list, n)
  add_10_index_list(offset_list, n)
  
  #BROWN_4
  n = 122
  check_list_count(options['debug_level'], offset_list, n)
  add_6_index_list(offset_list, n)
  
  #MAUVE
  n = 128
  check_list_count(options['debug_level'], offset_list, n)
  add_8_index_list(offset_list, n)
  
  #PURPLE
  n = 136
  check_list_count(options['debug_level'], offset_list, n)
  add_8_index_list(offset_list, n)
  
  #BLUE
  n = 144
  check_list_count(options['debug_level'], offset_list, n)
  add_10_index_list(offset_list, n)
  
  #LIGHT_BLUE
  n = 154
  check_list_count(options['debug_level'], offset_list, n)
  add_8_index_list(offset_list, n)
  
  #PINK
  n = 162
  check_list_count(options['debug_level'], offset_list, n)
  add_8_index_list(offset_list, n)
  
  #LIGHT_PURPLE
  n = 170
  check_list_count(options['debug_level'], offset_list, n)
  add_8_index_list(offset_list, n)
  
  #RED
  n = 178
  check_list_count(options['debug_level'], offset_list, n)
  temp_list = [
    [   n,  n+1,  n+2],#1
    [ n+1,  n+2,  n+3],#2
    [ n+2,  n+3,  n+4],#3
    [ n+3,  n+4,  n+5],#4
    [ n+4,  n+5,  n+6],#5
    [ n+5,  n+6,  n+7],#6
    [ n+6,  n+7,  n+7],#7--
    [ n+7,  n+6,  n+6],#8--
    [ n+8,  n+7,  n+6],#9
    [ n+9,  n+8,  n+7],#10
    [n+10,  n+9,  n+8],#11
    [n+11, n+10,  n+9],#12
    [n+12, n+11, n+10],#13
    [n+13, n+12, n+11]#14
  ]
  append_offset_list(offset_list, temp_list)
  
  #ORANGE
  n = 192
  check_list_count(options['debug_level'], offset_list, n)
  temp_list = [
    [  n,   64,  63],#1
    [ n+1, n+0,  64],#2
    [ n+2, n+1, n+0],#3
    [ n+3, n+2,  n+1],#4
    [ n+4, n+3, n+2],#5
    [ n+5, n+4, n+3]#6
  ]
  append_offset_list(offset_list, temp_list)
  
  #CC1
  n = 198
  check_list_count(options['debug_level'], offset_list, n)
  add_8_index_list(offset_list, n)
  
  #GREEN
  n = 206
  check_list_count(options['debug_level'], offset_list, n)
  temp_list = [
    [    n, 93,  92],#1
    [ n+1, n+0,  93],#2
    [ n+2, n+1, n+0],#3
    [ n+3, n+2, n+1]# 4
  ]
  append_offset_list(offset_list, temp_list)
  
  #CYAN
  n = 210
  check_list_count(options['debug_level'], offset_list, n)
  temp_list = [
    [  n, n+1, n+2],#1
    [n+1, n+2, n+2],#2
    [n+2, n+3, n+3],#3
    [n+3, n+2, n+2],#4
    [n+4, n+3, n+2]# 5
  ]
  append_offset_list(offset_list, temp_list)
  
  #ALPHAPINK & ACT
  n = 215
  check_list_count(options['debug_level'], offset_list, n)
  temp_list = [
    [  n+0,  n+0,  n+0],#1  - index 215
    [  n+1,  n+1,  n+1],#2  - index 216
    [  n+2,  n+2,  n+2],#3  - index 217
    [  n+3,  n+3,  n+3],#4  - index 218
    [  n+4,  n+4,  n+4],#5  - index 219
    [  n+5,  n+5,  n+5],#6  - index 220
    [  n+6,  n+6,  n+6],#7  - index 221
    [  n+7,  n+7,  n+7],#8  - index 222
    [  n+8,  n+8,  n+8],#9  - index 223
    [  n+9,  n+9,  n+9],#10 - index 224
    [ n+10, n+10, n+10],#11 - index 225
    [ n+11, n+11, n+11],#12 - index 226
    [ n+12, n+12, n+12],#13 - index 227
    [ n+13, n+13, n+13],#14 - index 228
    [ n+14, n+14, n+14],#15 - index 229
    [ n+15, n+15, n+15],#16 - index 230
    [ n+16, n+16, n+16],#17 - index 231
    [ n+17, n+17, n+17],#18 - index 232
    [ n+18, n+18, n+18],#19 - index 233
    [ n+19, n+19, n+19],#20 - index 234
    [ n+20, n+20, n+20],#21 - index 235
    [ n+21, n+21, n+21],#22 - index 236
    [ n+22, n+22, n+22],#23 - index 237
    [ n+23, n+23, n+23],#24 - index 238
    [ n+24, n+24, n+24],#25 - index 239
    [ n+25, n+25, n+25],#26 - index 240
    [ n+26, n+26, n+26],#27 - index 241
    [ n+27, n+27, n+27],#28 - index 242
    [ n+28, n+28, n+28],#29 - index 243
    [ n+29, n+29, n+29],#30 - index 244
    [ n+30, n+30, n+30],#31 - index 245
    [ n+31, n+31, n+31],#32 - index 246
    [ n+32, n+32, n+32],#33 - index 247
    [ n+33, n+33, n+33],#34 - index 248
    [ n+34, n+34, n+34],#35 - index 249
    [ n+35, n+35, n+35],#36 - index 250
    [ n+36, n+36, n+36],#37 - index 251
    [ n+37, n+37, n+37],#38 - index 252
    [ n+38, n+38, n+38],#39 - index 253
    [ n+39, n+39, n+39],#40 - index 254
    [ n+40, n+40, n+40] #41 - index 255
  ]
  append_offset_list(offset_list, temp_list)
  
  # final check
  n = 256
  check_list_count(options['debug_level'], offset_list, n)

  # continuation of job_list-related stuff from before creating offset list...
  for job in job_list:
    # defining lists just so they exist
    all_jobs = []
    job_chunks = []
    queue = []
    # variable for adding a pixel to some threads in case full image result can't be divided by thread count
    extra = 0
    # open image
    chunk_image = Image.open(inputFolder + job[0] + '.png')
    # get their average size, rounded down
    chunk_average_size = math.floor(chunk_image.width/thread_count)
    # get the remaining pixel columns after rounded down division
    chunk_modulo_size = chunk_image.width % thread_count 
    # get x-axis starts and ends of strips
    for thread in range(0, thread_count):
      start = chunk_average_size * thread
      end = (chunk_average_size * (thread+1))
      # add extra pixels in case full image width can't be divided by thread count
      start += extra
      if thread < chunk_modulo_size:   
        extra += 1
      end += extra

      # define a list to append into a big chunk of jobs for 1 task
      # (not utilized anymore but can be if parameters are overridden
      # and everything is launched from python with changing the options from here)
      job_chunk_list = [
                        thread, #0 - threadID
                        job[0], #1 - input_name
                        start,  #2 - x_start
                        end,    #3 - x_end
                        job[1], #4 - allowed_colour_types
                        job[2], #5 - disallowed_colour_types
                        job[3], #6 - allowed_colour_indexes
                        job[4], #7 - disallowed_colour_indexes
                        job[5], #8 - alpha_ignore
                        job[6], #9 - alpha_offset_1
                        job[7], #10- alpha_offset_2
                        job[8], #11- red_weight
                        job[9], #12- green_weight
                        job[10],#13- blue_weight
                        job[11],#14- colour_shift
                        job[12],#15- debug_level
                        offset_list,#16
                        options['individual_temp'],#17
                        options['checker_alpha'],#18
                        options['probability_alpha'],#19
                        options['checker_alpha_pink'],#20
                      ]
      # append the job chunk list in to job chunks
      job_chunks.append(job_chunk_list)
      # append the list of job pieces into queue
      queue.append( [thread, job[0], start, end, job[1], job[2], job[3], job[4], job[5], job[6], job[7], job[8], job[9], job[10], job[11], job[12], offset_list, options['individual_temp'], options['checker_alpha'], options['probability_alpha'], options['checker_alpha_pink'] ])
    # append the job chunks into all jobs
    all_jobs.append(job_chunks)

    # go through all jobs and print what they are about to do
    for a_job in all_jobs:
      print_lvl_5(options['debug_level'], '-'*32)
      thread_id = 0
      for b_thread in a_job:
        if thread_id == 0:
          thread_id += 1
          print_lvl_5(options['debug_level'], 'Job: ' + str(b_thread[0]))
          print_lvl_5(options['debug_level'], ' '*10 + 'Start, ' + 'End')
          print_lvl_5(options['debug_level'], 'Thread ' + str(thread_id) + ': ' + str(b_thread[1]) + ', ' + str(b_thread[2]))#
    # print the whole queue (debug level 7, this thing is LONG)
    print_lvl_7(options['debug_level'], (queue))
    

    # ----------------------------------------------------------------------------------------------------------------
    #     M U L T I T H R E A D E D       P R O C E S S     S T A R T
    # ----------------------------------------------------------------------------------------------------------------
    # pool used on rgb2palette
    pool = multiprocessing.Pool(processes = thread_count)
    pool.map(rgb2palette, queue)
    pool.close()
    pool.join()
    # ----------------------------------------------------------------------------------------------------------------
    #     M U L T I T H R E A D E D       P R O C E S S    E N D
    # ----------------------------------------------------------------------------------------------------------------
    # print arguments for debug
    combineResults_args = queue#, thread_count, palette_data, options['debug_level'], options['individual_temp'], options['auto_clean_temp']
    print_lvl_5(options['debug_level'], 'combineResults args: ' + str(combineResults_args) )
    # combine the results of the individual threads
    combineResults(queue, thread_count, palette_data, options['debug_level'], options['individual_temp'], options['auto_clean_temp'])

    # finished time for timestamp
    tx = time.time()
    # format the time. I forgot how this works but it does.
    finishedTime = datetime.datetime.fromtimestamp(tx).strftime('%H:%M:%S')
    # elapsed time for timestamp
    te = tx - tt
    # format the elapsed time. I forgot how this works but it does.
    elapsedTime = str(datetime.timedelta(seconds=int(te)))

    # print the time it took to do all this mess
    print('Started:  ' + startedTime)
    print('Finished: ' + finishedTime)
    print('-'*18)
    print('Elapsed:  ' + elapsedTime)

if __name__ == '__main__':
  # define arguments/parameters
  parser = argparse.ArgumentParser(description = 'Process some arguments.')
  parser.add_argument('-t','--thread_count',
                      help='Number of theads to run, Default: 16',
                      type = int,
                      required = False)
  parser.add_argument('-n','--input_name',
                      help='File to process. Without .png extension. File can only be RGBA (not RGB)',
                      required = True)
  parser.add_argument('-e','--allowed_colour_types',
                      help='Allowed colour types (list of strings), Default: "ALL"',
                      nargs = '+',
                      required = False)
  parser.add_argument('-f','--disallowed_colour_types',
                      help='Disallowed colour types (list of strings), Default: nothing',
                      nargs = '+',
                      required = False)
  parser.add_argument('-i','--allowed_colour_indexes',
                      help='Allowed colour indexes (list of numbers), Default: nothing',
                      nargs = '+',
                      type = int,
                      required = False)
  parser.add_argument('-y','--disallowed_colour_indexes',
                      help='Disallowed colour indexes (list of numbers), Default: nothing',
                      nargs = '+',
                      type = int,
                      required = False)
  parser.add_argument('-a','--alpha_ignore',
                      help='Threshold of ignoring transparency. Default: 128',
                      type = int,
                      required = False)
  parser.add_argument('-o','--alpha_offset_1',
                      help='Threshold of transparency to colour shift by 1 index. Default: 178',
                      type = int,
                      required = False)
  parser.add_argument('-p','--alpha_offset_2',
                      help='Threshold of transparency to colour shift by 2 indexes. Default: 230',
                      type = int,
                      required = False)
  parser.add_argument('-r','--red_weight',
                      help='Weight of red input for colour comparing. Default: 1',
                      type = float,
                      required = False)
  parser.add_argument('-g','--green_weight',
                      help='Weight of green input for colour comparing. Default: 1',
                      type = float,
                      required = False)
  parser.add_argument('-b','--blue_weight',
                      help='Weight of blue input for colour comparing. Default: 1',
                      type = float,
                      required = False)
  parser.add_argument('-c','--colour_shift',
                      help='For semi-transparent pixels, shifts index to attempt to compensate alpha. Default: True',
                      action='store_false')
  parser.add_argument('-d', '--debug_level',
                      help='Amount of info shown in console. Default: 1, Min: 1, Max: 7',
                      type = int,
                      required = False)
  parser.add_argument('-z', '--individual_temp',
                      help='Filenames in temp folder are unique for each input filename, to allow running on multiple inputs at the same time. (Temp folder can get larger)',
                      action='store_true')
  parser.add_argument('-x', '--auto_clean_temp',
                      help='Automatically remove temp files after results are combined.',
                      action='store_true')
  parser.add_argument('-j', '--checker_alpha',
                      help='Leave half of the pixels out in a checker pattern.',
                      type = int,
                      required = False)
  parser.add_argument('-l', '--checker_alpha_pink',
                      help='Left out alpha pixels are pink. Requires allowing a pink index to be filtered by -i',
                      action='store_true')
  parser.add_argument('-k', '--probability_alpha',
                      help='The more alpha in the source, the more probability those pixels stay.',
                      action='store_true')
  options = vars(parser.parse_args())
  # defaults for parameters
  default_values = [
      ('thread_count',              16),
      ('allowed_colour_types',      ['ALL']),
      ('disallowed_colour_types',   []),
      ('allowed_colour_indexes',    []),
      ('disallowed_colour_indexes', []),
      ('alpha_ignore',              128),
      ('alpha_offset_1',            178),
      ('alpha_offset_2',            230),
      ('red_weight',                1),
      ('green_weight',              1),
      ('blue_weight',               1),
      ('debug_level',               1),
      ('checker_alpha',             0),
  ]
  for name, def_value in default_values:
    if not options[name]:
      options[name] = def_value
  
  run()