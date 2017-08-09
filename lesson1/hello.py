
#let us print strings

#1. output: Hello World
print("Hello World")

#this will print the two strings 
#separated by the character assigned to sep.
#The sep stands for separator 

#2.output: Hello*World
print("Hello","World",sep='*')

#3.output: Hello++World
print("Hello","World",sep='++')

#4.output: Hello World
#output is same as 1. If the sep parameter 
#is not specified it defaults to an empty
#space.
print("Hello", "World",sep=' ')

#5. output: Hello!!!World&&&
#The end parameter is a string that appears 
#at  the end of printed output. If the end is
#not specified it defaults to a newline ('\n')
print("Hello", "World",sep='!!!',end='&&&')

#6. print a newline
print("\n")
