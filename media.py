import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube_id, rating, release_date, critic_score, cast) :
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_id = trailer_youtube_id
        self.rating = rating
        self.release_date = release_date
        self.critic_score = critic_score
        self.cast = cast

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
