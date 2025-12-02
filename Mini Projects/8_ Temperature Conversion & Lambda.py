# Problem 6 — Temperature Conversion & Lambda
# Ask the user to input 5 temperatures with their units (C or F).
# Convert them all to the other unit using lambda + map().
# Print temperatures above 100°F or above 37.8°C.
# Bonus: Store results in a dictionary where key = original temp, value = converted temp.

temperature = []
for t in range(5):
    temp = input("Enter Temperature with theri unit: ")
    temperature.append(temp.strip())


temperature.sort()
print(temperature)

clean_data = []
for i in temperature:
    item = i.replace(" ","")
    value = float(i[:-1])
    unit = i[-1].upper()
    clean_data.append((value, unit))
print(clean_data)

c_to_f = lambda c : (c * 9/5) + 32
f_to_c = lambda f : (f - 32) * 5/9

cont_temp = list(
    map(
        lambda x: (x[0], x[1], c_to_f(x[0]) if x[1] == "C" else f_to_c(x[0])),
        clean_data
    )
)

final_dit = {}
for og, unit, value in cont_temp:
    final_dit[f"{og} {unit}"] = value
    
print("\nTemperatures above limit:")
for orig, unit, conv in cont_temp:
    if (unit == "F" and orig > 100) or (unit == "C" and orig > 37.8) or (unit == "C" and conv > 100) or (unit == "F" and conv > 37.8):
        print(f"{orig} {unit} -> {conv}")


print("\nOriginal → Converted dictionary:")
print(final_dit)