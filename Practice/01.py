#print("hello jee") 

#-----------------------------------------------------------------------------
# a = int(input("Enter first number : ")) 
# b = int(input("Enter sec number: ")) 

# print(a+b) 

#----------------------------------------------------------------------------- 

# num = input("Enter number")

# print(type(num)) 

#----------------------------------------------------------------------------- 
 
# a = int(input("Enter first number : ")) 

# b = int(input("Enter second number : ")) 

# c = (a+b) /2

# print("the avg of this two number :",type(c)) 

#----------------------------------------------------------------------------- 

# a = int(input("Enter number that you want to make square : ")) 
# ans  = a**3 

# print("Ans:",ans) 

#-----------------------------------------------------------------------------  

# str = "01234567890" 

# strSlice = str[-3:-1]
# print(strSlice) 

#-----------------------------------------------------------------------------  


# str = "This is good boy \t boy "
# print(str)  

#-----------------------------------------------------------------------------

# a = int(input("Enter number "))


# print("The square of two number is : ",a**2) 

#----------------------------------------------------------------------------- 
# letter = "Dear Harry, \n this python course is nice. \n Thanks!" 

# print(letter) 

#----------------------------------------------------------------------------- 
#list is mutable and string is immutable
# fruit2 = ["mmmm"]
# fruit = ['apple','apple','mango','orange','strawbeery','coconut','lichy','babana']
# res = fruit
# print(res) 

#----------------------------------------------------------------------------- 

# mark = [] 

# student1 = int(input("Enter the mark of first student1")) 
# mark.append(student1)
# student2 = int(input("Enter the mark of first student2")) 
# mark.append(student2)
# student3 = int(input("Enter the mark of first student3"))
# mark.append(student3)
# student4 = int(input("Enter the mark of first student4"))
# mark.append(student4)
# student5 = int(input("Enter the mark of first student5"))
# mark.append(student5)
# student6 = int(input("Enter the mark of first student6"))
# mark.append(student6)

# mark.sort() 

# print(mark) 

#----------------------------------------------------------------------------- 

# a = (7, 0, 8, 0, 0, 9) 

# res = sum(a)

# print(res)
#-----------------------------------------------------------------------------

# lang = {
#     "billi":"cat",
#     "kutta":"dog",
#     "bail":"ox",
#     "gay":"cow"
# } 

# word = input("Enter the name of animal that ypu want to see english mean : ") 


# print(lang.get(word)) 

#-----------------------------------------------------------------------------

# setNumer = set() 
# num1 = input("Enter first number")
# setNumer.add(num1)
# num2 = input("Enter second number")
# setNumer.add(num2) 
# num3 = input("Enter the third number") 
# setNumer.add(num3) 
# num4 = input("Enter fourth number") 
# setNumer.add(num4)
# num5 = input("Enter five number") 
# setNumer.add(num5)
# num6 = input("Enter six number") 
# setNumer.add(num6)
# num7 = input("Enter 7 number") 
# setNumer.add(num7)
# num8 = input("Enter 8 number") 
# setNumer.add(num8)

# print(setNumer) 

#----------------------------------------------------------------------------- 

# setNum = {'18',18}

# print(setNum) 

#----------------------------------------------------------------------------- 

# s= { }

# print(type(s)) 

#----------------------------------------------------------------------------- 

# langObj = {

# }

# name = input("Enter the name ")
# lang = input("Enter your fav lang") 

# langObj.update({name:lang})

# name = input("Enter the name ")
# lang = input("Enter your fav lang") 

# langObj.update({name:lang})

# name = input("Enter the name ")
# lang = input("Enter your fav lang") 

# langObj.update({name:lang})

# name = input("Enter the name ")
# lang = input("Enter your fav lang") 

# langObj.update({name:lang})

# print(langObj)  

#----------------------------------------------------------------------------- 

# s = {8,7,12,'harry',[1,2]} 

# s.update({})
#----------------------------------------------------------------------------- 

# '''Write a program to print yes when the age entered by the user is greater 
# than or equal to 18.'''


# age  = int(input("Enter your age "))

# if(age >= 18):
#     print("You are eligible for voting") 
# else:
#     print("You are not eligible ") 

#-----------------------------------------------------------------------------  
#CHAPTER 6 – PRACTICE SET 

#1. Write a program to find the greatest of four numbers entered by the user. 

# a = int(input("Enter first number"))
# b = int(input("Enter second number"))
# c = int(input("Enter third number"))
# d = int(input("Enter fourth number")) 

# if(a>b and a>c and a>d):
#     print(f"{a} is grater number")
# elif(b>a and b>c and b>d): 
#     print(f"{b} is greater number") 
# elif(c>a and c>b and c>d):
#     print(f"{c} is greater number") 
# elif(d>a and d>b and d>c):
#     print(f"{d} is greater number") 
#-----------------------------------------------------------------------------
'''Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user.''' 

# sub1 = int(input("Enter English subject mark : ")) 
# sub2 = int(input("Enter Math Mark :")) 
# sub3 = int(input("Enter Science Mark :")) 

# if(sub1 >= 40 and sub2>=40 and sub3>=40):
#     print("Congratulation you are pass!!") 
# else:
#     print("Soory you are failed")  


# sub1 = int(input("Enter English subject mark : ")) 
# sub2 = int(input("Enter Math Mark :")) 
# sub3 = int(input("Enter Science Mark :")) 

# total_percentage = float(((sub1+sub2+sub3)*100)/300) 

# if(total_percentage >= 40 and sub1 >= 33 and sub2 >=33 and sub3 >= 33):
#     print("Congratulation you are passed you are scored ",total_percentage)

# else:
#     print("Soory try next year")
 

#----------------------------------------------------------------------------- 

'''A spam comment is defined as a text containing following keywords: 
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams. ''' 

# p1 = 'Make a lot of money'
# p2 = 'buy now'
# p3 ='subscribe this' 

# strr = input("Enter a string and i am tell you that is spam contain ") 

# if((p1 in strr) or (p2 in strr) or (p3 in strr)):
#     print("It Contain spam word ")
# else:
#     print("It Does not contain spam word") 

#-----------------------------------------------------------------------------  
'''Write a program to find whether a given username contains less than 10 
characters or not.''' 

# userName = input("Enter you userName")
# print(len(userName))
# if(len(userName) > 10 ):
#     print("your username to long like it more than 10 word") 
# else:
#     print("your name is short than 10 character")
#-----------------------------------------------------------------------------
# '''Write a program which finds out whether a given name is present in a list or not.'''  

# nameList = ["hari","shubham","shivam","tejas"] 

# name = input("Enter your name")

# if(name in nameList):
#     print("Your name is available in list") 

# else:
#     print("Your name is not available in list")
#----------------------------------------------------------------------------- 
'''Write a program to calculate the grade of a student from his marks from the 
following scheme: 
90 – 100 => Ex 
80 – 90 => A 
70 – 80 => B 
60 – 70  =>C 
50 – 60 => D 
<50 => F''' 

# mark = int(input("Enter your mark : "))
# if(mark >90 and mark <=100):
#     print(" Grade Excellent") 
# elif(mark >80 and mark <=90):
#     print("Grade A")
# elif(mark >70 and mark <=80):
#     print("Grade B")
# elif(mark >60 and mark<=70):
#     print("Grade c")
# elif(mark >50 and mark<=60):
#     print('Grade D') 
# elif(mark < 50):
#     print("Soory Your grade is F (fail)")
# else:
#     print("Check Mark Again that you enter")

#----------------------------------------------------------------------------- 
''' Write a program to find out whether a given post is talking about “Harry” or not.'''

# post  = input("Enter post ") 
# yourName  = input("Enter your name ")

# if(yourName.lower() in post.lower()):
#     print(f"This post is talking about {yourName}")
# else:
#     print(f"This post not talking about you{yourName}") 
#-----------------------------------------------------------------------------  
'''Quick Quiz: Write a program to print 1 to 50 using a while loop.''' 

# i = 1
# while(i<=50):
#     print(i) 
#     i = i+1
#-----------------------------------------------------------------------------
'''Quick Quiz:  Write a program to print the content of a list using while loops.''' 

# name = ["hari","shubham","shivam","tejas"] 
# i=0
# while(len(name) > i):
#     print(name[i])
#     i = i+1
#----------------------------------------------------------------------------- 

'''Write a program to print multiplication table of a given number using for loop.''' 
# number = int(input("Enter the number that you want to print table ")) 

# for i in range(1,11):
#     print(f"{number} * {i} == {number*i}")
#----------------------------------------------------------------------------- 

# nameList = ["Harry", "Soham", "Sachin", "Rahul"]  

# nameRes = []

# for i in nameList:
#     if(i.lower().startswith('s')):
#         nameRes.append(i)

# print(nameRes)

#----------------------------------------------------------------------------- 
''' Write a program to print multiplication table of a given number using while loop. ''' 

# number = int(input("Enter The number that you want to print table")) 

# i=1 

# while(i<=10):
#     print(f"{number} * {i} == {number*i}")
#     i = i+1

#----------------------------------------------------------------------------- 
''' Check the input number is prime or not'''
# number = int(input("Enter number that you want to check its prime or not")) 

# if(number <= 1):
#     print("Its not prime number") 
# else:
#     isPrime = True 
    
#     for i in range(2,number):
#         print(number)
#         if(number % i == 0):
#             isPrime = False
#             break
    
#     if(isPrime):
#         print("Its prime number")
#     else:
#         print("Its not prime number")
#-----------------------------------------------------------------------------  
'''Sum of natural number''' 

# number = int(input("Enter the number that you want sum upto the number")) 

# i = 0 
# sum = 0 

# while(i<=number):
#     sum = sum+i
#     i = i+1 

# print(sum) 

# n  = int(input("Enter the number that you want to check ")) 

# for i in range(2,n):
#     if(n%i) == 0:
#         print("Its not prime number")
#         break
# else:
#         print("Its prime number")

#-----------------------------------------------------------------------------
'''factorial of number''' 

# res = 1 

# number  = int(input("Enter the number that you want factorial"))

# for i in range(1,number+1):
#     res = res*i

# print(res) 

#----------------------------------------------------------------------------- 

''' Write a program to print multiplication table of n using for loops in reversed 
order.'''  


n = int(input("Enter the number that you want print table in reveserd order"))
 
for i in range(1,11):
    print(f"{n} * {11-i} == {n*(11-i)}")