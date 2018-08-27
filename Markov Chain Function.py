f = open(" library_metadata.csv","r")
library = f.read()
split_library = library.split ("\n")
library_data = []
for each in split_library:
    library_data.append(each.split(","))

f = open("canteen_metadata.csv","r")
canteen = f.read()
split_canteen = canteen.split("\n")
canteen_data = []
for each in split canteen:
    canteen_data.append(each.split(","))

f = open("gym_matadata.csv","r")
gym = f.read()
split_gym = gym.split("\n")
gym_datra = []
for each in split gym:
    gym_data.append(each.split(","))

def function_name(Markov_Perdict):
