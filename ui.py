import tkinter as tk
from datetime import datetime


def update_clock(label):
    # Display the current local time using a 24-hour clock.
    current_time = datetime.now().strftime("%H:%M:%S")
    label.config(text=current_time)

    # Schedule the next update without blocking Tkinter's event loop.
    label.after(1000, update_clock, label)


def create_window():
    # Configure the application's main window.
    window = tk.Tk()
    window.title("Digital Clock")

    # Create and position the label used to display the time.
    clock_label = tk.Label(
        window,
        text="00:00:00",
        font=("Arial", 48)
    )
    clock_label.pack(padx=30, pady=30)

    update_clock(clock_label)

    return window


def launch():
    # Start the application and listen for user interface events.
    window = create_window()
    window.mainloop()
