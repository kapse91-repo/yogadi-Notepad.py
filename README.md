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

Notes and improvements  <br>
Current behavior and issues:  <br>

Several menu items are placeholders and call the same functions (e.g., New Window, Recent, Save as, etc.). You can implement distinct behavior for each.   <br>
Some commands are wired incorrectly (e.g., Cut calls save_file, and many Edit/View items reuse the file_menu instead of having separate menus). This README includes an improved script below.    <br>
No undo/redo, find/replace, or font settings yet.   <br>
No explicit error handling for file I/O beyond simple dialogs.   <br>
Suggested improvements:   

  <br> Separate menus for File, Edit, and View.
  <br> Implement Cut/Copy/Paste/Delete/Select All using the Text widget methods.
  <br> Add keyboard shortcuts (Ctrl+N, Ctrl+S, Ctrl+O, Ctrl+Q, Ctrl+Z, Ctrl+Y, Ctrl+A).
  <br> Implement "Save As" and "New Window" functionality.
 <br> Add autosave and recent-files list.
