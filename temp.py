import pyautogui
import time
import webbrowser
import requests
import pyperclip
from useful import *
import random
from os import path, listdir
import ebay


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


def vars(listingName, images, pricesDic, picPath):
    time.sleep(1)
    zoomInF()
    time.sleep(2)
    fullscrollDown()
    time.sleep(2)
    pyautogui.moveTo(1254 , 1228)
    pyautogui.click()  
    time.sleep(2)

    zoomOutF()

    time.sleep(1)
    fullscrollDown()
    #zoom
    with pyautogui.hold('ctrl'):
        pyautogui.press('+', presses=4)

    pyautogui.moveTo(28 , 766)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('Change photos in your listing based on this attribute')
    pyautogui.press('enter')
    pyautogui.moveTo(220 , 869)
    pyautogui.click()
    pyautogui.press('down')
    pyautogui.press('enter')   
    pyautogui.moveTo(46 , 757)
    pyautogui.click()
    time.sleep(1)

    #selecting for pictures now
    for i in  range(len(listingName)):
        item = listingName[i]
        fullscrollUp()
        '''pyautogui.moveTo(1272 , 169)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'f')
        pyperclip.copy('Send us your comments')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        fullscrollUp()'''
        pyautogui.moveTo(1340 , 371)
        pyautogui.click()
        
        #ctrl f and find the card number automatically scrolls to it
        pyautogui.hotkey('ctrl', 'f')
        pyperclip.copy(item)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)
        #clicks the card
        pyautogui.moveTo(390 , 812)
        pyautogui.click()
        time.sleep(3)

        #scroll to the bottom and click to be safe
        fullscrollDown()
        pyautogui.moveTo(2155 , 1323)
        pyautogui.click()
        time.sleep(3)

        pyperclip.copy('Change photos in your listing based on this attribute. This determines which photos buyers see when they select a variation option.')
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        savePic(i, images, picPath)
        time.sleep(3)

    with pyautogui.hold('ctrl'):
        for i in range(5):
            time.sleep(0.1)
            pyautogui.scroll(-100)

def savePic(index, images, picPath):
    #spot is which part of the list were in, for example if spot is 3, were on the 3rd card in the list so get the 3rd pic in the folder
    pyautogui.moveTo(1121 , 1253)
    pyautogui.click()
    pyautogui.write(picPath+'\\'+images[index])
    pyautogui.press('enter')
    time.sleep(1)


def repeat():
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

        if counter > 20:
            break
        

time.sleep(1)
quantDic = ebay.setQuantity(r'C:\Users\Zohaib\OneDrive\Desktop\Poke_Sets\temporal_forces\quantites.txt')

print(quantDic)

listingName, images = getLists(r'C:\Users\Zohaib\OneDrive\Desktop\Poke_Sets\temporal_forces\quantites.txt', r'C:\Users\Zohaib\OneDrive\Desktop\Poke_Sets\temporal_forces\pics')

pricesDic = ebay.prices(r'C:\Users\Zohaib\OneDrive\Desktop\Poke_Sets\temporal_forces\prices.txt')
print(pricesDic)
ebay.setPrices(pricesDic, listingName, quantDic)