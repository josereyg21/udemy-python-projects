
def add_movie():
    title =input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    
    movies.append({
        'title' : title,
        'director' : director,
        'year' : year
    })

def show_movies():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Realease Year: {movie['year']}\n")

def findmovie():
    search_title = input("Enter the movie you want to find ")
    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)

user_option = {
    "a" : add_movie,
    "l" : show_movies,
    "f" : findmovie
}

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie bye title or 'q' to quit:  "
movies= []
selection = input(MENU_PROMPT)

while selection != "q":
    if selection in user_option:
        selected_function = user_option[selection]
        selected_function()
    else:
        print("Unknwon Command, Please Try Again")
    selection = input(MENU_PROMPT)


    
