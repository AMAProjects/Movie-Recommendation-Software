genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sports', 'Thriller', 'War', 'Western']

movies = {
    "Action": [
        {"title": "Mad Max: Fury Road", "rating": "5/5", "age_recommendation": "16+"},
        {"title": "John Wick", "rating": "4/5", "age_recommendation": "18+"},
        {"title": "The Dark Knight", "rating": "5/5", "age_recommendation": "13+"},
        {"title": "Die Hard", "rating": "4/5", "age_recommendation": "16+"},
        {"title": "Gladiator", "rating": "3/5", "age_recommendation": "16+"}
    ],
    "Adventure": [
        {"title": "Jurassic Park", "rating": "4/5", "age_recommendation": "13+"},
        {"title": "Indiana Jones: Raiders of the Lost Ark", "rating": "5/5", "age_recommendation": "12+"},
        {"title": "The Revenant", "rating": "3/5", "age_recommendation": "18+"},
        {"title": "The Lord of the Rings: The Fellowship of the Ring", "rating": "5/5", "age_recommendation": "12+"},
        {"title": "Life of Pi", "rating": "2/5", "age_recommendation": "10+"}
    ],
    "Animation": [
        {"title": "Toy Story", "rating": "5/5", "age_recommendation": "0+"},
        {"title": "Spider-Man: Into the Spider-Verse", "rating": "4/5", "age_recommendation": "9+"},
        {"title": "Finding Nemo", "rating": "5/5", "age_recommendation": "0+"},
        {"title": "Shrek", "rating": "3/5", "age_recommendation": "6+"},
        {"title": "Coco", "rating": "5/5", "age_recommendation": "0+"}
    ],
    "Biography": [
        {"title": "The Social Network", "rating": "4/5", "age_recommendation": "13+"},
        {"title": "Bohemian Rhapsody", "rating": "3/5", "age_recommendation": "13+"},
        {"title": "Schindler’s List", "rating": "5/5", "age_recommendation": "18+"},
        {"title": "A Beautiful Mind", "rating": "4/5", "age_recommendation": "13+"},
        {"title": "The Wolf of Wall Street", "rating": "2/5", "age_recommendation": "18+"}
    ],
    "Comedy": [
        {"title": "Superbad", "rating": "3/5", "age_recommendation": "17+"},
        {"title": "The Grand Budapest Hotel", "rating": "4/5", "age_recommendation": "16+"},
        {"title": "Step Brothers", "rating": "2/5", "age_recommendation": "16+"},
        {"title": "Dumb and Dumber", "rating": "3/5", "age_recommendation": "10+"},
        {"title": "Ferris Bueller’s Day Off", "rating": "5/5", "age_recommendation": "13+"}
    ],
    "Crime": [
        {"title": "The Godfather", "rating": "5/5", "age_recommendation": "18+"},
        {"title": "Goodfellas", "rating": "5/5", "age_recommendation": "18+"},
        {"title": "Pulp Fiction", "rating": "4/5", "age_recommendation": "18+"},
        {"title": "The Departed", "rating": "3/5", "age_recommendation": "18+"},
        {"title": "No Country for Old Men", "rating": "2/5", "age_recommendation": "18+"}
    ],
    "Documentary": [
        {"title": "Won’t You Be My Neighbor?", "rating": "5/5", "age_recommendation": "0+"},
        {"title": "Free Solo", "rating": "4/5", "age_recommendation": "12+"},
        {"title": "13th", "rating": "5/5", "age_recommendation": "16+"},
        {"title": "Inside Job", "rating": "3/5", "age_recommendation": "14+"},
        {"title": "The Act of Killing", "rating": "2/5", "age_recommendation": "18+"}
    ],
    "Drama": [
        {"title": "Forrest Gump", "rating": "5/5", "age_recommendation": "13+"},
        {"title": "The Shawshank Redemption", "rating": "5/5", "age_recommendation": "16+"},
        {"title": "Parasite", "rating": "4/5", "age_recommendation": "16+"},
        {"title": "The Green Mile", "rating": "3/5", "age_recommendation": "16+"},
        {"title": "A Star Is Born", "rating": "2/5", "age_recommendation": "16+"}
    ],
    "Family": [
        {"title": "The Lion King", "rating": "5/5", "age_recommendation": "0+"},
        {"title": "Paddington 2", "rating": "5/5", "age_recommendation": "0+"},
        {"title": "Harry Potter and the Sorcerer’s Stone", "rating": "4/5", "age_recommendation": "8+"},
        {"title": "Aladdin (1992)", "rating": "3/5", "age_recommendation": "6+"},
        {"title": "Frozen", "rating": "4/5", "age_recommendation": "0+"}
    ],
    "Fantasy": [
        {"title": "The Lord of the Rings: The Fellowship of the Ring", "rating": "5/5", "age_recommendation": "12+"},
        {"title": "Harry Potter and the Prisoner of Azkaban", "rating": "4/5", "age_recommendation": "10+"},
        {"title": "Pan’s Labyrinth", "rating": "3/5", "age_recommendation": "16+"},
        {"title": "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "rating": "4/5", "age_recommendation": "8+"},
        {"title": "Stardust", "rating": "2/5", "age_recommendation": "12+"}
    ],
    "History": [
        {"title": "12 Years a Slave", "rating": "5/5", "age_recommendation": "18+"},
        {"title": "Schindler’s List", "rating": "5/5", "age_recommendation": "18+"},
        {"title": "The Last Emperor", "rating": "4/5", "age_recommendation": "16+"},
        {"title": "The King's Speech", "rating": "4/5", "age_recommendation": "12+"},
        {"title": "Gladiator", "rating": "3/5", "age_recommendation": "16+"}
    ],

    "Horror": [
        {"title": "The Shining", "rating": "5/5", "age_recommendation": "18+"},
        {"title": "Get Out", "rating": "4/5", "age_recommendation": "16+"},
        {"title": "A Quiet Place", "rating": "3/5", "age_recommendation": "13+"},
        {"title": "It (2017)", "rating": "2/5", "age_recommendation": "16+"},
        {"title": "Hereditary", "rating": "5/5", "age_recommendation": "18+"}
    ],
    "Musical": [
        {"title": "La La Land", "rating": "4/5", "age_recommendation": "12+"},
        {"title": "The Greatest Showman", "rating": "3/5", "age_recommendation": "0+"},
        {"title": "Les Misérables", "rating": "4/5", "age_recommendation": "12+"},
        {"title": "Mamma Mia!", "rating": "5/5", "age_recommendation": "0+"},
        {"title": "West Side Story (1961)", "rating": "2/5", "age_recommendation": "12+"}
    ],
    "Mystery": [
        {"title": "Gone Girl", "rating": "4/5", "age_recommendation": "18+"},
        {"title": "Knives Out", "rating": "5/5", "age_recommendation": "13+"},
        {"title": "Se7en", "rating": "3/5", "age_recommendation": "18+"},
        {"title": "Prisoners", "rating": "4/5", "age_recommendation": "16+"},
        {"title": "The Girl with the Dragon Tattoo (2011)", "rating": "2/5", "age_recommendation": "18+"}
    ],
    "Romance": [
        {"title": "Titanic", "rating": "5/5", "age_recommendation": "13+"},
        {"title": "Pride & Prejudice (2005)", "rating": "4/5", "age_recommendation": "0+"},
        {"title": "The Notebook", "rating": "3/5", "age_recommendation": "13+"},
        {"title": "A Walk to Remember", "rating": "2/5", "age_recommendation": "10+"},
        {"title": "Before Sunrise", "rating": "5/5", "age_recommendation": "16+"}
    ],
    "Sci-Fi": [
        {"title": "Inception", "rating": "5/5", "age_recommendation": "13+"},
        {"title": "Interstellar", "rating": "4/5", "age_recommendation": "13+"},
        {"title": "Blade Runner 2049", "rating": "3/5", "age_recommendation": "16+"},
        {"title": "The Matrix", "rating": "5/5", "age_recommendation": "16+"},
        {"title": "E.T. the Extra-Terrestrial", "rating": "5/5", "age_recommendation": "0+"}
    ],
    "Sports": [
        {"title": "Rocky", "rating": "5/5", "age_recommendation": "10+"},
        {"title": "Remember the Titans", "rating": "4/5", "age_recommendation": "10+"},
        {"title": "Moneyball", "rating": "3/5", "age_recommendation": "12+"},
        {"title": "Creed", "rating": "4/5", "age_recommendation": "13+"},
        {"title": "The Blind Side", "rating": "2/5", "age_recommendation": "10+"}
    ],
    "Thriller": [
        {"title": "Fight Club", "rating": "5/5", "age_recommendation": "18+"},
        {"title": "Black Swan", "rating": "4/5", "age_recommendation": "18+"},
        {"title": "The Silence of the Lambs", "rating": "5/5", "age_recommendation": "18+"},
        {"title": "Oldboy (2003)", "rating": "3/5", "age_recommendation": "18+"},
        {"title": "The Girl on the Train", "rating": "2/5", "age_recommendation": "16+"}
    ],
    "War": [
        {"title": "Saving Private Ryan", "rating": "5/5", "age_recommendation": "16+"},
        {"title": "Hacksaw Ridge", "rating": "4/5", "age_recommendation": "16+"},
        {"title": "Full Metal Jacket", "rating": "3/5", "age_recommendation": "18+"},
        {"title": "Apocalypse Now", "rating": "5/5", "age_recommendation": "18+"},
        {"title": "1917", "rating": "4/5", "age_recommendation": "16+"}
    ],
    "Western": [
        {"title": "The Good, the Bad and the Ugly", "rating": "5/5", "age_recommendation": "18+"},
        {"title": "Unforgiven", "rating": "4/5", "age_recommendation": "16+"},
        {"title": "Django Unchained", "rating": "5/5", "age_recommendation": "18+"},
        {"title": "True Grit", "rating": "3/5", "age_recommendation": "16+"},
        {"title": "The Magnificent Seven", "rating": "4/5", "age_recommendation": "13+"}
    ]
}

