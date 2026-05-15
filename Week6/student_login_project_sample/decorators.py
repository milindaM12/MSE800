from datetime import datetime


# Decorator function used to add logging functionality
def log_activity(func):

    # Wrapper function handles execution of original function
    def wrapper(*args, **kwargs):
        print("===================================")
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}")
        print("Activity started...")

        # Execute original function
        result = func(*args, **kwargs)

        print("Activity completed.")
        print("===================================\n")

        # Return result from original function
        return result
    
    # Return wrapper function
    return wrapper
