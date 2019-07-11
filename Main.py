


def initializeHash():
      global driver_hash 
      driver_hash = {}
      print('driver map initialized')

def insertHash (violations, lic):
    global driver_hash
    if(driver_hash.get(lic)==None):
         driver_hash[lic] = violations
    else:
        driver_hash[lic] = driver_hash.get(lic)+violations

def printViolators (driverhash):
    global driver_hash
    count = 0
    file = open("violators.txt","w")
    for k,v in driver_hash.items():
        if(v>=driverhash):
            count = count+1
            file.write("{key},{value}\n".format(key = k,value = v))
    if(count==0):
        file.write("No violators found")
    file.close



initializeHash()
insertHash(3,"l123")
insertHash(4,"l124")
insertHash(1,"l125")
insertHash(3,"l126")
printViolators(10)
