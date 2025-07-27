# mainloop()
- `mainloop()` allow applications operate on an event loop
- this loop continuously monitors for user interactions (like button clicks or key presses) and updates the display accordingly
    - under the hood this loop looks something like

               while True:
                 listen
            
- keeps the window on screen and listening for screen events
- `root.mainloop()` nust be the last line of code