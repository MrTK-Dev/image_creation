#///////////|Image Creation|///////////#

#Author: *MrTK*
#module image_creation

#|Imports|#

import os

#|Workspace|#

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#import PIL

from PIL import Image
import random as Rng
import json

fileName = "test.png"
fileName_Star = "testStar.png"
newfileName = "editedPic.png"

jsonFileName = "booleanMap.json"

StarImage = Image.open("stars/" + "star8x8.png", 'r')
StarImage_2 = Image.open("stars/" + "star8x8.png", 'r')
#print(str(StarImage.size))
BackgroundImage = Image.open("background/" + fileName, 'r')

class RandomCalculated():
    rngRange = 20000
    rngMininum = 1150
    StarBubble = 3

class Box():
    width, height = StarImage.size
    bq_width, bq_height = BackgroundImage.size
    MaxX = bq_width - width
    MaxY = bq_height - height
    CountMaxX = int(MaxX / width)
    CountMaxY = int(MaxY / height)

class Bubble():
    area = 5

#def PlaceStarsOnBackground():
#Data Base
data = {}


def CheckX():
    offset_x = 0
    offset_y = 0
    boolPainted = False

    while offset_x <= Box.MaxX and offset_y <= Box.MaxY:

        #Random Generator
        randomNumber = Rng.randrange(RandomCalculated.rngRange)
        rngMultiplierY = offset_y

        boxCoordinateX = offset_x / Box.width
        boxCoordinateY = offset_y / Box.height
        boxName = str(boxCoordinateX) + ' - ' + str(boxCoordinateY)

        #randomly generates Stars without any Conditions
        if (randomNumber + rngMultiplierY) <= RandomCalculated.rngMininum and boolPainted == False:
            boolPainted = True
        else:
            boolPainted = False

        #Data Declaration
        data[boxName] = []
        data[boxName].append({
            'x': boxCoordinateX,
            'y': boxCoordinateY,
            'bool': boolPainted
        })

        #switches to offset_y if offset_x is done
        offset_x = offset_x + Box.width
        if offset_x > Box.MaxX:
            offset_y = offset_y + Box.height
            offset_x = 0
    
    #Json
    filePathNameWExt = 'data/' + jsonFileName
    print(filePathNameWExt)
    with open(filePathNameWExt, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, ensure_ascii=False, indent=4)
    
    print("Created " + "CheckX" + jsonFileName)


def CheckY():
    boxX = 0
    boxY = 0
    boxName = str(boxX) + '.0 - ' + str(boxY) + '.0'
    while boxX <= (Box.CountMaxX - 1) and boxY <= (Box.CountMaxY - 1):

        for entry in data[boxName]:
            boxCoordinateX = entry['x']
            boxCoordinateY = entry['y']
            boolPainted = entry['bool']

            #Other Boxes
            if boxY != 0:
                boxName_Up = str(boxX) + '.0 - ' + str(boxY - 1) + '.0'
                for entry_Up in data[boxName_Up]:
                    boolPainted_Up = entry_Up['bool']
            else:
                boolPainted_Up = False

            if boxY != (Box.CountMaxY - 1):
                boxName_Down = str(boxX) + '.0 - ' + str(boxY + 1) + '.0'
                for entry_Down in data[boxName_Down]:
                    boolPainted_Down = entry_Down['bool']
            else:
                boolPainted_Down = False

            if boolPainted == True and boolPainted_Up == False and boolPainted_Down == False:
                boolPainted = True
            else:
                boolPainted = False
            
            data[boxName] = []
            data[boxName].append({
                'x': boxCoordinateX,
                'y': boxCoordinateY,
                'bool': boolPainted
            })
        
        boxX = boxX + 1

        if boxX > (Box.CountMaxX - 1):
            boxX = 0
            boxY = boxY + 1        

        boxName = str(boxX) + '.0 - ' + str(boxY) + '.0'

    #Json
    filePathNameWExt = 'data/' + jsonFileName
    print(filePathNameWExt)
    with open(filePathNameWExt, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, ensure_ascii=False, indent=4)
    
    print("Created " + "CheckY" + jsonFileName)


def CheckBubble():
    boxX = 0
    boxY = 0
    boxName = str(boxX) + '.0 - ' + str(boxY) + '.0'

    while boxX <= (Box.CountMaxX - 1) and boxY <= (Box.CountMaxY - 1):

        for entry in data[boxName]:
            boxCoordinateX = entry['x']
            boxCoordinateY = entry['y']
            boolPainted = entry['bool']

            #scannt nur Boxen, die aktiv sind #saveRAM
            if boolPainted == True:
                #Other Boxes
                # schaut nach, ob die Strecke nach oben und unten bzw. rechts und links kleiner als die Bubble-Maße sind
                # Werte werden daraufhin angepasst, um unbekannte Boxen zu vermeiden           
                #check X
                BubbleX = Bubble.area
                if boxX <= (Bubble.area - 1):    
                    BubbleX = boxX
                elif boxX >= (Box.CountMaxX - Bubble.area):
                    BubbleX = Box.CountMaxX - boxX
                
                #check Y
                BubbleY = Bubble.area
                if boxY <= (Bubble.area - 1):
                    BubbleY = boxY
                elif boxY >= (Box.CountMaxY - Bubble.area):
                    BubbleY = Box.CountMaxY - boxY

                #data from Boxes
                #-5
                #-4
                #-3
                #-2
                #-1
                #-5 -4 -3 -2 -1 boxX|boxY 1 2 3 4 5
                #1
                #2
                #3
                #4
                #5

                rangeX = range((boxX - BubbleX), (boxX + BubbleX))
                rangeY = range((boxY - BubbleY), (boxY + BubbleY))
                countStars = 0

                #Count Stars [Trues]
                #geht vom minimalen y zum maximalen y
                #fült währenddessen die x-Reihe auf
                for countCoordinateY in rangeY:
                    for countCoordinateX in rangeX:

                        boxNameBubble = str(countCoordinateX) + '.0 - ' + str(countCoordinateY) + '.0'

                        for entry in data[boxNameBubble]:
                            boolPaintedBubble = entry['bool']

                        if boolPaintedBubble == True:
                            countStars = countStars + 1

                #Kondition mit der Anzahl der Sterne in der zu prüfenden Bubble
                if countStars >= RandomCalculated.StarBubble:
                    #debug Print
                    #print("X:" + str(boxX) + " Y: " + str(boxX) + " Stars: " + str(countStars))
                    boolPaintedBubble = False
                else:
                    boolPaintedBubble = True
            else:
                boolPaintedBubble = False


            data[boxName] = []
            data[boxName].append({
                'x': boxCoordinateX,
                'y': boxCoordinateY,
                'bool': boolPaintedBubble
            })

        boxX = boxX + 1

        if boxX > (Box.CountMaxX - 1):
            boxX = 0
            boxY = boxY + 1        

        boxName = str(boxX) + '.0 - ' + str(boxY) + '.0'

        #Json
    filePathNameWExt = 'data/' + jsonFileName
    print(filePathNameWExt)
    with open(filePathNameWExt, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, ensure_ascii=False, indent=4)
    
    print("Created " + "CheckBubble" + jsonFileName)



def PasteImage():
    boxX = 0
    boxY = 0
    boxName = str(boxX) + '.0 - ' + str(boxY) + '.0'

    while boxX <= (Box.CountMaxX - 1) and boxY <= (Box.CountMaxY - 1):

        for entry in data[boxName]:
            boxCoordinateX = entry['x']
            boxCoordinateY = entry['y']
            boolPainted = entry['bool']

            offset_x = int(boxCoordinateX * Box.width)
            offset_y = int(boxCoordinateY * Box.height)
            offset = (offset_x, offset_y)

            if boolPainted == True:
                rng_Star = Rng.randrange(2)
                if rng_Star == 0:
                    BackgroundImage.paste(StarImage, offset)
                else:
                    BackgroundImage.paste(StarImage_2, offset)
        
        boxX = boxX + 1

        if boxX > (Box.CountMaxX - 1):
            boxX = 0
            boxY = boxY + 1        

        boxName = str(boxX) + '.0 - ' + str(boxY) + '.0'

    BackgroundImage.save(newfileName)
    print("CheckBubbleCreated: " + "RandomCalculated" + newfileName)


#def ExportPlacedStars():


CheckX()
CheckY()
CheckBubble()
PasteImage()