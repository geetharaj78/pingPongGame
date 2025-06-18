bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi,2)) #we want to run the BMI upto 2 decimal places. 
#assignement operator
score = 0
score +=1
print(score)
#in python, we can use f - strings to insert a variable or an expression into a string
print("Your score is "+str(score))
#it is very difficult to convert everything into a string, so - 
score = 0
height = 1.8
is_winning = True
print(f"your score is = {score}, your height is {height}. you are winning is {is_winning}") 
age = int(input("enter the age of the person;\n"))
print(f"the age of the person is: {age}") 