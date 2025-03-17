def outer_function():
    def inner_function():
        return "This is the inner function."
    return f"This is the outer function. {inner_function()}"

print(outer_function())
