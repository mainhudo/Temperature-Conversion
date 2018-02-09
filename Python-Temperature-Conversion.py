## FILENAME.PY
## Mai Nhu Do    mdo@temple.edu 
## 20/09/2017
## Lab 1 CIS1051 Fall 2017

##
## Temperature Conversion
##   Convert Fahrenheit degrees to Celsius based on user input

temperature = float(input())
print("Enter temperature: ")
c = (temperature - 32)*5/9
round(c,1)
print("The temperature is %.1f" % c )
if temperature <70:
    print("Too cold")
    import datetime as dt
    print(dt.datetime.now ())

elif temperature >=70 and temperature <80:
    print("Just right")
    import datetime as dt
    print(dt.datetime.now ())

else:
    print("Too hot")
    import datetime as dt
    print(dt.datetime.now ())



