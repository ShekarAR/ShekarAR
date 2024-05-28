import Admin_m
def cust_opt():
    print("________________")
    print("1 add coustmer ")
    print("2 view coustmer ")
    print("3 mobile number emploee ")
    print("0 prious menu ")
    print("9 Main menu ")
    print("________________")
    k=int(input("slect the option "))
    match(k):
        case 1:
            print("coustmer added sucessfully....")
            cust_add()
            print("________________")
        case 2:
            print("coustmer Viewed sucessfully....")
            cust_view()
            print("________________")
        case 3:
            print("======================")
            print("coustmer mobile numberd suceussfuly,,,,,,")
            cust_mobile()
        case 0:
            cust_opt()
        case 9:
            Admin_m.option()
        


def cust_add():
    print("________________")
    name=(input("enter the name of coustmer"))
   
    print("coustmer name ",name)

def cust_view():
    print("________________")
    print("------------------_")
    print(" coustmer name ",)

def cust_mobile():
    print("------------------------")
    print("||||||||||||||||||||||||||||")
    m=int(input("enter the mobile number"))
    print("mobile number the coustmer",m)
    
    
