import crossbar_simulator
class fault_dict_mem:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.fault_dict = [[-1 for _ in range(n)] for _ in range(m)]
        self.detected_faulty_wordline = -1
        self.detected_faulty_bitline = -1

    def eliminate_wordline_and_bitline(self, wordline_tested, bitline_tested):
        for bitline in range(self.n):
            # set all non-faulty or untested bitlines across the wordline as non-faulty
            if self.fault_dict[wordline_tested][bitline] != 1:
                self.fault_dict[wordline_tested][bitline] = 0
        for wordline in range(self.m):
            # set all non-faulty or untested wordlines across the bitline as non-faulty
            if self.fault_dict[wordline][bitline_tested] != 1:
                self.fault_dict[wordline][bitline_tested] = 0

    def set_faulty_wordline(self, eliminated_wordlines):
        for wordline in range(self.m):
            if wordline not in eliminated_wordlines:
                self.detected_faulty_wordline = wordline
                return
            
    def set_faulty_bitline(self, eliminated_bitlines):
        for bitline in range(self.n):
            if bitline not in eliminated_bitlines:
                self.detected_faulty_bitline = bitline
                return

    def fault_dictionary(self):
        simul = crossbar_simulator.crossbar_simulator(self.m, self.n)
        eliminated_wordlines = []       #set of wordlines with no fault detected
        eliminated_bitlines = []        #set of bitlines with no fault detected
        for wordline in range(self.m):
            for bitline in range(self.n):
                if wordline in eliminated_wordlines:
                    break
                if bitline in eliminated_bitlines:
                    continue
                if(simul.detect_current(wordline, bitline) == 2):
                    #wordline and bitline does not consist of faulty memristor
                    self.eliminate_wordline_and_bitline(wordline, bitline)
                    eliminated_wordlines.append(wordline)
                    eliminated_bitlines.append(bitline)
                else:
                    #wordline or bitline has faulty memristor
                    self.fault_dict[wordline][bitline] = 1
        self.set_faulty_wordline(eliminated_wordlines)
        self.set_faulty_bitline(eliminated_bitlines)
        if(self.detected_faulty_wordline == -1 or self.detected_faulty_bitline == -1):
            print("Fault detection unsucessful")      
        elif(simul.verify_fault([self.detected_faulty_wordline, self.detected_faulty_bitline])):
            print(f"Fault found at [{self.detected_faulty_wordline},{self.detected_faulty_bitline}] and verified successfully")
        else:
            print(f"Fault found at [{self.detected_faulty_wordline},{self.detected_faulty_bitline}] and not verified successfully")
            
            
temp = fault_dict_mem(10, 10)
temp.fault_dictionary()
