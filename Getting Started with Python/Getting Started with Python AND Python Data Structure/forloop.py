for x in 'python':
    print("Current Letter :", x)

string = "Vaibhav"
for name in string:
    print("Current Alphabet :", name)


lister = [1, 2, 'frost', 'hi']
for crack in lister:
    print(crack)

    
fruits = ["banana", "apple", "orange"]
for eat in range(len(fruits)):
    print("Current fruit:", fruits[eat])
    
print("Sayonara!") #type code in format i,e; write under for loop,
     #python compiler consider for satatement, However, it's not. 
    
    

for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print ('%d equals %d * %d', (num,i,j))
         break #to move to the next number, the #first FOR
      else:                  # else part of the loop
         print ('is a prime number', [num]) 
