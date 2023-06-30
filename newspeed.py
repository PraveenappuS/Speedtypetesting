from time import *
import random as r

def mistake(partest, usertest):
    e = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                e = e+1
        except:
            e = e+1
    return e

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

test = [" I own a small plot of land next to our house. I cultivate gardening there. Every day, I spend half an hour gardening."]
test1 = r.choice(test)
print("****** Typing Speed ******")
print(test1)
print()
print()
time_1 = time()
testinput = input("Enter : ")
time_2 = time()


print('Speed: ' ,speed_time(time_1, time_2, testinput),"w/sec")
print("Errors: ",  mistake(test1, testinput))