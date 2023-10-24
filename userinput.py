# -*- coding: utf-8 -*-
#Creating a dataset with User Input
#Dataset to store records of employee performance appraisals
# Initialize an empty list to store the dataset
dataset = []

# Number of records in the dataset
num_records = int(input("Enter the number of records: "))

# Input data for each record
for i in range(num_records):
    record = {}
    print(f"Record {i + 1}:")

    # Input data for each variable
    record["Name"] = input("Name: ")
    record["Salary"] = int(input("Salary: "))
    record["Hours"] = int(input("Hours: "))
    record["Grade"]=(input("Grade:"))

    # Add the record to the dataset
    dataset.append(record)

# Print the dataset
print("\nDataset:")
for i, record in enumerate(dataset, 1):
    print(f"Record {i}: {record}")
