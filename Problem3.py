#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
print("Execution Started")

def smallest_prime_divisor(number):
  divisor = 2
  while(number%divisor!=0):
    divisor+=1
  return divisor
      
next_divisor=0
number = 600851475143
while (number!=1):
  next_divisor = smallest_prime_divisor(number)
  number/=next_divisor
  #print(next_divisor)
  #print(number)

print(next_divisor)
