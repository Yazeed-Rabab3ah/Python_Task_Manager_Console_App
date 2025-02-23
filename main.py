from datetime import datetime

import sql
from termcolor import colored # to colored console output
from art import * # for ascii art
import inquirer # for interactive console

from sql import read_users
from prettytable import PrettyTable # to display data in table format

def notify_user(message):
    message = text2art(message)
    print(colored(message,'green'))

def main():
    # ASCII banner
    ascii_banner = text2art("Task Manager")
    print(colored(ascii_banner, "red"))

    print('This is a task manager application to manage your daily tasks.\n')
    print('Please choose an option:\n')

    # List of actions
    actions = [
        'Create User',
        'Update User Info',
        'Delete User',
        'Create User Details',
        'Update User Details',
        'Delete User Details',
        'view_user_details',
        'Create Task',
        'Update Task',
        'Delete Task',

        'Create Tag',
        'Update Tag Name',
        'Delete Tag',
        'Assign Tag to Task',
        'list Tags for a Task',
        'list Tasks for a Tag',

        'Dissociate Tags from Tasks',
        'Fetch All Users',
        'Fetch All Tasks',
        'Exit',
    ]

    while True:

        questions = [
            inquirer.List(
                'action',
                message="What do you want to do?",
                choices=actions,
            )
        ]

        answer = inquirer.prompt(questions)
        if answer is None:
            print("Goodbye!")
            break
        
        
        action = answer['action']


        if action == 'Create User':
            print("Creating a user...")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            sql.create_user(name, email)
            notify_user('User created!')

        elif action == 'Update User Info':
            print('Updating User Info... ')
            user_id = int(input('Enter User ID: '))
            name = input("Enter User Name: ")
            email = input("Enter User Email: ")
            sql.update_user_info(user_id, name, email)
            notify_user('User Updated! ')

        elif action == 'Delete User':
            print ('Deleting User... ')
            user_id = int(input('Enter User ID: '))
            sql.delete_user(user_id)    
            notify_user('User Deleted! ')

        elif action == 'Create User Details':
            print("Creating user details...")
            user_id = int(input('Enter User ID: '))
            phone_number = input('Enter Phone Number: ')
            preferences = input('Enter preferences: ')
            address = input('Enter Address: ')
            sql.create_user_details(user_id,phone_number,preferences,address)
            notify_user('User Details created!')
        
        elif action == 'Update User Details':
            print('Updating User Details... ')
            user_id = int(input('Enter User ID: '))
            phone_number = input('Enter Phone Number: ')
            preferences = input('Enter preferences: ')
            address = input('Enter Address: ')
            sql.update_user_details(user_id,phone_number,preferences,address)
            notify_user('User Details updated!')           

        elif action == 'Delete User Details':
            print('Deleting User Details... ')
            user_id = int(input('Enter User ID: '))
            phone_number = input('Enter Phone Number: ')
            preferences = input('Enter preferences: ')
            address = input('Enter Address: ')
            sql.delete_user_details(user_id,phone_number,preferences,address)
            notify_user('User Details Deleted!') 

        elif action == 'view_user_details':
            print('Viewing User Details... ')
            user_details_id = int(input('Enter User ID: '))
            sql.view_user_details(user_details_id)
            notify_user('User Details Deleted!') 

        elif action == 'Create Task':
            print("Creating a task...")
            user_id = int(input('Enter User ID: '))
            description = input('Enter description: ')
            date = input('Enter date(YYYY-MM-DD): ')
            status = input('Enter status: ')
            sql.create_task(user_id, description, date, status)
            notify_user('Task created!')

        elif action == 'Update Task':
            print("Updating a task...")
            user_id = int(input('Enter User ID: '))
            description = input('Enter description: ')
            date = input('Enter date(YYYY-MM-DD): ')
            status = input('Enter status: ')
            sql.update_task(user_id, description, date, status)
            notify_user('Task Updated!')

        elif action == 'Delete Task':
            print("Deleting a task...")
            user_id = int(input('Enter User ID: '))
            description = input('Enter description: ')
            date = input('Enter date(YYYY-MM-DD): ')
            status = input('Enter status: ')
            sql.delete_task(user_id, description, date, status)
            notify_user('Task Deleted!')    

        elif action == 'Create Tag':
            print("Creating a tag...")
            name = input('Enter name: ')
            sql.create_tag(name)
            notify_user('Tag created!')

        elif action == 'Update Tag Name':
            print('Updating Tag Name')
            name = input('Enter tag name: ')
            sql.update_tag_name(name)
            notify_user('Tag Name updated! ')

        elif action == 'Delete Tag':
            print("Deleting a tag...")
            name = input('Enter name: ')
            sql.delete_tag(name)
            notify_user('Tag Deleted!')


        elif action == 'Assign Tag to Task':
            print("Assigning a tag to a task...")
            task_id = int(input('Enter Task ID: '))
            tag_id = int(input('Enter Tag ID: '))
            sql.create_task_tag_relation(task_id,tag_id)
            notify_user('Task Tag Relation created!')
        
        elif action == 'list Tags for a Task':   
            print('listing Tags for a Task')
            task_id = int(input('Enter Task ID: '))
            sql.list_tags_for_task(task_id)
            notify_user('list Tags for a Task Done! ')

        elif action == 'list Tasks for a Tag':   
            print('listing Tasks for a Tag')
            tag_id = int(input('Enter Tag ID: '))
            sql.list_tasks_for_tag(tag_id)
            notify_user('list Tasks for a Tag Done! ')    

        elif action == 'Dissociate Tags from Tasks':
            print("Dissociating a tag to a task...")
            task_id = int(input('Enter Task ID: '))
            tag_id = int(input('Enter Tag ID: '))
            sql.delete_task_tag_relation(tag_id,task_id)
            notify_user('Task Tag Relation created!')

        elif action == 'Fetch All Users':
            print("Fetching all users...")
            users = sql.read_users()
            table = PrettyTable(["ID", "Name", "Email"])
            for user in users:
                table.add_row(list(user))
            print(table)


        elif action == 'Fetch All Tasks':
            print("Fetching all tasks...")
            tasks = sql.read_tasks()
            table = PrettyTable(["Task ID","User ID", "Description", "Date", "Status"])
            for task in tasks:
                table.add_row(list(task)) 
            print(table)

        elif action == 'Exit':
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
