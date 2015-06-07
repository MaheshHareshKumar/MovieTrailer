import webbrowser
class Movie():
    """This is documetation for media file"""
    #MOVIE_RATING = ["A","B","C"]
    #Intialization of instance
    def __init__(self, movie_title,movie_story_line,poster_image, trailer_youtube,actor,releasedate):
        self.title = movie_title
        self.storyline = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.actor = actor
        self.releasedate = releasedate 
    #Calling youtube url by click of image
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
