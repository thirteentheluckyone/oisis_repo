IP = input('Введите IP-адрес: ')

IP = IP.split('.')
A,B,C,D = IP

A = int(A)
B = int(B)
C = int(C)
D = int(D)



if  (A >= 1) and (A <= 223):
    print ('unicast')
elif (A >= 224) and (A <= 239):
    print ('multicast')
elif (A == 255) and (B == 255) and (C == 255) and (D == 255):
    print ('local broadcast')
elif (A == 0) and (B == 0) and (C == 0) and (D == 0):
    print ('unassigned')
else:
    print ('unused')