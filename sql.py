import sqlite3
from datetime import datetime

from typing import List, Tuple, Optional


def get_conn() -> sqlite3.Connection:
    """Create and return a connection to the SQLite database."""
    return sqlite3.connect('todo_list.db')

#========================User=================================

def read_users() -> List[Tuple]:
    """Retrieve all users from the Users table."""
    try:
        with get_conn() as conn: # with keyword is to ensure that the connection is closed after the code is executed
            cursor = conn.cursor() # cursor is like a middleman between python code and sqlite
            cursor.execute('SELECT * FROM Users;')
            users = cursor.fetchall()
        return users
    except sqlite3.Error as e:
        print(f"Error reading users: {e}")
        return []


def create_user(name: str, email: str) -> None:
    """Insert a new user into the Users table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO Users (name, email) VALUES (?, ?);',
                (name, email)
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating user: {e}")


def delete_user(user_id: int) -> None:
    """Delete a user from the Users table by ID."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'DELETE FROM Users WHERE user_id = ?;',
                (user_id,)
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting user: {e}")


def read_user(user_id: int) -> Optional[Tuple]:
    """Retrieve a single user by ID from the Users table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM Users WHERE user_id = ?;',
                (user_id,)
            )
            user = cursor.fetchone()
        return user
    except sqlite3.Error as e:
        print(f"Error reading user: {e}")
        return None
    
def update_user_info(user_id: int, name: str, email: str) -> None :
    """Update an existing user's information in the Users table."""

    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'UPDATE Users SET name = ?, email = ? WHERE user_id = ? ', (name, email, user_id)
            )  
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error Updating user Info {e}")     



# ======================= UserDetails =======================

def create_user_details(user_id:int, phone_number: str, preferences: str, address: str) -> None:
    """Insert a new user details into UserDetails table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO UserDetails (user_id,phone_number, preferences, address) VALUES (?, ?, ?, ?);',
                (user_id,phone_number, preferences, address)
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating user details: {e}")

def view_user_details(user_details_id: int) -> Optional[Tuple]:
    """view user details from the UserDetails table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM UserDetails WHERE user_details_id = ?",
                (user_details_id,)
            )
            details = cursor.fetchone()  # Fetch one record matching the criteria
        return details
    except sqlite3.Error as e:
        print(f"Error reading user details: {e}")
        return None

def update_user_details(user_id: int, phone_number: str, preferences: str, address: str) -> None:
    """Update user details in the UserDetails table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE UserDetails SET phone_number = ?, preferences = ?, address = ? WHERE user_id = ?",
                (phone_number, preferences, address, user_id)
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating user details: {e}")

def delete_user_details(user_details_id: int) -> None:
    """Delete user details from the UserDetails table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM UserDetails WHERE user_details_id = ?",
                (user_details_id,)
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting user details: {e}")

#==================Tasks=====================
def read_tasks() -> List[Tuple]:
    """Retrieve all tasks from the Tasks table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Tasks;')
            tasks = cursor.fetchall()
        return tasks
    except sqlite3.Error as e:
        print(f"Error reading tasks: {e}")
        return []


def create_task(user_id: int, description: str, date: str, status: str) -> None:
    """Insert a new task into the Tasks table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO Tasks (user_id, description, date, status) VALUES (?, ?, ?, ?);',
                (user_id, description, date, status)
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating task: {e}")


def update_task(task_id: int, description: str, date: str, status: str) -> None:
    """Update an existing task's information in the Tasks table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'UPDATE Tasks SET description = ?, date = ?, status = ? WHERE task_id = ?;',
                (description, date, status, task_id)  # Added task_id as the last parameter
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating task: {e}")


def delete_task(task_id: int) -> None:
    """Delete a task from the Tasks table by ID."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'DELETE FROM Tasks WHERE task_id = ?;',
                (task_id,)
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting task: {e}")




def read_task(task_id: int) -> Optional[Tuple]:
    """Retrieve a single Task by ID from the Tasks table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM Tasks WHERE task_id = ?;',
                (task_id,)
            )
            task = cursor.fetchone()
        return task
    except sqlite3.Error as e:
        print(f"Error reading task: {e}")
        return None

def mark_task_as_complete(task_id: int) -> None:
    """ Mark a spacific task as a Complete"""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'UPDATE Tasks SET status = ? WHERE task_id = ?;', ("Completed", task_id))

            conn.commit()
    except sqlite3.Error as e:
        print(f"Error Mark as complete ")



#======================Tags==============================

def read_tags() -> List[Tuple]:
    """Retrieve all tags from the Tags table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Tags;')
            tags = cursor.fetchall()
        return tags
    except sqlite3.Error as e:
        print(f"Error reading tags: {e}")
        return []


def create_tag(name: str) -> None:
    """Insert a new tag into the Tags table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Tags (name) VALUES (?);', (name,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating tag: {e}")


def update_tag_name(tag_id: int, name: str) -> None:
    """Update an existing tag's name in the Tags table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE Tags SET name = ? WHERE tag_id = ?;', (name, tag_id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating tag: {e}")


def delete_tag(tag_id: int) -> None:
    """Delete a tag from the Tags table by ID."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM Tags WHERE tag_id = ?;', (tag_id,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting tag: {e}")


def read_tag(tag_id: int) -> Optional[Tuple]:
    """Retrieve a single Tag by ID from the Tags table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Tags WHERE tag_id = ?;', (tag_id,))
            tag = cursor.fetchone()
        return tag
    except sqlite3.Error as e:
        print(f"Error reading tag: {e}")
        return None


def list_tags_for_task(task_id: int) -> List[Tuple]:
    """Retrieve all tags for a specific task from TasksTags table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT tag_id FROM TasksTags WHERE task_id = ?;', (task_id,))
            tags = cursor.fetchall()
        return [tag[0] for tag in tags]
    except sqlite3.Error as e:
        print(f"Error reading tags for task: {e}")
        return []


def list_tasks_for_tag(tag_id: int) -> List[Tuple]:
    """Retrieve all tasks for a specific tag from TasksTags table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT task_id FROM TasksTags WHERE tag_id = ?;', (tag_id,))
            tasks = cursor.fetchall()
        return [task[0] for task in tasks]  # Corrected the list comprehension to get task_id
    except sqlite3.Error as e:
        print(f"Error reading tasks for tag: {e}")
        return []


def create_task_tag_relation(task_id: int, tag_id: int) -> None:
    """Insert a new task-tag relation into the TasksTags table."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO TasksTags (task_id, tag_id) VALUES (?, ?);', (task_id, tag_id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating task-tag relation: {e}")


def delete_task_tag_relation(tag_id: int, task_id: int) -> None:
    """Delete a task-tag relation."""
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM TasksTags WHERE tag_id = ? AND task_id = ?;', (tag_id, task_id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting task-tag relation: {e}")
