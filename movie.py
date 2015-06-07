import media
import fresh_tomatoes

# firt instance varibles of the movies created and then they will be assigned to movies array
ddlj = media.Movie("DDLJ","Storyline","http://upload.wikimedia.org/wikipedia/en/8/80/Dilwale_Dulhania_Le_Jayenge_poster.jpg","https://www.youtube.com/watch?v=c25GKl5VNeY","Sharukh Khan , Kajol","20 Oct 1995")
rockstar = media.Movie("Rockstar","Storyline","http://upload.wikimedia.org/wikipedia/en/6/68/Rockstar-Movie-Poster.jpg","https://www.youtube.com/watch?v=X3y6xksjre4","Ranbir Kapoor , Nargis Fakhri","11 Nov 2011")
znmd = media.Movie("Zindagi Na Milegi Dobara","Storyline","http://upload.wikimedia.org/wikipedia/en/3/3d/Zindaginamilegidobara.jpg","https://www.youtube.com/watch?v=GFIZzoJ2QeY","Hrithik Roshan, Katrina Kaif","13 Feb 2014")

movies = [ddlj,rockstar,znmd]
#Calling fresh tomatoes create movie page functionality
fresh_tomatoes.open_movies_page(movies)
