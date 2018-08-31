import urllib.request
import time
import datetime
import random


def getreal_time_canteen(url):
    html_can = urllib.request.urlopen(url).read()
    print(html_can)
    return html_can

def getreal_time_lib(url):
    html_lib = urllib.request.urlopen(url).read()
    print(html_lib)
    return html_lib


while True:

    aurl = "http://192.168.35.131/real_time_canteen.csv"
    html_can = getreal_time_canteen(aurl)
    html_can_rows=str(html_can).split("\\n")
    can=html_can_rows[1]
    print(can)

    f = open("real_time_canteen.csv","a")
    f.write(can)
    f.write("\n")

    aurl = "http://192.168.35.133/real_time_library.csv"
    html_lib = getreal_time_lib(aurl)
    html_lib_rows=str(html_lib).split("\\n")
    lib=html_lib_rows[1]
    print(lib)

    f = open("real_time_library.csv","a")
    f.write(lib)
    f.write("\n")

    can1=can.split(",")
    canfu=can1[1]
    lib1=lib.split(",")
    libfu=lib1[1]

    now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f = open("real_time_else.csv","a")
    f.write(str(now)+","+str(200-int(canfu)-int(libfu)-random.randint(-5,5))+"\n")

    print("下载成功")
    time.sleep(10)
