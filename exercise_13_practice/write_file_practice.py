# opening the file, using 'a' will append, 'w' will overwrite
file_handler = open('pelican.txt', 'w')
# will write the first line, \n gives new line
file_handler.write("A wonderful bird is the pelican,\n")
# will write the second line
file_handler.write("His bill holds more than his belican, \n")
# specifying a list with the other lines
lines = ["He can take in his beak, \n", "Enough food for a week, \n", "But I'm damned if I see how the helican. \n"]
# use the .writelines method to add this list on; need \n to give the linebreaks
file_handler.writelines(lines)
# good practice to close the file afterwards
file_handler.close()
