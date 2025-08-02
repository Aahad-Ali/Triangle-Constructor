class Triangle:

    object_count = 0

    def __init__(self,sideA=1.0,sideB=None,sideC=None):
        if isinstance(sideA,Triangle):
         self.__sideA=sideA.sideA
         self.__sideB=sideA.sideB
         self.__sideC=sideA.sideC
        
        else:
            if sideB is None or sideC is None:
                #Equilateral triangle
                self.__sideA = sideA
                self.__sideB = sideA
                self.__sideC = sideA

            elif sideC is None:
            #isosceles triangle
                self.__sideA = sideA
                self.__sideB = sideA
                self.__sideC = sideB

            else:
                #Scalene triangle
                self.__sideA = sideA
                self.__sideB = sideB
                self.__sideC = sideC

#Increment object count
        Triangle.object_count += 1

#getter and setter for sideA
    @property
    def sideA(self):
        return self.__sideA
    
    @sideA.setter
    def sideA(self,value):
        if value > 0:
            self.__sideA = value
        else:
            print("Side A must be positive.")
            
            #getter and setter for sideA


#getter and setter for sideB
    @property
    def sideB(self):
        return self.__sideB
    
    @sideB.setter
    def sideB(self,value):
        if value > 0:
            self.sideB = value
        else:
            print("Side B must be positive.")
            
            #getter and setter for sideB


#getter and setter for sideC
    @property
    def sideC(self):
        return self.__sideC
    
    @sideC.setter
    def sideC(self,value):
        if value > 0:
            self.sideC = value
        else:
            print("Side C must be positive.")
            
            #getter and setter for sideC


    def perimeter(self):
        return self.__sideA + self.__sideB + self.__sideC
    
    def is_right_angled(self):
        sides = sorted([self.__sideA, self.__sideB, self.__sideC])
        a ,b,c=sides
        return abs(a**2 + b**2 - c**2) < 1e-9
    
    def __str__(self):
        return  f"Triangle with sides:{self.__sideA}, {self.__sideB},{self.__sideC}"
    
    
    
    #total object count
    @classmethod
    def total_objects(cls):
        return cls.object_count