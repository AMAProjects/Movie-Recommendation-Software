from welcome import *
from data import *

print_welcome()


#Main function to process the programme
def call_program():
    start_search()
    

#Function search by genre
def insert_genres():
    print('\n' + 'Perfect! Here are our available genres: ' + '\n')
    for i, genre in enumerate(genres, start = 0):
        print('- ' + str(i) + '. ' + genre + '\n')

    chosen_genre = input('Please select the number corresponding to the genre you want to look for: ')
    display_movies_from_genre = genres[int(chosen_genre)]

    #Ask if user wants to apply any filters to their seach
    filters(display_movies_from_genre)
    
    print(f'\nThe movies in the {display_movies_from_genre} genre are:\n' )
    for movie in movies[display_movies_from_genre]:
        print(f'\n - {movie['title']}, \n   rating: {movie['rating']}  \n   Suitable for ages: {movie['age_recommendation']}')

#Function to ask about search type
def start_search():
    search_type = str(input("Would you like to search by name or genre? Write 'n' for 'name' and 'g' for 'genre': "))
    if search_type == 'g':
        print(insert_genres())
    if search_type == 'n':
        neame_search = input ('Please enter the name of first letter/s of the movie you are looking for: ')

#Apply filters function
def filters(filtered_genre):
    apply_filters = input(f"\nBefore we display the movies under {filtered_genre} genre; Would you like to apply any filters to your search? \n\n Filters available: \n - Age rating \n - Movie rating \n\n Please indicate 'y' for yes or 'n' no:  ")
    
    if apply_filters.lower() == 'y':
        pass #TO DO!
    if apply_filters.lower() == 'n':
        pass #TO DO
    else:
        print('Please enter a valid input')


call_program()




