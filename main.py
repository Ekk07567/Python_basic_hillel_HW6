N = int(input('Enter Number:'))
A = 0
while N > A:
    print('*' * (N - A))
    A += 1

N2 = int(input('Enter Number 2:'))
A2 = 1
while N2 >= A2:
    print('*' * A2)
    A2 += 1

N3 = int(input('Enter Number 3:'))
A3 = 0
B = ' '
while N3 > A3:
    print((B * A3) + '*' * (N3 - A3))
    A3 += 1

N4 = int(input('Enter Number 4:'))
A4 = 1
B = ' '
while N4 >= A4:
    print(B * (N4 - A4) + '*' * A4)
    A4 += 1
