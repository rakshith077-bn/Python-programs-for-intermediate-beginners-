class Time:

    def __init__(self, h = 0, m = 0, s = 0):
        self.hour=h
        self.min=m
        self.sec=s

    def time_to_int(self):
        minute=self.hour*60+self.min
        seconds=minute*60+self.sec
        return seconds

    def int_to_time(self, seconds):
        t=Time()
        minutes, t.sec=divmod(seconds,60)
        t.hour, t.min=divmod(minutes,60)
        return t

    def __str__(self):
        return "%.2d:%.2d:%.2d"%(self.hour,self.min,self.sec)

    def __eq__(self,t):
        return self.hour==t.hour and self.min==t.min and self.sec==t.sec

    def __add__(self,t):
        if isinstance(t, Time):
            return self.addTime(t)
        else:
            return self.increment(t)

    def addTime(self, t):
        seconds=self.time_to_int()+t.time_to_int()
        return self.int_to_time(seconds)

    def increment(self, seconds): seconds += self.time_to_int()
        return self.int_to_time(seconds)

    def __radd__(self,t):
        return self.__add__(t)

T1 = Time(3,40)
T2 = Time(5,45)
print("T1 is:",T1)
print("T2 is:",T2)
print("Is T1 same as T2??" ,T1 == T2)
T3=T1+T2

print("Sum of T1 and T2 is given by ",T3)
T4=T1+75
print("Sum of T5 + 75 is given as " ,T4)

T5=130+T1
print("Sum of 130 + T1 is given as ",T5)

T6=sum([T1,T2,T3,T4])
print("Using sum([T1,T2,T3,T4]): ",T6)
