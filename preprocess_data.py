idFile = open('articleID.txt', 'w')
articleFile = open('articleText.txt', 'w')

with open('text_wo_categories.txt') as f:
	for lines in f:
		ID = lines.split(' ',1)[0]
		line = lines.split(' ',1)[1]
		idFile.write(ID)
		idFile.write('\n')
		articleFile.write(line)
		
idFile.close()
articleFile.close()