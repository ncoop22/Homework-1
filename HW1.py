__author__ = 'Nickolas'


def menu():
    while True:
        menu="a.Input Employee First Name\nb.Input Last Name\nc.Input DOB\nd.Input SS#\ne.Input Street Address\nf.Input City\ng.Input Zip\nh.Print Out Info\ni.Quit"
        print(menu)
        s=input ("choose function a-i").strip()
        if s=="a":
            a=names()
            print(a)
            print("\n")
        if s=="b":
            b=last()
            print(b)
            print("\n")
        if s=="c":
            c=DOB()
            print(c+"\n")
        if s=="d":
            d=SS()
            print(d+"\n")
        if s=="e":
            e=Address()
            print(e+"\n")
        if s=="f":
            f=City()
            print(f+"\n")
        if s=="g":
            g=Zip()
            print(g+"\n")
        if s=="h":
            f= open('employee.info', 'r', encoding='utf-8')
            f.seek(0)
            for line in f:
                print(line)
        if s=="i":
            return ("Quit")

def names():
    f= open ('employee.info', 'a+', encoding='utf-8')
    a=input("First Name").strip("\r\n").title()
    f.write(a+"\n")
    f.close()
    return(a)

def last():
    f= open ('employee.info', 'a+', encoding='utf-8')
    b=input("Last Name").strip("\r\n").title()
    f.write(b+"\n")
    f.close()
    return(b)

def DOB():
    f= open ('employee.info', 'a+', encoding='utf-8')
    c=input("DOB").strip("\r\n").title()
    f.write(c+"\n")
    f.close()
    return(c)

def SS():
    f= open ('employee.info', 'a+', encoding='utf-8')
    d=input("SS").strip("\r\n").title()
    f.write(d+"\n")
    f.close()
    return(d)

def Address():
    f= open ('employee.info', 'a+', encoding='utf-8')
    e=input("Address").strip("\r\n").title()
    f.write(e+"\n")
    f.close()
    return(e)

def City():
    f= open ('employee.info', 'a+', encoding='utf-8')
    g=input("City").strip("\r\n").title()
    f.write(g+"\n")
    f.close()
    return(g)

def Zip():
    f= open ('employee.info', 'a+', encoding='utf-8')
    h=input("Zip").strip("\r\n").title()
    f.write(h+"\n")
    f.close()
    return(h)
(menu())