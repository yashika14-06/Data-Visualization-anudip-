# time conversion of seconds into hours , minutes , seconds

# logic
# for ex : 7340
# 7340/3600 ---- as the output it will give hours 
# rem = 7340%3600 ---- it will give remainder in seconds now we will convert those seconds into min,sec
# rem/60 --- minutes
# rem%60 --- seconds
secs = int(input("enter the time in seconds"))
# 7340
if(secs < 0):
    print("invalid input")
else:
    if(secs < 60):
        print("00:00:",secs)
    elif(secs < 3600):
        mins = (secs%3600)/60
        # secs_2 is to store the remainder of secs and then we wil divide the remainder by 60 
        secs_2 = (secs%3600)
        secs_3 = secs_2%60
        print("00hr:",int(mins),"min:",secs_3,"sec")
    else:
        hours = secs/3600
        mins = (secs%3600)/60
        # secs_2 is to store the remainder of secs and then we wil divide the remainder by 60 
        secs_2 = (secs%3600)
        secs_3 = secs_2%60
        print(int(hours),":",int(mins),":",secs_3)



# print(int(hours))
# mins = (secs%3600)/60
# print(int(mins))
# secs_2 = (secs%3600)
# secs_3 = secs_2%60
# print(secs_3)