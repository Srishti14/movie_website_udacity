import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy, Andy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://youtu.be/vwyZH85NQC4")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")
#avatar.show_trailer()

inside_out = media.Movie("Inside Out",
                         "Riley and her five core emotions, Fear, Anger, Joy, Disgust and Sadness, struggle to cope with her new life in San Francisco.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/0/0a/Inside_Out_%282015_film%29_poster.jpg/220px-Inside_Out_%282015_film%29_poster.jpg",
                         "https://youtu.be/1HFv47QHWJU")
#inside_out.show_trailer()

the_martian = media.Movie("The Martian",
                          "Stuggles of a man to keep himself alive on Mars with minimum resources, while other scientists work tirelessly to bring him home.",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_Martian_film_poster.jpg/220px-The_Martian_film_poster.jpg",
                          "https://youtu.be/ej3ioOneTy8")

school_of_rock = media.Movie("School Of Rock",
                             "Using rock music to learn.",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                             "https://youtu.be/LqEszt5wG9I")

big_hero_6 = media.Movie( "Big Hero 6",
                          "The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada,who team up with a group of friends to form a band of high-tech heroes..",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/Big_Hero_6_%28film%29_poster.jpg/220px-Big_Hero_6_%28film%29_poster.jpg",
                          "https://youtu.be/d2S8D_SCAJY")

frozen = media.Movie("Frozen","storyline",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Frozen_%282013_film%29_poster.jpg/220px-Frozen_%282013_film%29_poster.jpg",
                     "https://youtu.be/TbQm5doF_Uc")

mean_girls = media.Movie("Mean Girls","storyline of movie","https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/Mean_Girls_movie.jpg/220px-Mean_Girls_movie.jpg",
                          "https://youtu.be/KAOmTMCtGkI")

shawshank_r = media.Movie("Shawshank Redemption","storyline2","https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                          "https://youtu.be/6hB3S9bIaco")

the_prestige = media.Movie("The Prestige","nothing","https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Prestige_poster.jpg/220px-Prestige_poster.jpg",
                           "https://youtu.be/a1AqrIkD7vU")

logan = media.Movie("Logan","ggh","https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg","https://youtu.be/Div0iP65aZo")

zootopia = media.Movie("Zootopia","hush","https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg","https://youtu.be/jWM0ct-OLsM")



movies = [toy_story,avatar,inside_out,the_martian,school_of_rock,big_hero_6,frozen,mean_girls,shawshank_r,the_prestige,logan,zootopia]
fresh_tomatoes.open_movies_page(movies)
