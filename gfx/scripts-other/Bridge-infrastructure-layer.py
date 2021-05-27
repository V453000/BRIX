import os
from PIL import Image

def load_sequence(positions, frame_size, shift, input_image):
    sequence = []
    with Image.open(input_image) as img:
        for pos in positions:
            rectangle = (
                pos[0] * frame_size[0] + shift[0],
                pos[1] * frame_size[1] + shift[1],
                pos[0] * frame_size[0] + frame_size[0] + shift[0],
                pos[1] * frame_size[1] + frame_size[1] + shift[1]
            )
            print(frame_size, rectangle)
            sequence.append( img.crop( rectangle ) )
    return sequence

def put_pieces(instructions, sequence, target_image, frame_size, shift):
    for instruction in instructions:
        frame = instruction[1]
        extra_y = int(64 / 256 * frame_size[0])
        if frame > 1:
            extra_y = int(96 / 256 * frame_size[0])
        rectangle = (
            int( instruction[0][0] * frame_size[0] + shift[0]),
            int( instruction[0][1] * frame_size[1] + extra_y + shift[1]),
            int( instruction[0][0] * frame_size[0] + frame_size[0] + shift[0]),
            int( instruction[0][1] * frame_size[1] + frame_size[1] + extra_y + shift[1])
        )
        # print(frame, rectangle)
        target_image.paste( sequence[frame], box = rectangle )
    #return output_image

def debug_image_print(image_list):
    id = 0
    folder = 'debug'
    os.makedirs(folder, exist_ok = True)
    for img in image_list:
        full_path = os.path.join(folder, 'debug_image_' + str(id).zfill(2) + '.png')
        print(full_path)
        img.save(full_path)
        id += 1


road_sequence_positions = [
    ( 0, 0),
    ( 1, 0),
    (11, 0),
    (12, 0),
    (13, 0),
    (14, 0)
]
rail_sequence_positions = [
    ( 6, 0),
    ( 7, 0),
    (26, 0),
    (27, 0),
    (28, 0),
    (29, 0)
]
mono_sequence_positions = [
    ( 6, 3),
    ( 7, 3),
    (26, 3),
    (27, 3),
    (28, 3),
    (29, 3)
]
mglv_sequence_positions = [
    ( 6, 6),
    ( 7, 6),
    (26, 6),
    (27, 6),
    (28, 6),
    (29, 6)
]

road_bridge_instructions = [
    ((0,0), 1 ),# ramps
    ((1,0), 1 ),
    ((2,0), 0 ),
    ((3,0), 0 ),
    ((4,0), 2 ),
    ((5,0), 4 ),
    ((6,0), 5 ),
    ((7,0), 3 ),
    
    (( 8,0), 1 ),# wooden ramps
    (( 9,0), 1 ),
    ((10,0), 0 ),
    ((11,0), 0 ),
    ((12,0), 2 ),
    ((13,0), 4 ),
    ((14,0), 5 ),
    ((15,0), 3 ),
    
    (( 0,1), 0 ),# suspended bridge
    (( 1,1), 0 ),
    (( 2,1), 1 ),
    (( 3,1), 1 ),
    ((20,1), 0 ),
    ((21,1), 0 ),
    ((22,1), 1 ),
    ((23,1), 1 ),
    ((40,1), 0 ),
    ((41,1), 1 ),

    ((0,2), 1),# concrete bridge
    ((1,2), 0),

    ((0,3), 1),# arc bridge
    ((1,3), 0),
    
    (( 0,4), 1),# cantliever bridge
    (( 1,4), 1),
    (( 2,4), 1),
    (( 3,4), 0),
    (( 4,4), 0),
    (( 5,4), 0),

    ((0,5), 0),# wooden bridge
    ((1,5), 1),

    ((0,6), 1),# steel bridge
    ((1,6), 0),

    (( 0,7), 1),# tubular bridge
    (( 1,7), 1),
    (( 2,7), 1),
    (( 3,7), 0),
    (( 4,7), 0),
    (( 5,7), 0),
]
rail_bridge_instructions = [
    ((16,0), 1 ),# ramps
    ((17,0), 1 ),
    ((18,0), 0 ),
    ((19,0), 0 ),
    ((20,0), 2 ),
    ((21,0), 4 ),
    ((22,0), 5 ),
    ((23,0), 3 ),
    
    ((24,0), 1 ),# wooden ramps
    ((25,0), 1 ),
    ((26,0), 0 ),
    ((27,0), 0 ),
    ((28,0), 2 ),
    ((29,0), 4 ),
    ((30,0), 5 ),
    ((31,0), 3 ),
    
    (( 4,1), 0 ),# suspended bridge
    (( 5,1), 0 ),
    (( 6,1), 1 ),
    (( 7,1), 1 ),
    ((24,1), 0 ),
    ((25,1), 0 ),
    ((26,1), 1 ),
    ((27,1), 1 ),
    ((42,1), 0 ),
    ((43,1), 1 ),

    ((2,2), 1),# concrete bridge
    ((3,2), 0),

    ((2,3), 1),# arc bridge
    ((3,3), 0),
    
    (( 6,4), 1),# cantliever bridge
    (( 7,4), 1),
    (( 8,4), 1),
    (( 9,4), 0),
    ((10,4), 0),
    ((11,4), 0),

    ((2,5), 0),# wooden bridge
    ((3,5), 1),

    ((2,6), 1),# steel bridge
    ((3,6), 0),

    (( 6,7), 1),# tubular bridge
    (( 7,7), 1),
    (( 8,7), 1),
    (( 9,7), 0),
    ((10,7), 0),
    ((11,7), 0),
]
monorail_bridge_instructions = [
    ((32,0), 1 ),# ramps
    ((33,0), 1 ),
    ((34,0), 0 ),
    ((35,0), 0 ),
    ((36,0), 2 ),
    ((37,0), 4 ),
    ((38,0), 5 ),
    ((39,0), 3 ),
    
    ((40,0), 1 ),# wooden ramps
    ((41,0), 1 ),
    ((42,0), 0 ),
    ((43,0), 0 ),
    ((44,0), 2 ),
    ((45,0), 4 ),
    ((46,0), 5 ),
    ((47,0), 3 ),
    
    (( 8,1), 0 ),# suspended bridge
    (( 9,1), 0 ),
    ((10,1), 1 ),
    ((11,1), 1 ),
    ((28,1), 0 ),
    ((29,1), 0 ),
    ((30,1), 1 ),
    ((31,1), 1 ),
    ((44,1), 0 ),
    ((45,1), 1 ),

    ((4,2), 1),# concrete bridge
    ((5,2), 0),

    ((4,3), 1),# arc bridge
    ((5,3), 0),
    
    ((12,4), 1),# cantliever bridge
    ((13,4), 1),
    ((14,4), 1),
    ((15,4), 0),
    ((16,4), 0),
    ((17,4), 0),

    ((4,5), 0),# wooden bridge
    ((5,5), 1),

    ((4,6), 1),# steel bridge
    ((5,6), 0),

    ((12,7), 1),# tubular bridge
    ((13,7), 1),
    ((14,7), 1),
    ((15,7), 0),
    ((16,7), 0),
    ((17,7), 0),
]
maglev_bridge_instructions = [
    ((48,0), 1 ),# ramps
    ((49,0), 1 ),
    ((50,0), 0 ),
    ((51,0), 0 ),
    ((52,0), 2 ),
    ((53,0), 4 ),
    ((54,0), 5 ),
    ((55,0), 3 ),
    
    ((56,0), 1 ),# wooden ramps
    ((57,0), 1 ),
    ((58,0), 0 ),
    ((59,0), 0 ),
    ((60,0), 2 ),
    ((61,0), 4 ),
    ((62,0), 5 ),
    ((63,0), 3 ),
    
    ((12,1), 0 ),# suspended bridge
    ((13,1), 0 ),
    ((14,1), 1 ),
    ((15,1), 1 ),
    ((32,1), 0 ),
    ((33,1), 0 ),
    ((34,1), 1 ),
    ((35,1), 1 ),
    ((46,1), 0 ),
    ((47,1), 1 ),

    ((6,2), 1),# concrete bridge
    ((7,2), 0),

    ((6,3), 1),# arc bridge
    ((7,3), 0),
    
    ((18,4), 1),# cantliever bridge
    ((19,4), 1),
    ((20,4), 1),
    ((21,4), 0),
    ((22,4), 0),
    ((23,4), 0),

    ((6,5), 0),# wooden bridge
    ((7,5), 1),

    ((6,6), 1),# steel bridge
    ((7,6), 0),

    ((18,7), 1),# tubular bridge
    ((19,7), 1),
    ((20,7), 1),
    ((21,7), 0),
    ((22,7), 0),
    ((23,7), 0),
]

frame_size = (256, 320)
roads_x4     = load_sequence( road_sequence_positions, frame_size, (0,0), 'inputs/roads-masked_0000.png'  )
rails_x4     = load_sequence( rail_sequence_positions, frame_size, (0,0), 'inputs/tracks-masked_0000.png' )
monorail_x4  = load_sequence( mono_sequence_positions, frame_size, (0,0), 'inputs/tracks-masked_0000.png' )
maglev_x4    = load_sequence( mglv_sequence_positions, frame_size, (0,0), 'inputs/tracks-masked_0000.png' )

frame_size_x1 = (64, 80)
roads_x1     = load_sequence( road_sequence_positions, frame_size_x1, (12800,0), 'inputs/roads-masked_0000.png'  )
rails_x1     = load_sequence( rail_sequence_positions, frame_size_x1, (12800,0), 'inputs/tracks-masked_0000.png' )
monorail_x1  = load_sequence( mono_sequence_positions, frame_size_x1, (12800,0), 'inputs/tracks-masked_0000.png' )
maglev_x1    = load_sequence( mglv_sequence_positions, frame_size_x1, (12800,0), 'inputs/tracks-masked_0000.png' )

#debug_image_print(roads_x1)

bridge_output = Image.new('RGBA', (16384, 3200), color = (0,0,0,0) )

put_pieces(road_bridge_instructions,     roads_x4,     bridge_output, frame_size, (0,0) )
put_pieces(rail_bridge_instructions,     rails_x4,     bridge_output, frame_size, (0,0) )
put_pieces(monorail_bridge_instructions, monorail_x4,  bridge_output, frame_size, (0,0) )
put_pieces(maglev_bridge_instructions,   maglev_x4,    bridge_output, frame_size, (0,0) )

put_pieces(road_bridge_instructions,     roads_x1,     bridge_output, frame_size_x1, (0,2560) )
put_pieces(rail_bridge_instructions,     rails_x1,     bridge_output, frame_size_x1, (0,2560) )
put_pieces(monorail_bridge_instructions, monorail_x1,  bridge_output, frame_size_x1, (0,2560) )
put_pieces(maglev_bridge_instructions,   maglev_x1,    bridge_output, frame_size_x1, (0,2560) )

bridge_output.save('outputs/bridge-infrastructure.png')
bridge_output.close()