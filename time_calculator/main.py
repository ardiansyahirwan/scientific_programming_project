import time_calculator
from test_module import time_test

ask_test = input("Do you want to run test auto ? (y/n) \n")
if 'Y' in ask_test or 'y' in ask_test:
   for start, dura, day in time_test:
      print(time_calculator.add_time(start, dura, day))
else:
   print("Thank you")