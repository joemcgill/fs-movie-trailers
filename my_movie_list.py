import webbrowser
import os
import re
import json

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title></title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css">
    <!-- Project Styles -->
    <link rel="stylesheet" href="css/styles.css">
    <link href='http://fonts.googleapis.com/css?family=Oswald:400,700' rel='stylesheet' type='text/css'>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="theatre" id="theater">

    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Movie Openings</a>
          </div>
        </div>
      </div>
    </div>

    <div class="container movies-wrap">
    </div>

    <!-- Backbone Templates -->

    <script id="tmpl-movie" type="text/template">
        <div class="movie-tile" >
            <figure class="movie-fig">
                <img class="movie-thumb" src="<%= poster_image_url %>">
            </figure>
            <div class="movie-body">
                <h3 class="movie-heading"><%= title %></h3>
                <p class="movie-meta">
                    <span class="movie-rating"><strong>Rated:</strong> <%= rating %></span>
                    <span class="movie-date"><strong>Release:</strong> <%= release_date %></span>
                </p>
            </div>
        </div>
    </script>

    <script id="tmpl-movie-details" type="text/template">
        <div class="container">
            <button class="close">Close</button>
            <div class="movie-trailer">
                <img src="http://placehold.it/600x300&text=<%= trailer_youtube_url %>">
            </div>
            <div class="movie-details">
                <h2 class="movie-heading"><%= title %></h2>
                <p class="movie-desc"><%= storyline %></p>
                <div class="meta">
                    <p class="cast"><strong>Cast:</strong> <%= cast %></p>
                    <p>
                        <span class="movie-rating"><strong>Rating:<strong> <%= rating %></span>
                        <span class="movie-release"><strong>Release Date:<strong> <%= release_date %></span>
                        <span class="movie-critic-score"><strong>Critic Score:<strong> <%= critic_score %></span>
                    </p>
                </div>
            </div>
        </div>
    </script>

    <!-- / Backbone Templates -->

    <!-- Include external JS files -->
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    <script src="http://underscorejs.org/underscore-min.js"></script>
    <script src="http://backbonejs.org/backbone-min.js"></script>
    <script src="js/movies.js"></script>
    <script src="js/script.js"></script>
    <script type="text/javascript">
        var movies = {movie_tiles};

        // start the app
        new Movies.MovieList( movies );
    </script>
  </body>
</html>
'''

def open_movies_page( movie_collection ):
    # Create or overwrite the output file
    output_file = open('movie-list.html', 'w')

    movies = ''
    for movie in movie_collection:
        movies += ( json.dumps( movie.__dict__ ) + ', ' )
    movies = '[' + movies + ']'

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    # rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))
    rendered_content = main_page_content.format( movie_tiles=movies )


    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
