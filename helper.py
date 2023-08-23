import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_x(list): #add action
    list.append({"kind": input('enter animal kind: '),"name": input('enter animal name: '),"age": input('enter animal age: ')}) 

def delete_x(list): #delete action
    res = search_action(list)
    if(res != None): 
        list.remove(res)
        print(f'{res["kind"]} - {res["name"]}, {res["age"]} deleted succesfully')
    else: print('no such animal in database')

def search_x(list): #search + print action
    res = search_action(list)
    if(res != None): print(f'{res["kind"]} - {res["name"]}, {res["age"]}')
    else: print('no such animal in database')

def search_action(list): #generic search function
    if(list):
        kind = input('enter animal kind to search: ') # brand from user
        found = False
        for x in list:
            if x["kind"] == kind: 
                tmp=x
                found = True
        if found: return (tmp)
        return None        
    else: print('no data at all')

def update_data(list): #update data
    res = search_action(list)
    if(res != None): 
        b = True
        while(b):
            print('What to update?')
            t = int(input(f'{res["kind"]} = 1 | {res["name"]} = 2 | {res["age"]} = 3 | if end enter 4 ?'))
            if t == 1: res["kind"] = input("Enter updated kind: ")
            if t == 2: res["name"] = input("Enter updated name: ")
            if t == 3: res["age"] = input("Enter updated age: ")
            if t == 4: return
            print(f'Updated to: {res["kind"]} - {res["name"]}, {res["age"]}')
    else: print('no such car in database')

def print_all(list): #print all
    if(list):
        c = 1
        for x in list:
            print(f'{c}/{len(list)} : {x["kind"]} - {x["name"]}, {x["age"]}') # 'kind' - 'name', 'age'
            c=c+1
    else: print(list)