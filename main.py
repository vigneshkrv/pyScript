import numpy as np
import random
arr = np.array([10,20,30,40])
pyscript.write('output4',f"my array is {arr}")

def shuffle_array(*args):
    shuffled=sorted(arr, key=lambda k:random.random())
    pyscript.write('output4',f"shuffled array is {shuffled}")