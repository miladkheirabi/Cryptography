import math

def hex_to_int(hex_string):
    """Convert hex string to integer."""
    return int(hex_string, 16)

def process_file(filename, hex_string):
    """Process the file and return the resulting binary string."""
    hex_value = hex_to_int(hex_string)
    result = []

    with open(filename, 'r') as file:
        for line in file:
            # Read each line and convert it to an integer
            large_integer = int(line.strip())
            difference = large_integer - hex_value
            
            # Calculate the square root
            sqrt_value = math.sqrt(difference)
            
            # Print the value of the square root for debugging
            print(f"Large Integer: {large_integer}, Difference: {difference}, sqrt: {sqrt_value}")

            # Enhanced check for perfect square
            if difference < 0:
                result.append(1)  # Consider negative difference as float (not a valid sqrt)
            else:
                sqrt_int = int(sqrt_value)
                if sqrt_int * sqrt_int == difference:
                    result.append(0)  # Perfect square
                else:
                    result.append(1)  # Not a perfect square

    # Convert binary result to string
    binary_string = ''.join([str(i) for i in result])
    
    return binary_string

def main():
    filename = 'Output.txt'  # Change this to your file name
    hex_string = '2bf8ae2175e04baef248' # Taken from Challenge file t list
    
    # Process the file and get the binary string
    binary_result = process_file(filename, hex_string)
    
    print("Binary Result:", binary_result)
    
    # Reverse operation: convert binary string to plaintext
    flag = [int(binary_result[i:i + 8], 2) for i in range(0, len(binary_result), 8)]
    plaintext = ''.join(chr(i) for i in flag)
    
    print("Plaintext:", plaintext)

if __name__ == "__main__":
    main()
