import csv
import numpy
import pandas as pd

df1=pd.read_csv('1.csv',header=None)
df2=df1.iloc[:,0]
a=df2.values

df3=pd.read_csv('2.csv',header=None)
df4=df3.iloc[:,0]
b=df4.values

df5=pd.read_csv('3.csv',header=None)
df6=df5.iloc[:,0]
c=df6.values

#print(a.size)
u=numpy.unique(a) 
z=u.size
#print(u[0])

for i in range(0,z):

	count=0
	for index, item in enumerate(a):
	
		if item is u[i]:
			if count==0:
				print(u[i])	
				print(b[index]+' '+c[index])
			#print(c[index])
				count=count+1
			else:
			#print('123')
				print(b[index]+' '+c[index])
                        #print(c[index])
				count=count+1
	print('\n')
#print(count)
#df3=df2.name.unique()
#print(df3)
#for num,line in enumerate(f):  
#        print(num)
        
        #f1=open('labels_list_clipped_count.txt','a')
        #f1.write(cleaned_line)
        #f1.close()




#with open('1.csv') as csvfile:
#        reader = csv.reader(csvfile,delimiter='	') #csv.r
#	for row in reader:
#		print(row)
