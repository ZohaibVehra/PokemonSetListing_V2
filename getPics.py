from os import path
import pyautogui
import pyperclip
import webbrowser
import time
from useful import *
import requests

def getPics(path, set):

    #get holo numbers
    url, setplus = goToSite(set)
    code = getSiteCode(url)
    holoList, listlink = holoNum(setplus)
    links, holoList = picsUrls(code, setplus, holoList)
    print(links)
    download(links,path)
    return listlink, holoList

def holoNum(set):
    xpos = 734
    ystart = 471
    yincrement = 40
    setName = set.replace('_',' ')
    setName = setName.replace('+',' ')

    with open('Sets.txt', 'r', encoding='utf-8') as file:
        setsList = file.readlines()

    setsList = [line.lower() for line in setsList]
    cleanLines = []

    for line in setsList:
        cleanLine = line[3:-1]
        if cleanLine == 'pokémon 151':
            cleanLine = '151'
            
        cleanLines.append(cleanLine)
    lineNum = cleanLines.index(setName.lower())

    acr = setsList[lineNum][:3].upper()

    holoListUrl = 'https://limitlesstcg.com/cards/'+acr+'?display=list'

    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

    # Open the constructed URL in Chrome
    webbrowser.get('chrome').open(holoListUrl)
    time.sleep(2)
    moveClick(376,449)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    return holosFromPaste(pyperclip.paste()), holoListUrl

    
def holosFromPaste(paste):
    holoNumList= []
    lines = paste.split('\n')
    rStrippedLines = []
    for line in lines:
        if '\r' in line:
            line = line.replace('\r',"")
            rStrippedLines.append(line)
    
    shortenedList  = rStrippedLines[36:-19]
    checkLine = 'Rare'
    if any('Holo Rare' == s for s in shortenedList):
        checkLine = 'Holo Rare'


    for index, line in enumerate(shortenedList):
        if(line == checkLine):
            i = index
            found = False
            count = 0
            while (not found and i >= 0):
                count+=1
                if count>100:
                    break
                if shortenedList[i].isdigit():
                    holoNumList.append(shortenedList[i])
                    found = True
                i = i-1
                
    return holoNumList





def getSiteCode(url):
    #need to go to site manually for this shit to work
    pyperclip.copy(url)
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

    # Open the specified URL in Chrome
    webbrowser.get('chrome').open(url)
    time.sleep(4)

    pyautogui.moveTo(250,250)

    for i in range(50):        
        time.sleep(0.02)
        pyautogui.scroll(-1350)

    pyautogui.press('f12')
    time.sleep(2)
      # Move to the first point and perform a right click
    pyautogui.moveTo(2134, 212)
    pyautogui.rightClick()

    # Pause for a moment
    time.sleep(1)

    # Move to the second point and hover for 2 seconds
    pyautogui.moveTo(2235, 392)
    time.sleep(2)

    # Move to the third point and perform a left click
    moveClick(2471, 382)

    pyautogui.hotkey('alt', 'tab')
    time.sleep(.5)

    return pyperclip.paste()

def replace_char_by_index(string, index):
    return string[:index] + string[index].upper() + string[index + 1:]

def goToSite(set):
    
    #note urls are weird for base sets figure that shit out with a if set == '' set url to exact url manually
    #sample https://www.pokedata.io/set/Paradox+Rift?s=4
    set = set.replace('_', '+')
    indices = [i for i, char in enumerate(set) if char == '+']
    set = replace_char_by_index(set, 0)
    for i in indices:
        set = replace_char_by_index(set, i+1)

    url = 'https://www.pokedata.io/set/'+set+'?s=4'
    print(url)
    
    return url, set


def picsUrls(code, setplus, holos):
    s = f'https://pokemoncardimages.s3.us-east-2.amazonaws.com/images/{setplus}/'
    content = code
    count = 0
    Urls = []
    for i in range(300, 0, -1):
        if i < 10:
            a ='00'+str(i)
        elif i <100:
            a = '0'+str(i)
        else:
            a = str(i)

        if s+a+'.webp' in content and str(i) in holos:
            Urls.append(s+a+'.webp')
        
        if s+a+'r.webp' in content:
            Urls.append(s+a+'r.webp')
    
    return Urls, holos

def download(links, path):

    for link in links:
        response = requests.get(link)
        if response.status_code != 200:
            exit
        name = link.split(".")[-2]

        print(name)
        check = name[-4:]
        savename = ''
        if check[-1] == 'r':
            savename = check[:-1]+'.png'
        else:
            savename = check[1:]+'h.png'
        

        with open(path+'/'+savename, 'wb') as file:
            file.write(response.content)

