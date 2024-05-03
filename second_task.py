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
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

