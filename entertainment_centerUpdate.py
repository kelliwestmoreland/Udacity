import fresh_tomatoes2
import media 
#add in arguments for media file to read after media.Movie
justice_league = media.Movie("Justice League", 
						"American superhero film based on the DC Comics superhero team of the same name", 
						"https://upload.wikimedia.org/wikipedia/en/thumb/3/31/Justice_League_film_poster.jpg/220px-Justice_League_film_poster.jpg",
						"https://www.youtube.com/watch?v=r9-DM9uBtVI",
						"Chris Terrio and Zack Snyder", 
						"November 17, 2017")
#print(justice_league.storyline)

#print(avatar.storyline)
#avatar.show_trailer()
wonder_woman = media.Movie("Wonder Woman", 
				"Before she was Wonder Woman (Gal Gadot), she was Diana, princess of the Amazons, trained to be an unconquerable warrior.",
					"https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
					"https://www.youtube.com/watch?v=VSB4wGIdDwo",
					"Zack Synder, Allen Heinberg, and Jason Fuchs",
					"June 2, 2017")

thor = media.Movie("Thor: Ragnarok", 
							"American superheo film based on the Marvel Comics character, Thor", 
							"https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
							"https://www.youtube.com/watch?v=H84al-zYhq8",
							"Craig Kyle and Christopher Yost",
							"November 3, 2017")
star_wars = media.Movie("Star Wars: The Last Jedi", 
						"Upcoming American epic space opera film", 
						  "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
						  "https://www.youtube.com/watch?v=Q0CbN8sfihY",
						  "Rian Johnson",
						  "coming December 20, 2019")

movies = [justice_league, wonder_woman, thor, star_wars]
fresh_tomatoes2.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__module__)