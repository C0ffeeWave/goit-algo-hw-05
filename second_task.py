import re
from typing import Callable

def generator_numbers(text: str):
    # Finding of floating-point numbers
    pattern = r"[-+]?\d*\.?\d+"
    
    # Finding all numbers matching the pattern 
    matches = re.findall(pattern, text)
    
    # Creating of generator 
    for match in matches:
        yield float(match)  

def sum_profit(text: str, func: Callable):
    # Calling of generator function 
    numbers_generator = func(text)
    
    # Summing numbers in the generator
    total_sum = sum(numbers_generator)
    
    return total_sum

# Test
text = "The total income of an employee consists of several parts: 1000.01 as the main income, supplemented with additional revenues of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
