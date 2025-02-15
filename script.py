from welcome import *
from data import *

print_welcome()


#Main function to process the programme
def call_program():
    start_search()

#The 
def insert_genres():
    print('\n' + 'Perfect! Here are our available genres: ' + '\n')
    for genre in genres:
        print('- ' + genre + '\n')


def start_search():
    search_type = str(input("Would you like to search by name or genre? Write 'n' for 'name' and 'g' for 'genre': "))
    if search_type == 'g':
        print(insert_genres())
    if search_type == 'n':
        neame_search = input ('Please enter the name of first letter/s of the movie you are looking for: ')


call_program()




