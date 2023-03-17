ratingsSum = []
with open("ratings.csv", "r") as ratings:
    next(ratings)
    for row in ratings:
        rating = row.split(",")
        try:
            ratingsSum.append(float(rating[2]))
        except ValueError:
            print("Unable to convert string to float")

print(f"{sum(ratingsSum) / len(ratingsSum):.2f}")
