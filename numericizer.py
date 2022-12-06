import pandas as pd
turning_points = [100000, 1000000, 5000000, 10000000, 20000000, 50000000, 100000000, 160000000, 240000000, 300000000]

def getGrossLabel(g):
    for i, tp in enumerate(turning_points):
        if g < tp:
            return i
    return len(turning_points)

df = pd.read_csv('boxoffice_with_synopsis_discretize.csv')

df['gross_label'] = df['domestic_gross'].map(getGrossLabel)
genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western']
def isGenre(i, genres):
    if genres == "['-']":
        return 0
    genresArr = map(int, genres[1:-1].split(", "))
    return i in genresArr

for i in range(len(genres)):
    df[''.join(['is', genres[i]])] = df['genres_enum'].map(lambda x: isGenre(i, x))
df.to_csv('box_office_with_gross_labels.csv')
for i in range(len(turning_points)):
    print('< $' + str(turning_points[i]) + ":", len(df[df['gross_label'] == i]))
print('> $' + str(turning_points[-1]) + ":", len(df[df['gross_label'] == len(turning_points)]))