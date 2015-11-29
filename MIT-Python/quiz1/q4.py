def findAll(wordList, lStr):
	 """
	 assumes: 
	 	wordList is a list of words in lowercase.
	 	lStr is a str of lowercase letters.
	 	No letter occurs in lStr more than once
	 returns: 
	 	a list of all the words in wordList that contain
	 	each of the letters in lStr exactly once and no
	 	letters not in lStr.
	 """
	 result = list()
	 for word in wordList:
	 	if not(set(word).issubset(set(lStr))): continue
	 	
	 	temp = dict()
	 	char_rep = False
	 	for char in list(word):
	 		temp[char] = temp.get('char', 0) + 1
	 		if temp[char] > 1: 
	 			char_rep = True
	 			break
	 	if char_rep == True: continue

	 	result.append(word)

	 return result