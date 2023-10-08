 # creating empty list called beatles
beatles = []
 # Appending all the names to the empty list beatles
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print(beatles)  # Printing out the list

#Adding Stu Sutcliffe and Pete Best
print('Enter the names: ')
for name in range(2):
     user_input = input()
     beatles.append(user_input)

print(f'The new list with added names is: {beatles}')
print()  # Creating blank line space in the console
 # Deleting Stu Sutcliffe and Pete Best
del beatles[3:5]
print(f'The list with new names is: {beatles}')
