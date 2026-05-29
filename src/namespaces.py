#A namespace in Python is a container that maps names (variables, functions, classes, modules) to objects.


x = 10

def my_func():
    x = 20
    print(x)

my_func()
print(x)

#ouptput -   20
            #10


#Types of namespaces:
#1.Build-in namespace - print() , len()
#2.Global namespace -

x = 100 #global namespace

def show():
    pass

print(globals())

######################


x = 100

def display():
    print(x)

display()

#ouput - 100
#Python finds x in the global namespace.

#local namespace:


def test():
    y = 50 #local namespace
    print(y)

test()


#Enclosing Namespace:

def outer():
    x = 100

    def inner():
        print(x)

    inner()

outer()

#output - 100

#inner() cannot find x locally, so it checks the enclosing function (outer).

#LEGB Rule

#L → E → G → B

x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()

#output - "local"

x = "global"

def outer():
    x = "enclosing"

    def inner():
        print(x)

    inner()

outer()

#output - "enclosing"  --> inner couldn't find the local namespace , it went for enclosing namespace and found x = 'enclosing'









