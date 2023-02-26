#assign the list of integers to a variable array
array=[1,2,3]
#create the sum variable to add the integers to
sum=0
#for loop to count through the integers and add to sum variable
for i in array:
    sum+=i
#outputs the sum of the integers using f string
print(f"The sum of integers is {sum}")