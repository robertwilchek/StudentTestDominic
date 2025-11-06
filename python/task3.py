"""
It appeared that events should only use input from the current function call
I've reinitialize events on each function call so that multiple function calls don't share the same reference
"""

"""
Alternatively, if we only log one event at a time, we can return that event inside of a list in one line

def log_event(event):
    return [event]
"""

def log_event(event):
    events = []
    events.append(event)
    return events


if __name__ == "__main__":
    print(log_event("start"))      # expect ["start"]
    print(log_event("next"))       # expect ["next"], NOT ["start", "next"]