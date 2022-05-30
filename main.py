import numpy as np
import random

output_el = Element('output4').element

#prints the element tag itself
console.log(output_el)

arr = np.array([10,20,30,40])
# pyscript.write('output4',f"Original array is {arr}")  
output_el.innerHTML=f"Original array is {arr}"

def shuffle_array(*args):
    shuffled=sorted(arr, key=lambda k:random.random())
    # pyscript.write('output4',f"Shuffled array is {shuffled}")
    output_el.innerHTML=f"Shuffled array is {shuffled}"