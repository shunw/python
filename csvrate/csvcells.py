import csv

# column start from the row
startRow = 1

def is_empty(strValue):	
	return strValue is None or len(str(strValue)) == 0

def is_number(strValue):
	try:
		float(strValue)
		return True
	except:
		return False

class cellKeys:
	''' cell keys for a rowIndex and colIndex '''
	def __init__(self, rowKeys, colKeys):
		self.rowKeys = rowKeys
		self.colKeys = colKeys

	def __hash__(self):
		return hash(str(self))

	def __eq__(self, other):
		this = str(self)
		that = str(other)
		return this == that

	def __str__(self):
		return str(self.rowKeys)+', '+str(self.colKeys)


class cellObject:
	''' valid cell to operate '''
	def __init__(self, rowIndex, colIndex, value):
		self.rowIndex = rowIndex
		self.colIndex = colIndex
		self.value    = value		

	def setCellKeys(self, key):
		self.keys = key

	def __str__(self):
		return '(' + str(self.rowIndex)+', '+ str(self.colIndex) +') => ' + str(self.value) + ', '+str(self.keys)

class startRowCol:
	def __init__(self, csvFile):
		self.csvFile = csvFile
		self.startRow = -1
		self.startCol = -1
		self.fileStream = open(csvFile, 'rb')
		self.csvData = csv.reader(self.fileStream, dialect='excel')

	def closeFile(self):
		#self.fileStream.close()
		pass

	def getIndex(self):
		rowIndex = 0
		for row in self.csvData:
			#print str(row)
			if rowIndex > 0: #bypass the first row
				colIndex = 0
				# for col in row:
				# 	if self.startCol == -1 and not is_empty(col):
				# 		#print str(rowIndex) +', '+ str(colIndex) + ': ' + str(row)
				# 		self.startCol = colIndex
				# 		break
				# 	colIndex += 1
				# if self.startCol == -1: continue
				if not is_empty(row[self.startCol-1]): # find the row title index
					self.startRow = rowIndex
					break
			else:
				colIndex = 0
				for col in row:
					if colIndex > 0 and not is_empty(col):
						self.startCol = colIndex
						break
					colIndex += 1
			rowIndex += 1
		self.startRow += 1 # titleRowIndex+1



def getRowKeys(csvList, startRowIndex, rowIndex, startColIndex):
	rowKeys = []
	for c in range(0, startColIndex):
		for r in range(rowIndex, startRowIndex-1, -1):
			if not is_empty(csvList[r][c]):
				rowKeys.append(csvList[r][c])
				break
	return rowKeys


def getColKeys(csvList, startRowIndex, startColIndex, colIndex):
	colKeys = []
	for r in range(startRow, startRowIndex):
		for c in range(colIndex, startColIndex-1, -1):
			if not is_empty(csvList[r][c]):
				colKeys.append(csvList[r][c])
				break
	return colKeys

def testStartRowCol(csvFile):
	''' test get the start rowIndex and the start columnIndex '''
	src = startRowCol(csvFile)
	src.getIndex()
	print str(src.startRow) + ", " + str(src.startCol)

def getListData(csvFile):
	fileStream = open(csvFile, 'rb')
	csvData = csv.reader(fileStream)
	csvList = []
	for r in csvData:
		csvList.append(r)
	return csvList

def writeListData(csvFile, listData):
	fileStream = open(csvFile, 'wb')
	csvWriter = csv.writer(fileStream)
	csvWriter.writerows(listData)

def getData(csvFile, includeEmpty):
	''' get a cellObject list for a csv file '''
	startInfo = startRowCol(csvFile)
	startInfo.getIndex()
	fileStream = open(csvFile, 'rb')
	csvData = csv.reader(fileStream)
	cellDict = {}
	csvList = []
	rowIndex = 0
	for row in csvData:
		csvList.append(row)
		if rowIndex < startInfo.startRow: 
			rowIndex+=1 
			continue
		colIndex = 0
		for col in row:
			if colIndex < startInfo.startCol:
				colIndex += 1
				continue
			if includeEmpty or is_number(col):
				rowKeys0 = getRowKeys(csvList, startInfo.startRow, rowIndex, startInfo.startCol)
				colKeys0 = getColKeys(csvList, startInfo.startRow, startInfo.startCol, colIndex)
				keys = cellKeys(rowKeys0, colKeys0)
				if includeEmpty:
					print 'keys:' + str(rowIndex)+ str(colIndex)
				fv = 0
				if not is_empty(col):
					try:
					 	fv = float(col)
					except Exception,e:
					 	print 'err pos: ' + str(rowIndex) +', ' + str(colIndex)
					 	raise e
					
				cell0 = cellObject(rowIndex, colIndex, fv)
				cell0.setCellKeys(keys)
				cellDict[keys]=cell0
			colIndex += 1
		rowIndex += 1
	return cellDict