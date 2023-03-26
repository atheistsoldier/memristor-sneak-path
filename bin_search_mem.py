import crossbar_simulator
class bin_search_mem:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.detected_faulty_wordline=-1
        self.detected_faulty_bitline=-1

    def set_faulty_bitline(self,simul,wordline_ok):
        bitline_start=1
        bitline_end=self.n-1
        while(bitline_start<=bitline_end):
            mid_bitline_range=(bitline_start+bitline_end)//2
            if(simul.detect_current_range([[wordline_ok,wordline_ok]],[[bitline_start,mid_bitline_range]])==2):
                bitline_start=mid_bitline_range+1
            else:
                bitline_end=mid_bitline_range-1
            self.detected_faulty_bitline=mid_bitline_range
    
    def set_faulty_wordline(self,simul,bitline_ok):
        wordline_start=1
        wordline_end=self.m-1
        while(wordline_start<=wordline_end):
            mid_wordline_range=(wordline_start+wordline_end)//2
            if(simul.detect_current_range([[wordline_start,mid_wordline_range]],[[bitline_ok,bitline_ok]])==2):
                wordline_start=mid_wordline_range+1
            else:
                wordline_end=mid_wordline_range-1
            self.detected_faulty_wordline=mid_wordline_range
                
    def bin_search(self):
        m=self.m
        n=self.n
        simul=crossbar_simulator.crossbar_simulator(m,n)
        bitline=0
        wordline=0
        if(simul.detect_current(wordline,bitline)==2): #first input vector passes
            #first wordline and bitline is not faulty
            self.set_faulty_bitline(simul,wordline_ok=0)
            self.set_faulty_wordline(simul,bitline_ok=0)
        else:
            bitline=1
            if(simul.detect_current(wordline,bitline)==2): #second input vector passes
                #first bitline is faulty
                self.detected_faulty_bitline=0
                self.set_faulty_wordline(simul,bitline_ok=1)#second bitline is working
            else:
                #first wordline is faulty
                self.detected_faulty_wordline=0
                self.set_faulty_bitline(simul,wordline_ok=1)#second wordline is working
        
        if(self.detected_faulty_wordline==-1 or self.detected_faulty_bitline==-1):
            print("Fault detection unsucessful")      
        elif(simul.verify_fault([self.detected_faulty_wordline,self.detected_faulty_bitline])):
            print(f"Fault found at [{self.detected_faulty_wordline},{self.detected_faulty_bitline}] and verified successfully")
        else:
            print(f"Fault found at [{self.detected_faulty_wordline},{self.detected_faulty_bitline}] and not verified successfully")
            
temp=bin_search_mem(10,10)
temp.bin_search()