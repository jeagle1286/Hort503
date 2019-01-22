name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height * 2.54} centimeters tall.")
print(f"He's {weight / 2.20462} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height * 3.54 + weight / 2.20462
print(f"If I add {age}, {height * 2.54}, and {weight / 2.20462} I get {total}.")
