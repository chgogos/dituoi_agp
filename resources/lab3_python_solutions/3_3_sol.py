import csv

# Φόρτωση του αρχείου με τις αξιολογήσεις
movies = {}
with open("ml-100k/u.data") as f:
    csv_reader = csv.reader(f, delimiter="\t")
    for row in csv_reader:
        user, movie_id, rating, timestamp = row
        rating = int(rating)
        if movie_id not in movies:
            movies[movie_id] = [rating]
        else:
            movies[movie_id].append(rating)
print(f"Πλήθος ταινιών = {len(movies)}")


# Διαγραφή ταινιών με λιγότερες από 50 αξιολογήσεις
movies_to_be_deleted = []
for movie in movies:
    if len(movies[movie]) < 50:
        movies_to_be_deleted.append(movie)

for movie in movies_to_be_deleted:
    del movies[movie]
print(f"Πλήθος ταινιών με τουλάχιστον 50 αξιολογήσεις = {len(movies)}")

# Μέση βαθμολογία ταινιών, ταξινόμηση, εμφάνιση 10 πρώτων
movie_avg_rating = []
for movie in movies:
    movie_avg_rating.append((movie, sum(movies[movie]) / len(movies[movie])))

movie_avg_rating.sort(key=lambda x: x[1], reverse=True)

# Φόρτωση του αρχείου με τους τίτλους ταινιών
titles = {}
with open("ml-100k/u.item") as f:
    csv_reader = csv.reader(f, delimiter="|")
    for row in csv_reader:
        movie_id, title = row[0], row[1]
        titles[movie_id] = title

for i in range(10):
    movie_id = movie_avg_rating[i][0]
    print(f"{titles[movie_id]:60} {movie_avg_rating[i][1]:.4f}")
