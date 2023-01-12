def liters_100km_to_miles_gallon(liters):
    #calculating gallon 
    c = 0
    a = (1 / 3.785411784) * liters
    #calculating american mile
    b = (1/1609.344) * 1000 * 100
    c = b/a
    return c


print(liters_100km_to_miles_gallon(3.9))