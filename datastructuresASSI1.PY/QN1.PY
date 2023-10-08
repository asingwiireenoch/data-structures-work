lists = [1, 2, 3, 4, 5]  

while True:
    try:
        user_input = int(input(f'Enter the number that you want to replace in the middle of this list: {lists}: '))
        lists[2] = user_input  # Changing the middle number 3 to that from the user input
        print()
        print(f'The new list is {lists}')

        # code to remove the last value
        print()
        del lists[-1]  # code that deletes the last element
        print(f'The list when the last number is removed is: {lists}')

        length_of_new_list = len(lists)  # A code to find the length of the given list
        print(f'The length of the new list {lists} is: {length_of_new_list} ')
        break

    except ValueError:
        print('Invalid input, please enter the a number')