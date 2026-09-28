# Countdown Timer

## Project Overview

Countdown Timer is a Python project that lets a user enter a duration and count down to zero. The project includes:

- A command-line version for terminal-based execution.
- The original Tkinter graphical version.
- Input validation.
- MM:SS time formatting.
- A small automated test suite.

The project uses only Python standard-library modules, so no third-party package installation is required.

## Project Structure

```text
countdown-timer/
├── main.py
├── gui_timer.py
├── tests/
│   └── test_timer.py
├── requirements.txt
├── PROJECT_REPORT.md
├── README.md
└── .gitignore
```

## Requirements

- Python 3.x
- For the optional GUI version, a Python installation with Tkinter support.

No external Python packages are required.

## Setup

1. Install Python 3.x.
2. Clone this repository.
3. Open a terminal in the repository folder.
4. (Optional) Create a virtual environment:

```bash
python -m venv .venv
```

Activate it before running the project if you created one.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

There are no third-party dependencies to install.

## Run the command-line version

Interactive input:

```bash
python main.py
```

Or provide the duration directly:

```bash
python main.py --minutes 0 --seconds 10
```

For a quick demonstration without real-time waiting:

```bash
python main.py --minutes 0 --seconds 5 --no-wait
```

## Run the graphical version

```bash
python main.py --gui
```

The graphical version is based on Tkinter and contains Start, Pause/Resume, Reset, Stop, and history features.

## Run the tests

```bash
python -m unittest discover -s tests -v
```

## Input rules

- Minutes must be zero or greater.
- Seconds must be from 0 to 59.
- The total duration must be greater than zero.

## Notes

The command-line mode is the primary terminal-executable entry point for evaluation. The GUI version is provided as an additional interface.

Before submission, review every file and make sure you understand and can explain the code yourself.
