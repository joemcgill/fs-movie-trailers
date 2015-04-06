import config
import media
import my_movie_list
import youtube_search

# Rotten Tomatoes API for Python
# docs: https://github.com/zachwill/rottentomatoes
from rottentomatoes import RT

# initialize a rotten tomatoes instance
rt = RT( config.api_key )

# get a list of movie openings from RT
opening_movies = rt.lists('movies', 'opening')

# iterate through opening movies and create instances of our Movie class for each
movie_collection = []
for mov in opening_movies['movies']:
    # Find youtube trailer
    options = youtube_search.Options( mov['title'] + ' trailer', 1 )
    trailer_id = youtube_search.search(options)

    # Convert cast names to a comma separated list
    cast = ''
    l = mov['abridged_cast'].__len__() - 1
    for i, actor in enumerate( mov['abridged_cast'] ):
        cast += actor['name']
        if i < l:
            cast += ', '

    movie = media.Movie(mov['title'], mov['synopsis'], mov['posters']['thumbnail'], trailer_id, mov['mpaa_rating'], mov['release_dates']['theater'], mov['ratings']['critics_score'], cast)
    movie_collection.append(movie)

# print movies
my_movie_list.open_movies_page( movie_collection )
