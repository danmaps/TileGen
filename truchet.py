import random
import svgwrite
import math

n = random.randint(1, 5) # Generate a random integer between 1 and 10
power_of_2 = int(math.pow(2, n)) # Calculate 2^n

# Set the size of the canvas and the number of tiles in each dimension
canvas_size = 500
num_tiles = power_of_2

print(num_tiles)

tile_size = canvas_size // num_tiles

# Initialize a new SVG drawing
dwg = svgwrite.Drawing(filename="truchet_tiles_bw.svg", size=(canvas_size, canvas_size))

# Draw the tiles
for i in range(num_tiles):
    for j in range(num_tiles):
        orientation = random.randint(0, 3)
        if orientation == 0:
            path_data = f"M {i*tile_size},{j*tile_size} L {(i+1)*tile_size},{j*tile_size} L {i*tile_size},{(j+1)*tile_size} Z"
        elif orientation == 1:
            path_data = f"M {(i+1)*tile_size},{j*tile_size} L {(i+1)*tile_size},{(j+1)*tile_size} L {i*tile_size},{(j+1)*tile_size} Z"
        elif orientation == 2:
            path_data = f"M {i*tile_size},{j*tile_size} L {(i+1)*tile_size},{j*tile_size} L {i*tile_size},{(j+1)*tile_size} Z"
            if random.random() > 0.5:
                path_data = f"M {(i+1)*tile_size},{j*tile_size} L {i*tile_size},{j*tile_size} L {(i+1)*tile_size},{(j+1)*tile_size} Z"
        else:
            path_data = f"M {(i+1)*tile_size},{j*tile_size} L {(i+1)*tile_size},{(j+1)*tile_size} L {i*tile_size},{(j+1)*tile_size} Z"
            if random.random() > 0.5:
                path_data = f"M {(i+1)*tile_size},{j*tile_size} L {(i+1)*tile_size},{(j+1)*tile_size} L {i*tile_size},{j*tile_size} Z"
        dwg.add(dwg.path(d=path_data, fill="black"))

# Save the SVG drawing
dwg.save()
