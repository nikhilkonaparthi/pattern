def pyramid_pattern(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print ascending part of the pyramid
        for j in range(1, i + 1):
            print(j, end="")
        # Print descending part of the pyramid
        for j in range(i - 1, 0, -1):
            print(j, end="")
        # Move to the next line
        print()

# Define the number of rows for the pyramid
n = 5

# Generate and print the pyramid pattern
pyramid_pattern(n)
