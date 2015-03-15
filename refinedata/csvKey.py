import csv
import sys

class addData:
	def __init__(self):
		pass
	def setNumCols(self, numCols):
		self.numCols = numCols	# number column names
	def setCols(self, cols):
		self.cols = cols # key column names
	def setObjDict(self, objDict):
		self.objDict = objDict

class eqList:
	''' equal object for a list '''
	def __init__(self, keys):
		self.keys = keys

	def __hash__(self):
		return hash(str(self))

	def __eq__(self, other):
		this = str(self)
		that = str(other)
		return this == that

	def __str__(self):
		return str(self.keys)

def fd_task(fl_name, fd_title, task_title):
#fd_title is row 1st: to find the field col. 
#task_title is row 1st: to find the chose field col. 
#taskValues in the same col of task title and to define the col function. 
	Handler=open(fl_name, 'rb')
	csvData=csv.DictReader(Handler)
	tasks = {}
	for line in csvData:
		taskValue = line[task_title]
		if len(taskValue) == 0: continue
		if taskValue not in tasks: tasks[taskValue] = []
		tasks[taskValue].append(line[fd_title])
	return tasks

def getData(datafile, fd_dict, extraDict):
#purpose: to get data with defined fields. fields with x tag need to be combined; fields with cal tag need to be sum up.
#fd_dict has two type of data deal method. x->combine these fields; cal->calculate these fields.
#data file has the raw data
#note: mark is to separate the field later
	comb='x'; sumup='cal'
	file_handle=open(datafile, 'rb')
	csvData=csv.DictReader(file_handle)
	datastream={}
	aData = addData()
	kk = []
	for fd in fd_dict[comb]:
		kk.append(fd)	
	aData.setCols(kk)
	ncs = []
	for c in fd_dict[sumup]:
		ncs.append(c)
	aData.setNumCols(ncs)
	count = 0
	for line in csvData:
		if line[fd_dict[comb][0]]!="":

			keys = []
			need_include = True
			if len(extraDict) == 0:
				for fd in aData.cols:
					keys.append(line[fd])						
			else:
				for fd in aData.cols:
					if fd not in extraDict:
						keys.append(line[fd])
					elif line[fd] != extraDict[fd]:
						need_include = False
						break
			if not need_include: continue

			obj = eqList(keys)
			if obj not in datastream:
				datastream[obj] = {}
				for cal in fd_dict[sumup]:
					datastream[obj][cal]=int(line[cal])
			else:
				for cal in fd_dict[sumup]:
					datastream[obj][cal]+=int(line[cal])

			# for fd in fd_dict[comb]:
			# 	fdtemp+=mark+line[fd]
			# if fdtemp not in datastream:
			# 	for cal in fd_dict[sumup]:
			# 		datastream[fdtemp]=line[cal]
			# else:
			# 	for cal in fd_dict[sumup]:
			# 		datastream[fdtemp]+=line[cal]
	aData.setObjDict(datastream)	
	return aData

def csvDataWrite(outputfile, aData):
	row=list()
	output = open(outputfile, 'wb')
	csvWriter = csv.writer(output)
	count = 0
	datastream = aData.objDict
	numCols = aData.cols[:]
	for n in aData.numCols:
		numCols.append(n)
	csvWriter.writerow(numCols)
	for fd in datastream:
		keys = fd.keys[:]
		for n in aData.numCols:
			keys.append(datastream[fd][n])		
		csvWriter.writerow(keys)	
		#csvWriter(datastream[fd])
		
def selectTable(jobData, problemData, extraDictInProblem):
	extraValues = []
	indexKeys = []
	for i in extraDictInProblem:
		indexKeys.append(i)

	newjobData = addData()
	newCols = jobData.cols[:]
	for i in indexKeys:
		newCols.append(i) # add column keys
	newjobData.setCols(newCols)

	newNumCols = jobData.numCols[:]
	for i in problemData.numCols:
		newNumCols.append(i) # add number column keys
	newjobData.setNumCols(newNumCols)

	datastream = {}
	for jd in jobData.objDict:			
		newKeys = jd.keys[:]

		for i in indexKeys:
			newKeys.append(extraDictInProblem[i])
	
		newObj = eqList(newKeys)
		if newObj not in datastream:

			datastream[newObj] = {}
			for (k,v) in jobData.objDict[jd].items():
				datastream[newObj][k] = v
		if jd not in problemData.objDict:
			for ni in problemData.numCols:
				datastream[newObj][ni] = 0
		else:
			for d in problemData.objDict[jd]:
				datastream[newObj][d] = problemData.objDict[jd][d]

	newjobData.setObjDict(datastream)

	return newjobData

if __name__ == '__main__': 

	extraDict = {'Issue': 'Toner Explosions', 'Issue Category':'PQ Ranking'}
	proTasks=fd_task("keys.csv", 'pro','pro-key')
	pData=getData("pro.csv", proTasks, extraDict)
	print len(pData.objDict)

	csvDataWrite("test.csv", pData)

	jobTasks = fd_task('keys.csv', 'jobs', 'jobs-key')
	jData = getData('jobs.csv', jobTasks, {})

	newData = selectTable(jData, pData, extraDict)

	csvDataWrite("testNew.csv", newData)