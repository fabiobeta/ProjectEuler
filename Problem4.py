#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
print("Execution Started")

def isPalindrome(number):
  numberString=str(number)
  lenght=len(numberString)
  for x in range(lenght):
    if numberString[x]!=numberString[lenght-1-x]:
        return False
  return True
      
#print(isPalindrome("pot"))
maxPalindromeNnumber=1

for factor1 in range(100,999):
    for factor2 in range(100,999):
        number=factor1*factor2
        if isPalindrome(number):
            if number>maxPalindromeNnumber:
                    maxPalindromeNnumber=number

print(maxPalindromeNnumber)
