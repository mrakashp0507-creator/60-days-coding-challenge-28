# Day 28 – Pattern Recognition: Two Sum Treasure Hunt

## Overview
This project solves the Two Sum problem using two different algorithms. Given a list of coordinates and a target sum, it finds two distinct elements whose values add up to the target and returns their indexes.

## Objectives
- Implement a brute-force solution.
- Implement an optimized hash-map solution.
- Compare execution times.
- Visualize complement lookups.
- Understand time and space complexity.

## Example

**Input**
```text
Coordinates: [2, 7, 11, 15]
Target: 9
```

**Output**
```text
Pair: 2 + 7 = 9
Indexes: (0, 1)
```

## Algorithms

### 1. Brute Force
Checks all possible pairs until a matching sum is found.

- Time complexity: O(n²)
- Extra space complexity: O(1)

### 2. Hash Map Optimization
Stores previously visited values and their indexes. For each value, it searches for `target - value`.

- Average time complexity: O(n)
- Extra space complexity: O(n)

## Performance Testing
The program tests both algorithms using 5,000 coordinates and prints their execution times. Measurements can vary between systems.

## How to Run
1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python day28_two_sum.py
```

## Real-World Applications
- Matching financial transactions
- Recommendation systems
- Search optimization
- Finding complementary values in datasets

## Learning Outcome
Learned how hash maps improve lookup efficiency and how algorithm complexity affects performance as input size increases.
