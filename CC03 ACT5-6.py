# The List Below All The Colors in Rainbow:
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
print("\nThe List Below All The Colors in Rainbow:")
print(colors)

colors.insert(0, "Teal")
colors.insert(colors.index("Orange") + 1, "Pink")
#Added New Colors in the list
print("\nAdded New Colors in the list:")
print(colors)
#Added New Colors in the list Again
colors.append("Pink")
colors.append("Brown")
print("\nAdded New Colors in the list Again:")
print(colors)
#Remove another Color in the list 
if "Indigo" in colors:
    colors.remove("Indigo")
print("\nRemove another Color in the list :")
print(colors)
#Remove another Color in the list 
if "Brown" in colors:
    colors.remove("Brown")
print("\nRemove another Color in the list :")
print(colors)
#Arrange The Color Names To The List Alphabetically and Its Length
sorted_colors = sorted(colors)
print("\nArrange The Color Names To The List Alphabetically and Its Length:")
print(sorted_colors, "-", len(sorted_colors))


duplicates = {color: colors.count(color) for color in set(colors) if colors.count(color) > 1}

#Colors that are Duplicated and the Number of Times They Repeat
print("\nColors that are Duplicated and the Number of Times They Repeat:")
for color, count in duplicates.items():
    print(f'["{color.lower()}"] - {count}')