import fresh_tomatoes
import media

Avatar = media.Movie("Avatar | Official Trailer",
                        "The story Movie in box",
                        "3.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")


Avengers = media.Movie("Avengers | Official Trailer", "The story Movie in box",
                           "2.jpg",
                           "https://www.youtube.com/watch?v=6ZfuNTqbHE8")



Fast_Furious_8 = media.Movie("Fast & Furious 8", "The story Movie in box",
                          "1.jpg",
                          "https://www.youtube.com/watch?v=NxhEZG0k9_w")


movies = [Avatar,Avengers, Fast_Furious_8]
fresh_tomatoes.open_movies_page(movies)
