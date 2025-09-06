# yogadi-Notepad.py  <br>
Author : ADITYA KAPSE
Simple Notes App (Tkinter) <br>
Short description <br>
Simple Notes App is a lightweight desktop note-taking application built with Python's tkinter. It provides basic file operations (new, open, save) and a simple menu-driven interface for writing and saving plain text notes. <br>

Features  <br>
Create a new note  <br>
Open existing .txt files  <br>
Save notes to disk  <br>
Basic menu structure: File, Edit, View  <br>
Simple, minimal UI using tkinter   <br>

Notes and improvements
Current behavior and issues:

Several menu items are placeholders and call the same functions (e.g., New Window, Recent, Save as, etc.). You can implement distinct behavior for each.
Some commands are wired incorrectly (e.g., Cut calls save_file, and many Edit/View items reuse the file_menu instead of having separate menus). This README includes an improved script below.
No undo/redo, find/replace, or font settings yet.
No explicit error handling for file I/O beyond simple dialogs.
Suggested improvements:

Separate menus for File, Edit, and View.
Implement Cut/Copy/Paste/Delete/Select All using the Text widget methods.
Add keyboard shortcuts (Ctrl+N, Ctrl+S, Ctrl+O, Ctrl+Q, Ctrl+Z, Ctrl+Y, Ctrl+A).
Implement "Save As" and "New Window" functionality.
Add autosave and recent-files list.
