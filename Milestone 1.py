def movies_a():
    movies.append({
        'title': input('Title '),
        'director': input('Director '),
        'year': input('Year ')
        })


def movies_l():
    
    print('Title     Director     Year')
    for i in movies:
        title, director, year = i['title'], i['director'], i['year']
        print(f'{title}     {director}     {year} ')



    
def movies_f():
    x = input('What movie are you looking for? You can look by Name, Director or Year  ')
    for i in range(len(movies)):
        if x == movies[i]['title'] or x == movies[i]['director'] or x == movies[i]['year']:
            title, director, year = movies[i]['title'], movies[i]['director'], movies[i]['year']
            print(f'{title}     {director}     {year} ')
        
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

while True:
    main_input = input(MENU_PROMPT)
    if main_input == "a":
        movies_a()
    elif main_input == "l":
        movies_l()
    elif main_input == "f":
        movies_f()
    elif main_input == "q":
        break
    else:
        print('Unknown command. Please try again.')
