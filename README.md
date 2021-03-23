# Python_Data_Engineer_Test

1. Write a function power which accepts two integer arguments and has a default value
of 4 for the second argument. It should return the first argument to the power of the
second one. It should also check to make sure that each argument is an integer.
Example: power(2, 5) -> 32

2. You have the list:
list1 = list(range(20))
Create a second list, list2, which has all elements from list1 which are greater
than 10.

3. You have the following string:
input = '3, 5, 7, 9, 11'
Split the input string into a:
• list of numbers.
• tuple of numbers.

4. You have two lists:
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
Write a program which prints the numbers from the two lists in pairs. Meaning, the
output should be:
1 5
2 6
3 7
4 8

5. You have the following function:
def loop(times):
for i in range(times):
if i == 10:
break
Make it so the break condition can be dynamically defined. You can change anything you want in the code.

6. Write a Python program to display the current date and time in UTC.

7. Write a class Person that has two properties – name and age.
Write static method compare in class Person that accepts two arguments p1 and
p2 of type Person and returns True if age in p1 is greater than age in p2.
Write a program that creates two objects of class Person. The first object should
have properties set to name = "Peter" and age = 15. The second object should
have properties set to name = "Ivan" and age = 23. Call static method compare
and print the result from the comparison of the two objects.

8. Write a generator function which returns all positive integers. Print the first 5
numbers that the generator returns.

9. Using the file wine-reviews.csv:
• Read it into a Pandas DataFrame.
• Find the taster with the most reviews.
• Find the province with the highest average rating of the wines.
• Are the wines with the highest points also the most expensive? Make a plot
to show it visually
