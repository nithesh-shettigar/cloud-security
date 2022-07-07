import CS_lab2

# 1. Reading the contents of one file and copying it another file
assert (CS_lab2.copy_file_content('file1.txt') == 'done')

# 2. Program to read the number of characters from a file
assert (CS_lab2.count_file_char('file2.txt') == 2)

# 3. Reversing the content of the file
assert (CS_lab2.rev_file_content('file2.txt') == 'iH')
CS_lab2.rev_file_content('file1.txt')

# 4. Program to get the number of occurance of characters in a file
CS_lab2.file_char_occr('file1.txt')

# 5. finding the top 5 most frequent characters present in the file
CS_lab2.freq_char('file3.txt')

# 6. Finding if the given number is prime number or not
assert(CS_lab2.is_prime(3) == 'PRIME')
assert(CS_lab2.is_prime(1) == 'NOTPRIME')
assert(CS_lab2.is_prime(5) == 'PRIME')

# 7. Finding if the two numbers are coprime or not
assert(CS_lab2.are_coprime(3, 7) == True)
assert(CS_lab2.are_coprime(2, 3) == True)
assert(CS_lab2.are_coprime(7, 10) == True)
assert(CS_lab2.are_coprime(6, 8) == False)