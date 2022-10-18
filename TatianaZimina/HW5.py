class Devices:
    def __init__(self, name, screen_resolution, volume):
        self.name = name
        self.screen_resolution = screen_resolution
        self.__volume = volume

    def get_volume(self):
        if self.__volume >20:
            print("Too loud")

    def set_volume(self):
        if self.__volume > 50:
            self.__volume = 20
        return self.__volume


class TV(Devices):
    def __init__(self, name, screen_resolution, volume, smthelse):
        super().__init__(name, screen_resolution, volume)
        self.smthelse = smthelse

    def find_control(self):
        print('smb find control for me')


class Phone(Devices):
    def __init__(self, name, screen_resolution, volume):
        super().__init__(name, screen_resolution, volume)

    def call(self):
        print('Call me')

TV1 = TV('tv', 100, 51, 11111)
TV1.find_control()
print(TV1.__dict__)
TV1.get_volume()
TV1.set_volume()
print(TV1.__dict__)


iphone = Phone('iphone', "15'", 50)
iphone.call()
print(iphone.__dict__)
