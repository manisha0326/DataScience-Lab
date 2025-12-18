user_input = input("Enter movies and ratings: ")
items = user_input.split(",")
movies = []

for item in items:
    name, rating = item.split("-")
    movies.append((name, float(rating)))

total = 0
for m in movies:
    total += m[1]

avg = total / len(movies)
print("Average rating:", avg)

highest = movies[0]
for m in movies:
    if m[1] > highest[1]:
        highest = m

print("Highest rated movie:", highest[0])

above = []
below = []

for m in movies:
    if m[1] > avg:
        above.append(m[0])
    elif m[1] < avg:
        below.append(m[0])

print("Movies above average:", above)
print("Movies below average:", below)




# movies = [] 

# n = int(input("How many movies do you want to enter? "))

# for i in range(n):
#     name = input(f"Enter movie {i+1} name: ")
#     rating = float(input(f"Enter rating for {name}: "))
#     movies.append((name, rating))

# total = 0
# for movie in movies:
#     total += movie[1]

# average = total / len(movies)
# print("\nAverage rating:", average)

# highest = movies[0]
# for movie in movies:
#     if movie[1] > highest[1]:
#         highest = movie

# print("Highest-rated movie:", highest[0], "-", highest[1])

# print("\nMovies with rating above average:")
# for movie in movies:
#     if movie[1] > average:
#         print(movie[0], "-", movie[1])

