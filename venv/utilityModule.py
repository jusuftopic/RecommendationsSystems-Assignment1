import unittest


class Statistics:


    def computeMeanRating(self, file_name):
        try:
            return self.calculate_avg_rating(file_name)
        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Error reading file.")

    def calculate_avg_rating(self, file_name):
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


class StatisticsTest(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics()

    def test_compute_mean_rating(self):
        mean = self.statistics.computeMeanRating("ratings.csv")
        self.assertAlmostEqual(mean, 3.5, places=2)

    def test_compute_mean_rating_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            self.statistics.computeMeanRating("nonexistent_file.csv")

    def test_compute_mean_rating_io_error(self):
        with self.assertRaises(IOError):
            self.statistics.computeMeanRating("/path/to/unreadable_file.csv")