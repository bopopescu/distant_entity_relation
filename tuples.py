import csv
import numpy

#a=numpy.array([1000,1])
with open('labels_list_clipped_count.txt') as csvfile:
	reader = csv.reader(csvfile,delimiter='.') #csv.reader(f, delimiter=',')
        count=0
#	print(reader)
        for rid,row in enumerate(reader):
	#	print(rid)
		if len(row)==3:	
			a=row[0]
			b='user'
	        	#print(type(a))
			if a is not 'user' or 'base':
				print(row[0])
