import random
class crossbar_simulator:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.__faulty_memristor=[random.randrange(m),random.randrange(n)]
    
    def verify_fault(self, expected_faulty_memristor_position):
        if expected_faulty_memristor_position==self.__faulty_memristor:
            return True
        else:
            return False
    
    def detect_current_range(self, activated_wordline_ranges,activated_bitline_ranges):
        for wordline_range in activated_wordline_ranges:
            if(len(wordline_range)!=2):
                raise Exception(wordline_range+"is not a valid wordline range. It should be a list of 2 numbers with lower and upper range")
            if(wordline_range[0]>wordline_range[1]):
                raise Exception(wordline_range+"is not a valid wordline range. Lower range cannot be greater than upper range")
            if(wordline_range[0]<0 or wordline_range[0]>=self.m or wordline_range[1]<0 or wordline_range[1]>=self.m):
                 raise Exception(wordline_range+"is not a valid wordline range. Activated wordline should be less than "+self.m+" and greater than 0")
        
        for bitline_range in activated_bitline_ranges:
            if(len(bitline_range)!=2):
                raise Exception(bitline_range+"is not a valid bitline range. It should be a list of 2 numbers with lower and upper range")
            if(bitline_range[0]>bitline_range[1]):
                raise Exception(bitline_range+"is not a valid bitline range. Lower range cannot be greater than upper range")
            if(bitline_range[0]<0 or bitline_range[0]>=self.n or bitline_range[1]<0 or bitline_range[1]>=self.n):
                 raise Exception(bitline_range+"is not a valid bitline range. Activated wordline should be less than "+self.n+" and greater than 0")
             
        for wordline_range in activated_wordline_ranges:
            if(self.__faulty_memristor[0]>=wordline_range[0] and self.__faulty_memristor[0]<=wordline_range[1]):
                return 1
            
        for bitline_range in activated_bitline_ranges:
            if(self.__faulty_memristor[1]>=bitline_range[0] and self.__faulty_memristor[1]<=bitline_range[1]):
                return 1
        return 2
    
    def detect_current(self,activated_wordline, activated_bitline):
        if(activated_wordline>=self.m or activated_wordline<0):
            raise Exception("activated wordline should be less than "+self.m+" and greater than 0")
        if(activated_bitline>=self.n or activated_bitline<0):
            raise Exception("activated bitline should be less than "+self.n+" and greater than 0")
        if(self.__faulty_memristor[0]== activated_wordline or self.__faulty_memristor[1]==activated_bitline):
            return 1
        return 2

temp=crossbar_simulator(5,6)

print(temp.verify_fault([2,3]))

print(temp.detect_current_range([[2,3]], [[2,2]]))