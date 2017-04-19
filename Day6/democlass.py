class Employee():
    
    def __init__(self, empId, empName): #self is like "this"
        self.empId = empId
        self.empName = empName
    
    def __str__(self):
        return('ID: '+ str(self.empId) +' Name: ' + self.empName)
            
    def getEmpId(self):
        return self.empId
    
    def getEmpName(self):
        return self.empName
    
       
emp = Employee(101, 'Ankur')

print(emp.getEmpId())
print(emp.getEmpName())
print(emp)
print(getattr(emp, 'empId'))
print(getattr(emp, 'empName'))
print(emp.empId)