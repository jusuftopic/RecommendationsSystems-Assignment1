import csv
import itertools


def print_movies_information():
    with open("movies.csv", "r", encoding="utf8") as movies_csv:
        movies = csv.reader(movies_csv)
        next(movies)
        movies1, movies2 = itertools.tee(movies)
        genres = get_movie_genres(movies1)
        print("Genres:")
        print(genres)
        movies_per_genre_count = get_count_movies_per_genre(movies2, genres)
        print("Movies per genre:")
        print(movies_per_genre_count)
        print("Most popular genre:")
        print(next(iter(movies_per_genre_count.items())))


def get_movie_genres(movies):
    genres_set = set()
    for genre in get_genres_row(movies):
        if "|" in genre:
            genres_set.update(genre.split("|"))
        else:
            genres_set.add(genre)

    return genres_set


def get_count_movies_per_genre(movies, genres):
    movies_per_genre_dict = {}
    genres_row = get_genres_row(movies)
    for genre in genres:
        movies_count = len([genre_row for genre_row in genres_row if genre in genre_row])
        movies_per_genre_dict[genre] = movies_count

    return dict(sorted(movies_per_genre_dict.items(), key=lambda item: item[1], reverse=True))


def get_genres_row(movies):
    movie_row = map(lambda r: r[len(r) - 1], movies)
    return list(genres for genres in movie_row if "(no genres listed)" not in genres)


print_movies_information()