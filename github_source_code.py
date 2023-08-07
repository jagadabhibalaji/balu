def say_hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting = say_hello(user_name)
    print(greeting)
