import numpy

arr = [numpy.random.randint(4250,4270) for i in range(20)]

arr = numpy.array(arr)

print(arr)

print(arr.shape)

arr = arr/arr[0]

print(arr-1)

sign = []

for i in range(len(arr)):

    if arr[i]>0:

        sign.append('up')

    else:

        sign.append('down')

print(sign)
