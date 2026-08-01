"""First exercise: say hello and show a tiny bit of Python."""


def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to learning Python."


if __name__ == "__main__":
    print(greet("world"))
