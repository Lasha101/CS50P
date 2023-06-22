import re

# Define the main function
def main():
    # Prompt the user to enter an IPv4 address and pass it to the validate function
    print(validate(input("IPv4 Address: ")))

# Define the validate function
def validate(ip):
    # Define the regular expression pattern for matching an IPv4 address
    reg_ex = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"
    # Use re.search to find a match for the pattern in the given IP address
    matches = re.search(r"^" + reg_ex + "\." + reg_ex + "\." + reg_ex + "\." + reg_ex + "$", ip)
    # If a match is found, return True
    if matches:
        return True
    # If no match is found, return False
    else:
        return False

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function
    main()
