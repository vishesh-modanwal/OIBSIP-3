import random
print("Welcome to Password Generator")
req_length=int(input("Enter the Specified Length for password: "))



ASCIIVal_AZ=random.randint(65,90)
ASCIIVal_az=random.randint(97,122)
ASCIIVal_09=random.randint(48,57)


Special_Character=['#','$','@','&','%']


char_AZ=chr(ASCIIVal_AZ)
char_az=chr(ASCIIVal_az)
char_09=chr(ASCIIVal_09)
Final_Password=''


number=random.randint(1,4) 
sp_number=random.randint(0,len(Special_Character)-1)



for i in range(0,req_length):
    if(number==1):
        Final_Password+=char_AZ
        ASCIIVal_AZ=random.randint(65,90)
        char_AZ=chr(ASCIIVal_AZ)
    elif(number==2):
        Final_Password+=char_az
        ASCIIVal_az=random.randint(97,122)
        char_az=chr(ASCIIVal_az)
    elif(number==3):
        Final_Password+=char_09
        ASCIIVal_09=random.randint(48,57)
        char_09=chr(ASCIIVal_09)
    elif(number==4):
        Final_Password+=Special_Character[sp_number]
        sp_number=random.randint(0,len(Special_Character)-1)
    number=random.randint(1,4)
    





print("Your Generated Password is ",Final_Password)