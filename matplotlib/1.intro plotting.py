import matplotlib.pyplot as plt

#data points
x=[1,2,3,4,5,6,7]
y=[50,51,52,53,54,55,56]

#labeling and titling
plt.xlabel('day')
plt.ylabel('temperature')
plt.title('weather')

#plotting
#plt.plot(x,y,color='green',linewidth=5,linestyle='dotted')#check google for all other possible values it can take

x=[1,2,3,4,5,6,7]
y=[10,51,22,43,54,45,56]

#plt.plot(x,y,'g+--',markersize=20)#displays only points with +-- markers, check the internet for more options

plt.plot(x,y,alpha=2)#controls the transparency of the line

#displaying
plt.show()
