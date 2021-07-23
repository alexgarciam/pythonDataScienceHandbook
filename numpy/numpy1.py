import numpy as np

print(np.__version__)

#integer array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#float32 array
arr2 = np.array([1, 2, 3, 4, 5], dtype='float32')
print(arr2)

np.random.seed(0)

x1=np.random.randint(10, size=6)
x2=np.random.randint(10, size=(3, 4))
x3=np.random.randint(10, size=(3, 4, 5))

print("x2: ", x2)
print("x2 ndim: ", x2.ndim)
print("x2 shape:", x2.shape)
print("x2 size: ", x2.size)
print("dtype:", x2.dtype)

print(x2[2, 0])
print("dtype: ", x3.dtype)

print("size: ", x2.size)
print("itemSize: ", x2.itemsize)
print("nbytes: ", x2.nbytes)

print(x1)
print(x1[0])
print(x1[4])

print(x1[-1])
print(x1[-2])

print(x2)
print(x2[0,0])

#substrings
x = np.arange(10)
print(x)
print(x[:5])
print(x[5:])
print(x[4:7])
print(x[::2])

print(x[::-1])
print(x[5::-2])
print("----------------------")
print(x2)
print(x2[:,:])

x2_sub = x2[:2, :2]
print(x2_sub)
x2_sub[0, 0] = 99
print(x2_sub)

print(x2)

x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)
x2_sub_copy[0, 0] = 42
print(x2_sub_copy)
print(x2)



#Reshaping arrays
print("")
print("#Reshaping arrays")
print("----------------------------------")

grid = np.arange(1, 10)
print(grid)
grid = np.arange(1, 10).reshape((3, 3))
print(grid)