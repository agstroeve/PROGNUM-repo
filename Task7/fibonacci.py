class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    def __init__(self, n, M):
        self.cache = [0,1]  # starting numbers 
        self.dd = n
        self.ss = M
    def __call__(self):
        if self.dd < len(self.cache):  # if n is already computed return cache 
            return self.cache[n]
        else: 
            a = 0
            b = 1 
            i=len(self.cache)
            while i<self.dd:
                number = a + b   # compute the next fibonacci number 
                self.cache.append(number)  # add calculated value to cache 
                a, b = b, number 
                i+=1
            return self.cache[-1]
        
    def calc(self):
        list1=[]
        for i in self.cache:
            if i%self.ss == 0:
                list1.append(i)
        return(list1)
            
    #def __calc__(self, n): 
    #    list1 = []
    #    for i in self.cache:  # for a number i in the cache 
    #        if i%M == 0:  # if can be divided by M
    #            list1.append(i)
    #        print(list1)

term = Fibonacci(100, 7)
print(term.__call__())
print(term.calc())