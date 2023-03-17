def computeMeanRating(file_name):
    try:
        return calculate_avg_rating(file_name)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading file.")


def calculate_avg_rating(file_name):
    ratings_sum = []
    with open(file_name, "r") as ratings:
        next(ratings)
        for row in ratings:
            rating = row.split(",")
            try:
                ratings_sum.append(float(rating[2]))
            except ValueError:
                print("Unable to convert string to float")

        return round(sum(ratings_sum) / len(ratings_sum), 2)


print(computeMeanRating("ratings.csv"))
