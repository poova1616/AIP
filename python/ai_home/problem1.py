"""
# area of square  

def area_of_square(length):
    area = length * length
    return area

length =int( input("Enter square of length :"))

#print(area_of_square(length))

#==============================================================#

# area of rectangle

def area_of_rectangle(length,hight):
    area = length*hight

    return area

width = int(input("Enter rectangle of width : "))

area=area_of_rectangle(length,width)

#print("area of rectangle :"+str(area))

#===================================================================#

# area of circle
pi =3.14

def area_of_circle(radius):
    area = pi * radius * radius

    return area

radius = float(input("Enter the Radius:"))

area = area_of_circle(radius)

#print("area of circle is :",area)

#===================================================================#

"""


"""

# area of triangle

base = float(input("Enter base on triangle :"))

hight =float(input("Enter hight on triangle :"))

def area_of_triangle(base,hight):

    area = 0.5 * base * hight

    return area

area = area_of_triangle(base,hight)

print("Area of triangle :",area)

"""

# simple interest calculation

# simple interest formula si=prt/100

p = float(input("Enter principle of amount : "))
r = float(input("Enter rate of interest :"))
t = float(input("Enter time period in year :"))

def simple_interest(principle,rate,time):
    
    si = (principle * rate * time)/100

    return si

#print(simple_interest(p,r,t))

#==================================================#

# compound interst calculations

# compound interest formula A=p(1+/n)^nt

# a = final amount (principal + interest)

# P = principle (original amount)

# r = annual interest rate decimal

# n = number of times interest is compounded per year

# t = time of year

n=float(input("Enter number of time compound in year :"))
def compound_interest(principle,rate,time,number_of_time):

    compound_interest= p(1+r/n)^n*t

    return compound_interest


print(str(compound_interest(p,r,t,n)))

