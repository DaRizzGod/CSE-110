min_opening = 999999999999
min_movie_data = []

with open('Harry-Potter.txt') as potter_file:
    potter_file.readline()
    for line in potter_file:
        line = line.strip()
        movie_data = line.split(',')
       
        # opening_weekend = float(movie_data[3])
        # if opening_weekend > max_opening:
        #     max_opening = opening_weekend
        #     max_movie_data = movie_data
            
        release_data = movie_data[5].split(' ')
        if release_data[0] == 'Nov':
            opening_weekend = float(movie_data[3])
            if opening_weekend < min_opening:
                min_movie_data = movie_data
                min_opening = opening_weekend
            
            
print(f'The movie released in November with the smallest opening weekend is')
print(f'{min_movie_data[0]} with ${min_opening:.2f}')
