import random
class crossbar_simulator:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.faulty_memristor=[random.randrange(m),random.randrange(n)]
    
    def verify_fault(self, expected_faulty_memristor_position):
        if expected_faulty_memristor_position==self.faulty_memristor:
            return True
        else:
            return False
    
    def detect_current(self, activated_bitline_ranges,activated_wordline_ranges):
        for bitline_range in activated_bitline_ranges:
            if(self.faulty_memristor[0]>=bitline_range[0] and self.faulty_memristor[0]<=bitline_range[1]):
                return 1
        for wordline_range in activated_wordline_ranges:
            if(self.faulty_memristor[1]>=wordline_range[0] and self.faulty_memristor[1]<=wordline_range[1]):
                return 1
        return 2

temp=crossbar_simulator(5,6)
print(temp.faulty_memristor)
print(temp.verify_fault(temp.faulty_memristor))
print(temp.detect_current([[temp.faulty_memristor[0],temp.faulty_memristor[0]]], [[2,2]]))