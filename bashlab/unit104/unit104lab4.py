# Objectives

# The Python library “os” must be utilized
# At least three variables must be declared in Python that contain bash operations
# Use the python os function to print the following commands below.  These are bash commands and we are going to run them through a python script.
# Add description printed to the terminal of what is about to run



# whoami
# ip a
# lshw -short
# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.
# Instead of os.system() function, utilize the subprocess module instead. Refer to python.org for how this can be achieved.



# This will not run on windows needs to be mac or linux due to os being bash

import subprocess
import os
import platform

# Define bash commands as variables
user_command = "whoami"
ip_command = "ip a" 
hardware_command = "lshw -short"

# Detect operating system
system = platform.system().lower()

print(f"\nDetected Operating System: {platform.system()}")

if system == "linux":
    # Linux commands
    print("\nShowing current user:")
    os.system(user_command)

    print("\nShowing network interfaces:")
    os.system(ip_command)

    print("\nShowing hardware information:")
    os.system(hardware_command)

elif system == "darwin":  # macOS
    # Adjust commands for macOS
    print("\nShowing current user:")
    os.system(user_command)

    print("\nShowing network interfaces:")
    os.system("ifconfig")  # macOS equivalent of 'ip a'

    print("\nShowing hardware information:")
    os.system("system_profiler SPHardwareDataType")  # macOS equivalent of 'lshw'

elif system == "windows":
    # Windows commands
    print("\nShowing current user:")
    os.system("whoami")

    print("\nShowing network interfaces:")
    os.system("ipconfig")  # Windows equivalent of 'ip a'

    print("\nShowing hardware information:")
    os.system("systeminfo")  # Windows equivalent of 'lshw'

else:
    print("Unsupported operating system")
