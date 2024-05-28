import emp_e
import cust_m
import product_e
def option():
           print("1 employee")
           print("2 customer")
           print("3 product")
           print("________________")
           s=int(input("enter the option:"))
           match(s):
               case 1:
                   print(" empolye")
                   emp_e.emp_opt()                            
               case 2:
                   print("customer")
                   cust_m.cust_opt()    
               case 3:
                   print("product")
                   product_e.product_opt()
