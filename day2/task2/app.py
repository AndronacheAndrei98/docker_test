import time

def main():
    print("Starting application...")
    
    try:
        # Try to open and process the data file
        print("Reading data from data.txt...")
        with open('data.txt', 'r') as file:
            data = file.readlines()
            
            # Parse the data (will crash if format is incorrect)
            total = 0
            for line in data:
                # This will crash if the line isn't a number
                value = int(line.strip())
                total += value
            
            print(f"Data processed successfully! Total: {total}")
            
            # Print success message
            print("\n" + "="*50)
            print("SUCCESS! You've fixed the crashing container issue!")
            print("The application needed valid numeric data in data.txt.")
            print("="*50 + "\n")
            
            # Keep the container running
            print("Application running...")
            while True:
                time.sleep(10)
                print("Still running...")
    
    except FileNotFoundError:
        print("ERROR: Could not find data.txt file!")
        exit(1)
    except ValueError as e:
        print(f"ERROR: Invalid data format in data.txt - {str(e)}")
        print("The file should contain only numbers, one per line.")
        exit(1)
    except Exception as e:
        print(f"ERROR: Unexpected error - {str(e)}")
        exit(1)

if __name__ == "__main__":
    main() 