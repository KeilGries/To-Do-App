import time
import functions
#from functions import get_todos, write_todos

todos = []

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', now)

while True:
    user_action = input("Type add, show, completed, edit, or exit: \n")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new 'to do': ")
            todos[number] = new_todo + '\n'

            print('Here is how it will look', todos)

            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid. Please enter the number of the item you wish to edit.')
            continue

    elif user_action.startswith('completed'):
        try:
            number = int(user_action[10:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f'List item called \'{todo_to_remove}\' was removed from the list'
            print(message)
        except IndexError:
            print('No item with that number. Please enter a valid \'to do\' item number.')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Please enter a valid command.')

print('Bye')
