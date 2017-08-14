def listfreq(listt,doc):
	print 'list sent to function'
	print listt
	print 'sentence sent to function'
	print doc
	summ=0
	count=0
	for word in listt:
		count=doc.count(word)
		print 'freq of'+word+'is:'
		print count
		summ=summ+count;
	print 'sum'
	print summ
	return summ

doc= "chehak is a nice girl. chehak loves rahil. rahil is a sweetheart"
listt= ["chehak","is","girl","rahil"]
listfreq(listt,doc)