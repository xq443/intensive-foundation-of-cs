import math
import CloseWords
# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n) + 1)):
#         if(n % i == 0):
#             return False
        
#     return True


# def isPalindrome(n):
#     num_str = str(n)
#     return num_str == num_str[::-1]
        
# if __name__ == '__main__':
#     res = []
#     count = 0
#     num = 11

#     while(count <10):
#         if isPalindrome(num):
#             count+= 1
#             res.append(num)
#         num+= 1
        
        
            
#     print(res)

# def binary_to_decimal(binary_number):
#     decimal_equivalent = int(str(binary_number), 2)
#     return decimal_equivalent

# # Example usage:
# binary_number = 1010
# decimal_equivalent = binary_to_decimal(binary_number)

# print(f"The decimal equivalent of {binary_number} is {decimal_equivalent}")
# def generate_binary_powers_of_two(limit):
#     binary_numbers = []
#     current_power = 0

#     while len(binary_numbers) < limit:
#         binary_number = bin(2**current_power)[2:]  # Convert to binary and remove '0b' prefix
#         binary_numbers.append(binary_number)
#         current_power += 1

#     return binary_numbers

# # Example usage:
# result = generate_binary_powers_of_two(10)
# print("First 10 terms of the sequence:", result)
# decimal_number = 42  # Replace with your decimal number

# binary_representation = bin(decimal_number)[2:]  # Convert to binary and remove '0b' prefix

# print(f"The binary representation of {decimal_number} is: {binary_representation}")

# def is_power_of_two(number):
#     return number > 0 and (number & (number - 1)) == 0

# count = 0
# num = 1
# res = []
# while(count < 10):
#     if is_power_of_two(num):
#         data = bin(num)[2:]  
#         res.append(data)
#         count += 1
#     num+= 1
# print(res)
# print(type(data))

# sum = 0
# for i in range(1,4):
#     for j in range(0, 3):
#         sum += j/i
# print(sum)
# prev = 0; curr = 1 ;next = 1
# res = []
# for i in range(1, 6):
#     postnext = next + curr - prev
#     res.append(postnext)
#     prev = curr
#     curr = next 
#     next = postnext
# print(res)
# res = [];n = 1
# for i in range(0,11):
#     num = ((-1)**((n-1)/2))* ((n+1)/2) / 2
#     res.append(num)
# print(res)
    
    
    
# # print((-1)**(1/3))
# print((8**15) % 23)

# def power(base, exp):
#     if exp == 0:
#         return 1
#     else:
#         smaller = power(base, exp -1)
#         return  base * smaller 
    
# def countVowel(s):
#     if len(s) == 0:
#         return 0
#     else:
#         if s[len(s) - 1] in 'aeiou':
#             return 1 + countVowel(s[: len(s)-1])
#         else:
#             return countVowel(s[: len(s) -1])
        
# def fib(n):
#     if n == 1 or n == 0:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
        
# if __name__ == '__main__':
#     print(power(2,10))
#     print(countVowel('CATHY'.lower()))
#     print(fib(4))
    
# print((4**3) % 23)
print(CloseWords.offByOne("read", "rexd"))