# YouTube Video Manager - Mini Project

A command-line application to manage your YouTube video collection with persistent data storage.

## 🎯 Project Overview

This is a Python-based mini project that demonstrates practical programming concepts including file handling, data persistence, and user interface design. The application allows users to manage their YouTube video collection through an intuitive menu-driven interface.

## ✨ Key Features

### 1. **List All Videos**
   - Displays all saved videos in a numbered, user-friendly format
   - Shows video name and duration for each entry
   - Uses `enumerate()` to create numbered lists starting from 1, making it easy to reference videos

### 2. **Add a Video**
   - Add new videos to your collection
   - Prompts for video name and duration
   - Automatically saves data to JSON file after adding

### 3. **Update Video Details**
   - Modify existing video information
   - Select video by number from the displayed list
   - Updates both name and duration
   - Includes input validation to prevent errors

### 4. **Delete a Video**
   - Remove videos from your collection
   - Select video by number from the displayed list
   - Includes input validation and confirmation feedback

### 5. **Exit Application**
   - Clean exit from the application
   - All data is automatically saved before exiting

## 🛠️ Technical Highlights

### **JSON Data Storage**
- Uses JSON format for data persistence
- Data is stored in `youtube.txt` file
- Automatically loads existing data on startup
- Saves data immediately after any modification (add, update, delete)
- Handles file not found errors gracefully (returns empty list on first run)

### **List Enumeration**
- Uses Python's `enumerate()` function with `start=1` parameter
- Provides user-friendly numbering (1, 2, 3...) instead of 0-based indexing
- Makes it intuitive for users to select videos by number
- Simplifies the interaction between display and user input

### **User-Friendly Design**
- Clear menu-driven interface
- Numbered options for easy navigation
- Descriptive prompts and feedback messages
- Input validation to prevent crashes
- Visual separators for better readability

## 📁 Project Structure

```
MiniProject/
├── youtube_manager.py    # Main application file
├── youtube.txt           # JSON data file (created automatically)
└── README.md             # This file
```

## 🚀 How to Run

1. Make sure you have Python 3.10+ installed (for match-case support)
2. Navigate to the MiniProject directory
3. Run the application:
   ```bash
   python youtube_manager.py
   ```
4. Follow the on-screen menu to manage your videos


## 📌 Notes

- The `youtube.txt` file is created automatically when you first add a video
- All data is saved immediately after any modification
- Video numbers start from 1 (not 0) for user convenience
- The application handles invalid inputs gracefully

---

**Created as a Python learning project to demonstrate practical programming skills and data management concepts.**
