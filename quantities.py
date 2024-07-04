from os import path, listdir
import pyautogui
import pyperclip
import webbrowser
import time
from useful import *

def getQuantitiesTxt(listUrl, picsPath, holoList, qpath):
    outOf = outOfNumber(picsPath)
    print(outOf)
    allInfo = getAllInfo(listUrl, outOf, holoList)
    print(allInfo)
    #we have to remove double rares still
    allInfo = removeDoubleRares(allInfo, picsPath)
    print(allInfo)
    with open(qpath, "w") as file:
        for string in allInfo:
            file.write(f"{string}\n")


def outOfNumber(picsPath):
    # List all files in the folder
    files = listdir(picsPath)

    # Get the full path for each file
    full_paths = [path.join(picsPath, file) for file in files]

    # Find the last file based on the default sorting of Windows
    outOfNumber = min(full_paths, key=path.getctime)[-7:-4]
    return outOfNumber


def getAllInfo(link, outOf, holoList):
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

    # Open the constructed URL in Chrome
    webbrowser.get('chrome').open(link)
    time.sleep(2)
    moveClick(376, 449)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    code = pyperclip.paste()

    allList= []
    lines = code.split('\n')
    rStrippedLines = []
    for line in lines:
        if '\r' in line:
            line = line.replace('\r',"")
            rStrippedLines.append(line)
    
    shortenedList  = rStrippedLines[36:-19]

    
    for index, line in enumerate(shortenedList):
        pokemon = ''
        if line.isdigit():
            if len(line) == 1:
                pokemon = '00'+line+'/'+outOf + ' ' + shortenedList[index+1] + ' Reverse Holo'
            elif len(line) == 2:
                pokemon = '0'+line+'/'+outOf+ ' ' + shortenedList[index+1] + ' Reverse Holo'
            elif len(line) == 3:
                pokemon = line+'/'+outOf+ ' ' + shortenedList[index+1] + ' Reverse Holo'
            if line == outOf:
                allList.append(pokemon)
                if line in holoList:
                    allList.append(pokemon.replace(' Reverse', ''))
                break
            allList.append(pokemon)
            if line in holoList:
                allList.append(pokemon.replace(' Reverse', ''))
            if int(line)%30 == 0:
                allList.append('\n')
    return allList


def removeDoubleRares(allInfo, picPath):
    file_names = []
    for file in listdir(picPath):
        if path.isfile(path.join(picPath, file)):
            file_names.append(file)
    file_names = [x for x in file_names if 'h' not in x]        
    file_names = [x[:3] for x in file_names]
    print(file_names)

    newAllInfo = []

    for i in range(len(allInfo)):
        first3 = allInfo[i][:3]
        if first3 in file_names:
            newAllInfo.append(allInfo[i])


    return newAllInfo