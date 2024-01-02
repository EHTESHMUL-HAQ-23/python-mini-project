# my owm program first time made .
BCA=50
print("Bachelor of Computer Application Total Students is :" ,BCA)
print()
MCA=int(input("Enter the MCA Total students:"))
print(MCA)
print()
if BCA > MCA:
    print("BCA  STUDENTS WAS HIGH TOTAL")  # bca is greather than mca.
    MCA=int(input("mca second if 1 "))
    if BCA >= MCA:
       
        print("goods with correct")
elif BCA < MCA:
    print("MCA STUDENTS WAS HIGH TOTAL")   # mca is greather than bca.
    MCA=int(input("mca second if 2"))
    if BCA <= MCA:
      
       print("goods with mca ")
    else:
        print("nothing with happen")       
elif  BCA == MCA:
    print("BCA AND MCA ARE EQUAL STUDENTS AND STRENGTH.") 


     