import noise
import numpy as np
import random as rand
import matplotlib.pyplot as plt
from PIL import Image

shape = (1024,1024)
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

base = rand.randint(0,1)

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=base)
        world[i][j] = (world[i][j]+0.5) * 255
        
Image.fromarray(world).show()