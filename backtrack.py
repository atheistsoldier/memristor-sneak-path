from crossbar_simulator import *

# choose all memristors
# for each memristor test all paths containing memristor
# if any path returns ideal current then consideration is wrong
# backtrack and check some other memristor

class backtrack:
	def __init__(self, m, n):
		self.m = m
		self.n = n
		self.detected_faulty_wordline=-1
		self.detected_faulty_bitline=-1

	def locate_faulty_memristor(self):
		m = self.m
		n = self.n
		simul = crossbar_simulator(m,n)

		# testing all m*n memristors for fault one by one
		for i in range (0,n):
			for j in range (0,m):
				
				# assume that current memristor is faulty
				fault = 1
				
				# test all rows, keeping column (where current memristor 
				# is located) fixed, to see if current flowing in the path
				# formed by that row and column is ideal or not
				for a in range (0,n):
					fault = simul.detect_current(a,j)
					# if current value in path is ideal, assumption is wrong
					# so no need to check any other path containing memristor
					if(fault == 2):
						break
				# if current value in path is ideal, assumption is wrong
				# so no need to check different column combinations, we
				# can now start with the next memristor
				if fault == 2:
					continue
				
				# test all columns, keeping row (where current memristor 
				# is located) fixed, to see if current flowing in the path
				# formed by that row and column is ideal or not
				for b in range (0,m):
					fault = simul.detect_current(i,b)
					# if current value in path is ideal, assumption is wrong
					# so no need to check any other path containing memristor
					if(fault == 2):
						break
				# if current value in path is ideal, assumption is wrong
				# so we need to skip the print and instead start with the
				# next memristor
				if fault == 2:
					continue

				# if we didn't skip the loop it means fault value stayed 1
				# for all rows and columns containing the current memristor 
				# in its path, i.e all paths recorded a faulty current value
				# which means we have successfully located the faulty memristor
				self.detected_faulty_wordline = i
				self.detected_faulty_bitline = j
				# verify fault location with tester code and print results
				if(simul.verify_fault([self.detected_faulty_wordline,self.detected_faulty_bitline])):
					print(f"Fault found at [{self.detected_faulty_wordline},{self.detected_faulty_bitline}] and verified successfully")
				else:
					print(f"Fault found at [{self.detected_faulty_wordline},{self.detected_faulty_bitline}] and not verified successfully")
				
				return

# creating a 5*5 memristive crossbar randomly initialized
# with a faulty memristor location
temp = backtrack(5,5)
# locate and print location of faulty memristor using 
# backtracking algorithm
temp.locate_faulty_memristor()
