import urllib.request

def getpopulation(url):
    html = urllib.request.urlopen(url).read()
    print(html)
    return html

aurl = "http://192.168.35.130/population.csv"
html = getpopulation(aurl)
print(html)

f = open("real_time_cateen.csv","wb")
f.write(html)

print("下载成功")
