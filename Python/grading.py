mazematic=int(input("Enter Maths: "))
kisw=int(input("Enter Kiswahili: "))
Eng=int(input("Enter English: "))
SST=int(input("Enter Maths: "))

total=mazematic+kisw+Eng+SST

av=total/4

if av >=80 and av <=100:
    grade="Grade A"
elif av<=79 and av >=70:
    grade="Grade B"
elif av<=69 and av >=60:
    grade="Grade C"
elif av <= 59 and av >= 50:
    grade=  "Grade D"
elif av>0 and av <50:
    grade="Fail"
else:
    grade="See Me"

print("MATHS.... ",mazematic)
print("ENGLISH.... ",Eng)
print("KISWAHILI.... ",kisw)
print("SOCIAL STUDIES.... ",SST)
print("TOTAL.... ",total)
print("AVERAGE.... ",av)
print("GRADE.... ",grade)


