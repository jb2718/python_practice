shopping_list = []

def add_to_list(item):
    shopping_list.append(item)
    
    print("Item added to list!")
    print("You have {} items on your list".format(len(shopping_list)))
    
    
def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'SHOW' to display all items in list.
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for the help menu.
    """)

def show_list():
    print("Shopping List")
    print("----------------")
    for item in shopping_list:
        print(item)
    
    
show_help()
while True:
    new_item = input("> ")
    
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    
    add_to_list(new_item)
        
show_list()
           