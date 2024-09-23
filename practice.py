names = ["Shehadi", "Ryan", "Ethan", "Quinn", "Eddie", "Jake"]
print(names)

# del name[0]
names.remove("Shehadi")
print(names)

#loop through the name

for name in names:
    print(f"{name} is on my table")
    
# Sort names
names.sort()
print(names)