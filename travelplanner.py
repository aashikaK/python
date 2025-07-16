# trip=(source, destination,price)
trip1=("Kathmandu","Lumbini",2000)
trip2=("Gaighat","Illam",2500)
trip3=("Jhapa","Pokhara",4500)
trip4 = ("Pokhara", "Chitwan", 1500)

# update price of trip1
trip1=tuple(list(trip1)[:2]+[2500])

# put all the trips in single tuple
all_trips=(trip1, trip2, trip3, trip4)
 
#  unpack and print details
for trips in all_trips:
    (start, destination, price) = trips
    print(f"Trip: {start} -> {destination} costs Rs. {price}")

# add new trips
new_trips=(
     ("Chitwan", "Biratnagar", 2200),
    ("Pokhara", "Mustang", 4000)
)

all_trips= all_trips + new_trips

print("/n Updated trips")
for trips in all_trips:
    print(trips)

# count trips starting from Kathmandu 
count=0
for trips in all_trips:
    if trips[0]== "Kathmandu":
        count+=1
print(f"\nTrips starting from Kathmandu: {count}")

# count trips starting from Pokhara
count=0
for trips in all_trips:
    if trips[0]== "Pokhara":
        count+=1
print(f"\nTrips starting from Pokhara: {count}")

# find indexof trip
index_of_trip=all_trips.index(trip2)
print(f"Trip2 is at index: {index_of_trip}")