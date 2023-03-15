class college:
    
    increase_stdf=1.05

    def __init__(self,name,id,fees):
        self.name=name
        self.id=id
        self.fees=fees
        self.email=name+ '.' + '@gmail.com'

    def fullname(self):
        return '{}'.format(self.name)
    
    def increase_fees(self):
        self.fees=int(self.fees * self.increase_stdf)

    '''@classmethod
    def set_raise_fees(cls,amount):
        cls.increase_stdf=amount'''
        #self.fees=self.fees * self.amount
    '''@staticmethod
    def isworkday(day):
        if (day.weekday()==5 or day.weekday()==6):
            return False
        return True'''
class data(college):
     def __init__(self,name,id,fees,height):
         super().__init__(name,id,fees)
         self.height=height

class Teacher(college):
    def __init__(self,name,id,fees,height,stds=None):
        super().__init__(name,id,fees,)

        if stds is None :
            self.stds= []
        else:
            self.stds=stds
            
    def addNew(self,std):
        if std not in self.stds:
            self.stds.append(std)

    def remove(self,std):
        if std in self.stds:
            self.stds.remove(std)

    def print_stds(self):
        for std in self.stds:
            print('>', std.fullname())
         
std_1= data('nithin',100,1000,'1.5m')
std_2= data('kumar',150,1500,'1.6m')

teacher_1= Teacher('Priya',101,10,[std_1 ])

'''import datetime
mydate=datetime.date(2023,3,11)
print(college.isworkday(mydate))'''

'''print(std_1.fees)
std_1.increase_fees()
print(std_1.fees)'''

'''college.set_raise_fees(1.06)
print(std_1.increase_stdf)'''

print(teacher_1.email)
teacher_1.addNew(std_2)
teacher_1.addNew(std_1)
teacher_1.remove(std_2)
teacher_1.print_stds()



