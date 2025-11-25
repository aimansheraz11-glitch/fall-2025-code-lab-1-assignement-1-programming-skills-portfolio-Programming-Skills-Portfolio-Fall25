Biology=int(input("Enter Biology Marks: "))
Chemistry=int(input("Enter Chemistry Marks: "))
Physics=int(input("Enter Physics Marks: "))
Maths=int(input("Enter Maths Marks: "))
English=int(input("Enter English Marks: "))

Total=Biology+Chemistry+Physics+Maths+English
Avg=Total/5
per=(Total/500)*100
print(Avg)
print("percentage: ",per, "%" )
