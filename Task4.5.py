polynom1 = open('polynom1.txt', 'w') 
polynom1.write('10x^2 + 15x + 16 = 0')
polynom1.close()
polynom2 = open('polynom2.txt', 'w')
polynom2.write('7x^2 + 3x + 7 = 0')
polynom2.close()
text_1 = open('polynom1.txt', 'r')
line1 = text_1.read().split('+')
line1 = [i.strip() for i in line1]
polynom1.close()
line1 = [i.rstrip(' =0') for i in line1]
line1 = [i.rstrip('x^2') for i in line1]
line1 = [int(i) for i in line1]
text_2 = open('polynom2.txt', 'r')
line2 = text_2.read().split('+')
line2 = [i.strip() for i in line2]
polynom2.close()
line2 = [i.rstrip(' =0') for i in line2]
line2 = [i.rstrip('x^2') for i in line2]
line2 = [int(i) for i in line2]
line3 = []
for i in range(3):
    line3.append(line1[i] + line2[i]) 
result = str(line3[0]) + 'x^2' + ' + ' + str(line3[1]) + 'x' + ' + ' + str(line3[2])  + ' = 0'
polynom_result = open('polynom_result.txt', 'w')
polynom_result.write(result)
polynom_result.close()