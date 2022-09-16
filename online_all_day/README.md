```bash
    pip install pyautogui
````

Once that code has ran, you can check if it is downloaded with the command:

```bash
    pip list
```
This will show you a list of libraries you have downloaded.


```bash
    import pyautogui
    import time
    while True:
        pyautogui.moveRel(0, 10)
        time.sleep(2)
```

Let’s go through each line and what it does:
- The first line is to import the library pyautogui. This means that we are using it in this project.
- The second line does the same as the first, but imports the time library.
- The third line, which says “while True” is just a line of code to tell the computer that you want to run the next lines of code while the state is set as “True”. Because we never set it to false at any point within the code, the lines of code underneath it will run forever, until you stop the program.
- The fourth line uses the pyautogui library, and specifically the .moveRel function, which is used to move your cursor 10 pixels to the right.
- The fifth line uses the time library, specifically the .sleep function of this library, which pauses your code from running for 2 seconds. You can change these numbers to whatever suits you.

**Because the fourth and fifth line are underneath the “while true” on the third line, these lines will keep running over and over. So in this case, with the numbers included in the example, your cursor would move 10 pixels every 2 seconds.**