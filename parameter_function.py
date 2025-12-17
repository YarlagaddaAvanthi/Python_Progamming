#default parameter
def greet(name="guest"):
    print(f"hello {name} welcome.")

greet("Avanthi")
greet()
print("--------------------------------")
##variable length Arguments
# positional arguments
def print_numbers(*args):#*args refers to m no.of parameters
    for num in args:
        print(num)

print_numbers(1,2,3,4,4,5,6,7,8,8,9,9,2,3,4,5,6,6,7,7,8,"END")
print("-----------------------------------------------")
#keywords Arguments
def print_details(**kwargs):

    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_details(name="Avanthi",occupation="Student",state="AP",Country="India")
print("--------------------------------")