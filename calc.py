import math


name = "Ugochuwku Mayor Chukwuemeka ";
reg = "MOUAU/CMP/21/117513";
dept = "Computer Science";
print("   Student Details")
print(" ")
print("   Name: " , name)
print("   Reg. Number: ", reg)
print("   Department: ", dept)
def calc():
    while True:
        print(" ")
        print("==========================================================")
        print(" ")
        wel = "Welcome, What Operation Do You Want To Perform:"
        
        print(wel.center(30))
        
        print(" ")

        print("1. Addition(+)")


        print("2. Subtraction(-)")


        print("3. Multiplication(*)")


        print("4. Division(/)")


        print("5. SquareRoot(√)")


        print("6. Power(^)")


        print("7. Modulus(%)")

        print(" ")
        print("****************************************")
       
        ret = int(input("Enter The Number Of An Operation: "))
        
        
        if ret == 1:
            add_1 = int(input("First Num To Add:  "))
            add_2 = int(input("Second Num To Add :"))
            
            result = add_1 + add_2
            
            print("Result: {}".format(result))
            
        elif ret == 2:
            sub_1 = int(input(" Num To Subtract: "))
            sub_2 = int(input("Num To Subtract: "))
            
            result = sub_1  - sub_2
            
            print("Result: {}".format(result))
            
            
        elif ret == 3:
            mut_1 = int(input(" Num To Multiply: "))
            mut_2 = int(input("Num To Multiply: "))
            
            result = mut_1 *mut_2
            
            print("Result: {}".format(result))
            
            
        elif ret == 4:
            
            div_1 = int(input(" Num To Divide: "))
            div_2 = int(input("Num To Divide: "))
            
            result = div_1/div_2
            
            print("Result: {}".format(result))
            
            
        elif ret == 5:
            rot_1 = int(input(" Num To Find Root: "))
            result = math.sqrt(rot_1)
            
            print("Result: {}".format(result))
        
        
        
        elif ret == 6:
            pow_1 = int(input(" Num To Find Power: "))
            result = (pow_1**2)
            
            print("Result: {}".format(result))
            
          
        elif ret == 7:
            mod_1 = int(input(" Num To Find Mod: "))
            mod_2 = int(input("Num To Find Mod: "))
            result = mod_1 % mod_2
            
            print("Result: {}".format(result))
            
calc()

