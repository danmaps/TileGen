import random
import svgwrite

# define the size of the grid and the size of the tiles
grid_size = 10
tile_size = 50

# define color options
color_options = ['black', 'red', 'blue', 'green', 'orange']

stroke=random.choice(color_options)
if stroke == 'black':
    fill = 'white'
else:
    fill=random.choice(['black','white'])

def create_labyrinth(grid_size=grid_size,tile_size=tile_size,stroke=stroke,fill=fill):
    print(stroke,fill)

    # create a new SVG drawing
    dwg = svgwrite.Drawing(filename='labyrinth_in_color.svg', size=(grid_size*tile_size, grid_size*tile_size))

    # loop through each tile in the grid
    for i in range(grid_size):
        for j in range(grid_size):
            # generate a random number to determine the orientation of the tile
            rand_num = random.random()
            if rand_num < 0.5:
                # draw a white square with a diagonal line in the top-left to bottom-right direction
                dwg.add(dwg.rect((i*tile_size, j*tile_size), (tile_size, tile_size), fill=fill))
                dwg.add(dwg.line((i*tile_size, j*tile_size), ((i+1)*tile_size, (j+1)*tile_size), stroke=stroke))
            else:
                # draw a white square with a diagonal line in the top-right to bottom-left direction
                dwg.add(dwg.rect((i*tile_size, j*tile_size), (tile_size, tile_size), fill=fill))
                dwg.add(dwg.line(((i+1)*tile_size, j*tile_size), (i*tile_size, (j+1)*tile_size), stroke=stroke))

    # save the drawing
    dwg.save()

# create_labyrinth(stroke='green',fill='black')
create_labyrinth()