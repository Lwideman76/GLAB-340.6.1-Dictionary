import json
from datetime import datetime

# Define an empty dictionary to store movies
movies = {}

# Function to add a new movie
def add_movie():
    title = input("Enter movie title: ")
    genre = input("Enter genre: ")
    director = input("Enter director: ")
    release_date_str = input("Enter release date (YYYY-MM-DD): ")
    release_date = datetime.strptime(release_date_str, "%Y-%m-%d").date()
    actors = input("Enter actors (comma-separated): ").split(",")
   
    movies[title] = {
        "genre": genre,
        "director": director,
        "release_date": release_date_str,
        "actors": actors
    }
    print("Movie added successfully!")

# Function to edit a movie
def edit_movie():
    title = input("Enter movie title to edit: ")
    if title in movies:
        print("Select field to edit:")
        print("1. Title")
        print("2. Genre")
        print("3. Director")
        print("4. Release Date")
        print("5. Actors")
        choice = input("Enter choice: ")

        if choice == "1":
            new_title = input("Enter new title: ")
            movies[new_title] = movies.pop(title)
        elif choice == "2":
            movies[title]["genre"] = input("Enter new genre: ")
        elif choice == "3":
            movies[title]["director"] = input("Enter new director: ")
        elif choice == "4":
            new_release_date_str = input("Enter new release date (YYYY-MM-DD): ")
            movies[title]["release_date"] = new_release_date_str
        elif choice == "5":
            new_actors = input("Enter new actors (comma-separated): ").split(",")
            movies[title]["actors"] = new_actors
        else:
            print("Invalid choice.")
    else:
        print("Movie not found.")

# Function to delete a movie
def delete_movie():
    title = input("Enter movie title to delete: ")
    if title in movies:
        del movies[title]
        print("Movie deleted successfully!")
    else:
        print("Movie not found.")

# Function to view all movies
def view_all_movies():
    for title, info in movies.items():
        print(f"Title: {title}")
        print(f"Genre: {info['genre']}")
        print(f"Director: {info['director']}")
        print(f"Release Date: {info['release_date']}")
        print(f"Actors: {', '.join(info['actors'])}")
        print()

# Function to search movies
def search_movies():
    criteria = input("Enter search criteria: ")
    found_movies = []
    for title, info in movies.items():
        if criteria.lower() in title.lower() or \
           any(criteria.lower() in str(value).lower() for value in info.values()):
            found_movies.append(title)
    if found_movies:
        print("Matching Movies:")
        for movie in found_movies:
            print(movie)
    else:
        print("No matching movies found.")

# Function to save the movie database to a file
def save_database(filename):
    with open(filename, "w") as file:
        json.dump(movies, file)
    print("Database saved successfully!")

# Function to load the movie database from a file
def load_database(filename):
    global movies
    try:
        with open(filename, "r") as file:
            movies = json.load(file)
        print("Database loaded successfully!")
    except FileNotFoundError:
        print("Database file not found.")

# Main program loop
if __name__ == "__main__":
    while True:
        print("\nMovie Database Management System")
        print("1. Add a new movie")
        print("2. Edit a movie")
        print("3. Delete a movie")
        print("4. View all movies")
        print("5. Search movies")
        print("6. Save database to file")
        print("7. Load database from file")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            edit_movie()
        elif choice == "3":
            delete_movie()
        elif choice == "4":
            view_all_movies()
        elif choice == "5":
            search_movies()
        elif choice == "6":
            save_database("movies.json")
        elif choice == "7":
            load_database("movies.json")
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")