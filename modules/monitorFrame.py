import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from PIL import Image, ImageTk
import datetime

class SerialMonitorFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Serial Monitor", padding="10")
        
        # Load icons
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "icons")
        self.clear_icon = self._load_icon(os.path.join(icon_path, "clear.png"))
        
        # Create main container
        self.container = ttk.Frame(self)
        self.container.pack(fill=BOTH, expand=YES)
        
        # Serial monitor text area
        self.monitorText = tk.Text(self.container, wrap=tk.WORD, height=10, 
                                  state="disabled", font=("Consolas", 10))
        
        # Add scrollbars
        self.textYScroll = ttk.Scrollbar(self.container, orient=VERTICAL, 
                                         command=self.monitorText.yview)
        self.monitorText.configure(yscrollcommand=self.textYScroll.set)
        
        # Pack text and scrollbar
        self.textYScroll.pack(side=RIGHT, fill=Y)
        self.monitorText.pack(side=LEFT, fill=BOTH, expand=YES)
        
        # Button frame
        self.btnFrame = ttk.Frame(self)
        self.btnFrame.pack(fill=X, pady=(5, 0))
        
        # Clear button
        self.clearBtn = ttk.Button(self.btnFrame, text="Clear", 
                                   image=self.clear_icon, compound=TOP,
                                   command=self.clearMonitor)
        self.clearBtn.pack(side=RIGHT)
    
    def appendToMonitor(self, message, direction="TX"):
        """Append a message to the monitor with timestamp
        
        Args:
            message (str): Message to append
            direction (str): Direction of message (TX or RX)
        """
        timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        formatted_msg = f"[{timestamp}] {direction}: {message}\n"
        
        self.monitorText.configure(state="normal")
        self.monitorText.insert(tk.END, formatted_msg)
        self.monitorText.see(tk.END)  # Auto-scroll to the end
        self.monitorText.configure(state="disabled")
    
    def clearMonitor(self):
        """Clear the monitor text area"""
        self.monitorText.configure(state="normal")
        self.monitorText.delete("1.0", tk.END)
        self.monitorText.configure(state="disabled")
    
    def _load_icon(self, path, size=(14, 14)):
        """Load an icon from path and resize it"""
        try:
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading icon {path}: {e}")
            return None