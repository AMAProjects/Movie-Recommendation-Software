from welcome import *
from data import *
from filters import *

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
        print('\n --------------------------------\n')
    
     # After this point, you can either exit or loop back to another function, but not start_search() again
    again = input("\nWould you like to search again? (y/n) ").lower()

    if again == 'y':
        start_search()  # Call again if the user wants to start a new search  
    else:
        print("\nThank you for using the movie search program!\n")
        exit()


#Function to ask about search type
def start_search():
    search_type = str(input("Would you like to search by name or genre? Write 'n' for 'name' and 'g' for 'genre': "))
    if search_type.lower() == 'g':
        insert_genres()
    elif search_type.lower() == 'n':
        print("Name search functionality not implemented yet.")
        #name_search = input ('\nPlease enter the name of first letter/s of the movie you are looking for: \n')
        #TO DO
    else:
        print("\nPlease select either 'g' or 'n'\n")
        start_search()




call_program()




