import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
import sys

from modules.serialFrame import SerialConnectionFrame
from modules.commandFrame import CommandControlFrame
from modules.monitorFrame import SerialMonitorFrame
from modules.logics import SerialLogic

class RobotTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Test Automation")
        self.root.geometry("1200x900")
        
        # Set theme to light
        self.style = ttk.Style("litera")  # Using a light theme

        self.style.configure('TButton', 
                            background='#e0e0e0',     # Default background color
                            foreground='#333333',     # Default text color
                            borderwidth=0,
                            focuscolor='')            # Remove focus outline

        # For hover effect
        self.style.map('TButton', 
                    background=[('active', 'lightblue')],    # Hover background color
                    bordercolor=[('active', 'lightblue')],  # Hover border color 
                    foreground=[('active', '#ffffff')])    # Hover text color
            
        # Configure main container with padding
        self.mainframe = ttk.Frame(self.root, padding="10")
        self.mainframe.pack(fill=BOTH, expand=YES)
        
        # Create frames
        self.serialFrame = SerialConnectionFrame(self.mainframe)
        self.serialFrame.pack(fill=X, padx=5, pady=5)
        
        self.commandFrame = CommandControlFrame(self.mainframe)
        self.commandFrame.pack(fill=BOTH, expand=YES, padx=5, pady=5)
        
        self.monitorFrame = SerialMonitorFrame(self.mainframe)
        self.monitorFrame.pack(fill=BOTH, expand=YES, padx=5, pady=5)

        self.logic = SerialLogic(self.serialFrame, self.commandFrame, self.monitorFrame)