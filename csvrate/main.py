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
	csvcells.testStartRowCol(problemCsvFile)
	print 'problem file: ' + problemCsvFile
	print 'job file: ' + jobCsvFile
	print 'output file: ' + outputCsvFile
	raw_input('press enter to continue...')
	problemData = csvcells.getData(problemCsvFile, True)
	jobData = csvcells.getData(jobCsvFile, False)
	listData = csvcells.getListData(problemCsvFile)

	changedData = []
	for pkey in problemData:
		if not pkey in jobData: continue
		pValue = problemData[pkey]
		jValue = jobData[pkey]
		if pValue.value == 0 and jValue.value != 0:
			print 'NA Key: ' + str(pkey)
			pjv = 'NA/'+str(jValue.value)
		else:
			pjv = round(jValue.value/pValue.value, 2)

		cValue = (pValue.rowIndex, pValue.colIndex, pjv)
		changedData.append(cValue)
	rowIndex = 0
	for c in changedData:
		listData[c[0]][c[1]] = c[2]
	csvcells.writeListData(outputCsvFile, listData)