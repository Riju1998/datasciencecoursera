# Number Puzzle Solver for Competitions
# Given a list of numbers, find all combinations that sum to a target

from itertools import combinations

# Input numbers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the target sum: "))

found = False
print(f"\nCombinations that sum to {target}:")

# Check all combination lengths
for r in range(1, len(numbers)+1):
    for combo in combinations(numbers, r):
        if sum(combo) == target:
            print(combo)
            found = True

if not found:
    print("No combination found.")
