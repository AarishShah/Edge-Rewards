# Automated String Typer for Microsoft Edge

## Description
This Python script automates the process of opening the on-screen keyboard, launching Microsoft Edge, typing random 10-character strings with a delay of 10 seconds between each input, and then closing both applications. The delay, string length, and number of repetitions can be adjusted as needed.

## Prerequisites
- Python 3.x
- `pyautogui` library (Install using `pip install pyautogui`)

## Installation
1. **Install Python:** Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install pyautogui:** Open a command prompt or terminal and run:
    ```bash
    pip install pyautogui
    ```

## Usage
1. **Save the Script:**
    - Save the provided script as a Python file (e.g., `rewards.py`).

2. **Run the Script:**
    - Open a command prompt or terminal.
    - Navigate to the directory where the script is saved.
    - Run the script using:
        ```bash
        python rewards.py
        ```

## Script Explanation
The script performs the following actions:
1. Opens the on-screen keyboard.
2. Opens Microsoft Edge.
3. Types random 10-character strings with a delay of 10 seconds between each input.


## Notes
- Do not move the mouse while the script is running, as it may interfere with the typing actions.
- Do not switch to another window while the script is running, as it may disrupt the typing actions.
- Adjust the `interval`, `length`, and `repetitions` variables as needed for your use case.
