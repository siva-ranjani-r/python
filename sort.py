week = ["sunday","monday","tuesday","wenesday","thursday","friday",
"staturday"]
month=["January","February","March","April","May","June","July","August","September","October","November","December"]
add=week+month
add.sort(reverse=True)
print(add)
x=add[0:3]
del add[0:3]
print(add)
y=add+x
print(y)

