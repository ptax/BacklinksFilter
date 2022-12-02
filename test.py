




test = 'string1;string2; string3'
test = test.split(';')
test = [x.strip() for x in test]
test = str(test).replace('[','').replace(']','')
print (test)

