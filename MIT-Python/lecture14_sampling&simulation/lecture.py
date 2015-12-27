import random, pylab

def flipPlot(minExp, maxExp):
	ratio = []
	diffs = []
	xAxis = []

	for exp in range(minExp, maxExp):
		xAxis.append(2**exp)
	for numFlips in xAxis:
		numHeads = 0
		for n in range(numFlips):
			if random.random() < .5:
				numHeads += 1
		numTails = numFlips - numHeads
		ratio.append(numHeads / float(numTails))
		diffs.append(abs(numHeads - numTails))
	
	pylab.title('Difference Between Heads and Tails')
	pylab.xlabel('Number of Flips')
	pylab.ylabel('Abs(#Heads - #Tails)')
	pylab.plot(xAxis, diffs)
	
	pylab.figure()
	pylab.plot(xAxis, ratio)
	pylab.title('Heads/Tails Ratios')
	pylab.xlabel('Number of Flips')
	pylab.ylabel('Heads/ Tails')
	
	pylab.figure()
	pylab.title('Difference Between Heads and Tails')
	pylab.xlabel('Number of Flips')
	pylab.ylabel('Abs(#Heads - #Tails')
	pylab.plot(xAxis, diffs, 'bo')
	pylab.semilogx()
	pylab.semilogy()

	pylab.figure()
	pylab.plot(xAxis, ratio, 'b^')
	pylab.title('Heads/Tails Ratios')
	pylab.xlabel('Number of Flips')
	pylab.ylabel('Heads/Tails')
	pylab.semilogx()


if __name__ == '__main__':
	flipPlot(4, 20)
	pylab.show()