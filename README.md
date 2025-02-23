# Task Manager Console App

A simple task manager console application built using Python, SQLite, and various packages to provide a user-friendly command-line interface.

## Features
- Full CRUD operations for **Users**, **Tasks**, and **Tags**
- Uses **SQLite** as the database
- Interactive and user-friendly CLI using:
  - `prettytable` for formatted table displays
  - `termcolor` for colorized text
  - `inquirer` for interactive prompts

## Installation

### Prerequisites
Make sure you have Python installed on your system (Python 3.7+ recommended).

### Clone the Repository
```sh
git clone https://github.com/yourusername/task-manager-cli.git
cd task-manager-cli
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage
Run the application using:
```sh
python main.py
```
Follow the on-screen prompts to create users, manage tasks, and organize them using tags.

## CRUD Operations
### Users
- Create new users
- List all users
- Update user details
- Delete users

### Tasks
- Create tasks with descriptions, deadlines, and status
- View tasks assigned to a user
- Update task details
- Delete tasks

### Tags
- Add tags to categorize tasks
- List available tags
- Assign tags to tasks
- Remove tags from tasks

## Technologies Used
- **Python**: Core programming language
- **SQLite**: Lightweight database
- **prettytable**: Display tabular data in CLI
- **termcolor**: Add colors to CLI output
- **inquirer**: Interactive command-line prompts
