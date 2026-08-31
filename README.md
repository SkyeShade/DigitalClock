# Digital Clock

A simple desktop digital clock written in Python using Tkinter.

The project was created as a small GUI application for learning Python, Tkinter, application structure, and building standalone Windows executables.

## Features

* Displays the current local time
* Updates automatically
* Simple Tkinter graphical interface
* Can be built as a standalone Windows executable
* Does not require Python when using the packaged `.exe`

## Requirements

To run the project from source:

* Python 3
* Tkinter

Tkinter is normally included with the standard Windows Python installation.

## Running from Source

Clone the repository:

```bash
git clone <repository-url>
cd DigitalClock
```

Run the application:

```bash
python main.py
```

## Building the Windows Executable

The project can be packaged using PyInstaller.

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the application:

```bash
pyinstaller --onefile --windowed --name DigitalClock main.py
```

The resulting executable will be created at:

```text
dist/DigitalClock.exe
```

## Project Structure

```text
DigitalClock/
├── main.py
├── ui.py
├── README.md
└── .gitignore
```

### `main.py`

Contains the application entry point and starts the GUI.

### `ui.py`

Contains the Tkinter window and digital clock logic.

## Releases

Prebuilt Windows executables can be found in the GitHub Releases section of this repository.

## License

This project is intended primarily as a learning project.
