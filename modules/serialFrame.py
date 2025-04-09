import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from PIL import Image, ImageTk

class SerialConnectionFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Serial Connection", padding="10")
        
        # Load icons
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "icons")
        self.refresh_icon = self._load_icon(os.path.join(icon_path, "refresh.png"))
        self.connect_icon = self._load_icon(os.path.join(icon_path, "connect.png"))
        
        # Create main container
        self.container = ttk.Frame(self)
        self.container.pack(fill=X, expand=YES)
        
        # COM Port selection
        self.comLabel = ttk.Label(self.container, text="COM Port:")
        self.comLabel.pack(side=LEFT, padx=(0, 5))
        
        self.comPortVar = tk.StringVar()
        self.comPortCombo = ttk.Combobox(self.container, textvariable=self.comPortVar, 
                                         state="readonly", width=10)
        
        self.comPortCombo.pack(side=LEFT, padx=(0, 10))
        
        # Baudrate selection
        self.baudLabel = ttk.Label(self.container, text="Baudrate:")
        self.baudLabel.pack(side=LEFT, padx=(0, 5))
        
        self.baudRateVar = tk.StringVar()
        self.baudRateCombo = ttk.Combobox(self.container, textvariable=self.baudRateVar, 
                                         state="readonly", width=10)
        self.baudRateCombo['values'] = ['9600', '19200', '38400', '57600', '115200']
        self.baudRateCombo.current(0)  # Set default to 9600
        self.baudRateCombo.pack(side=LEFT, padx=(0, 10))
        
        # Buttons container
        self.btnContainer = ttk.Frame(self.container)
        self.btnContainer.pack(side=RIGHT)
        
        # Refresh button
        self.refreshBtn = ttk.Button(self.btnContainer, text="Refresh", image=self.refresh_icon, compound=TOP)
        self.refreshBtn.pack(side=LEFT, padx=5)
        
        # Connect button
        self.connectVar = tk.StringVar(value="Connect")
        self.connectBtn = ttk.Button(self.btnContainer, textvariable=self.connectVar, 
                                    image=self.connect_icon, compound=TOP)
        self.connectBtn.pack(side=LEFT, padx=5)
        
    def _load_icon(self, path, size=(14, 14)):
        """Load an icon from path and resize it"""
        try:
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading icon {path}: {e}")
            return None