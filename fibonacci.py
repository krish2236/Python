def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

if __name__ == "__main__":
    n = int(input("Enter the range: "))
    fibonacci(n)
