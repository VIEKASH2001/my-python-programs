#operators in numpy

#size
#shape
#printing the array matrix
#using for loop on np array
#reshaping
#slicing
#linspace
#min
#max
#sum
#sum of axis
#square root
#standard deviation: we find the mean of all the elements in the array and find by how much each element deviate from the mean
#addition,multiplication,subtraction,division---all these happen element wise
#concatination
#arange
#special functions: trignometric function, loagaritmic,exponential


import numpy as np

#size,shape and printing
a=np.array([(1,2,3,4,5,6,7),(8,9,10,11,12,13,14),(8,9,10,11,12,13,14)]) #2D array (2,7)
print(a.size) #gives the total number of elements = rxc
print(a.shape) #gives number of rows and number of columns as (r,c)
print(a) #prints in matrix format
for x in np.nditer(a): #using for loop on np array
    print(x)

#reshaping: we can change the no.of rows and columns of the array
b=a.reshape(7,3)
print(b)

#slicing: to slice out a particular part of an array
print(a[0,2]) #gives the element in the position (0,2)
print(a[0:,3]) #0: means from zeroth row till the last row all elements of column 3 will be printed
print(a[0:2,3])#to print only 3rd element of 0th and 1st row


#line spacing: syntax: np.linspace(initial number,final number, number of equaly spaced values to be displayed between initial and final numbers including the initial and final number)
c=np.linspace(1,3,5)
print(c)


print(a.max())
print(a.min())
print(a.sum())#sum of all elements



#the rows are called axis 1
#the columns are called axis 0
d=np.array([(1,4,9),(9,16,25)])
print(d.sum(axis=0))#sum of elements in each column
print(d.sum(axis=1))#sum of elements in each row

#sqrt and std deviation
print(np.sqrt(d))# gives square root of each element in array format
print(np.std(d))

#addition,multiplication,subtraction,division

e=np.array([(1,4,9),(9,16,25)])
f=np.array([(1,4,9),(9,16,25)])

print(e+f)#happens element wise
print(e-f)
print(e*f)
print(e/f)

#concatination
print(np.vstack((e,f)))#verticle stacking/concatination
print(np.hstack((e,f)))#horizontal stacking/concatination
print(e.ravel())#convert 2D array into a 1D array

#arange: returns an array with evenly spaced elements as per the interval : [start,stop)
#syntax: np.arange(start,stop,step,dtype)
#start : [optional] start of interval range. By default start = 0
#stop  : end of interval range
#step  : [optional] step size of interval. By default step size = 1,For any output out, this is the distance between two adjacent values, out[i+1] - out[i]. 
#dtype : type of output array
#Length of array being generated  = Ceil((Stop - Start) / Step)
g=np.arange(4,10,3)
print(g)

#special functions
import matplotlib.pyplot as plt

print(np.pi)#gives the value of pi

#trignometric functions

#domain x
x=np.arange(0,3*np.pi,0.1)#gives a value set between 0 and 3pi with steps 0.1
#function y and z andr
y=np.sin(x) # also can do for cos and tan
plt.plot(x,y)# to plot a graph---plt is a key word
plt.show()# to display the graph


#exponential and logarithmic functions
h=np.array([1,2,3])
print(np.exp(h))#e^x
print(np.log(h))#natural log
print(np.log10(h))#log base 10


















