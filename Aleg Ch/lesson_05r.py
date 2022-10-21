# HomeWork 5
#
# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#      - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания
#      значений этого атрибута нужно использовать методы get и set
#
class Audio:
    def __init__(self, artist, name, duration):
        self.artist = artist
        self.name = name
        self.duration = duration

    def play(self):
        return 'playback'

    def stop(self):
        return 'stop'


class Music(Audio):
    def __init__(self, artist, name, duration, genre, year, mood):
        super().__init__(artist, name, duration)
        self.genre = genre
        self.year = year
        self.__mood = mood

    def get_mood(self):
        return f'mood of the {self.name} is {self.__mood}'

    def set_mood(self, new_mood):
        self.__mood = new_mood


song_001 = Music('The Beatles', 'Hey Jude', '7:05', 'pop rock', 1968, '7')
song_002 = Music('Nirvana', 'Smells Like Teen Spirit', '4:38', 'grunge', 1991, '3, 4, 5')
music_001 = Music('Mozart', 'Symphony No.40', '26:24', 'classic', 1788, '1, 2, 3, 4, 5, 6, 7, 8, 9')
music_002 = Music('Yann Tiersen', 'La valse d\'Amélie', '2:00', 'Valse musette', 2001, '2, 3')

print(song_001.get_mood())  # mood of the Hey Jude is 7
song_001.set_mood('7, 8, 9')
print(song_001.get_mood())  # mood of the Hey Jude is 7, 8, 9
print(music_002.play())  # playback

playlist_01 = [song_002, music_002, song_001]
for item in playlist_01:
    print(item.__dict__.values())
#
# dict_values(['Nirvana', 'Smells Like Teen Spirit', '4:38', 'grunge', 1991, '3, 4, 5'])
# dict_values(['Yann Tiersen', "La valse d'Amélie", '2:00', 'Valse musette', 2001, '2, 3'])
# dict_values(['The Beatles', 'Hey Jude', '7:05', 'pop rock', 1968, '7, 8, 9'])
#
# 5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий
# На Github при создании нового репозитория есть инструкции для 3-х случаев.
# Добавляем наш уже существующий локальный репозиторий на Github:
# git remote add origin git@github.com:Aleg-Ch/HW5.git
# git branch -M master
# git push -u origin master
#
