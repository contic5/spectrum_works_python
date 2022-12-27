import names
import random
"""
Columns
Name, Username, ID Number, Email, Phone, City, State
"""

class User:
    def __init__(self) -> None:
        self.firstname,self.lastname=self.generate_name()
        self.username=self.generate_username(self.firstname,self.lastname)
        self.id_num=self.generate_id_num()
        self.email=self.generate_email(self.firstname,self.lastname)
        self.phone=self.generate_phone
        self.city,self.us_state=self.generate_city_and_state()

    def generate_name(self):
        return names.get_first_name(),names.get_last_name()
    def generate_username(self,firstname,lastname):
        return firstname[0]+lastname+self.generate_digits(5)
    def generate_digits(self,total_digits,zero_first=True):
        digits=""
        for i in range(total_digits):
            if(i==0 and not zero_first):
                digits+=str(random.randint(1,9))
            else:
                digits+=str(random.randint(0,9))
        return digits
    def generate_id_num(self):
        return self.generate_digits(7)
    def generate_phone(self):
        return self.generate_digits(3,False)+" "+self.generate_digits(3)+"-"+self.generate_digits(4)
    def generate_email(self,firstname,lastname):
        pass
    def generate_phone(self):
        pass
    def generate_city_and_state(self):
        pass

total_users=50
def main():
    users=[]
    for i in range(total_users):
        user=User()
        users.append(user)
    print(users[0])

if __name__=="__main__":
    main()