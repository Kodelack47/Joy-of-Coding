print("Hello World!")

#print ("hello world")

#x = 4 
#y = x + 2

#print(y)

#import math  
#print ( math.sqrt(25))

#from math import sqrt

#print(sqrt(25))

import turtle 

turtle.color("red")

size = 100
turtle.forward(size)
turtle.right(120)
turtle.forward(size)
turtle.right(120)
turtle.forward(size)
turtle.right(120)

#for i in range(1,11):
 # print(i)
  
 # for <loop variable> in <sequence>:
  # for char in "hello":
  # print(char)
#for i in range( 2, -48, -2) :
  #print(i)
#for letter in range(10) :
  #print("hello world")
  
for i in range( 2, -10, 4) :
  print(i)
  
  
   
#for hi in range(5):
 # print(hi)

#print("_"*10)

#for lo in range(7, -7, -3):
  #print(lo)
  
  #print("_"*10)
  
  #phrase = "money python"
  #for letter in phrase:
    #print(letter, end="-")
   # print()
   
   
   import turtle
   turtle.color("red")
   
   size = 100
   turtle.forward(size)
   turtle.right(120)
   turtle.forward(size)
   turtle.right(120)
   turtle.forward(size)
   turtle.right(120)
   
   import turtle
turtle.color("red")


size = 100
#repeat loop
for i in range(3):
 turtle.forward(size)
 turtle.left(120)
 
 
 
 
 
 
 import turtle

turtle.color("red")

size = 100
#using loop to repeat
#for i in range(3):
  #turtle.forward(size)
  #turtle.left(120)
  
#creating the new fuctions Back
#helper functions to move my turtle back
def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

  #creating function!
def triangle(size):
 for i in range(3):
  turtle.forward(size)
  turtle.left(120)

#creating 3 different sizes by calling the same fuction
#test function calls
triangle(100)
back(75)
triangle(50)
back(50)
triangle(25);





#making a Square 
#creating the new fuctions Back
#helper functions to move my turtle back
def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

  #creating function!
def square(size):
 for i in range(4):
  turtle.forward(size)
  turtle.left(90)

#creating 3 different sizes by calling the same fuction
#test function calls
square(100)
back(75)
square(50)
back(50)
square(25)


 
  
 
 
 
 
 
 
 
 
 
 import turtle
turtle.color("red")
  
#creating the new fuctions Back
#helper functions to move my turtle back
def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

#can just add a forward helper function
def move(len):
 back(-1*len)

#creating function for polygon
def polygon(num, size):
 for i in range(num):
  turtle.forward(size)
  turtle.left(360/num)

#creating the defferent shapes
# polygon(3, 100)
# back(125)
# polygon(4, 50)

def spiral(len, angle):
  for i in range(len,5, -5):
    turtle.forward(i)
    turtle.right(angle)
    
spiral(75, 45)
move(150)
turtle.color("blue")
spiral(100,90)

#uncomment this part to see the polygon
# for n in range(3, 10):
#   move(-50)#forward
#   polygon(n,100 / n)
#   back(50)
#   turtle.right(360 / 7)