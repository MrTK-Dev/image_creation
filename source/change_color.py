#///////////|Color Change|///////////#

#Author: *MrTK*
#module change_color

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

Box = IC.Box
#newfileName =  IC.ExportPlacedStars()





def ApplyColor(fileName):
    basImage = Image.open("placed_stars/" + fileName, 'r')
    imageData = basImage.load()

    boxX = 0
    boxY = 0

    while boxX <= (Box.CountMaxX - 1) and boxY <= (Box.CountMaxY - 1):

        centerX = Box.width / 2 + Box.width * boxX
        centerY = Box.height / 2 + Box.height * boxY
        #print(str(centerX))

        if imageData[centerX, centerY] != (0, 0, 43):
            StarX = int(centerX - 4)
            StarY = int(centerY - 4)

            rng_ColorR = Rng.randrange(255)
            rng_ColorG = Rng.randrange(255)
            rng_ColorB = Rng.randrange(255)
            StarColorRGB = (rng_ColorR, rng_ColorG, rng_ColorB)
            
            for PixelY in range(StarY, (StarY + Box.height)):
                for PixelX in range(StarX, (StarX + Box.width)):
                    if imageData[PixelX, PixelY] != (0, 0, 43):

                        imageData[PixelX, PixelY] = StarColorRGB
                        #debug Print
                        #print("X:" + str(PixelX) + " Y:" + str(PixelY) + " Color:" + StarColor)

        boxX = boxX + 1

        if boxX > (Box.CountMaxX - 1):
            boxX = 0
            boxY = boxY + 1        

    basImage.save('appliedColor_stars/' + "newColor" + fileName)
    print("newColor" + fileName)

def ExportPlacedStars():
    for counter in range(10):
        print(str(counter))
        newfileName = "editedPic" + str(counter) + ".png"
        ApplyColor(newfileName)

ExportPlacedStars()