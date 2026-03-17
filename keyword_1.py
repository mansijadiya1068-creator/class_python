def student_info(name,age,city):
    print("name :" ,name)
    print("Age :",age)
    print("city :",city)
    student_info(age=18,city="rajkot",name="ravi")


def display(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    display(1,a=3,b=2)

def simple_insert(p:float,r:int,t:float):
    si=(p*r*t)/100
    print("simple intrest :",si)
    simple_intrest(p=10000,t=2,r=1.5)
    simple_intreat(t=1.5,p=15000,r=2)
    