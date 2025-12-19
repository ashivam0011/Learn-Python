"""
YouTube Video Manager - Mini Project
=====================================
A command-line application to manage your YouTube video collection.
This project demonstrates:
- JSON file handling for data persistence
- List enumeration for user-friendly display
- CRUD operations (Create, Read, Update, Delete)
- User-friendly menu-driven interface
"""

import json


def load_data():
    """
    Loads video data from JSON file.
    
    Uses JSON to read stored video information from 'youtube.txt'.
    If the file doesn't exist, returns an empty list to start fresh.
    This ensures the app works even on first run without errors.
    
    Returns:
        list: List of video dictionaries, or empty list if file not found
    """
    try:
        with open('youtube.txt', 'r') as file:
            videos = json.load(file)
            return videos
    except FileNotFoundError:
        # Return empty list if file doesn't exist (first time running)
        return []
    

def save_data_helper(videos):
    """
    Saves video data to JSON file.
    
    Persists the current video list to 'youtube.txt' using JSON format.
    This ensures data is saved after every modification (add, update, delete).
    
    Args:
        videos (list): List of video dictionaries to save
    """
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    """
    Displays all videos in a user-friendly numbered format.
    
    Uses enumerate() to create numbered list starting from 1,
    making it easy for users to select videos by number.
    Each video shows its name and duration.
    
    Args:
        videos (list): List of video dictionaries to display
    """
    print("\n")
    print("*" * 70)
    # Using enumerate with start=1 for user-friendly numbering (1, 2, 3...)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 70)


def add_video(videos):
    """
    Adds a new video to the collection.
    
    Prompts user for video name and duration, then adds it to the list.
    Automatically saves the updated list to JSON file for persistence.
    
    Args:
        videos (list): List of video dictionaries to modify
    """
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)  # Save immediately after adding


def update_video(videos):
    """
    Updates an existing video's details.
    
    First displays all videos with numbers, then allows user to select
    which video to update by entering its number. Validates the index
    to prevent errors and provides clear feedback.
    
    Args:
        videos (list): List of video dictionaries to modify
    """
    list_all_videos(videos)  # Show numbered list for easy selection
    index = int(input("Enter the video number to update: "))
    
    # Validate index is within valid range (1 to length of list)
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name': name, 'time': time}  # Convert to 0-based index
        print('Video updated successfully')
        save_data_helper(videos)  # Save changes to JSON
    else:
        print("Invalid index selected")


def delete_video(videos):
    """
    Deletes a video from the collection.
    
    Displays all videos with numbers, then allows user to select
    which video to delete by entering its number. Validates the index
    and provides confirmation feedback.
    
    Args:
        videos (list): List of video dictionaries to modify
    """
    list_all_videos(videos)  # Show numbered list for easy selection
    index = int(input("Enter the video number to be deleted: "))
    
    # Validate index is within valid range (1 to length of list)
    if 1 <= index <= len(videos):
        del videos[index-1]  # Convert to 0-based index for deletion
        print('Video deleted successfully')
        save_data_helper(videos)  # Save changes to JSON
    else:
        print("Invalid video index selected")


def main():
    """
    Main function that runs the YouTube Manager application.
    
    Provides a user-friendly menu-driven interface with 5 options:
    1. List all videos
    2. Add a video
    3. Update a video
    4. Delete a video
    5. Exit
    
    Uses match-case for clean option handling and loads data from JSON
    at startup, ensuring persistence across sessions.
    """
    # Load existing data from JSON file (or empty list if first run)
    videos = load_data()
    
    # Main application loop - runs until user chooses to exit
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        # Match-case statement for clean option handling
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Thank you for using YouTube Manager!")
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()