import fresh_tomatoes
import media

wonder_woman = media.Movie("Wonder Woman",
                           "A story of a warrior princess",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://youtu.be/VSB4wGIdDwo")
print(wonder_woman.storyline)

justice_league = media.Movie("Justice League",
                             "The story of legends",
                             "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",
                             "https://youtu.be/RWCQ22JyCL4")
print(justice_league.storyline)
wonder_woman.show_trailer()
justice_league.show_trailer()

movies = [wonder_woman, justice_league]
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
fresh_tomatoes.open_movies_page(movies)
