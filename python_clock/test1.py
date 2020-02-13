from clock import Clock

c1 = Clock(4, 7, 3)
print(c1)
print(c1.hr, c1.min, c1.sec)
c1.tick( )
print(c1)

c2 = Clock(4, 7, 59)
c2.tick( )
print(c2)

c3 = Clock(4, 59, 59)
c3.tick( )
print(c3)

c4 = Clock(23, 59, 59)
c4.tick( )
print(c4)
