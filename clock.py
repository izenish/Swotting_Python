# a=1
# b=1
# while(a!=0):
#     # print(a)
    
#     print("\n")
#     a=a+1s testing wheter its fast 
#     if (a%60==0):
#         print(b)
#         b=b+1


import time
# import simpleaudio
# from playsound import playsound
# from goto import goto,comefrom,label


def countdown(t):
    while t:
        sound=1
        min=t//60
        sec=t%60
        timer='{:02d}:{:02d}'.format(min,sec)
        print(timer,end="\r")
        time.sleep(1)
        t-=1
        
    print("BlastOff!")
    # playsound('alert.mp3')
# t=input("enter the time in seconds:")
print("----------------------------------------------------")
print("\n Set Timer in:")
print("\n (1) Seconds")
print("\n (2) Minutes")
print("\n (3) Hours")
print("----------------------------------------------------")
x=input("Select Option: ")
if x=='1':
    t=input("enter the time in seconds: ")
    countdown(int(t))
elif x=='2':
    y=input("Enter the time in minutes: ")
    t=int(y)*60
    countdown(int(t))
elif x=='3':
    y=input("Enter the time in hours: ")
    t=int(y)*60*60
    countdown(int(t))   
else:
    print("Wrong Option try again!")
   