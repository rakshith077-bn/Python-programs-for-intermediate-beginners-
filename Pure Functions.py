class time:

    def printTime(t):
        print("%.2d:%.2d:%.2d"(t.hour, t.minute, t.second))

    def add_time(t1, t2):

        sum = Time()
        sum.hour = t1.hour + t2.hour
        sum.minute = t1.minute + t2.minute
        sum.second = t1.second + t2.second

        if sum.second >= 60:
            sum.second -= 60
            sum.minute += 1

        if sum.minute >= 60:
            sum.minute -= 60
            sum.hour += 1
            return sum

        t1=Time()
        t1.hour=10
        t1.minute=34
        t1.second=25
        print("Time 1 is:")
        printTime(t1)
        t2=Time()
        t2.hour=2
        t2.minute=12
        t2.second=41
        print("Time 2 is :")
        printTime(t2)
        t3=add_time(t1,t2)
        print("After adding two time objectswe get: ")
        printTime(t3)
