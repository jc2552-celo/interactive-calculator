from calculator import operations

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

def repl():
    print("=== Interactive Calculator ===")
    print("Type 'exit' to quit.")
    while True:
        op = input("Choose operation (+, -, *, /): ").strip()
        if op.lower() == 'exit':
            break
        if op not in ['+', '-', '*', '/']:
            print("Invalid operation.")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        try:
            result = {
                '+': operations.add,
                '-': operations.subtract,
                '*': operations.multiply,
                '/': operations.divide
            }[op](a, b)
