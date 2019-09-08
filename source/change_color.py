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
newfileName =  IC.newfileName





def ApplyColor(fileName):
    basImage = Image.open(fileName, 'r')
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
            
            rng_Color = Rng.randrange(2)
            if rng_Color == 0:
                StarColorRGB = (255, 0, 0)
                #StarColor = "Red"
            else:
                StarColorRGB = (0, 255, 0)
                #StarColor = "Green"
            
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

    basImage.save("newColor" + fileName)
    print("newColor" + fileName)


ApplyColor(newfileName)