
import time


def two_sum_brute_force(numbers, target):
    """Check every possible pair."""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return None


def two_sum_optimized(numbers, target):
    """Use a dictionary for fast complement lookup."""
    seen = {}

    for i, number in enumerate(numbers):
        complement = target - number

        if complement in seen:
            return (seen[complement], i)

        seen[number] = i

    return None


def visualize_lookup(numbers, target):
    """Show how the hash-map lookup works step by step."""
    seen = {}

    print("\n=== Optimized Lookup Visualization ===")
    print("Target:", target)

    for i, number in enumerate(numbers):
        complement = target - number

        print(f"\nStep {i + 1}: Current coordinate = {number}")
        print(f"  Required complement = {target} - {number} = {complement}")
        print(f"  Coordinates already seen = {seen}")

        if complement in seen:
            print(f"  TREASURE FOUND: {complement} + {number} = {target}")
            print(f"  Indexes: {seen[complement]} and {i}")
            return (seen[complement], i)

        seen[number] = i
        print(f"  No match yet. Store {number} at index {i}.")

    print("\nNo matching pair found.")
    return None


def main():
    print("=" * 42)
    print("       PIRATE TREASURE HUNT")
    print("=" * 42)

    # Small example for understanding the algorithms
    coordinates = [2, 7, 11, 15]
    target = 9

    print("\nCoordinates:", coordinates)
    print("Target sum:", target)

    brute_result = two_sum_brute_force(coordinates, target)
    optimized_result = two_sum_optimized(coordinates, target)

    print("\n=== Brute-Force Result ===")
    if brute_result is not None:
        i, j = brute_result
        print(f"Pair: {coordinates[i]} + {coordinates[j]} = {target}")
        print("Indexes:", brute_result)
    else:
        print("No matching pair found.")

    print("\n=== Optimized Result ===")
    if optimized_result is not None:
        i, j = optimized_result
        print(f"Pair: {coordinates[i]} + {coordinates[j]} = {target}")
        print("Indexes:", optimized_result)
    else:
        print("No matching pair found.")

    visualize_lookup(coordinates, target)

    # Benchmark: pair is at the end, so brute force checks many pairs
    print("\n=== Performance Comparison ===")
    large_coordinates = list(range(1, 5001))
    large_target = 9999

    start = time.perf_counter()
    brute_result = two_sum_brute_force(large_coordinates, large_target)
    brute_time = time.perf_counter() - start

    start = time.perf_counter()
    optimized_result = two_sum_optimized(large_coordinates, large_target)
    optimized_time = time.perf_counter() - start

    print("Number of coordinates:", len(large_coordinates))
    print("Target sum:", large_target)
    print("Brute-force indexes:", brute_result)
    print("Optimized indexes:", optimized_result)
    print(f"Brute-force time: {brute_time:.6f} seconds")
    print(f"Optimized time:   {optimized_time:.6f} seconds")

    if optimized_time > 0:
        print(f"Approximate speedup: {brute_time / optimized_time:.2f}x")

    print("\nTreasure hunt completed!")


if __name__ == "__main__":
    main()
