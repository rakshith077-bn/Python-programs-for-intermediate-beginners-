class itmcls(object):
    def __init__(self, name, val, vol):
        self.name = name
        self.val = val
        self.vol = vol
        
    def getvalue(self):
        return self.val
    
    def getvol(self):
        return self.vol
    
    def density(self):
        return (self.val)/(self.vol)
    
    def __str__(self):
        return self.name 
  
# Defining a function for building a bag 
# which generates list of itmcls    
def buildbag(names, values, volumes):
    bag = []
    for i in range(len(names)):
        bag.append(itmcls(names[i], values[i], volumes[i]))
    return bag

# Implementation of greedy algorithm to choose 
# one of the optimum choice
def greedy(items, maxvol, keyfunction):
    itemscopy = sorted(items, key = keyfunction, reverse = True)
    
    result = []
    totalval = 0 
    totalvol = 0
    
    for i in range(len(items)):
        if (totalvol + itemscopy[i].getvol() <= maxvol):
            result.append(itemscopy[i])
            totalval = totalval + itemscopy[i].getvalue()
            totalvol = totalvol + itemscopy[i].getvol()
            
    return (result, totalval)


itemlist = ['Phones', 'Laptops', 'Airpods', 'The MacMini', 'Electronics', 'Hello World', 'Coca-Cola', 'Bowling']
values = [89,90,95,78,97,84,32,45]
volumes = [6,8,15,17,12,18,8,9]
itemlistt = buildbag(itemlist, values, volumes)
maxvol = 54

taken, totvalue = greedy(itemlistt, maxvol, itmcls.density)

print('Total vaule taken : ', totvalue)

for i in range(len(taken)):
    print('  ', taken[i])
