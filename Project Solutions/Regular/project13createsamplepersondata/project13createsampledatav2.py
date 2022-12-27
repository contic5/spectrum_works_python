import names
import random
from faker import Faker
from faker.providers import BaseProvider
from fpdf import FPDF

"""
Columns
,Name, Username, ID Number, Email, Phone, City, State
"""
columnnames_written="#,Name,Username,ID Number,Email,Phone,City,State".split(",")
columnnames="rownum,name,username,id_num,email,phone,city,us_state".split(",")
offset=36
widths=[6,30,30,24,50,26,38,32]
class User:
    totalrows=0
    def __init__(self) -> None:
        fake = Faker('en_US')
        fake.add_provider(BaseProvider)
        profile=fake.simple_profile()
        self.userdata={}
        self.userdata["rownum"]=str(User.totalrows+1)
        User.totalrows+=1
        
        self.userdata["name"]=profile["name"].split(" ")[0]+" "+profile["name"].split(" ")[1]
        self.userdata["username"]=profile["username"]
        self.userdata["id_num"]=self.generate_id_num()
        self.userdata["email"]=profile["mail"]
        self.userdata["phone"]=self.generate_phone()
    
        self.userdata["city"]=fake.city()
        self.userdata["us_state"]=fake.state()

    def generate_digits(self,total_digits,zero_first=True):
        digits=""
        for i in range(total_digits):
            if(i==0 and not zero_first):
                digits+=str(random.randint(1,9))
            else:
                digits+=str(random.randint(0,9))
        return digits
    def generate_letters(self,total_letters):
        all_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letters=""
        for i in range(total_letters):
            letters+=all_letters[random.randint(0,len(all_letters)-1)]
        return letters

    def generate_id_num(self):
        return self.generate_letters(3)+"-"+self.generate_digits(4)
    def generate_phone(self):
        return self.generate_digits(3,False)+" "+self.generate_digits(3)+"-"+self.generate_digits(4)
    
    def __str__(self) -> str:
        res=self.userdata["rownum"]+","
        res+=self.userdata["name"]+","
        res+=self.userdata["username"]+","
        res+=self.userdata["id_num"]+","
        res+=self.userdata["email"]+","
        res+=self.userdata["phone"]+","
        res+=self.userdata["city"]+","
        res+=self.userdata["us_state"]
        return res

total_users=50
def main():
    Faker.seed(0)
    users=[]
    user=None
    for i in range(total_users):
        user=User()
        users.append(user)
    print(",Name, Username, ID Number, Email, Phone, City, State")
    for user in users:
        print(user)

    pdf=FPDF(orientation="L")
    pdf.add_page()

    pdf.set_font("Arial",style="B",size=9)
    columnon=0
    for columnname,width in zip(columnnames_written,widths):
        if(columnon==len(columnnames)-1):
            pdf.cell(width,10,txt=columnname,ln=1)
        else:
            pdf.cell(width,10,txt=columnname,ln=0)
        columnon+=1

    pdf.set_font("Arial",size=9)
    rowon=2
    for user in users:
        columnon=0
        for item,width in zip(columnnames,widths):
            if(columnon==len(columnnames)-1):
                pdf.cell(width,10,txt=user.userdata[item],ln=1)
            else:
                pdf.cell(width,10,txt=user.userdata[item],ln=0)
            columnon+=1
        rowon+=1
        
    pdf.output("Sample Data.pdf")
    print("Sample Data Updated")


if __name__=="__main__":
    main()