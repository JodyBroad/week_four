# slurps the entire contents of the file in, in read mode
infile = open('pelican.txt', 'r')
# checks the file type and assigns to the variable filetype
filetype = type(infile)
# _io.TextIOWrapper is the file type
print("File type is : ", filetype, "\n")
# this is not printing the contents of the file, just its metadata
# print(infile)
# .read will read and print the entire thing in one go
print("If we print the whole thing in one go: \n \n", infile.read())

# create a list of the individual lines
limerick_list = open('pelican.txt').readlines()
print("Printing the limerick as a list: \n", limerick_list, "\n")
# calculate how many lines there are
limerick_length = len(limerick_list)
print("The length of the limerick is: ", limerick_length, "lines \n ")

# a loop to print line by line using the file object iterator, end="" removes blank lines
print("Using a loop we can print line by line: \n")
for line in open('pelican.txt'):
    print(line, end="")

# close the file once we are done
infile.close()