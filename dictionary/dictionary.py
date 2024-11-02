def process_data(data):
    # Check if the input is a list
    if isinstance(data, list):
        # Return the sum of the list
        return sum(data)  # Return type: int
    elif isinstance(data, str):
        # Return the length of the string
        return len(data)  # Return type: int
    else:
        # Return a message for unsupported types
        return "Unsupported data type"  # Return type: str

# Example usages
result1 = process_data([1, 2, 3, 4])  # Returns 10 (int)
result2 = process_data("Hello")        # Returns 5 (int)
result3 = process_data(42)              # Returns "Unsupported data type" (str)

print(result1)  # Output: 10
print(result2)  # Output: 5
print(result3)  # Output: Unsupported data type
