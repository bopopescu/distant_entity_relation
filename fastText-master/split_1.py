f= open('output.csv','r')
#limerick_line = []
import numpy
count=0
fin=[]
for line in f:
       # cleaned_line = line.replace("http://rdf.freebase.com/ns/",'')
        #print(line)
	#line.split()
        a=numpy.asarray(line.split())
        f1=open('relationship_embedding.csv','a+')
        f1.write(a)
        f1.close()
        count=count+1
        #count=count+1
        #f1=open('relationship_embedding.csv','a+')
        #f1.write(line.split())
        #f1.close()
f.close()
#print(numpy.size(limerick_line))
