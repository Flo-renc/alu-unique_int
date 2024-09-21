import os

# Define maximum and minimum integer values based on 64-bit limits
MAX_INT = 2**64 - 1
MIN_INT = -2**64 + 1

# Function to check if a line contains a valid integer within the defined range
def is_valid_integer(value):
    try:
        num = int(value.strip())
        # Check if the integer is within the 64-bit range
        if MIN_INT <= num <= MAX_INT:
            return num
        else:
            return None  
    except ValueError:
        return None  
# This function processes the input file and generates the result file
# It uses the function is_valid_integer to check if each line has a valid integer
def process_file(input_file_path, output_file_path):
    distinct_ints = set()  # Set to store unique integers
    with open(input_file_path, 'r') as file:
        lines = file.readlines()  
        for line in lines:
            line = line.strip() 
            # This block of code checks if the line contains a valid integer and adds it to the set
            valid_int = is_valid_integer(line)
            if valid_int is not None:
                distinct_ints.add(valid_int)  
    
    # Sort the distinct integers in ascending order
    sorted_distinct_ints = sorted(distinct_ints)

    # Write the sorted unique integers to the output file
    with open(output_file_path, 'w') as result_file:
        for number in sorted_distinct_ints:
            result_file.write(f"{number}\n")

    print(f"Results written to {output_file_path}")

# This function is to process multiple sample input files
def process_all_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the output folder if it doesn't exist

    for input_file in os.listdir(input_folder):
        if input_file.endswith(".txt"):  
            input_file_path = os.path.join(input_folder, input_file)
            output_file_name = f"{input_file}_results.txt"  
            output_file_path = os.path.join(output_folder, output_file_name)

            process_file(input_file_path, output_file_path)


input_folder = 'sample_inputs'
output_folder = 'sample_results'


process_all_files(input_folder, output_folder)