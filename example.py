# example.py
from interactive_dispatcher import Action, MenuItem, ReturnSignal, interactive_dispatcher

# Register a custom signal
ReturnSignal.register("RESTART")

# Sample functions
def greet(name: str) -> str:
    print(f"Hello, {name}!")
    return f"Greeted {name}"

def log(msg: str) -> str:
    print(f"[Log] {msg}")
    return "Logged"

def exit_program() -> str:
    print("Goodbye!")
    return "Exited"

# Menu configuration
menu: list[MenuItem] = [
    MenuItem(
        keys=["greet", "g"],
        description="Greet a user and log the action",
        actions=[
            Action(function=greet, args=("Alice",)),
            Action(function=log, args=("Greeting sent to Alice",))
        ],
        return_signal=ReturnSignal.CONTINUE
    ),
    MenuItem(
        keys=["restart", "r"],
        description="Restart the application",
        actions=[
            Action(function=log, args=("Restarting...",))
        ],
        return_signal=ReturnSignal.RESTART
    ),
    MenuItem(
        keys=["exit", "e", "q"],
        description="Exit the program",
        actions=[
            Action(function=exit_program)
        ],
        return_signal=ReturnSignal.BREAK
    )
]

# Dispatcher loop
while True:
    results, signal = interactive_dispatcher("Choose an option:", menu)
    print(f"Results: {results}")
    print(f"ReturnSignal: {signal}")

    if signal == ReturnSignal.BREAK:
        break
    elif signal == ReturnSignal.RESTART:
        print("Restarting...\n")
