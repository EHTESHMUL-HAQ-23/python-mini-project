print("***** Welcome to Python Class in Zukun Academy")

print("**** Note: Allowed only IT students --> MCA, Msc, BCA, CSE, B.Tech, IT related")
# This is for securtiy Man asked to each and Indiviual guy's

department=input("Enter Your Department Name:")

if department=="MCA" or department=="MSC" or department=="BCA" or department=="B.Tech":
    print("Please Come Inside to Our Fest")
    
    if department=="MCA":
        print("Go to First Floor ") 
    
        registration=input("Registration Done Yes or No:")
        
        if registration=="yes" or registration=="YES":
            print("Come Inside and Enjoy")
        else:
            print("First go  and Register your Name")
    
    elif department=="MSC":
        print("Go to Second Floor")
        
        registration=input("Registration Done Yes or No:")
        
        if registration=="yes" or registration=="YES":
            print("Come inside  and Enjoy")
        else:
            print("First go  and Register Your Name")
    
    elif department=="BCA":
        print("Go to Third Floor and  Enjoy ")
        
        semester=input("Semester:")
        for i in semester:
            print(i)
        
    
    elif department=="B.Tech" or department=="CSE":
        print("Engineering Department students go to under ground for backup managing")
        
        
        registration=input("Registration Done Yes or No:")
        if registration=="yes" or registration=="YES":
            print("Come Inside  and Enjoy")
        
        else:
            print("First go and regiser Your Name")


elif department=="teacher":
    teacher_name=input("Teacher  Name:")
    if teacher_name=="ameen":
        print(f"You are Not Allowed  {teacher_name} sir")   
        
    elif teacher_name=="ifthiquar":
        print(f"Get out {teacher_name}")
    
    elif teacher_name=="aashfaque":
        print(f"Yes {teacher_name} sir, Your  Always welcome  in anytime and anywhere ")
    
    elif teacher_name=="teepu" or teacher_name=="rahim" or teacher_name=="mahboob":
        entry_fees=int(input(f"{teacher_name} Entry Fees:"))
        # print("wait a minute  and give Entry fees")
        if entry_fees==10:
            print("please come later ")
        
        elif entry_fees==20:
            print("come after 10 minutes")
        
        elif entry_fees==30:
            print("yes come and not make noise")
    
    else:
        print("This is Only Authorized Teacher Only Sorry For Say!")
        
    

elif department=="water supply":
    admin=input("Enter Admin Name:")
    print(f"Go to Back Gate and get it 35 Rs/- from  {admin} ")

else:
    print("Out of College St .")         
        
        
        
            
            