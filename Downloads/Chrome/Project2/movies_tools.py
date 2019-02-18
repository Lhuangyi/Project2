import csv

class Movie:
    def __init__(self,a_tuple):
        self.a_tuple = a_tuple

    def __str__(self):
        return "{} | {}".format(self.a_tuple[0], self.a_tuple[14])

if __name__ == "__main__":
    with open("movies_clean.csv","r", encoding = 'utf8') as f:
        reader = csv.reader(f)
        csv_list = list(reader)
        test_movie = Movie(csv_list[5])
        print(test_movie)
