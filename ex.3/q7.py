class Time:
    hours = 00
    minutes = 00

    def __init__(self):
        self.hours = 2
        self.minutes = 42

    def addTime(self, time2):
        hrs = self.hours + time2.hours
        mins = self.minutes + time2.minutes
        if mins >= 60:
            hrs += mins//60
            mins = mins % 60
        print(hrs, mins)

    def displayTime(self):
        print(self.hours, self.minutes)

    def displayMinute(self):
        print(self.hours*60 + self.minutes)


tim1 = Time()
tim2 = Time()
tim1.displayTime()
tim2.displayMinute()
tim1.addTime(tim2)