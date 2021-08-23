class GYM:
    def __init__(self):
        self.super_user=[6239901774,123456]
        self.member={}
        self.Regimen={}
    
    def assign_Regimen(self):
        x=int(input("enter your mobile number again for verication "))
        a=[i for i in self.member.keys()]
        if x in a:
            if self.member[x][4] <= 18.5:
                print("Your Regimen is: ")
                print("Mon: Chest\nTue: Biceps\nWed: Rest\nThu: Back\nFri: Triceps\nSat: Rest\nSun: Rest")
                
            elif self.member[x][4] > 18.5 and self.member[x][4]<=25:
                print("Your Regimen is : ")
                print("Mon: Chest\nTue: Biceps\nWed: Cardio/Abs\nThu: Back\nFri: Triceps\nSat: Legs\nSun: Rest")
            elif self.member[x][4]> 25 and self.member[x][4]<=30:
                print("Your Regimen is : ")
                print("Mon: Chest\nTue: Biceps\nWed: Abs/Cardio\nThu: Back\nFri: Triceps \nSat: Legs\nSun: Cardio")
            elif self.member[x][4]>30:
                print("your Regimen is : ")
                print("Mon: Chest\nTue: Biceps\nWed: Cardio\nThu: Back\nFri: Triceps\nSat: Cardio\nSun: Cardio")
                
        
        
        
    def view_Regimen(self):
        a=input("you want to see full Regimen or for particular BMI ? [enter full or bmi]")
        if a=='full':
            print("This may be empty because you didn't create Regimen")
            print(self.Regimen)
        elif a=='bmi':
            print("This is the Default Regimen assign ny Edyoda!!!")
            x=float(input("Enter BMI for which you want to Se Regimen: "))
            if x<=18.5:
                print("Mon: Chest\nTue: Biceps\nWed: Rest\nThu: Back\nFri: Triceps\nSat: Rest\nSun: Rest")
            elif x>18.5 and x<=25:
                print("Mon: Chest\nTue: Biceps\nWed: Cardio/Abs\nThu: Back\nFri: Triceps\nSat: Legs\nSun: Rest")
            elif x>25 and x<=30:
                print("Mon: Chest\nTue: Biceps\nWed: Abs/Cardio\nThu: Back\nFri: Triceps \nSat: Legs\nSun: Cardio")
            elif x>30:
                 print("Mon: Chest\nTue: Biceps\nWed: Cardio\nThu: Back\nFri: Triceps\nSat: Cardio\nSun: Cardio")
        else:
            print("Invalid choice!!!")
                
            
            
            
        
        
    def create_Regimen(self):
        a=int(input("how many regimen you want to create: "))
        for i in range(a):
            b={}
            x=int(input("Please enter BMI for which you want to create Regimen: "))
            print("Enter exercise according to day: ")
            Mon=input("Enter exercise for Monday: ")
            Tue=input("Enter exercise for Tuesday: ")
            Wed=input("Enter exercise for Wednesday: ")
            Thu=input("Enter exercise for Thursday: ")
            Fri=input("Enter exercise for Friday: ")
            Sat=input("Enter exercise for Saturday: ")
            Sun=input("Enter exercise for Sunday: ")
            b[x]={"Mon":Mon,"Tue":Tue,"Wed":Wed,"Thu":Thu,"Fri":Fri,"Sat":Sat,"Sun":Sun}
            self.Regimen.update(b)
                
                
        print("Successfully created!!")
        
        
        
    
    
    def delete_Regimen(self):
        a=int(input("enter BMI for which you want to delete Regimen:  "))
        b=[i for i in self.Regimen.keys()]
        if a in b:
            del self.Regimen[a]
            print("Successfully Deleted")
        else:
            print("First Create Regimen for that BMI OR")
            print("BMI does not exit!!")
        
        
        
    
    def update_Regimen(self):
        x=float(input("Enter BMI for which you want to update Regimen: "))
        b=[i for i in self.Regimen.keys()]
        if x in b:
            ans=True
            while ans:
                a=int(input("1.enter 1 to update Monday: \n2.enter 2 to update Tuesday \n3.enter 3 to update Wedneday \n4.enter 4 to update Thursday \n5.enter 5 to update friday \n6.enter 6 to update Saturday \n7.enter 7 to update Sunday \n8.enter 0 to exit \n9.enter -1 to go back "))
                if a==1:
                    i=input("Enter new Regimen")
                    self.Regimen[x]["Mon"]=i
                    print("Successfully edited ")
                elif a==2:
                    i=input("enter new Regimen")
                    self.Regimen[x]["Tue"]=i
                    print("Successfully edited")
                elif a==3:
                    i=input("enter new Regimen")
                    self.Regimen[x]["Wed"]=i
                    print("Successfully edited")
                elif a==4:
                    i=input("enter new Regimen")
                    self.Regimen[x]["Thu"]=i
                    print("Successfully edited")
                elif a==5:
                    i=input("enter new Regimen")
                    self.Regimen[x]["Fri"]=i
                    print("Successfully edited")
                elif a==6:
                    i=input("enter new Regimen")
                    self.Regimen[x]["Sat"]=i
                    print("Successfully edited")
                elif a==7:
                    i=input("enter new Regimen")
                    self.Regimen[x]["Sun"]=i
                    print("Successfully edited")
                elif a==0:
                    ans=False
                elif a==-1:
                    self.gym_super_user()
                else:
                    print("Invalid Choice!!")
        
        else:
            print("First create Regimen for that BMI or Wrong!!!!")
        
        
    def create_member(self):
        a={}
        x=int(input("enter how many members you want to add ?"))
        for i in range(x):
            full_name =input("Enter full name of member: ")
            age=int(input("Enter age: "))
            gender=input("enter gender: ")
            mobile_number=int(input("enter 10 digit mobile number: "))
            e_mail=input("enter e-mail : ")
            BMI=float(input("enter BMI of user : "))
            membership_duration=int(input("Enter membership duration in months: "))
            a[mobile_number]=[full_name,age,gender,e_mail,BMI,membership_duration]
            self.member.update(a)
            
            
        print("Successfully Added")
        
        
        
        
        

            
                              
        
    def view_member(self):
                              
        x=input("do you want to see a particular member or all member ? [enter all or particular]")
        if x=='all':
            print(self.member)
            
        elif x=='particular':
            b=int(input("enter mobile number of member you want to view: "))
            a=[i for i in self.member.keys()]
            if b in a:
                print(self.member[b])
                self.super_user
                
            else:
                print("Please check!!")
        else:
            print("Invalid choice !!")
                              
                              
            
                              
        
    
    def delete_member(self):
        x=int(input("enter mobile number of member you want to delete: "))
        a=[i for i in self.member.keys()]
        if x in a:
            del self.member[x]
            
            print("Successfully Deleted")
            
            
        else:
            print("Please check!!!")
                              
                              
    
    def update_member(self):
        x=int(input("enter mobile number of member of user you want to update: "))
        a=[i for i in self.member.keys()]
        if x in a:
            ans=True
            while ans:
                l=int(input("1.enter 1 to edit name \n2.enter 2 to update mobile number  \n3.enter 3 to update e-mail \n4.enter 4 to update BMI \n5.enter 6 to update membership \n7.enter 0 to exit: \n8.enter -1 to go back "))
                
                
                print("WARNING if you press 0 program will end !!!! ,[advice type -1 intead of 0]")
                if l==1:
                    f=input("Enter new name if member: ")
                    self.member[x][0]=f
                    print("Successfully updated")
                elif l==2:
                    f=int(input("Enter new mobile number: "))
                    x=f
                    print("Successfully edited")
                elif l==3:
                    f=input("Enter new e-mail ")
                    self.member[x][3]=f
                    print("Successfully edited")
                elif l==4:
                    f=float("enter new BMI")
                    self.member[x][4]=f
                    print("Successfully edited")
                elif l==5:
                    f=int(input("Enter updated membership"))
                elif l==0:
                    ans=False
                elif l==-1:
                    self.gym_super_user()
                else:
                    print("Invalid choice!!!")
        else:
            print("You typed wrong number!!!")
                              
                   
        
    def gym_super_user(self):
        ans=True
        while ans:
            x=int(input("1. enter 1 to create member \n2.enter 2 to view member \n3.enter 3 to delete member \n4.enter 4 to update member \n5.enter 5 to create new Regimen \n6. enter 6 to view Regimen \n7.enter 7 to delete Regimen \n8.enter  8 to update Regimen \n9.enter 0 to exit \n10.enter -1 to go back "))
            
            
            print("WARNING if you press 0 program will end !!!! ,[advice type -1 intead of 0]")
            if x==1:
                self.create_member()
                
            elif x==2:
                self.view_member()
                
            elif x==3:
                self.delete_member()
                
            elif x==4:
                self.update_member()
                
            elif x==5:
                self.create_Regimen()
                
            elif x==6:
                self.view_Regimen()
                
            elif x==7:
                self.delete_Regimen()
                
            elif x==8:
                self.update_Regimen()
                
            elif x==0:
                ans=False
            elif x==-1:
                self.menu()
            else:
                print("Invalid choice!!!!!")
                
        
    def gym_member(self):
        x=int(input("enter your mobile number for verication "))
        a=[i for i in self.member.keys()]  
        if x in a:
            ans=True
            while ans:
                f=int(input("1.Enter 1 to see your regimen \n2.enter 2 to view your profile \n3.enter 0 to exit \n4.enter -1 to go back"))
                
                
                print("WARNING if you press 0 program will end !!!! ,[advice type -1 intead of 0]")
                if f==1:
                    self.assign_Regimen()
                    
                elif f==2:
                    print(self.member[x])
                elif f==0:
                    ans=False
                elif f==-1:
                    self.menu()
                else:
                    print("Invalid choice!!")
        else:
            print("Sorry ,you are not a user!!!")
            print("Ask  superuser to add you")
        
        
    
        
    def menu(self):
        ans=True
        while ans:
            
            a=input("Are you a member or superuser  OR enter 0 to close the program ?")
            if a=='member' or a=='Member':
                self.gym_member()

            elif a=='superuser' or a=='Superuser':
                x=int(input("please enter your password to verify you are a superuser: [Hint: ***456]"))
                if x in self.super_user:
                    print("Yes! you are a super user ,here is a list what you want to do: ")
                    self.gym_super_user()
                else:
                    print("Sorry,Please check again")
            elif a=='0':
                ans=False



            else:
                print("Invalid Input!!!")
        
viki=GYM()
viki.menu()
        
        