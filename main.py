import tkinter as tk
import ttkbootstrap as ttk
import os
import sys

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our application class
from modules.app import RobotTestApp

def main():
    # Create the root window
    root = ttk.Window(themename="litera")  # Using light theme
    
    # Create the application
    app = RobotTestApp(root)
    
    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()