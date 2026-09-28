import argparse
import time


def validate_time(minutes, seconds):
    """Validate minutes and seconds and return the total number of seconds."""
    if minutes < 0 or seconds < 0:
        raise ValueError("Minutes and seconds cannot be negative.")
    if seconds >= 60:
        raise ValueError("Seconds must be between 0 and 59.")
    total = minutes * 60 + seconds
    if total <= 0:
        raise ValueError("Please enter a time greater than zero.")
    return total


def format_time(total_seconds):
    """Convert seconds to MM:SS format."""
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


def countdown(total_seconds, wait=True):
    """Run the countdown and return when it reaches zero."""
    while total_seconds >= 0:
        print(f"\rTime remaining: {format_time(total_seconds)}", end="", flush=True)
        if total_seconds == 0:
            break
        if wait:
            time.sleep(1)
        total_seconds -= 1
    print("\nTIME'S UP!")


def run_cli(minutes=None, seconds=None, wait=True):
    """Get the timer duration and run the command-line version."""
    if minutes is None:
        minutes = int(input("Enter minutes: "))
    if seconds is None:
        seconds = int(input("Enter seconds (0-59): "))

    total = validate_time(minutes, seconds)
    print(f"Starting countdown: {format_time(total)}")
    countdown(total, wait=wait)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Countdown Timer - command-line version"
    )
    parser.add_argument("-m", "--minutes", type=int, help="Number of minutes")
    parser.add_argument("-s", "--seconds", type=int, help="Number of seconds (0-59)")
    parser.add_argument(
        "--no-wait",
        action="store_true",
        help="Display the countdown without waiting one second between steps",
    )
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Open the original Tkinter graphical version",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.gui:
        try:
            import tkinter as tk
            from gui_timer import CountdownTimer
        except ImportError as exc:
            parser.error(f"GUI components are unavailable: {exc}")

        root = tk.Tk()
        CountdownTimer(root)
        root.mainloop()
        return

    try:
        run_cli(
            minutes=args.minutes,
            seconds=args.seconds,
            wait=not args.no_wait,
        )
    except (ValueError, TypeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
