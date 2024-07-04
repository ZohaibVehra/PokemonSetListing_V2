
from os import path, listdir
import pyautogui
import pyperclip
import webbrowser
import time
from useful import *

def eBayStuff(quantLink, picPath, setName, exactPicsDir):
    #take the last 4 characters off of the picPath var
    pricePath = picPath[:-4] + 'prices.txt'
    pricesDic = prices(pricePath)
    listingName, images = getLists(quantLink, picPath)
    startEbayListing()
    setName = cleanedName(setName)
    editMainPage(setName)
    vars(listingName, images, exactPicsDir)
    quantDic = setQuantity(quantLink)
    setPrices(pricesDic, listingName, quantDic)

def getLists(quantLink, picPath):

    with open(quantLink, 'r') as file:
        quantList = file.readlines()
    
    
    quantList = [x.strip() for x in quantList]
    quantList = list(filter(None, quantList))

    for i in range(len(quantList)):
        while quantList[i][-1].isdigit():
            quantList[i] = quantList[i][:-1]

    quantList = [x.strip() for x in quantList]

    file_names = []
    for file in listdir(picPath):
        if path.isfile(path.join(picPath, file)):
            file_names.append(file)

    return quantList, file_names



def startEbayListing():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

    # Open the constructed URL in Chrome
    webbrowser.get('chrome').open('https://www.ebay.ca/lstng?mode=SellSimilarItem&itemId=395275879098&sr=wn')
    time.sleep(10)

    #reset zoom in case
    zoomInF()
    zoomOutF()

def editMainPage(setName):
    moveClick(1239, 399)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')

    Title = pyperclip.paste()

    Title = Title.replace('---', setName)
    Title = Title + ' Cards'
    
    if len(Title) > 80:
        Title = Title.replace(' Cards', '')

    if len(Title) > 80:
        Title = Title.replace('Holos/Reverse Holo - Choose Your Own', 'Choose your own Cards')

    pyperclip.copy(Title)
    pyautogui.hotkey('ctrl', 'v')

    moveClick(1309, 1202)
    pyperclip.copy(setName)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1)

    #description editing
    pyautogui.scroll(-1900)
    pyautogui.move(0, 50)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    desc = pyperclip.paste()
    desc = desc.replace('***', setName)
    pyperclip.copy(desc)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    #edit vars time
    moveClick(870 , 658)
    time.sleep(10)

def cleanedName(setName):
    setName = setName.replace('_', ' ')
    words = setName.split(' ')
    print(words)

    for i in range(len(words)):
        if words[i].isalpha():
            words[i] = words[i].capitalize()

    setName = ' '.join(words)

    return setName

def prices(pricePath):
    #open the file and read the lines into a list and strip the new line chars at the end
    with open(pricePath, 'r') as file:
        prices = file.readlines()
    
    prices = [x.strip() for x in prices]

    pricesTracker = {}
    i = 0
    while i < (len(prices)):
        if len(prices[i].split(' ')) == 1:
            if prices[i] == '1.25' or prices[i] == '1.5' or prices[i] == '1.75' or prices[i] == '2' or prices[i] == '2.5' or prices[i] == '3':
                cards = prices[i+1].split(' ')
                pricesTracker[prices[i]] = cards   
                cards = []
                i = i+1
        i = i+1
    return pricesTracker

def setPrices(pricesDic, listingName, quantDic):
    #through price dictionary were going to find the listing names and replace with those in a new dictionary to be able to search
    newPricesDic = {}
    listingNameNums = [x[:3] for x in listingName]
    for price in pricesDic:  
        newNames = []
        for cardNum in pricesDic[price]:
            isHolo = False
            if 'h' in cardNum:
                isHolo = True
            cardNum = cardNum.replace('h', '')
            if len(cardNum) < 3:
                cardNum = '0' + cardNum
            if len(cardNum) < 3:
                cardNum = '0' + cardNum
            
            if cardNum in listingNameNums:
                index = listingNameNums.index(cardNum)
                cardFullName = listingName[index]
                if cardFullName not in quantDic['0']:
                    if isHolo:
                        index = index+1
                    newNames.append(cardFullName)
                    
        newPricesDic[price] = newNames
    

    zoomInF()

    #iterate through each keys list given key
    for key in newPricesDic:
        #skip if for some reason price 1 is written or empty list
        if key == '1' or newPricesDic[key] == []:
            continue
        for card in newPricesDic[key]:
            fullscrollUp()

            moveClick(1162 , 907)
            pyperclip.copy(card)
            pyautogui.hotkey('ctrl', 'f')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            pyautogui.press('enter')

            moveClick(1226 , 922)

            pyautogui.press('left', presses=250)
            
            moveClick(293 , 906)
        #cards are selected now we hit price button and reset selections
        fullscrollUp()
        '''
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.write('Send us your comments')
        pyautogui.press('enter')'''

        pyautogui.hotkey('ctrl', 'f')
        pyautogui.write('Variation combinations')
        pyautogui.press('enter')

        moveClick(1279, 1135)
        pyautogui.write(key)
        moveClick(1281, 1163)
        time.sleep(0.2)

        #deselect all
        fullscrollUp()
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.write('Actions')
        pyautogui.press('enter')
        moveClick(300 , 896)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)

    zoomOutF()
    fullscrollDown()
    moveClick(130, 1355)
    time.sleep(10)
 


def vars(listingName, images, exactPicsDir):
    moveClick(381 , 268)
    time.sleep(5)
    moveClick(103, 343)
    time.sleep(5)
    moveClick(69 , 328)
    moveClick(125 , 383)
    pyautogui.write('Cards')
    pyautogui.press('enter')
    moveClick(100 , 425)

    #now were gonna enter names, process is paste the name of the card and then enter enter and repeat for all
    for card in listingName:
        pyperclip.copy(card)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.press('enter')
        
    pyautogui.write('t')
    pyautogui.press('enter')

    fullscrollUp()
    zoomInF()

    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('Update variations')
    time.sleep(0.5)
    moveClick(1284 , 918)
    time.sleep(1)
    moveClick(1286 , 989)
    time.sleep(5)

    zoomOutF()

    time.sleep(1)
    fullscrollDown()
    #zoom
    with pyautogui.hold('ctrl'):
        pyautogui.press('+', presses=4)

    moveClick(28 , 766)
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('Change photos in your listing based on this attribute')
    pyautogui.press('enter')
    moveClick(220 , 869)
    pyautogui.press('down')
    pyautogui.press('enter')   
    moveClick(46 , 757)
    time.sleep(1)

    #selecting for pictures now
    for i in  range(len(listingName)):
        item = listingName[i]
        fullscrollUp()
        moveClick(1340 , 371)
        
        #ctrl f and find the card number automatically scrolls to it
        pyautogui.hotkey('ctrl', 'f')
        pyperclip.copy(item)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        #clicks the card
        moveClick(390 , 812)

        #scroll to the bottom and click to be safe
        fullscrollDown()
        moveClick(2155 , 1323)

        pyperclip.copy('Change photos in your listing based on this attribute. This determines which photos buyers see when they select a variation option.')
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        savePic(i, images, exactPicsDir)

    with pyautogui.hold('ctrl'):
        pyautogui.press('-', presses=4)


def savePic(index, images, picPath):
    #spot is which part of the list were in, for example if spot is 3, were on the 3rd card in the list so get the 3rd pic in the folder
    moveClick(1121 , 1253)
    pyautogui.write(picPath+'\\'+images[index])
    pyautogui.press('enter')
    time.sleep(1)

def delZeros(zeros):
    '''fullscrollDown()
    moveClick(121, 1354)
    time.sleep(7)
    fullscrollUp()
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('The price in the listing is either invalid')
    moveClick(1083 , 879)
    time.sleep(15)'''

    #repeat()

    zoomInF()

    for card in zeros:
        #with zoom this must be done thrice
        fullscrollUp()

        moveClick(1162 , 907)

        pyperclip.copy(card)
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.press('enter')

        moveClick(1226 , 922)
        pyautogui.press('left', presses=500)
        moveClick(293 , 906)
        time.sleep(1)

    zoomOutF()
            
    fullscrollDown()
    moveClick(72 , 1209)
    pyperclip.copy('Variation combinations')
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    moveClick(673, 837)
    time.sleep(1)
    moveClick(1309, 812)


def repeat():
    zoomInF()
    solved = False
    counter = 0
    while not solved:
        counter += 1
        fullscrollDown()
        time.sleep(1)
        moveClick(1217 , 652)
        time.sleep(3)
        fullscrollUp()
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.write('The price in the listing is either invalid')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        moveClick(1107 , 1274)
        time.sleep(15)

        zoomOutF()
        time.sleep(1)
        zoomInF()
        time.sleep(2)

        fullscrollUp()
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.write('UPC')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)


        pyautogui.moveTo(1769 , 1109)
        pyperclip.copy('abc')
        pyautogui.doubleClick()

        pyautogui.hotkey('ctrl', 'c')

        if pyperclip.paste() == 'abc':
            solved = True
            zoomOutF()
            fullscrollUp()

        if counter > 20:
            break

def quantitySetter(quantDic):
    fullscrollUp()
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('Variation combinations')
    moveClick(71 , 893)
    time.sleep(1)
    moveClick(135, 838)
    pyautogui.write('1')
    moveClick(338 , 980)
    time.sleep(1)

    moveClick(314 , 838)
    pyautogui.write('1')
    moveClick(519 , 987)
    time.sleep(1)

    moveClick(71 , 893)
    

    #now that defaults set we get into proper quants
    #now we start actually selecting based on quantity
    
    #all done in full zoom
    zoomInF()

    #iterate through each keys list given key
    for key in quantDic:
        if key == '1' or key == '0':
            continue
        for card in quantDic[key]:
            fullscrollUp()

            '''pyautogui.hotkey('ctrl', 'f')
            pyautogui.write('Send us your comments')
            pyautogui.press('enter')
            '''
            moveClick(1162 , 907)
            pyperclip.copy(card)
            pyautogui.hotkey('ctrl', 'f')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            pyautogui.press('enter')

            moveClick(1226 , 922)

            pyautogui.press('left', presses=250)
            moveClick(293 , 906)
        #cards are selected now we hit quant button and reset selections
        fullscrollUp()

        pyautogui.hotkey('ctrl', 'f')
        pyautogui.write('Variation combinations')
        pyautogui.press('enter')

        moveClick(1273, 1365)
        pyautogui.write(key)
        moveClick(1281 , 1163)
        time.sleep(0.2)

        #deselect all
        fullscrollUp()
        fullscrollUp()
        fullscrollUp()
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.write('Actions')
        pyautogui.press('enter')
        moveClick(300 , 896)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)

    zoomOutF()


def setQuantity(quantLink):
    #goal is to group every card with certain quant and set. 
    lines = []
    with open(quantLink, 'r') as file:
        lines = file.readlines()
    lines = [x.strip() for x in lines]
    lines = [x.strip() for x in lines if x.strip()]


    #incase 0s typed evn though it should be blank
    for i in range(len(lines)):
        if lines[i][-1] == '0' and lines[i][-2] != '1':
            print('hm')
            lines[i] = lines[i][:-1]
    lines = [x.strip() for x in lines]

    #create dictionary where key is price and value is list of cards
    quantDic = {}
    quantDic['0'] = []
    
    for line in lines:
        splitL = line.split(' ')
        
        #check if quantDic has key that is equal to the last element of splitL and if not create it with a list containing line
        if line[-1].isdigit() == False:
            quantDic['0'].append(line)
            continue
        dicAppend = ''.join(line[:-1]).strip()
        if splitL[-1] not in quantDic:
            quantDic[splitL[-1]] = [dicAppend]
        else:
            quantDic[splitL[-1]].append(dicAppend)



    #have to del 0s.
    delZeros(quantDic['0'])

    quantitySetter(quantDic)
    return quantDic
