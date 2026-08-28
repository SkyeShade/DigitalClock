# Tkinter user interface for the timezone-aware digital clock.

import tkinter as tk
from datetime import datetime
from tkinter import ttk
from zoneinfo import ZoneInfo, available_timezones


LOCAL_TIME = "Local system time"


def get_timezone_names():
    # Return the local-clock option followed by all available IANA zones.
    return [LOCAL_TIME, *sorted(available_timezones())]


def get_current_datetime(timezone_name):
    # Return the current aware datetime for the selected timezone.

    # The operating system supplies the rules for the local option. Named zones use
    # the IANA database, which automatically accounts for daylight-saving changes.

    if timezone_name == LOCAL_TIME:
        return datetime.now().astimezone()

    return datetime.now(ZoneInfo(timezone_name))


def update_clock(clock_label, date_label, timezone_name):
    # Refresh the display and schedule another update one second later.
    current_time = get_current_datetime(timezone_name.get())
    clock_label.config(text=current_time.strftime("%H:%M:%S"))
    date_label.config(
        text=current_time.strftime("%A, %d %B %Y  •  UTC%z")
    )

    # Schedule the next update without blocking Tkinter's event loop.
    clock_label.after(
        1000,
        update_clock,
        clock_label,
        date_label,
        timezone_name,
    )


def create_window():
    #Create and configure the clock's main application window.
    window = tk.Tk()
    window.title("Digital Clock")
    window.resizable(False, False)

    # StringVar lets the update loop see a selection as soon as it changes.
    timezone_name = tk.StringVar(value=LOCAL_TIME)

    selector_frame = ttk.Frame(window)
    selector_frame.pack(fill="x", padx=30, pady=(24, 0))

    ttk.Label(selector_frame, text="Time zone:").pack(side="left", padx=(0, 8))
    timezone_selector = ttk.Combobox(
        selector_frame,
        state="readonly",
        textvariable=timezone_name,
        values=get_timezone_names(),
        width=35,
    )
    timezone_selector.pack(side="left", fill="x", expand=True)

    # The time and date are separate so the time remains the visual focus.
    clock_label = tk.Label(
        window,
        text="00:00:00",
        font=("Arial", 48),
    )
    clock_label.pack(padx=30, pady=(20, 0))

    date_label = ttk.Label(window, text="")
    date_label.pack(padx=30, pady=(0, 24))

    update_clock(clock_label, date_label, timezone_name)

    return window


def launch():
    # Start the application and listen for user interface events.
    window = create_window()
    window.mainloop()
