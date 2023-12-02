import csv

# Open the input file
with open('perm.csv', 'r') as file:
    # Read the CSV data
    reader = csv.reader(file)
    # Create a list to store the filtered rows
    filtered_rows = []
    # Iterate over each row in the CSV data
    for row in reader:
        # Check if the first number is 7, 8, 9, or 10
        if row[0] not in ['7', '8', '9', '10']:
            # Count the occurrences of 10 in the row
            count = row.count('10')
            # Check if the count is less than 3
            if count < 3:
                # Add the row to the filtered rows list
                filtered_rows.append(row)

# Sort the filtered rows based on the given criteria
sorted_rows = sorted(filtered_rows, key=lambda x: (int(x[0]), sum(map(int, x[1:6])), x[1:6]))

# Open the output file
with open('perm.csv', 'w', newline='') as file:
    # Write the sorted rows to the output file
    writer = csv.writer(file)
    writer.writerows(sorted_rows)



# Open the output file
with open('perm.csv', 'w', newline='') as file:
    # Write the filtered rows to the output file
    writer = csv.writer(file)
    writer.writerows(filtered_rows)

