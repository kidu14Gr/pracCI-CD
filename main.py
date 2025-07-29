import sys

def say_hello(name: str) -> str:
    return f"Hello, {name}! This is GitHub Actions at work."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_name = sys.argv[1]
    else:
        user_name = "Developer"
    
    greeting = say_hello(user_name)
    print(greeting)
