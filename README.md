## MLSG Calculator

A small PyQt5-based GUI calculator implemented in `main.py`.

This project provides a simple four-function calculator with a basic GUI. It was built with PyQt5 and intended to be run locally on a desktop environment.

## Features

- Standard arithmetic: addition, subtraction, multiplication, division
- Decimal support
- Clear (`C`) and delete (`DEL`) buttons
- Simple, single-file implementation (`main.py`)

## Prerequisites

- Python 3.8 or newer
- A desktop environment (X11/Wayland) for the PyQt GUI
- The required Python packages listed in `requirements.txt` (PyQt5 is required)

## Install

It is recommended to use a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you prefer, you can install PyQt5 system-wide with your distribution package manager (for example, on Debian/Ubuntu: `sudo apt install python3-pyqt5`), but using `pip` inside a venv is generally easiest.

## Run

From the project root (where `main.py` lives):

```bash
python main.py
```

On some systems you may need to run `python3 main.py` instead.

## Usage

- Click number buttons to enter values.
- Click `+`, `-`, `*`, or `/` to choose an operation.
- Click `=` to evaluate the expression.
- `C` clears the entire input.
- `DEL` removes the last character.

The GUI is intentionally minimal and suitable for quick calculations.

## Troubleshooting

- If the GUI doesn't appear or you see errors installing `PyQt5` with `pip`, try installing the distribution package (`python3-pyqt5`) or consult your platform's PyQt5 install docs.
- If you get an `ImportError` for a package listed in `requirements.txt`, ensure you're running from the same Python interpreter/environment where you installed dependencies.

## Files

- `main.py` — main application; small PyQt5 calculator UI and logic.
- `requirements.txt` — dependencies used for development/testing.

## Next steps (optional)

- Add unit tests for the calculator logic (extract parsing/evaluation from the GUI first).
- Add packaging or an installer for your target OS.
