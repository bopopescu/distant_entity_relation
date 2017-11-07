f= open('distant-entity-relation/counts_clipped.csv','r')
for line in f:
	cleaned_line = line.replace("http://rdf.freebase.com/ns/",'')
	print(cleaned_line)
	f1=open('labels_list_clipped_count.txt','a')
	f1.write(cleaned_line)
	f1.close()
f.close()
