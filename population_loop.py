import time
import random
import datemtime
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
random_list = [random.randint(0,200) for i in range (1)]
for a in random_list:
    print (a)
#if a in random_list:
    #import random
    #random_list = [random.randint(0,200) for i in range(1)]
    #for a in random_list:
        #print(a)

def getcurrenttime():
    return nowTime
def getcurrentpopulation():
    return random.randint(0,200)
def writetofile(time,population):
    f = open("real_time_canteen.csv","w")
    f.write("time,canteen\n")
    f.write(str(time)+","+str(population)+"\n")
    return

while True:
    currenttime = getcurrenttime()
    currentpopulation = getcurrentpopulation()
    writetofile(currenttime,currentpopulation)
    time.sleep(10)
    print("sleeping")
