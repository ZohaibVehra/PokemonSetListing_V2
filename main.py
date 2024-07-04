#everything runs from here
from setup import *
from os import makedirs, path, listdir, getcwd
from getPics import *
import pyautogui
from quantities import *
from ebay import *

def main():

    #check for new set and create setup for it
    wp = ''
    print('Starting')
    y = input("If this is for the listing of a new set please hit y, hit n otherwise\n")
    if y ==  'y' or y == 'Y':
        #generate new folder
        setName = input("enter the set name\n")
        wp = newSet(setName)
        if wp == 'exit':
            exit 

        #creating sub folders and files needed - folder for pics - text file for quantities 
        makedirs(wp+'pics')
        picPath = wp+'pics/'

        with open(wp+'quantites.txt', 'w') as file:
            pass

        with open(wp+'prices.txt', 'w') as file:
            pass 
        
        listUrl, holoList = getPics(picPath, wp.split("/")[-2])

        print(listUrl, picPath, holoList, wp+'quantites.txt')
        getQuantitiesTxt(listUrl, picPath, holoList, wp+'quantites.txt')

    elif y == 'n' or y == 'N':

        y = input('do you want to list a set on ebay that already exists? y for yes or n for no\n')
        #ebay listing
        if y == 'y' or y == 'Y':
            name = input('enter the name of the set you want to list\n')
            name = name.replace(" ", "_").lower()
            current_directory = getcwd()
            parent_directory = path.dirname(current_directory)
            exactPicsDir = parent_directory+'\\'+name+'\\pics'
            spath = '../'+name + '/'

            eBayStuff(spath+'quantites.txt', spath+'pics', name, exactPicsDir)


def Test():
    #getQuantitiesTxt('https://limitlesstcg.com/cards/OBF?display=list', r'C:\Users\Zohaib\OneDrive\Desktop\Poke_Sets\obsidian_flames\pics', ['25', '30', '62', '70', '72', '85', '95', '136', '141', '188'], r'C:\Users\Zohaib\OneDrive\Desktop\Poke_Sets\obsidian_flames\quantites.txt')
    #eBayStuff(r'C:\Users\Zohaib\OneDrive\Desktop\Poke_Sets\obsidian_flames\quantites.txt', r'C:\Users\Zohaib\OneDrive\Desktop\Poke_Sets\obsidian_flames\pics', 'obsidian_flames')

    #lo test
    #eBayStuff(r'C:\Users\Zohaib\OneDrive\Desktop\Poke_Sets\lost_origin\quantites.txt', r'C:\Users\Zohaib\OneDrive\Desktop\Poke_Sets\lost_origin\pics', 'lost_origin')

    #test set
    eBayStuff(r'C:\Users\Zohaib\OneDrive\Desktop\Poke_Sets\test_set\quantites.txt', r'C:\Users\Zohaib\OneDrive\Desktop\Poke_Sets\test_set\pics', 'test_set')

main()
#Test()




