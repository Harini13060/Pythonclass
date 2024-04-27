class songs():
  def amma_song(self,song1,song2):
    self.songs1=song1
    self.songs2=song2
    print("Song1",self.songs1)
    print("Song2",self.songs2)
  def appa_song(self):
    print("Appa Song")
class movie(songs):
  print("Movie")
class cartoon(songs):
  def doraemon(self,episode1,episode2):
    self.epi1=episode1
    self.epi2=episode2
    print(self.epi1,self.epi2)
shinchan=cartoon()
shinchan.doraemon("Episode1","Episode2")
shinchan.amma_song("Song1","Song2")
shinchan.appa_song()