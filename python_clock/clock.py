#Dan Wright

#First, we'll use the new self method to access information within our tick class.


class Clock:
    #A first method, not a function.
    def __init__(self, the_hr, the_min, the_sec):
        self.hr = the_hr
        self.min = the_min
        self.sec = the_sec
        #This is how we initialize hr to do what we want inside the method.

    def __str__(self):
        return "{0:02d}: {1:02d}: {2:02d}".format(self.hr, self.min, self.sec)

    def tick(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1

        if self.min == 60:
            self.min = 0
            self.hr += 1

        # This above if statement makes it so that
        # a minute equals sixty seconds.
        
