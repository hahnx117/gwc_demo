#!/usr/bin/env python3
"""
Configuration manager script for GitHub practice.
Instructions:
1. Run the script to see how it manages a simple config file
2. Modify to add new configuration options
3. Commit changes
4. Create a branch for a new feature
5. Practice merging and resolving conflicts
"""

import json
import os

CONFIG_FILE = "config.json"

def load_config():
    """Load configuration from file or create default if not exists."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    else:
        # Default configuration
        default_config = {
            "username": "student",
            "theme": "light",
            "language": "en",
            "notifications": True
        }
        save_config(default_config)
        return default_config

def save_config(config):
    """Save configuration to file."""
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file, indent=4)
    print(f"Configuration saved to {CONFIG_FILE}")

def display_config(config):
    """Display the current configuration."""
    print("\nCurrent Configuration:")
    print("=====================")
    for key, value in config.items():
        print(f"{key}: {value}")

def update_setting(config, setting, value):
    """Update a configuration setting."""
    if setting in config:
        config[setting] = value
        print(f"Updated {setting} to {value}")
    else:
        print(f"Error: Setting '{setting}' not found in configuration.")
    return config

# TODO: Students can add more functions here
# For example: add_setting, remove_setting, reset_to_defaults, etc.


if __name__ == "__main__":
    # Load or create config
    config = load_config()
    
    # Display current config
    display_config(config)
    
    # Example of updating a setting
    print("\nUpdating theme setting...")
    config = update_setting(config, "theme", "dark")
    
    # Save changes
    save_config(config)
    
    # Display updated config
    display_config(config)
    
    print("\nTry modifying this script to add more functionality!")
