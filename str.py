# print("hello world ")

# s = "divya"  #double code use for show the string
# s = 'divya'  #single code use for show the string
# s = """d    #multiple code used triple """"""
# i
# v
# y
# a """  #triple code= use for multiple line
# #print-- output show
# print(s)
# print(type(s))     #type fumction define the data type
# t="jai"
# print(t)
# print(type(t))

# s = "UpflaIr.scomp"
# print(s.upper())  #upper is kind of method which show the letter in upper 
# print(s.lower())

# print(s.title())  #title explain the text as title form
# print(s.capitalize())

# print("i am in", s )
# print(s.strip())   #strip means to remove unwanted space 
# print(s.lstrip())
# print(s.rstrip())

# print(s.replace("comp", "company"))  #replace kind of replacing the old word with new
# print(s.swapcase())  #convert uppercase to lowercase to viceversa

# print(s.isupper())
# print(s.isalpha())
# print(s.isascii())    #denote a set of character with number

s="hello world"
print(s)
print(type(s))   
print(s.upper())
print(s.lower())
#split  
print(s.split(" "))
a=56
print(type(float(a)))
print(a)
#accessing string      #access the character by number/index start by zero ending by -1
a="hello"
print(a[3])     #digits show in bracket[]
#slicing  kind of print the piece of string
text="python is good"
print(text[1:6])       #print ython use extra number
print(text[:9])        #space also count
print(text[0:10])
print(text[5:])         #after colon print whole sentence
print(text[-5:-1])     #print backside
print(text[::-1])      #reverse the string
print(len(text))     #length show string
print(text.find ("good"))   #find method show in digit which i used to show
print(text.find("yes"))     #find method show if some character not in sentence then give -1
print(text.index("good"))     #same as show word index number
# print(text.index("yes"))      #but index show the error if some word not in sentence
print(text.startswith("p"))    #startwith show sentence start with which character
print(text.endswith("d"))      #showcondition true and false
print(text.count("o"))  #count the word in sentence
text="hello"
print(text.isalpha())    #space in between sentence show false
text="divya5619"
print(text.isalnum())    #show alphanumric both
text= "  "
print(text.isspace())      #show the space but in between character
text="23445"
print(text.isdigit())   #only digit condition show true
#join method
text="yes","world"
print(",".join(text))     #join method used for join the character/one string to another
#string concatenation
a="hello"
b="world"
print(a+" "+b)    #two charcter between space and join character


#list method    list is an ordered collection of item
#list is mutuable(changable)
#create list by using[] and rather than()/list contructor
fruit=["apple","bannan"]     #normal list print
print(fruit)
a=["apple",5,True,7.8]
print(type(a))      #a denote complete list
b=list(("c",6,7,True))
print(b)    #print list used ()()/used double parenthises

#accessing list item
f=["apple","banana"," kiwi"]
print(f[1])     #print whole character as banana is 1 and mango is 3
print(f[1:3])     #print banana and kiwi
print(f[:3])      #print 0 1 2(a,b,k)
print(f[3:])      #print mango after 3 one print
# print(f[-2:-1])
print(f[::-1])   #double colon used for reversed the list
print(f[-2:-1])   


#type conversion
x=1
y=3.5
z=2j
a=x
b=y
c=z
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))