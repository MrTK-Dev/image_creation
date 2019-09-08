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


#Globals
fileName = "background.png"
fileName_Star = "testStar.png"
jsonFileName = "booleanMap.json"

StarImage = Image.open("stars/" + "star8x8" + '.png', 'r')
StarImage_2 = Image.open("stars/" + "star8x8_2" + '.png', 'r')
BackgroundImage = Image.open("background/" + fileName, 'r')

StarList = [StarImage, StarImage_2]

#Data Base
data = {}

class RandomCalculated():
    rngRange = 200000
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

def PlaceStarsOnBackground():

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

            #adds a "star" variable
            #makes a new string for data save
            if boolPainted == True:
                #add amount of starList
                rng_Star = Rng.randrange(2)
                StarKind = rng_Star
                boolPainted_StarKind = "t - " + str(StarKind) 
            else:
                boolPainted_StarKind = "f"

            #Data Declaration
            data[boxName] = []
            data[boxName].append({
                #'bool': boolPainted
                'code': boolPainted_StarKind
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
                codePainted = entry['code']
                boolPainted = codePainted.startswith("t")

                #Other Boxes
                if boxY != 0:
                    boxName_Up = str(boxX) + '.0 - ' + str(boxY - 1) + '.0'
                    for entry_Up in data[boxName_Up]:
                        code_Up = entry_Up['code']
                        boolPainted_Up = code_Up.startswith("t")

                else:
                    boolPainted_Up = False

                if boxY != (Box.CountMaxY - 1):
                    boxName_Down = str(boxX) + '.0 - ' + str(boxY + 1) + '.0'
                    for entry_Down in data[boxName_Down]:
                        code_Down = entry_Down['code']
                        boolPainted_Down = code_Down.startswith("t")
                else:
                    boolPainted_Down = False

                if boolPainted == True and boolPainted_Up == False and boolPainted_Down == False:
                    boolPainted = codePainted
                else:
                    boolPainted = "f"

                data[boxName] = []
                data[boxName].append({
                    'code': boolPainted
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
                codePainted = entry['code']
                boolPainted = codePainted.startswith("t")

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
                                codePaintedBubble = entry['code']
                                boolPaintedBubble = codePaintedBubble.startswith("t")

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

                #add Random Image [Star]



                if boolPaintedBubble == True:
                    boolPaintedBubble = codePainted
                else:
                    boolPaintedBubble = "f"

                data[boxName] = []
                data[boxName].append({
                    'code': boolPaintedBubble
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


    CheckX()
    CheckY()
    CheckBubble()
    
    

def PasteImage(newfileName):
    boxX = 0
    boxY = 0
    boxName = str(boxX) + '.0 - ' + str(boxY) + '.0'

    while boxX <= (Box.CountMaxX - 1) and boxY <= (Box.CountMaxY - 1):

        for entry in data[boxName]:
            codePainted = entry['code']
            boolPainted = codePainted.startswith("t")

            if boolPainted == True:

                boxCoordinateXY = boxName.split(" - ")
                boxCoordinateX = float(boxCoordinateXY[0])
                boxCoordinateY = float(boxCoordinateXY[1])

                offset_x = int(boxCoordinateX * Box.width)
                offset_y = int(boxCoordinateY * Box.height)
                offset = (offset_x, offset_y)

                codePainted2 = codePainted.split(" - ")
                StarKindnum = int(codePainted2[1])
                BackgroundImage.paste(StarList[StarKindnum], offset)
        
        boxX = boxX + 1

        if boxX > (Box.CountMaxX - 1):
            boxX = 0
            boxY = boxY + 1        

        boxName = str(boxX) + '.0 - ' + str(boxY) + '.0'

    BackgroundImage.save('placed_stars/' + newfileName)
    print("CheckBubbleCreated: " + "RandomCalculated" + newfileName)


def ExportPlacedStars():
    PlaceStarsOnBackground()
    for counter in range(10):
        print(str(counter))
        newfileName = "editedPic" + str(counter) + ".png"
        PasteImage(newfileName)

ExportPlacedStars()