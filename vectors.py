import numpy as np
import math
arr1=np.array([1,-2,3,-4,5])
arr2=np.array([2,-4,6,-8,10])
mag1=np.linalg.norm(arr1)
mag2=np.linalg.norm(arr2)
print(f"Magnitude of vector_1 : {mag1}")
print(f"Magnitude of vector_2 : {mag2}")
print(f"Dot Product : {np.dot(arr1,arr2)}")
print(f"Angle between vectors : {math.degrees(math.acos(np.dot(arr1,arr2)/(mag1*mag2)))}")