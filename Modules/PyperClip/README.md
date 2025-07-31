# PyperClip
- a cross-platform Python module designed for interacting with the system clipboard, enabling copy and paste functionalities within Python scripts

- **pyperclip.copy(text):** copies the provided text string to the clipboard.
- **pyperclip.paste():** retrieves and returns the text currently stored on the clipboard as a string.
- **pyperclip.waitForPaste(timeout=None):** blocks execution until non-empty text is present on the clipboard, then returns that text
    - optional timeout argument can be specified, raising a PyperclipTimeoutException if the timeout is exceeded.
- **pyperclip.waitForNewPaste(timeout=None):** blocks execution until the text on the clipboard has changed from its previous state, then returns the new text
    - An optional timeout argument can be specified, raising a PyperclipTimeoutException if the timeout is exceeded.