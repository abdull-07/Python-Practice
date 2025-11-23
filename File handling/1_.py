# Write a program to read a text file and count the number of lines.
open_file = open("sample.txt", "r")
line_count = 0
for line in open_file:
    line_count += 1
open_file.close()
print("Number of lines in the file:", line_count)