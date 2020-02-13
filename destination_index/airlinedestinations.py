#This is a great example of pythons capability, an airline destination program!


menu_prompt = ('Available commands:\n'
               '    (add) Add passenger\n'
               '    (del) Delete passenger\n'
               '    (print) Print passenger list\n'
               '    (exit) Exit the program\n'
               'Enter the command listed above:\n')
#Our dictionary of destinations
destinations = ['CHI', 'MIL', 'MIN']

destination_prompt = ('Available destinations:\n'
                      ' (CHI)  Chicago\n'
                      ' (MIL)  Milwaukee\n'
                      ' (MIN)  Minneapolis-St. Paul\n')
#An empty dictionary of passengers who are going somewhere.
passengers = {}




print('Welcome to Bluejay Airlines!\n')
user_input = input(menu_prompt).strip().lower()

while user_input != 'exit':
    if user_input == 'add':
        name = input('Enter passenger name: \n').strip().upper()
        destination = input(destination_prompt).strip().upper()
        if destination not in destinations:
            print('Unknown destination, sorry!\n')
        else:
            passengers[name] = destination

    elif user_input == 'del':
        name = input('Enter passenger name:\n').strip().upper()
        if name in passengers:
            del passengers[name]

    elif user_input == 'print':
        for passenger in passengers:
            print('%s --> %s' % (passenger.title(), passengers[passenger]))

    else:
        print('Unrecognized command.')

    user_input = input('Enter a new command:\n').strip().lower()

