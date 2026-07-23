movies = {"The Matrix": "10:00 AM", "Inception": "2:00 PM", "Interstellar": "6:00 PM"}
for value in movies:
    print(value)

movie_selected = input("Which movie do you want to watch? \n")
showtimes = movies.get(movie_selected)
if movie_selected not in movies:
    print("Requested movie is not available.")
    print(showtimes)
else:
    print("You selected", movie_selected, "which is playing at", movies[movie_selected])
