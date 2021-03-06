from song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)
    new_song.set_title(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song


  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    curr_song = self.__first_song
    index = 0
    if self.length() is None:
      return -1
    else:
      while curr_song:
        if curr_song.get_title() == title:
          return index
        else:
          index += 1
          curr_song = curr_song.get_next_song()
      return -1


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    curr_song = self.__first_song

    if curr_song.get_title() == title: 
      self.__first_song = curr_song.get_next_song()
      return print(f'Deleted {title} from Playlist')

    else: 
      while curr_song.get_title() != title:
        if curr_song.get_next_song().get_title() == title: 
          curr_song.set_next_song(curr_song.get_next_song())
          return print(f'Deleted {title} from Playlist')
        else: 
          curr_song = curr_song.get_next_song()



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    index = 0
    curr_song = self.__first_song

    while curr_song != None:
      index += 1
      curr_song = curr_song.get_next_song()
      
    return index


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    index = 1
    curr_song = self.__first_song

    if curr_song == None:
      print(f"No songs foound in Playlist. Please add some")
      return None

    while curr_song:
      print(f"{index}. {curr_song.get_title()}")
      index += 1
      curr_song = curr_song.get_next_song()
