#!/usr/bin/env python3
"""
Simple TODO list application for GitHub practice.
Instructions:
1. Run the script to see how it works
2. Add a new feature (e.g., mark item as done, remove item)
3. Commit with descriptive message
4. Push to GitHub
5. Practice resolving merge conflicts with teammates
"""

class TodoList:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        """Add an item to the todo list."""
        self.items.append(item)
        print(f"Added: {item}")
    
    def list_items(self):
        """Display all items in the todo list."""
        if not self.items:
            print("Your todo list is empty!")
            return
        
        print("\nYour Todo List:")
        print("===============")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")

    # TODO: Students can add more methods here
    # For example: remove_item, mark_as_done, etc.


if __name__ == "__main__":
    todo = TodoList()
    
    # Add some initial items
    todo.add_item("Learn Git basics")
    todo.add_item("Practice committing changes")
    todo.add_item("Create a pull request")
    
    # Display the list
    todo.list_items()
    
    # Students can add more functionality below
    print("\nTry adding more features to this program!")
