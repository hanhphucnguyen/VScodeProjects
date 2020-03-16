
#--------------------------------------------------------------------
#File

# Open the text.txt we made earlier
my_file = open('test.txt')
# We can now read the file
my_file.read()
'Hello, this is a quick test file'

# Seek to the start of file (index 0)
my_file.seek(0)

# Readlines returns a list of the lines in the file.
my_file.readlines()   

# Add a second argument to the function, 'w' which stands for write
my_file = open('test.txt','w+')
# Write to the file
my_file.write('This is a new line')
# Read the file
my_file.read()

#--------------------------------------------------------------------
#If 
loc = 'Bank'
if loc == 'Auto Shop':
    print ('Welcome to the Auto Shop!')
elif loc == 'Bank':
    print ('Welcome to the bank!')
else:
    print ("Where are you?")