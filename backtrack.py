from crossbar_simulator import *

newCrossbar = crossbar_simulator(5,5)
# choose all memristors
# for each memristor test all paths containing memristor
# if any path returns ideal current then consideration is wrong
# backtrack and check some other memristor
def locate_faulty_memristor(m,n):
	for i in range (0,n):
		for j in range (0,m):
			fault = 1
			for a in range (0,n):
				fault = newCrossbar.detect_current(a,j)
				if(fault == 2) :
					break
			if fault == 2:
				continue
			for b in range (0,m):
				fault = newCrossbar.detect_current(i,b)
				if(fault == 2):
					break
			if fault == 2:
				continue
			return (i,j)
#print(newCrossbar._crossbar_simulator__faulty_memristor)
print(locate_faulty_memristor(5,5))
