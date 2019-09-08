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
import change_color as CC

def CreateGIF(listName):
    imageNames = listName
    images = []
    for n in imageNames:
        frame = Image.open("appliedColor_stars/" + n + ".png")
        images.append(frame)
    
    images[0].save('ColorAnimation.gif',
                    save_all=True,
                    append_images=images[1:],
                    duration=300,
                    loop=100)






def ExportGIF():
    listName = []
    for counter in range(10):
        print(str(counter))
        newfileName = "newColoreditedPic" + str(counter)
        listName.append(newfileName)
        print(newfileName)
    print(listName)
    CreateGIF(listName)

ExportGIF()
