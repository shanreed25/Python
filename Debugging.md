# Debugging
- Most IDEs (Intelligent Development Environments) such as PyCharm will have built-in tools for debugging
- This is normally known as the debugger. In many ways, they are like print statements on steroids.
- Debuggers allow us to 
  - peek into our code during execution
  - pause on chosen lines to figure out what is the inner mechanism and where it's going wrong.

- There are a couple of things that are the same in most IDEs which you should be familiar with:
  - Breakpoint: set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are)
    - This line will be where the program pauses during debug run.
  - Step Over: will go through the execution of your code line by line
    - allow you to view the intermediate values of your variables.
  - Step Into: will enter into any other modules that your code references
    - will show you the original code for that function so you can better understand its functionality and how it relates to your problems.
  - Step Into My Code: does the same thing as Step Into, but
    - it limits the scope to your own project code and ignores library code such as random

# Debugging Tips
## 1. Describe the Problem
- first step of solving a problem is being able to describe the problem

## 2. Reproduce Bug
- Some bugs are sneaky, they only occur under certain conditions
- In order to debug them, we need to be able to reliably reproduce the bug
  - this allows us to diagnose our problem to figure out which conditions trigger the bug

## 3. Play Computer
- go through your code line by line as if you were the computer to help you figure out what is going wrong

## 4. Fix the errors
- Fix any errors (red underlines) that show up in the editor before you run your code
- The warnings (yellow) are optional fixes, sometimes it will cause a problem down the line other times it's fine
  - the editor just doesn't understand what you are trying to do
- you can use a try/except block in Python to catch any exceptions that might occur

## 5. Use print()
- can help expose hidden values while your code is running
- In a for loop, the loop will follow some rules to perform a repeated block of code
  - during the loop it's difficult to see the intermediate values
  - this is a perfect example of how you can use print to expose those intermediate values and help you debug your code.

## 6. Use Debugger
- use a debugger to figure out what is the issue in the code and fix it
- Most IDEs (Intelligent Development Environments) such as PyCharm will have built-in tools for debugging

## 7. Take a break
- take a nap, have a cup of tea or do something else for a while and try to tackle it later
- when your brain has had a break or some downtime, you will be surprised how much easier thing are

## 8. Ask a friend
- preferably a developer
- you can join groups or channels that have other developers in them who also are learning or know the concepts you are using
- where you have fresh eyes looking at your code they may not make the same assumptions that you do
  - this allows them to be able to see things that you may not see

## 9. Run Code Often
- don't wait until you have written lots of code to run your code
- once you have changed the program run it to confirm that its actually doing what you want it to do
- this allows you to be able to tackle one problem at a time

## 10. Ask Stack Overflow
- Ask Question: when you think you have come across a bug or issue that is unique ask the question
- Search: when you think you have come across  a bug or issue that other people should have encountered it