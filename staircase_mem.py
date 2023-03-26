import crossbar_simulator
class staircase:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.detected_wordline=-1
        self.detected_bitline=-1
    def staircase_search(self):
        m=self.m
        n=self.n
        simul=crossbar_simulator.crossbar_simulator(m,n)
        bitline=0
        wordline=0
        while(simul.detect_current(wordline,bitline)!=1): #continues loop until it passes
            wordline+=1
            bitline+=1
        changed_bitline=(bitline+1)%n
        if(simul.detect_current(wordline,changed_bitline)==1):
            #fault in wordline
            self.detected_faulty_wordline=wordline
            changed_wordline=(wordline+1)%m
            for present_bitline in range(bitline,n):
                if(simul.detect_current(changed_wordline,present_bitline)==1):
                    self.detected_faulty_bitline=present_bitline
                    break
                
        else:
            #fault in bitline
            self.detected_faulty_bitline=bitline
            for present_wordline in range(wordline,m):
                if(simul.detect_current(present_wordline,changed_bitline)==1):
                    self.detected_faulty_wordline=present_wordline
                    break
        if(simul.verify_fault([self.detected_faulty_wordline,self.detected_faulty_bitline])):
            print(f"Fault found at [{self.detected_faulty_wordline},{self.detected_faulty_bitline}] and verified successfully")
        else:
            print(f"Fault found at [{self.detected_faulty_wordline},{self.detected_faulty_bitline}] and not verified successfully")
            
temp=staircase(10,10)
temp.staircase_search()