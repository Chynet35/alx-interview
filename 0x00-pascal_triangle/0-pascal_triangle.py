def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list if n is less than or equal to 0

    triangle = []  # Initialize an empty list to store the triangle

    for i in range(n):
        row = [1]  # Each row starts with 1

        if i > 0:
            prev_row = triangle[i - 1]  # Get the previous row

            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])  # Add the sum of two numbers above to the row

            row.append(1)  # Each row ends with 1

        triangle.append(row)  # Add the current row to the triangle

    return triangle
