import math

#get base
# inputOK=False
# while not inputOK:
# 	base = input ( "Enter Base: ")
# 	if type(base) == type(1.0): inputOK=True
# 	else: print(" Error: Base must be a floating point number")

# #get height
# inputOK =False
# while not inputOK:
# 	height = input( " Enter Height: ")
# 	if type(height) == type(1.0): inputOK = True
# 	else: print (" Error: Height must be a floating point number")
# hyp=math.sqrt(base**2+height**2)
# print "Base is " +str(base) + " , Height is " + str(height)+" , hpy is " + str(hyp)

def inputOK(name):
	inputOK=False
	while not inputOK:
		data=input( "Enter " + str(name) +": ")
		if type(data)==type(1.0): inputOK=True
		else: print("Error: "+str(name)+" must be a floating point number. ")
	return data

base=inputOK("base")
height=inputOK("height")
hyp=math.sqrt(base**2+height**2)
print  "Base is " +str(base) + " , Height is " + str(height)+" , hpy is " + str(hyp)