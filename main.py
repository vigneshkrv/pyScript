import numpy as np
import random
from utils import add_class

output_el = Element('output4').element

#prints the element tag itself
console.log(output_el)

arr = np.array([10,20,30,40])
# pyscript.write('output4',f"Original array is {arr}")  
output_el.innerHTML=f"Original array is {arr}"

def shuffle_array(*args):
    #shuffle array
    shuffled=sorted(arr, key=lambda k:random.random())

    #chnage color using another .py file
    add_class(output_el,"text-blue-500")
    # pyscript.write('output4',f"Shuffled array is {shuffled}")
    output_el.innerHTML=f"Shuffled array is {shuffled}"