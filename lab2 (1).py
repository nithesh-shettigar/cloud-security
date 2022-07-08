#a. Read the content from the file, and write into another file.
with open("f1.txt", "r") as a:
      
    with open("f2.txt", "w") as b:
          
        for line in a:
            b.write(line)
            
#b. Count the total number of characters in the file       
file = open("f1.txt", "r")

data = file.read()

n = len(data)

print(n)

#c. Reverse the content from the file.

f1 = open("reverse.txt", "w")
  

with open("f1.txt", "r") as myfile:
    data = myfile.read()
  

data_1 = data[::-1]
  

f1.write(data_1)
  
f1.close()     

#d. Find the histogram of each characters in the file

with open("f1.txt", "r") as myfile:
    data = myfile.read()

data=data.lower()
Dict=dict()
for word in data:
    if word not in Dict:
        Dict[word]=1
    else:
        Dict[word]=Dict[word]+1
print(Dict)
for key, val in Dict.items():
    print(key, '\t', '*' *val)
    
#e. List out the top 5 most frequent characters and least 5 characters present in the file
def sortedHistogram():
     #open file in read mode
    file = open("E:\Documents\ME\Course\Sem 2\Cloud Security\Submissions\Lab Submission 2\Read File.txt", "r")

    #read the content of file
    data = file.read()
    #Converting the string to lowercase to avoid any ruleovers
    data=data.lower()
    Dict=dict()
    for word in data:
        if word not in Dict:
            Dict[word]=1
        else:
            Dict[word]=Dict[word]+1
    #print(Dict)

    sorted_values = sorted(Dict.values()) # Sort the values
    sorted_dict = {}

    for i in sorted_values:
        for k in Dict.keys():
            if Dict[k] == i:
                sorted_dict[k] = Dict[k]
                break

    #print(sorted_dict)

    outL = dict(list(sorted_dict.items())[0: 5]) 
    print("\n\nThe lowest frequency characters are:" + str(outL))

        
    outH = dict(list(sorted_dict.items())[-5: ])  
    print ("The highest frequency characters are:" + str(outH))


#2 a. Get the value from the user and check the number is prime or not
number = int(input("Enter any number: "))


if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")


else:
    print(number, "is not a prime number")

#b. get the two values from the user and check the number is coprime or not
def are_coprime(a,b):
    
    hcf = 1

    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            hcf = i

    return hcf == 1

first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

if are_coprime(first, second):
    print('%d and %d are CO-PRIME' %(first, second))
else:
    print('%d and %d are NOT CO-PRIME' %(first, second))    