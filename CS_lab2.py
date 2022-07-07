# 1. Reading the contents of one file and copying it another file
def copy_file_content(filename):
    
    with open(filename, 'r') as firstfile, open('second.txt', 'a') as secondfile:
        for line in firstfile:
            secondfile.write(line)
    return 'done'
    
# 2. Program to read the number of characters from a file
def count_file_char(filename):
    
    file = open(filename, 'r')
    data = file.read()
    
    char_count = len(data)
    
    return char_count
    
# 3. Reversing the content of the file
def rev_file_content(filename):
    
    with open(filename, 'r') as file:
        data = file.read()
    
    rev_content = data[::-1]
    
    print(rev_content)
    
    return rev_content
    
# 4. Program to get the number of occurance of characters in a file
def file_char_occr(filename):

    text = open(filename, 'r')
    
    char_dict = dict()
    char_dict1 = dict()
    
    for line in text:
        
        line = line.strip()
        line = line.lower()
        
        words = line.split(" ")
        
        for word in words:
            if word in char_dict:
                word_count +=1
                char_dict[word] += 1
            else:
                word_count = 1
                char_dict[word] = 1
            
            for char in word:
                if char in char_dict1:
                    char_dict1[char] += 1
                else:
                    char_dict1[char] = 1
    
    #for key in list(char_dict.keys()):
    #    print(key, ":", char_dict[key])
    
    #for key in list(char_dict1.keys()):
    #    print(key, ":", char_dict1[key])
    
    for key, val in char_dict1.items():
        print(key, '\t', '*' * val)
        
    
    #print(char_count)

# 5. finding the top 5 most frequent characters present in the file
def freq_char(filename):
    
    text = open(filename, 'r')
    
    top_5_occr = {}

    for line in text:
        line = line.strip()
        line = line.lower()
        
        words = line.split(" ")

        for word in words:
            for char in word:
                if char in top_5_occr:
                    top_5_occr[char] += 1
                else:
                    top_5_occr[char] = 1
    x = sorted(top_5_occr.items(), key = lambda kv:(kv[1], kv[0]), reverse=True) #interchange of key, value is done
    print(x[:5])

# 6. Finding if the given number is prime number or not
def is_prime(num):

    if num > 1:
        # checking for factors
        for i in range(2, num):
            if num % i != 0:
                return 'PRIME'
            else:
                return 'NOTPRIME'
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return 'NOTPRIME'

# 7. Finding if the two numbers are coprime or not
# Two numbers whose Highest Common Factor (HCF) or 
# Greatest Common Divisor (GCD) is 1 are co-prime numbers.
# Ex (3, 7), (7, 10) ...
def are_coprime(num1, num2):
    
    hcf = 1
    for i in range(1, (num1 + 1)):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
    return hcf == 1
