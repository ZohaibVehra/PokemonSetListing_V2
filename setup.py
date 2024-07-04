from os import makedirs, path

def newSet(name):
    name = name.replace(" ", "_").lower()
    relative_path = '../'+name
    if not path.exists(relative_path):
        # Create the new folder
        makedirs(relative_path)
        print(name)
        return relative_path+'/'
    else:
        print("the set already has a folder please delete it and retry")
        return 'exit'


