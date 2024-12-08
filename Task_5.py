# Your solution comes here
cars=int(input('enter the number of cars'))
a='no'
total=0
speed=0
average=0 
for x in range  (cars) :
    speed=int(input('enter cars speed'))
    total=total+speed
    if speed > 60:
        a='yes'
average=total/cars 
roundaverage=(round(average,1))
print(roundaverage)
print(a)