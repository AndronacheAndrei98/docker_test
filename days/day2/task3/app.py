import time
import os
import sys

def main():
    print("Starting application...")
    print("This application will consume memory until it crashes")
    print("To fix it, you need to run the container with memory limits")
    print("For example: docker run --memory=100m day2-task3")
    print("\nStarting memory consumption in 5 seconds...")
    time.sleep(5)
    
    # Check if the container has memory limits set
    try:
        with open('/sys/fs/cgroup/memory/memory.limit_in_bytes', 'r') as f:
            memory_limit = int(f.read().strip())
            host_memory = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
            
            # If the memory limit is close to host memory, then no real limit was set
            if memory_limit > 0.9 * host_memory:
                print("No memory limit detected! Container will likely crash.")
            else:
                print(f"Memory limit detected: {memory_limit / (1024*1024):.2f} MB")
                
                # If memory limit is reasonable, don't crash
                if memory_limit < 200 * 1024 * 1024:  # Less than 200MB
                    print("\n" + "="*50)
                    print("SUCCESS! You've set appropriate memory limits!")
                    print("The container now runs without crashing.")
                    print("="*50 + "\n")
                    
                    print("Application running normally...")
                    while True:
                        time.sleep(10)
                        print("Still running...")
                    return
    except Exception as e:
        print(f"Could not detect memory limits: {e}")
        print("Continuing with memory consumption test...")
    
    # If we get here, we'll consume memory until crash
    memory_hog = []
    chunk_size = 10 * 1024 * 1024  # 10MB chunks
    
    try:
        while True:
            memory_hog.append(' ' * chunk_size)
            total_mb = len(memory_hog) * chunk_size / (1024 * 1024)
            print(f"Allocated {total_mb:.2f} MB of memory")
            time.sleep(0.1)
    except MemoryError:
        print("OUT OF MEMORY! Container is crashing...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 