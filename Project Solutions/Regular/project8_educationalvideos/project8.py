class Video:
    def __init__(self,name,url,year,topic) -> None:
        self.name=name
        self.url=url
        self.year=year
        self.topic=topic
    def printinfo(self):
        print(self.name)
        print("URL:",self.url)
        print("Topic:",self.topic)
        pass

videos=[]
videos.append(Video("How to Improve Communication Skills at Work [FOR WORKPLACE SUCCESS]","https://youtu.be/knUEdy-kOIQ",2019,"Workplace Communication"))
videos.append(Video("Public Speaking For Beginners","https://youtu.be/i5mYphUoOCs",2018,"Public Speaking"))
videos.append(Video("Self Advocacy Skills - Self Advocacy Strategies","https://youtu.be/74G_Zpz-7Bk",2019,"Self Advocacy"))
videos.append(Video("Tips for Effective Time Management","https://youtu.be/RiI1NkaDXlQ",2018,"Time Management"))
videos.append(Video("The Basics of MLA In-text Citations | Scribbr","https://youtu.be/ypWxhhpGeyM",2020,"Citations"))

for video in videos:
    video.printinfo()
    print()