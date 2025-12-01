# Use map to convert temperatures C → F

temp_c = [0, 23, 45, 51, 3, 2 , -1, -275]
def tem_c_to_f(temp_c):
    return (temp_c * 9/5) + 32

print(list(map(tem_c_to_f, temp_c)))