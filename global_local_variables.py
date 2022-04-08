# The main difference between local and global variables is scope. Scope of variable is only within the function. Whereas scope of the global variable would be throughout the entire program. Here a is global function and b is local function. If local and global functions are having the same name, first preference will be to local variable.
a = 20
def display():
    b=20
    print("Inside user-defined function:",a)
    print("local variable:",b)
display()
print("Outside the user-defined function:",a)

