import arithmetic_arranger
from test_module import test_module


ask_testing = input('are you want to run testing auto ?(y/n)\n')
if 'y' in ask_testing or 'Y' in ask_testing:
   for prob, show in test_module:
      print(arithmetic_arranger.arithmetic_arranger(prob,show))
else:
   # init variable
   ask = True
   problems=[]

   while ask == True:
      input_problem = input('Type your arithmetic operation... \n')
      problems.append(input_problem) # fill problems with input
      ask = input("add any operation ? (y/n)\n")
      if 'y' in ask or 'Y' in ask:
         ask = True
      elif 'N' in ask or 'n' in ask:
         ask =  False
      else:
         input_problem = input('Type your arithmetic operation... \n')

   show_answer = input('Show Answer ? (Y/N) \n') # show answer
   if 'y' in show_answer or 'Y' in show_answer: # Check show answer
      show_answer = True
   elif 'N' in show_answer or 'n' in show_answer:
      show_answer =  False
   else:
      show_answer = input('Show Answer ? (Y/N) \n')

   # Print and call dunction arithmetic
   print(arithmetic_arranger.arithmetic_arranger(problems, show_answer))