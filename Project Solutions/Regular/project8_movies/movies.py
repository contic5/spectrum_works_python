#Using length for the movie length would be an ok idea, but it is too similar to len.

class Movie:
    def __init__(self, name,year,company,rating,critics,audience):
        self.name=name
        self.year=year
        self.company=company
        self.rating=rating
        self.critics=critics
        self.audience=audience
    def summarize(self):
        print(self.name,"is a movie by",self.company,"that came out in",self.year)
        print(self.name,"is rated",self.rating)
        print("Audiences gave this movie a",str(self.audience),"on Rotten Tomatoes")
        if(abs(self.critics-self.audience)<=5):
            print("Critics roughly had the same opinion on the movie as audiences.",end=" ")
        elif(self.critics-self.audience<-5):
            print("Critics liked the movie less than audiences.",end=" ")
        else:
            print("Critics liked the movie more than audiences.",end=" ")
        print("They gave the movie",self.critics,"on Rotten Tomatoes.")
        print()
#Universal praise
movie1=Movie("Spiderman: Into the Spiderverse",2018,"Sony","PG",97,93)
movie1.summarize()

#Critical praise
movie2=Movie("Black Widow",2021,"Marvel","PG-13",79,91)
movie2.summarize()

#Audience praise
movie3=Movie("Eternals",2021,"Marvel","PG-13",47,78)
movie3.summarize()
movie4=Movie("Venom",2018,"Sony","PG-13",30,81)
movie4.summarize()

#Universal dislike
movie5=Movie("Last Airbender",2010,"Nickelodeon","PG",5,30)
movie5.summarize()