import csvcells
import sys


if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'missing arguments...'
		sys.exit(1)
	args = sys.argv[1:]
	problemCsvFile = args[0]
	jobCsvFile = args[1]
	outputCsvFile = 'test.csv'
	if (len(args) > 2):
		outputCsvFile = args[2]
	#csvcells.testStartRowCol('test.csv')
	print 'problem file: ' + problemCsvFile
	print 'job file: ' + jobCsvFile
	print 'output file: ' + outputCsvFile
	raw_input('press enter to continue...')
	problemData = csvcells.getData(problemCsvFile)
	jobData = csvcells.getData(jobCsvFile)
	listData = csvcells.getListData(problemCsvFile)
	changedData = []
	for pkey in problemData:
		if not pkey in jobData: continue
		pValue = problemData[pkey]
		jValue = jobData[pkey]
		cValue = (pValue.rowIndex, pValue.colIndex, round(jValue.value/pValue.value, 2))
		changedData.append(cValue)
	rowIndex = 0
	for c in changedData:
		listData[c[0]][c[1]] = c[2]
	csvcells.writeListData(outputCsvFile, listData)