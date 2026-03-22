# Create a function that receive the
# parameters inputs of any function (a, b, c...) and the n

# After that, its gonna receive an x that means where the x limit
# of our limit is goint to. Lest check this out!

# for any polinomial term => F(x) = a(n).x^n + a(n-1).x^(n-1) + ... + a(2).x^2 + a(1).x + a(0)
# So, we need to get the n and, by using the for loop, making our subtractions till we get 
# the last polinomial term 

# As the protocol says: 
print("\nLIMIT CALCULATOR")
print("================")

# First step: get the n and declare the list:
nTerm  = ""
validationLoop = True

# Try to turn it to an integer
while validationLoop:
    nTerm  = input("\nInsert de function degree: ")
    try:
        nTerm = int(nTerm)
        validationLoop = not(validationLoop)
    except ValueError:
        print("Value Error => Insert an integer value!")

# needa save this value to use latter...
degree = nTerm

# Check if its bigger than 0 
if(nTerm < 0):
    print("Not valid => Set Positive Numbers!")

termsList = []

# Second Step: to make the subtractions by the n term, we need to use a loop...
while nTerm >= 0:
    # First lest declare our "a" term
        while True:
            a = input(f"Set a for => a.x^{nTerm} term: ")
            
            # It needs to be an number too, but it can be any type
            try:
                a = int(a)
                break
            except ValueError: 
                print("Value Error => Insert an integer value!")
                

        termsList.append(a)
        nTerm = nTerm - 1
# Okay, we did it! Now we're gonna calculate the "As" terms with the x 
# Defined by us, and then, get our result for the limit. Lets go.

#Third Step: get our "x"
xValue = ""

while True:
    xValue = input("\nSelect the limit accumulation point: ")
    try:
        xValue = int(xValue)
        break
    except ValueError:
        print("Value Error => Insert numbers only! ")


# And now we need to roll on the list to calculate our limit
# and make the "body" of our function
bodyFunction = "f(x) = "
limit = 0
for i in termsList:
    valueTerm = (i * (xValue**degree))
    limit = limit + valueTerm

    if(degree > 0 ):
        if i == 0:
            bodyFunctionComponent = str(0) + " + "
        else:
            bodyFunctionComponent = str(i) + ".(x^"+ str(degree)+ ") + "
    elif(degree == 0 ):
        if i== 0:
            bodyFunctionComponent = str(0) 
        else:
            bodyFunctionComponent = str(i) + ".(x^"+ str(degree)+ ")"

    bodyFunction = bodyFunction + bodyFunctionComponent
    degree = degree - 1

print(bodyFunction)
print (f"lim (x=>{xValue}) f(x) = {limit}")