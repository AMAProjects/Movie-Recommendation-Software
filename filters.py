from data import *


#Apply filters function
def filters(filtered_item):
    apply_filters = input(f"\nBefore we display the movies under {filtered_item} genre; Would you like to apply any filters to your search? \n\n Filters available: \n\n - Age rating \n - Movie rating \n\n Please indicate 'y' for yes or 'n' no:  ")
    

    if apply_filters.lower() == 'y':
        which_filters = input("\nPlease introduce 'a' for age filters, 'r' for rating filters or 'b' to modify both filters: \n")

        if which_filters.lower() == 'a':
            age_limit = int(input("\nEnter the maximum age rating (e.g., 13, 16, 18): \n"))

            age_filtered_movies = [] #Created to keep track of the movies that match the filters

            for movie in movies[filtered_item]:
                movie_age = int(''.join(filter(str.isdigit, movie['age_recommendation'])))
                if movie_age <= age_limit:
                    age_filtered_movies.append(movie)
            
            if len(age_filtered_movies) > 0:
                print(f"\nMovies under {filtered_item} genre suitable for ages {age_limit} and below:\n")
                for movie in age_filtered_movies:
                    print(f" - {movie['title']}, Rating: {movie['rating']}, Age: {movie['age_recommendation']}\n")
            
            else:
                print('\nThere seems to be no movies matching your criteria. Sorry :( \n')
                print('Alternatively: ')

            
            return 

        if which_filters.lower() == 'r':
            rating = input("\nLooking for top-rated movies? Enter the minimum rating you'd consider (1-5, e.g., 4):  ")

            rating_filtered_movies = []

            for movie in movies[filtered_item]:
                movie_split = movie['rating'].split('/')

                if int(movie_split[0]) >= int(rating):
                    rating_filtered_movies.append(movie)
            
            if len(rating_filtered_movies) > 0:
                print(f"\nMovies under {filtered_item} genre with a rating of {rating}/5 or higher:\n")

                for movie in rating_filtered_movies:
                    print(f" - {movie['title']}, Rating: {movie['rating']}, Age: {movie['age_recommendation']}\n")
        
            
            else:
                print('\nThere seems to be no movies matching your criteria. Sorry :( \n')
                print('Alternatively: ')

            return

                
        if which_filters.lower() == 'b':
            age_limit = int(input("\nEnter the maximum age rating (e.g., 13, 16, 18): \n"))

            rating = input("\nLooking for top-rated movies? Enter the minimum rating you'd consider (1-5, e.g., 4):  ")

            age_and_rating_filtered_movies = [] #Created to keep track of the movies that match the filters

            for movie in movies[filtered_item]:
                movie_age = int(''.join(filter(str.isdigit, movie['age_recommendation'])))
                movie_split = movie['rating'].split('/')
                if movie_age <= age_limit and int(movie_split[0]) >= int(rating):
                    age_and_rating_filtered_movies.append(movie)
                

            if len(age_and_rating_filtered_movies) > 0:
                print(f"\nMovies under {filtered_item} genre suitable for ages {age_limit} and rating of {rating}/5 or higher are:\n")
                    
                for movie in age_and_rating_filtered_movies:
                        print(f" - {movie['title']}, Rating: {movie['rating']}, Age: {movie['age_recommendation']}\n")

            else:
                print('\nThere seems to be no movies matching your criteria. Sorry :( \n')
                print('Alternatively: ')
                
            return

        else:
            print("Invalid input. Please enter 'a', 'r', or 'b'.")
            filters(filtered_item)  # Recursively call to retry

    if apply_filters.lower() == 'n':
        return
    
    else:
        print('Please enter a valid input')