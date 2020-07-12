"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print("Command line arguments:")
for my_arg in sys.argv:
    print(my_arg)

# Print out the OS platform you're using:

print("Platform:")
print(sys.platform)

# Print out the version of Python you're using:
print("Python version:")
version = sys.version_info
print(str(version.major) + "." + str(version.minor) + "." + str(version.micro))

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("Current process ID:")
print(os.getpid())

# Print the current working directory (cwd):
print("Current working directory:")
print(os.getcwd())

# Print out your machine's login name
print("Current login:")
print(os.getlogin())
