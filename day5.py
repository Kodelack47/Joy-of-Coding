
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