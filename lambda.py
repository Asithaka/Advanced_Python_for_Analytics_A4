def testfunc(num):

    return lambda x: x*num

result10 =testfunc(10)
result100 = testfunc(100)

print(result10(9))
print(result100(9))

result10 = lambda x: x*10
result100 = lambda x: x*100

# filter function

numberslist = [2,6,8,10,4,12,7,13,17,0,3,21]
output=list(filter(lambda num: (num>7), numberslist))
print(output)

# map function

mapoutput = list(map( lambda num: num % 2, numberslist))
print(mapoutput)