import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from PIL import Image, ImageTk

class CommandControlFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Command Control", padding="10")
        
        # Load icons
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "icons")
        self.add_icon = self._load_icon(os.path.join(icon_path, "add.png"))
        self.delete_icon = self._load_icon(os.path.join(icon_path, "delete.png"))
        self.update_icon = self._load_icon(os.path.join(icon_path, "update.png"))
        
        # Top container for entries
        self.topContainer = ttk.Frame(self)
        self.topContainer.pack(fill=X, padx=5, pady=5)
        
        # Command entry
        self.cmdLabel = ttk.Label(self.topContainer, text="Command:")
        self.cmdLabel.pack(side=LEFT, padx=(0, 5))
        
        self.commandVar = tk.StringVar()
        self.commandEntry = ttk.Entry(self.topContainer, textvariable=self.commandVar, width=40)
        self.commandEntry.pack(side=LEFT, padx=(0, 10))
        
        # Cycles entry
        self.cycleLabel = ttk.Label(self.topContainer, text="Cycles:")
        self.cycleLabel.pack(side=LEFT, padx=(0, 5))
        
        self.cycleVar = tk.StringVar(value="1")
        self.cycleEntry = ttk.Entry(self.topContainer, textvariable=self.cycleVar, width=10)
        self.cycleEntry.pack(side=LEFT)
        
        # Command table frame
        self.tableFrame = ttk.Frame(self)
        self.tableFrame.pack(fill=BOTH, expand=YES, padx=5, pady=5)
        
        # Command table
        self.columns = ("command", "status", "response")
        self.commandTable = ttk.Treeview(self.tableFrame, columns=self.columns, show="headings")
                # Set style to remove focus and add grid lines
        style = ttk.Style()
        style.configure("Custom.Treeview", highlightthickness=0, bd=0, relief="flat", rowheight=25, font=('Arial', 10), foreground="#000000")

        
        # Style the headings and rows
        style.map("Custom.Treeview", background=[('selected', 'lightblue')], foreground=[('selected', 'black')])
        self.commandTable.configure(style="Custom.Treeview")
        
        # Set headings
        self.commandTable.heading("command", text="COMMANDS")
        self.commandTable.heading("status", text="STATUS")
        self.commandTable.heading("response", text="RESPONSE")
        
        # Set column widths
        self.commandTable.column("command", width=300)
        self.commandTable.column("status", width=100)
        self.commandTable.column("response", width=300)
        
        # Add scrollbars
        self.tableYScroll = ttk.Scrollbar(self.tableFrame, orient=VERTICAL, command=self.commandTable.yview)
        self.commandTable.configure(yscrollcommand=self.tableYScroll.set)
        
        # Pack table and scrollbar
        self.tableYScroll.pack(side=RIGHT, fill=Y)
        self.commandTable.pack(side=LEFT, fill=BOTH, expand=YES)
        self.commandTable.bind('<<TreeviewSelect>>', self.onTableSelect)
        
        # Table action buttons
        self.btnFrame = ttk.Frame(self)
        self.btnFrame.pack(fill=X, padx=5, pady=5)
        
        self.addBtn = ttk.Button(self.btnFrame, text="Add", image=self.add_icon, compound=TOP, command=self.addCommand)
        self.addBtn.pack(side=LEFT, padx=5)
        
        self.deleteBtn = ttk.Button(self.btnFrame, text="Delete", image=self.delete_icon, compound=TOP, command=self.deleteCommand)
        self.deleteBtn.pack(side=LEFT, padx=5)
        
        self.updateBtn = ttk.Button(self.btnFrame, text="Update", image=self.update_icon, compound=TOP, command=self.updateCommand)
        self.updateBtn.pack(side=LEFT, padx=5)
        
        # Control panel
        self.controlFrame = ttk.Frame(self)
        self.controlFrame.pack(fill=X, padx=5, pady=5)
        
        # Run/Stop button



        self.isRunning = False
        self.runStopBtn = ttk.Button(self.controlFrame, text="RUN", bootstyle="success",
                                       command=self.toggleRunStop, takefocus=False)
        self.runStopBtn.pack(side=LEFT, padx=5)
        
        # Cycles progress
        self.cycleProgressFrame = ttk.Frame(self.controlFrame)
        self.cycleProgressFrame.pack(side=LEFT, padx=20)
        
        self.cycleLabel = ttk.Label(self.cycleProgressFrame, text="CYCLES COMPLETED:")
        self.cycleLabel.pack(side=LEFT)
        
        self.cycleProgressVar = tk.StringVar(value="0/0")
        self.cycleProgress = ttk.Label(self.cycleProgressFrame, textvariable=self.cycleProgressVar)
        self.cycleProgress.pack(side=LEFT, padx=5)
        
        # Elapsed time
        self.timeFrame = ttk.Frame(self.controlFrame)
        self.timeFrame.pack(side=RIGHT, padx=5)
        
        self.timeLabel = ttk.Label(self.timeFrame, text="ELAPSED TIME:")
        self.timeLabel.pack(side=LEFT)
        
        self.elapsedTimeVar = tk.StringVar(value="00:00:00")
        self.elapsedTime = ttk.Label(self.timeFrame, textvariable=self.elapsedTimeVar)
        self.elapsedTime.pack(side=LEFT, padx=5)
    
    def toggleRunStop(self):
        """Toggle between Run and Stop states"""
        self.isRunning = not self.isRunning
        
        if self.isRunning:
            self.runStopBtn.configure(text="STOP", bootstyle="danger")
        else:
            self.runStopBtn.configure(text="RUN", bootstyle="success")

    def addCommand(self):
        """Add a new command to the table"""
        command = self.commandVar.get()
        cycles = self.cycleVar.get()
        if command:
            self.commandTable.insert('', 'end', values=(command, "", ""))
            self.commandVar.set("")  # Clear entry
        
    def deleteCommand(self):
        """Delete selected command from table"""
        selected = self.commandTable.selection()
        if selected:
            self.commandTable.delete(selected)
            
    def updateCommand(self):
        """Update selected command in table"""
        selected = self.commandTable.selection()
        if selected:
            command = self.commandVar.get()
            if command:
                self.commandTable.item(selected, values=(command, "", ""))

    def onTableSelect(self, event):
        """Update entry when a row is selected"""
        selected = self.commandTable.selection()
        if selected:
            values = self.commandTable.item(selected)['values']
            if values:
                self.commandVar.set(values[0])        
    
    def _load_icon(self, path, size=(14, 14)):
        """Load an icon from path and resize it"""
        try:
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading icon {path}: {e}")
            return None