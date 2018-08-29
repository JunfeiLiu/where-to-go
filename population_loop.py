import time
import random
random_list = [random.randint(0,200) for i in range (1)]
for a in random_list:
    print (a)
#if a in random_list:
    #import random
    #random_list = [random.randint(0,200) for i in range(1)]
    #for a in random_list:
        #print(a)

def getcurrenttime():
    return "2018/8/29 14:24:00"
def getcurrentpopulation():
    return "30"
def writetofile(time,population):
    f = open("real_time_cateen.csv","w")
    f.write("time,catten\n")
    f.write(time+","+population+"\n")
    return

while True:
    currenttime = getcurrenttime()
    currentpopulation = getcurrentpopulation()
    writetofile(currenttime,currentpopulation)
    time.sleep(10)
    print("sleeping")
