# HomeWork 5
#
# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#      - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания
#      значений этого атрибута нужно использовать методы get и set
#
class Music:
    def __init__(self, name, artist, duration, genre, mood):
        self.name = name
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.__mood = mood

    def play(self):
        return 'playback'

    def stop(self):
        return 'stop'


class Instrumental(Music):
    pass


class Song(Music):
    pass


song_001 = Song()

music_001 = Instrumental()

# playlist_01

#
# 5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий
#
