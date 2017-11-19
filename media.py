import webbrowser

class Movie():
	"""This class provides a way to store movie related information"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, writer, release_date):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.screenwriter = writer 
		self.launch_date = release_date


#self = avatar
#movie_title = "Avatar"
#movie_storyline = "A marine on an alien planet"
#poster_image = "the URL"
#trailer_youtube = "youtube url"
#screenwriter = "writer"
#launch_date = "release_date"

#two instances of class Movie ... toy story and avatar



	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

#Add extra information about your favorite movies (screenwriter, launch date, etc.) 
#and modify fresh_tomatoes.py to show it on your web page.