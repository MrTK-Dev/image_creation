#///////////|Shooting Star|///////////#

#Author: *MrTK*
#module shooting_star

#|Imports|#

import os

#|Workspace|#

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#import PIL

from PIL import Image
import random as Rng







'''
x = 0
RangeX = 0
while x <= 10:
    StarColorRGB = (255, 255, 255)
    for PixelX in range((RangeX - x), (RangeX + 2)):
        imageData[PixelX, PixelX] = StarColorRGB

    fileName = 'shootingStar' + str(x) + '.png'
    BackgroundImage.save('shootingS/' + fileName)
    print('Created: ' + fileName)
    x = x + 1
    RangeX = x * 100
'''
#range x=[960]
#range y=[0 - 1079]
#100y per frame

PositionX = 150
StarColorRGB = (255, 255, 255)
frames = 10

class ShootingStar1:
    StartPositionX = 500
    StartPositionY = 0
    #in Pixel
    LengthSS = 100 * int(10 / frames)


def PlaceShootingStars():
    for y in range(1, (frames + 1)):
        #BackgroundImage = Image.open("background/SSbackground.png", 'r').convert('RGB')

        BackgroundImage = Image.new('RGBA', (300, 500), (255, 0, 0 ,0))
        imageData = BackgroundImage.load()

        LengthY = ShootingStar1.LengthSS * y
        print(str(LengthY))

        rangeY_start = int((LengthY - 1000 / frames) / 2)
        for PixelY in range(rangeY_start, int(LengthY / 2)):
            imageData[PositionX, PixelY] = StarColorRGB

        fileName = 'shootingStar' + str(y - 1) + '.png'
        BackgroundImage.save('shootingS/' + fileName)
        print('Created: ' + fileName)


#PlaceShootingStars()

def PasteShootingStars(fileName, counter):
    basImage = Image.open("appliedColor_stars/" + fileName, 'r')
    imageData = basImage.load()

    y = counter + 1
    print(str(y))
    #LengthY = int(1000 / frames) * y
    LengthY = ShootingStar1.LengthSS * y
    print(str(LengthY))

    rangeY_start = int((LengthY - 1000 / frames) / 2)
    for PixelY in range(rangeY_start, int(LengthY / 2)):
        imageData[ShootingStar1.StartPositionX, PixelY] = StarColorRGB

    fileName = 'shootingStar' + str(y - 1) + '.png'
    basImage.save('shootingS/' + fileName)
    print('Created: ' + fileName)



def ExportPlacedShootingStars():
    for counter in range(10):
        #print(str(counter))
        newfileName = "newColoreditedPic" + str(counter) + ".png"
        PasteShootingStars(newfileName, counter)

ExportPlacedShootingStars()


#TODO
#Cast Light to environment
#Bubble System
#make Pixels lighter