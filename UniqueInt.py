import os

# Define maximum and minimum integer values based on 64-bit limits
MAX_INT = 2**64 - 1
MIN_INT = -2**64 + 1

# This function checks if a line contains a valid integer within the defined range
def is_valid_integer(value):
    try:
        num = int(value.strip())
        
        if MIN_INT <= num <= MAX_INT:
            return num
        else:
            return None  
    except ValueError:
        return None  

# This function implements bubble sort for sorting an array of integers
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap if the element found is greater than the next element

# remove duplicates from the list of integers
def dublicate_removal(arr):
    unique = []
    for num in arr:
        if num not in unique:  
            unique.append(num)
    return unique

# This function processes the input file and generates the result file
# It uses the function is_valid_integer to check if each line has a valid integer
def process_file(input_file_path, output_file_path):
    integers = []  # List to store all integers (no set used)
    
    with open(input_file_path, 'r') as file:
        lines = file.readlines()  

        for line in lines:
            line = line.strip()  
            
            # Check if the line contains a valid integer
            valid_int = is_valid_integer(line)
            if valid_int is not None:
                integers.append(valid_int)  

    # Remove duplicates using our custom function
    unique_integers = dublicate_removal(integers)

    # Sort the list using our custom bubble sort function created
    bubble_sort(unique_integers)

    # Write the sorted unique integers to the output file
    with open(output_file_path, 'w') as result_file:
        for number in unique_integers:
            result_file.write(f"{number}\n")

    print(f"Results written to {output_file_path}")

# This function is to process multiple sample input files
def process_all_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  

    for input_file in os.listdir(input_folder):
        if input_file.endswith(".txt"):  # Ensure only .txt files processing 
            input_file_path = os.path.join(input_folder, input_file)
            output_file_name = f"{input_file}_results.txt"  
            output_file_path = os.path.join(output_folder, output_file_name)

            process_file(input_file_path, output_file_path)


input_folder = 'sample_inputs'
output_folder = 'sample_results'


process_all_files(input_folder, output_folder)
