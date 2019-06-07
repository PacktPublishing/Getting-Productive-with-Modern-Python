# Here we'll check the memory consumption of each line of code-

# Importing the profile module-
from memory_profiler import profile


# We are using decoraters to assign with the below function 
# for memory consumption
@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (5 * 10 ** 7)
    del b
    return a
av = my_func()

# while running it will execute the function-
if __name__ == '__main__':
    my_func()
    
