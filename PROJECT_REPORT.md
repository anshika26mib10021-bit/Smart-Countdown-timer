# Project Report — Countdown Timer

## 1. Project Title

Countdown Timer

## 2. Introduction

The Countdown Timer is a Python application designed to count down from a user-defined duration to zero. It demonstrates basic Python programming concepts such as variables, functions, classes, conditional statements, loops, exception handling, command-line arguments, and the use of standard-library modules.

## 3. Problem Statement

A user may need a simple timer for activities such as studying, practice sessions, short tasks, or demonstrations. The project provides a small timer that accepts a duration, displays the remaining time, and indicates when the countdown is complete.

## 4. Objectives

- Accept a time duration from the user.
- Validate the entered minutes and seconds.
- Convert the duration into seconds for countdown processing.
- Display the remaining time in MM:SS format.
- Provide a terminal-based version that can be executed from the command line.
- Provide the original graphical version as an additional interface.
- Include basic automated tests for the reusable timer functions.

## 5. Technologies Used

- Python 3
- `argparse` for command-line arguments
- `time` for one-second countdown intervals
- `tkinter` for the optional graphical interface
- `unittest` for testing

All modules are part of the Python standard library.

## 6. Working Principle

The command-line program follows these main steps:

1. Read the minutes and seconds from command-line arguments or interactive input.
2. Check that the values are valid.
3. Convert the duration to total seconds.
4. Convert the remaining seconds into minutes and seconds for display.
5. Decrease the remaining time once per second.
6. Stop at `00:00` and display a completion message.

The GUI version provides buttons for starting, pausing/resuming, resetting, stopping, and clearing timer history.

## 7. Input Validation

The program rejects:

- Negative minutes.
- Negative seconds.
- Seconds greater than or equal to 60.
- A total duration of zero.

Invalid values result in an error message instead of starting the timer.

## 8. Testing

The test file checks:

- Conversion of seconds to MM:SS.
- Correct conversion of a valid duration into seconds.
- Rejection of negative values.
- Rejection of seconds outside the allowed range.
- Rejection of a zero-duration timer.

Run the tests with:

```bash
python -m unittest discover -s tests -v
```

## 9. Example Execution

Example command:

```bash
python main.py --minutes 0 --seconds 5 --no-wait
```

Expected behavior:

```text
Starting countdown: 00:05
Time remaining: 00:05
Time remaining: 00:04
Time remaining: 00:03
Time remaining: 00:02
Time remaining: 00:01
Time remaining: 00:00
TIME'S UP!
```

The exact terminal formatting can vary slightly by operating system.

## 10. Limitations

- The command-line version does not provide the full pause/reset button interface of the GUI.
- The GUI alarm behavior uses platform-dependent sound support.
- The project is intended as a Python Essentials course project rather than a production timer application.

## 11. Future Improvements

Possible improvements include:

- Saving timer history to a file.
- Adding multiple preset timers.
- Adding a configurable alarm sound.
- Adding a more advanced command-line menu.
- Adding more automated tests.

## 12. Conclusion

The project demonstrates how Python can be used to build a practical timer application while applying fundamental programming concepts. The command-line entry point makes the project directly executable from a terminal, while the GUI version provides a more interactive interface.

## 13. Student Declaration

I have reviewed the submitted project files and understand the main logic and implementation used in the project. I will make sure the final repository and report accurately represent my own work and course submission.
