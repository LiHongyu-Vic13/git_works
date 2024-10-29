def filter_lines(lambda_func, string_array):
    # Using list comprehension and lambda functions to filter arrays.
    filtered_array = [s for s in string_array if lambda_func(s)]
    return filtered_array

# Define a lambda function for filtering conditions.
lambda_func = lambda s: not (s.strip().startswith('a') or len(s) < 5 or ' ' in s)

# Example string array.
string_array = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "  avocado",
    "apricot",
    "blackberry",
    "  a",
    "short"
]

# Invoke the function and print the results.
filtered_results = filter_lines(lambda_func, string_array)
print(filtered_results)