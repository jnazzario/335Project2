from itertools import chain, combinations

# Generates all possible combos of stocks
def generate_candidates(input):
    n = len(input)
    for r in range(1, n + 1):
        for subset in combinations(input, r):
            yield list(subset)

# Checks to see if a stock combos satisfies the maximum stock value
def verifier(max_stock_value, stock_candidate):
    
    total = 0
    for i in range(len(stock_candidate)):
        total += stock_candidate[i][1]
    return (total <= max_stock_value)

# Calculates total value of a stock combo
def total_value(stock_candidate):
    total = 0
    for i in range(len(stock_candidate)):
        total += stock_candidate[i][0]
    return total

# Uses exhaustiv search to find the best stock combo
def exhaustive(stocks_array, max_amount):
    best = None
    for candidate in generate_candidates(stocks_array):
        if verifier(max_amount, candidate):
            if best is None or total_value(candidate) > total_value(best):
                best = candidate

    return total_value(best)

    
with open('input.txt', 'r') as file:
    lines = file.readlines()

i = 0
with open('output.txt', 'w') as outfile:
    while i < len(lines):
        if lines[i] == "\n":
            i += 1
        size_of_array = int(lines[i])
        stocks_array = eval(lines[i+1])
        amount = int(lines[i+2])
        i += 3
        

        outfile.write(f"Exhaustive Output: {exhaustive(stocks_array, amount)}\n\n")
      