import random

def switch_door(pick,goat):
    x = [1,2,3]
    x.remove(pick)
    x.remove(goat)
    return x[0]
stayed = []
switched = []
for i in range(10000):
    doors = [1,2,3]
    car_door  = random.choice(doors)
    pick_door = random.choice(doors)
    doors.remove(car_door)
    if pick_door in doors:
        doors.remove(pick_door)
    if car_door == 1:
        goat_door = random.choice(doors)
        if switch_door(pick_door,goat_door) == car_door:
            switched.append(1)
        else:
            switched.append(0)
        
    elif car_door == 2:
        goat_door = random.choice(doors)
        if switch_door(pick_door,goat_door) == car_door:
            switched.append(1)
        else:
            switched.append(0)
    else:
        goat_door = random.choice(doors)
        if switch_door(pick_door,goat_door) == car_door:
            switched.append(1)
        else:
            switched.append(0)
            
    if car_door == pick_door:
        stayed.append(1)
    else:
        stayed.append(0)
#print(stayed,"\n",switched)
print("Switched average ",sum(switched)/len(switched))
print("Stayed   average ",sum(stayed)/len(stayed))
