#///////////|GIF Creation|///////////#

#Author: *MrTK*
#module create_gif

#|Imports|#

import os

#|Workspace|#

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#import PIL

from PIL import Image
import random as Rng
import image_creation as IC

def CreateGIF():
    names = ["bild0", "bild1", "bild2", "bild3", "bild4", "bild3", "bild2", "bild1"]
    images = []
    for n in names:
        frame = Image.open("gif_test/" + n + ".png")
        images.append(frame)
    
    images[0].save('test_2.gif',
                    save_all=True,
                    append_images=images[1:],
                    duration=300,
                    loop=100)









CreateGIF()