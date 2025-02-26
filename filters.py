from data import *

def filters(filtered_item):
    # Validate 'y' or 'n' input
    print(f'Before we display the movies under {filtered_item} genre; Would you like to apply any filters to your search? \n\n Filters available: \n\n - Age rating \n\n - Movie rating \n')
    while True:
        apply_filters = input(f"\n\n Please indicate 'y' for yes or 'n' no:  \n")
        if apply_filters.lower() in ['y', 'n']:
            break
        print("\nInvalid input. Please enter 'y' for yes or 'n' for no.")

    if apply_filters.lower() == 'y':
        # Validate 'a', 'r', or 'b' input
        while True:
            which_filters = input("\nPlease introduce 'a' for age filters, 'r' for rating filters or 'b' to modify both filters: \n")
            if which_filters.lower() in ['a', 'r', 'b']:
                break
            print("\nInvalid input. Please enter 'a', 'r', or 'b'.")

        if which_filters.lower() == 'a':
            while True:
                age_input = input("\nEnter the maximum age rating (e.g., 13, 16, 18): \n")
                if age_input.isdigit():  
                    age_limit = int(age_input)  
                    if age_limit > 0:  
                        break  
                    else:
                        print("\nPlease enter a positive age limit greater than zero.")
                else:
                    print("\nInvalid input. Please enter a valid age.")

            age_filtered_movies = []  

            for movie in movies[filtered_item]:
                movie_age = int(''.join(filter(str.isdigit, movie['age_recommendation'])))
                if movie_age <= age_limit:
                    age_filtered_movies.append(movie)
            
            if age_filtered_movies:
                print(f"\nMOVIES UNDER {filtered_item.upper()} GENRE SUITABLE FOR AGES {age_limit} AND BELOW:\n")
                for movie in age_filtered_movies:
                    print(f'\n - {movie['title']}, \n   Rating: {movie['rating']}  \n   Suitable for ages: {movie['age_recommendation']}')
                    print('\n --------------------------------\n')
            else:
                print('\nThere seems to be no movies matching your criteria. Sorry :( \n')
            return 

        if which_filters.lower() == 'r':
            while True:
                rating = input("\nLooking for top-rated movies? Enter the minimum rating you'd consider (1-5, e.g., 4):  ")
                if rating.isdigit() and 1 <= int(rating) <= 5:
                    rating = int(rating)  # Convert to integer after validation
                    break
                print("\nInvalid input. Please enter a number between 1 and 5.")
            
            rating_filtered_movies = []

            for movie in movies[filtered_item]:
                movie_split = movie['rating'].split('/')
                if int(movie_split[0]) >= int(rating):
                    rating_filtered_movies.append(movie)
            
            if rating_filtered_movies:
                print(f"\nMOVIES UNDER {filtered_item.upper()} GERNE WITH A RATING OF {rating}/5 OR HIGHER:\n")
                for movie in rating_filtered_movies:
                    print(f'\n - {movie['title']}, \n   Rating: {movie['rating']}  \n   Suitable for ages: {movie['age_recommendation']}')
                    print('\n --------------------------------\n')
            else:
                print('\nThere seems to be no movies matching your criteria. Sorry :( \n')
            return

        if which_filters.lower() == 'b':
            age_limit = int(input("\nEnter the maximum age rating (e.g., 13, 16, 18): \n"))

            while True:
                rating = input("\nLooking for top-rated movies? Enter the minimum rating you'd consider (1-5, e.g., 4):  ")
                if rating.isdigit() and 1 <= int(rating) <= 5:
                    rating = int(rating)  # Convert to integer after validation
                    break
                print("\nInvalid input. Please enter a number between 1 and 5.")

            age_and_rating_filtered_movies = []

            for movie in movies[filtered_item]:
                movie_age = int(''.join(filter(str.isdigit, movie['age_recommendation'])))
                movie_split = movie['rating'].split('/')
                if movie_age <= age_limit and int(movie_split[0]) >= int(rating):
                    age_and_rating_filtered_movies.append(movie)

            if age_and_rating_filtered_movies:
                print(f"\nMOVIES UNDER {filtered_item.upper()} GENRE SUITABLE FOR AGES {age_limit} AND RATING OF {rating}/5 OR HIGHER ARE:\n")
                for movie in age_and_rating_filtered_movies:
                    print(f'\n - {movie['title']}, \n   Rating: {movie['rating']}  \n   Suitable for ages: {movie['age_recommendation']}')
                    print('\n --------------------------------\n')
            else:
                print('\nThere seems to be no movies matching your criteria. Sorry :( \n')
            return

    if apply_filters.lower() == 'n':
        return
