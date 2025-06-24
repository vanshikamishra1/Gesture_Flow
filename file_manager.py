import tkinter as tk
from tkinter import filedialog, Label, messagebox, Frame, Button, PhotoImage
import time
import os

class FileManager:
    """
    Handles file operations for the presentation application.
    """

    def __init__(self):
        """Initialize file manager with no selected file."""
        self.selected_file = None
        self.file_name = None

    def show_file_dialog(self):
        """
        Shows a file dialog to the user to select a PDF or PPT file.
        Returns the selected file path or None if no file was selected.
        """
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        
        # Create a new window for file selection
        dialog_window = tk.Toplevel(root)
        dialog_window.title("Hand Gesture Presentation Controller")
        dialog_window.geometry("500x300")
        dialog_window.configure(bg="#f0f0f0")
        dialog_window.resizable(False, False)
        
        # Center the window
        window_width = 500
        window_height = 300
        screen_width = dialog_window.winfo_screenwidth()
        screen_height = dialog_window.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        dialog_window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
        
        # Create a frame for the content
        content_frame = Frame(dialog_window, bg="#f0f0f0")
        content_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Title
        title_label = Label(
            content_frame, 
            text="Hand Gesture Presentation Controller", 
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=(0, 20))
        
        # Description
        desc_text = "Select a PDF or PowerPoint file to open with gesture controls."
        desc_label = Label(
            content_frame, 
            text=desc_text,
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#555555", 
            wraplength=450
        )
        desc_label.pack(pady=(0, 20))
        
        # Status label
        status_label = Label(
            content_frame, 
            text="Ready to select a file", 
            fg="#666666",
            bg="#f0f0f0",
            font=("Arial", 9)
        )
        status_label.pack(pady=(0, 10))
        
        # Upload button
        def upload_file():
            filepath = filedialog.askopenfilename(
                filetypes=[("Presentation Files", "*.pdf *.pptx")],
                title="Select a PDF or PowerPoint file"
            )
            if filepath:
                status_label.config(text=f"Selected: {os.path.basename(filepath)}", fg="green")
                dialog_window.update_idletasks()  # Refresh GUI
                time.sleep(1)  # Brief delay
                self.selected_file = filepath
                self.file_name = os.path.basename(filepath)
                dialog_window.destroy()
                root.destroy()
        
        button_frame = Frame(content_frame, bg="#f0f0f0")
        button_frame.pack(pady=10)
        
        upload_btn = Button(
            button_frame,
            text="Browse Files",
            command=upload_file,
            bg="#4285f4",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2"
        )
        upload_btn.pack(side=tk.LEFT, padx=5)
        
        cancel_btn = Button(
            button_frame,
            text="Cancel",
            command=lambda: [dialog_window.destroy(), root.destroy()],
            bg="#f0f0f0",
            fg="#333333",
            font=("Arial", 10),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2"
        )
        cancel_btn.pack(side=tk.LEFT, padx=5)
        
        # Footer
        footer_label = Label(
            content_frame, 
            text="Use hand gestures to control your presentation", 
            font=("Arial", 8),
            fg="#999999",
            bg="#f0f0f0"
        )
        footer_label.pack(side=tk.BOTTOM, pady=10)
        
        # Show window and wait for it to close
        dialog_window.protocol("WM_DELETE_WINDOW", lambda: [dialog_window.destroy(), root.destroy()])
        dialog_window.lift()
        dialog_window.focus_force()
        
        root.mainloop()
        
        return self.selected_file

    def show_help_dialog(self):
        """
        Display help dialog with gesture instructions.
        """
        root = tk.Tk()
        root.withdraw()
        
        help_window = tk.Toplevel(root)
        help_window.title("Gesture Controls Help")
        help_window.geometry("500x400")
        help_window.configure(bg="#f0f0f0")
        
        # Center the window
        window_width = 500
        window_height = 400
        screen_width = help_window.winfo_screenwidth()
        screen_height = help_window.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        help_window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
        
        # Title
        title_label = Label(
            help_window, 
            text="Hand Gesture Controls", 
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=(20, 15))
        
        # Instructions frame
        instructions_frame = Frame(help_window, bg="#f0f0f0")
        instructions_frame.pack(fill="both", expand=True, padx=25, pady=10)
        
        # Gesture instructions
        gestures = [
            ("Next Slide", "Show all fingers except thumb [0,1,1,1,1]"),
            ("Previous Slide", "Show only thumb [1,0,0,0,0]"),
            ("Pointer", "Show index and middle fingers [0,1,1,0,0]"),
            ("Draw", "Show only index finger [0,1,0,0,0]"),
            ("Erase", "Show index, middle, and ring fingers [0,1,1,1,0]"),
            ("Clear Screen", "Show all five fingers [1,1,1,1,1]"),
        ]
        
        for i, (action, gesture) in enumerate(gestures):
            row_frame = Frame(instructions_frame, bg="#f0f0f0")
            row_frame.pack(fill="x", pady=5, anchor="w")
            
            action_label = Label(
                row_frame, 
                text=action, 
                font=("Arial", 11, "bold"),
                width=15,
                anchor="w",
                bg="#f0f0f0",
                fg="#333333"
            )
            action_label.pack(side=tk.LEFT)
            
            gesture_label = Label(
                row_frame, 
                text=gesture, 
                font=("Arial", 10),
                bg="#f0f0f0",
                fg="#555555"
            )
            gesture_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Note about gesture area
        note_frame = Frame(help_window, bg="#f0f0f0")
        note_frame.pack(fill="x", padx=25, pady=(20, 5))
        
        note_label = Label(
            note_frame, 
            text="Note: Gestures are only detected in the upper right corner of the screen (above the green dotted line).",
            font=("Arial", 9),
            bg="#f0f0f0",
            fg="#666666",
            wraplength=450,
            justify=tk.LEFT
        )
        note_label.pack(anchor="w")
        
        # Close button
        button_frame = Frame(help_window, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        close_btn = Button(
            button_frame,
            text="Close",
            command=lambda: [help_window.destroy(), root.destroy()],
            bg="#4285f4",
            fg="white",
            font=("Arial", 10),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2"
        )
        close_btn.pack()
        
        help_window.protocol("WM_DELETE_WINDOW", lambda: [help_window.destroy(), root.destroy()])
        help_window.lift()
        help_window.focus_force()
        
        root.mainloop()

    def save_file_dialog(self, original_extension):
        """
        Show a dialog to save the file with annotations.
        
        Args:
            original_extension: The extension of the original file (.pdf or .pptx)
            
        Returns:
            The file path to save to, or None if canceled
        """
        root = tk.Tk()
        root.withdraw()
        
        filetypes = []
        if original_extension.lower() == ".pdf":
            filetypes = [("PDF Files", "*.pdf")]
            default_ext = ".pdf"
        elif original_extension.lower() == ".pptx":
            filetypes = [("PowerPoint Files", "*.pptx")]
            default_ext = ".pptx"
        
        filepath = filedialog.asksaveasfilename(
            defaultextension=default_ext,
            filetypes=filetypes,
            title="Save Presentation"
        )
        
        root.destroy()
        return filepath

if __name__ == "__main__":
    # Test the file manager
    fm = FileManager()
    selected_file = fm.show_file_dialog()
    print(f"Selected file: {selected_file}")
