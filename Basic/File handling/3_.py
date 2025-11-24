# Write a program to append new text to an existing file
append_file = open("sample.txt", "a+")
append_file.write("\nLorem ipsum dolor sit amet consectetur adipisicing elit.\nVeniam hic atque nemo at quae, animi expedita neque! Pariatur dolore, fuga at magni omnis optio possimus sunt officiis ducimus?\nAccusantium optio perspiciatis sint?")
print("New text appended to the file successfully.")
append_file.seek(0)
data = append_file.read()
print(data)
append_file.close()
