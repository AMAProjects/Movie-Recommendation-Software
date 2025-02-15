from welcome import *
from data import *

print_welcome()


#Main function to process the programme
def call_program():
    start_search()

#The 
def insert_genres():
    print('\n' + 'Perfect! Here are our available genres: ' + '\n')
    for i, genre in enumerate(genres, start = 0):
        print('- ' + str(i) + '. ' + genre + '\n')

    chosen_genre = input('Please select the number corresponding to the genre you want to look for: ')
    display_movies_from = genres[int(chosen_genre)]
    print(f'\nThe movies in the {display_movies_from} genre are:\n' )
    for movie in movies[display_movies_from]:
        print(f'\n - {movie['title']}, \n   rating: {movie['rating']}  \n   Suitable for ages: {movie['age_recommendation']}')


def start_search():
    search_type = str(input("Would you like to search by name or genre? Write 'n' for 'name' and 'g' for 'genre': "))
    if search_type == 'g':
        print(insert_genres())
    if search_type == 'n':
        neame_search = input ('Please enter the name of first letter/s of the movie you are looking for: ')


call_program()




