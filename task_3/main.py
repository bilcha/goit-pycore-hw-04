import sys
from colorama import Fore, Back, Style
from pathlib import Path

def parse_file(path, count = 0):
  for element in path.iterdir():
    if element.is_dir():
      print(" "*count + Fore.BLUE + f"{element.name}\\")
      parse_file(element, count+4)
    else: print(" "*count + Fore.YELLOW + f"{element.name}")


path_arguments = sys.argv

if len(path_arguments) > 1:
  try:
    absolute_path = Path(path_arguments[1])
    print (f"Element {absolute_path}")
    parse_file(absolute_path)
  except FileNotFoundError:
    print(Fore.MAGENTA + f"Wasn't able to find a file")

else: print(Fore.BLUE + f"Please provide path arguments")

