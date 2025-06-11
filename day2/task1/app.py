import os
import time

def main():
    print("Starting application...")
    
    try:
        # Try to get the required environment variable
        api_key = os.environ['API_KEY']
        
        # If we get here, the environment variable was found
        print(f"API Key found: {api_key[:3]}...{api_key[-3:]} (value obscured for security)")
        print("Application started successfully!")
        
        # Print success message
        print("\n" + "="*50)
        print("SUCCESS! You've fixed the environment variable issue!")
        print("The application needs the API_KEY environment variable to run.")
        print("="*50 + "\n")
        
        # Keep the container running
        print("Application running...")
        while True:
            time.sleep(10)
            print("Still running...")
    
    except KeyError:
        # Environment variable is missing
        print("ERROR: Missing required environment variable: API_KEY")
        print("This application requires the API_KEY environment variable to be set.")
        print("Please run the container with: -e API_KEY=your_api_key")
        exit(1)

if __name__ == "__main__":
    main() 