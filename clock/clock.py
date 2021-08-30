class Clock:
    
    MIN_IN_DAY = 24 * 60

    def __init__(self, hour, minute):
        self.hour, self.minute = divmod((hour * 60 + minute) % self.MIN_IN_DAY , 60)

    def __repr__(self):
        return "{:02d}:{:02d}".format(self.hour, self.minute)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour,self.minute + minutes) # instead of __class__()

    def __sub__(self, minutes):
        return self.__add__(-minutes)
