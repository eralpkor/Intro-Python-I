# Write a function is_even that will return true if the passed-in number is even.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# YOUR CODE HERE
def is_even(n):
  return n % 2 == 0

print(is_even(1))

# Read a number from the keyboard
num = input(f"{bcolors.BOLD}Enter a number: {bcolors.ENDC}")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
# if is_even(num):
#   print(f'{bcolors.OKBLUE}Even!{bcolors.ENDC}')
# else:
#   print(f'{bcolors.WARNING}Odd{bcolors.ENDC}')

print(f'Even!' if is_even(num) else 'Odd')
