# Submondules
- In addition to the main tkinter module, there are several specialized submodules are also available for specific functionalities
- modules extend the capabilities of the core tkinter module, allowing developers to create more complex and feature-rich GUI applications


### tkinter.ttk
- provides "themed Tk" widgets, offering a more modern and platform-native appearance compared to the classic Tkinter widgets
- includes modern versions of existing widgets and introduces new ones like Combobox, Notebook, Progressbar, and Treeview

### [tkinter.messagebox](./Messagebox.md)
- provides functions for displaying various standard message boxes, such as `showinfo()`, `showwarning()`, `showerror()`, `askquestion()`, `askokcancel()`, `askyesno()`, and `askretrycancel()`

### tkinter.filedialog
- offers functions for opening and saving files through standard file dialogs, like `askopenfilename()`, `asksaveasfilename()`, `askdirectory()`, and more

### tkinter.colorchooser
- provides a function `askcolor()` to display a color selection dialog
tkinter.simpledialog
- offers basic dialogs for getting user input, such as `askinteger()`, `askfloat()`, and `askstring()`
tkinter.scrolledtext
- provides a ScrolledText widget, which is a Text widget with a built-in vertical scrollbar

### tkinter.dnd(experimental)
- provides drag-and-drop support for Tkinter applications