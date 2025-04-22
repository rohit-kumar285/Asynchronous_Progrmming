## Everythin here is executed sequentiallly called synchronous programming.

## For Example we have a function hello() and a print statement : How are you as shown below : 

def hello():
    return "hello"


## here if i call the function first then first it will executed completely then print statement will execute 
## if i reverse the order then print stmt will execute first then function 
print(hello())
print("How are you !")