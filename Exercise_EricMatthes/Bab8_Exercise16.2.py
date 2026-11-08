# 1. import module_name
import my_function
my_function.greet()

# 2. from module_name import function_name
from my_function import greet
greet()

# 3. from module_name import function_name as fn
from my_function import greet as fn
fn()

# 4. import module_name as mn
import my_function as mn
mn.greet()

# 5. from module_name import*
from my_function import *
greet()