def SwipeText():
 
 F1 = input("Enter file 1 name: ")
 F2 = input("Enter file 2 name: ")

 data_a = open(F1, 'r')
 data_b = open(F2, 'r')

 print(data_a)
 print(data_b)

 Swap1 = open(F1, 'w')
 Swap2 = open(F2, 'w')

 Swap1.write(data_b)
 Swap2.write(data_a)
 
 print(Swap1.read())
 print(Swap2.read())

SwipeText()