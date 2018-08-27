import time

def get_history_data():
    f = open('', 'r')
    data = f.read()
    return(data)

def get_current_data():
    print("get now")
    return

def markovpredict():
    print
a = "y"
while a != "w":
    action = input("<")
    if action == "where to go":
        get_history_data()
        get_current_data()
        #print(suggestions)
    time.sleep(1)
