# file_handling_demo.py

import csv

# 1–5. TEXT FILE OPERATIONS WITH EXCEPTION HANDLING
try:
    # 1. Create text file & 2. Write user data into file
    with open("user_data.txt", "w") as file:
        file.write("Name:Devika\n")
        file.write("Course: Python\n")
        file.write("Marks: 90\n")
    print("Data written to user_data.txt")

    # 3. Read file contents
    with open("user_data.txt", "r") as file:
        print("\nReading file contents:")
        print(file.read())

    # 4. Append data to file
    with open("user_data.txt", "a") as file:
        file.write("Grade: A\n")
    print("Data appended to user_data.txt")

    # Read again after append
    with open("user_data.txt", "r") as file:
        print("\nAfter appending data:")
        print(file.read())

except FileNotFoundError:
    print("File not found!")
except IOError:
    print("File operation error!")

# 6–9. CSV FILE OPERATIONS
try:
    # 6. Create CSV file & 7. Write multiple rows
    with open("students.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["ID", "Name", "Course", "Marks"])
        writer.writerow([101, "Sai", "Python", 90])
        writer.writerow([102, "Anil", "Java", 85])
        writer.writerow([103, "Ravi", "C++", 88])

    print("\nCSV file students.csv created and data written")

    # 8. Read CSV data
    print("\nReading CSV data:")
    with open("students.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)

except Exception as e:
    print("CSV File Error:", e)

# 9. Files are closed properly using 'with' statement
print("\nAll files handled and closed properly.")
