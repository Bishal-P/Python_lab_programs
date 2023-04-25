marks=0
for i in range(4):
    marks+=int(input(f"Enter the marks of subject {i+1} : "))

marks=marks/4
print(marks)
if marks<50:
    print("Failed")

elif marks<65:
    print("Division 3")

elif marks<75:
    print("Division 2")

elif marks>=75:
    print("Division 1")

else:
    pass
