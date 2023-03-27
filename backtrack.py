from crossbar_simulator import *

# choose all memristors
# for each memristor test all paths containing memristor
# if any path returns ideal current then consideration is wrong
# backtrack and check some other memristor

class backtack:
	def __init__(self, m, n):
		self.m = m
		self.n = n
		self.detected_faulty_wordline=-1
		self.detected_faulty_bitline=-1

	def locate_faulty_memristor(self):
		m = self.m
		n = self.n
		simul = crossbar_simulator(5,5)

		for i in range (0,n):
			for j in range (0,m):
				
				fault = 1
				
				for a in range (0,n):
					fault = simul.detect_current(a,j)
					if(fault == 2) :
						break
				if fault == 2:
					continue
				
				for b in range (0,m):
					fault = simul.detect_current(i,b)
					if(fault == 2):
						break
				if fault == 2:
					continue

				self.detected_faulty_wordline = i
				self.detected_faulty_bitline = j
				if(simul.verify_fault([self.detected_faulty_wordline,self.detected_faulty_bitline])):
					print(f"Fault found at [{self.detected_faulty_wordline},{self.detected_faulty_bitline}] and verified successfully")
				else:
					print(f"Fault found at [{self.detected_faulty_wordline},{self.detected_faulty_bitline}] and not verified successfully")
				
				return

temp = backtack(5,5)
temp.locate_faulty_memristor()
