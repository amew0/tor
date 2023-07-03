# import time
# import sys

# outer_loop_iterations = 3
# inner_loop_iterations = 5
# def print_(str="",end="\n"):
#     sys.stdout.write(f"{str}{end}")
#     sys.stdout.flush()

# for i in range(outer_loop_iterations):
#     print_(f"\nOuter Loop Iteration: {i+1}")

#     for j in range(inner_loop_iterations):
#         print_(f"\tInner Loop Iteration: {j+1}","\r")
#         time.sleep(0.5)
#     print_()
# print_("\nFinished!")

from tqdm import tqdm
import time
a=tqdm(range(10))
print(tqdm)
# Create a loop with tqdm
for i in a:
    # Do some work
    time.sleep(0.5)
    
    
    # Update the progress bar with additional text
    a.set_postfix({'text':f'Step {i+1}'})
    a.set

