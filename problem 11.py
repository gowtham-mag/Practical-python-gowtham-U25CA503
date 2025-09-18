input_file = open("input.txt","r")
output_file = open("odd_lines.txt", "w")


line_no = 1
for line in input_file:
    if line_no % 2 == 1:
        output_file.write(line)
        print("completed")
    line_no += 1

input_file.close()
output_file.close()
