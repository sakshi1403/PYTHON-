'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class MedPLus: 
    """" MedPlus Pharmacy """ 
    def __init__(self, name, batchcode, price):
        """" To create new instance of class MedPlus
        name = name of the medicine 
        batchcode = number/code of the batch
        price = total cost of the medicine """ 
        
        self._name = str(name) 
        self._batchcode = int(batchcode) 
        self._price = float(price) 
    
    def get_name(self): 
        """" Return the name of medicine """ 
        return self._name 
    def get_batchcode(self):
        """" Return the batch number/code """
        return self._batchcode 
    def get_price(self): 
        """" Return the price of medicine """ 
        return self._price
First = MedPLus("Meftal Spas", "567432", "76.98")
print("Price of Medicine/Tablet : Rs.",First.get_price()) 
print("Tablet/Medicine name : ",First.get_name()) 
print("Batch Number/Code Oof Medicine/Tablet : ",First.get_batchcode())