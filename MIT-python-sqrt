raw=raw_input("Enter the data wants to be squared: ")
err=raw_input("Enter the error in this calculation: ")
# minRange=float()
# maxRange=float()

def check_float(data): 
	try: 
		checkData=float(data)
	except: 
		"input error"
	return checkData

rawData=check_float(raw)
error=check_float(err)
# print rawData, "+", error
if rawData<0: 
	print "data is less than 0, cannot do the calculate"
elif rawData>=1: 
	minRange=1
	maxRange=rawData
elif rawData<1:
	minRange=rawData
	maxRange=1

root=(minRange+maxRange)/2
candidata=root*root
while abs(candidata-rawData)>error:
	if candidata>rawData:
		maxRange=root
	else:
		minRange=root
	root=(maxRange+minRange)/2
	candidata=root*root
print root

	
