from enum import Enum
from helper import *
from xml_helper import *


animals = []

class Actions(Enum):
    Add = 1
    Search_by_brand = 2
    Delete_by_brand = 3
    Update_by_brand = 4
    Print = 5
    Exit = -1

def actions_display(): #display options
    for x in Actions: print(f'{x.name} = {x.value}')
    print('')
    return Actions(int(input('select an action: ')))

def zoo_menu(): #actions navigator
    while(True):
        slc = actions_display() # selection from user
        if slc == Actions.Add: add_x(animals)
        if slc == Actions.Search_by_brand: search_x(animals)
        if slc == Actions.Delete_by_brand: delete_x(animals)
        if slc == Actions.Update_by_brand: update_data(animals)
        if slc == Actions.Print: print_all(animals)
        if slc == Actions.Exit: return

#main
if __name__ == '__main__': 
    clear_screen()
    animals = load_data("zoo.csv")
    zoo_menu() 
    clear_screen()
    save_data(animals,"zoo.csv")
