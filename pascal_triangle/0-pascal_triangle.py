#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []  # This will hold all the rows

    for row_num in range(n):
        row = [1]  # Start every row with a 1

        # If we're not on the first row, calculate the inner values
        if triangle:
            prev_row = triangle[-1]  # Get the previous row
            for i in range(1, row_num):
                # Each value is the sum of the two values above it
                value = prev_row[i - 1] + prev_row[i]
                row.append(value)
            row.append(1)  # End every row with a 1

        triangle.append(row)  # Add the row to the triangle

    return triangle
