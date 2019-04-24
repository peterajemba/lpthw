from sys import argv
# Parse the input arguments
script, filename = argv
# Read in the file indicated by the filename
txt = open(filename)
# Print a message indicating the file to open
print(f"Here's your file {filename}:")
# Print the content of the file just read in
print(txt.read())
# Close the file
txt.close()
# Ask user to supply filename again
print("Type the filename again:")
# Read in the filename provided
file_again = input("> ")
# Read in the file indicated by the new filename
txt_again = open(file_again)
# Print the content of the file provided
print(txt_again.read())
# Close the file
txt_again.close()
