import time
import functools

def timeit(func):
    """Decorator: Prints the execution time of the function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timeit
def add_and_print(a, b):
    """Calculates the sum of two numbers and prints the result."""
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
    return result

@timeit
def read_and_write():
    """Reads two numbers from input.txt, calculates their sum, and writes the result to output.txt."""
    try:
        with open("input.txt", "r") as file:
            a, b = map(int, file.read().split())
        
        result = a + b
        
        with open("output.txt", "w") as file:
            file.write(str(result))
        
        print(f"The sum of {a} and {b} is {result}")
    except FileNotFoundError:
        print("The input file 'input.txt' was not found in the current directory.")
    except ValueError:
        print("Error: Please make sure the input file contains two integers separated by a space.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# test add_and_print
add_and_print(15, 25)

# test read_and_write
read_and_write()