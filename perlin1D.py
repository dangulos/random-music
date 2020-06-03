import noise
import numpy as np
import random as rand
import matplotlib.pyplot as plt
from PIL import Image

size = 1024
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

base = rand.randint(0,1)

world = np.zeros(size)
for i in range(size):
    world[i] = noise.pnoise1(i/scale, 
                            octaves=octaves, 
                            persistence=persistence, 
                            lacunarity=lacunarity, 
                            repeat=1024, 
                            base=base)
    world[i] = (world[i]+0.5) * 255
        
plt.plot(range(size), world)
plt.show()