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
import shooting_star as SS

choice = "casual"

if choice == "casual":
    pathName = "ShootingS/"
    image_name = "shootingStar"
    frames = 10
    gifName = 'ColorAnimation'
    durationTime = 300
else:
    pathName = "shootingS/"
    image_name = "shootingStar"
    frames = 25
    gifName = 'ShootingStar'
    durationTime = 1

def CreateGIF(listName):
    imageNames = listName
    images = []
    for n in imageNames:
        frame = Image.open(pathName + n + ".png")
        images.append(frame)
    
    images[0].save(gifName + '.gif',
                    save_all=True,
                    append_images=images[1:],
                    duration=durationTime,
                    #transparency=0,
                    loop=10)


def ExportGIF():
    listName = []
    for counter in range(frames):
        print(str(counter))
        newfileName = image_name + str(counter)
        listName.append(newfileName)
        #print(newfileName)
    print(listName)
    CreateGIF(listName)

ExportGIF()