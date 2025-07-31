### tkinter.messagebox
- is a module within Tkinter so it must be imported 
    - `from tkinter import messagebox`
- provides functions for displaying various standard message boxes
- messageboxes are modal dialogs used to inform the user or prompt for a decision
    - modal, mean they block interaction with the main application window until the user responds to the message box
- can be customized with a title, a message, and optional parameters like default (to specify the default focused button) and parent (to specify the parent window)
- **Return Values:** the message box functions return specific values (True, False, OK, None, Yes, No), depending on the type of message box and the user's interaction (clicking a button or closing the window)



#### Commonly used message box functions:
- **showinfo(title, message):** Displays a general information message.
- **showwarning(title, message):** Displays a warning message.
- **showerror(title, message):** Displays an error message.
- **askquestion(title, message):** Asks a question with "Yes" and "No" buttons. Returns "yes" or "no".
- **askokcancel(title, message):** Asks for confirmation with "OK" and "Cancel" buttons. Returns True (for OK) or False (for Cancel).
- **askyesno(title, message):** Asks for confirmation with "Yes" and "No" buttons. Returns True (for Yes) or False (for No).
- **askretrycancel(title, message):** Asks the user to retry or cancel an operation. Returns True (for Retry) or False (for Cancel).