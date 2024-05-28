def product_opt():
    print("________________")
    print("1 add productuct ")
    print("2 view productuct ")
    print("0 prious menu ")
    print("9 Main menu ")
    print("________________")
    k=int(input("slect the option "))
    match(k):
        case 1:
            print("productuct added sucessfully....")
            product_add()
            print("________________")
        case 2:
            print("productuct Viewed sucessfully....")
            product_view()
            print("________________")
        case 0:
            product_opt()
        case 9:
            Admin_m.option()
        


def product_add():
    print("________________")
    name=(input("enter the name of productuct"))
   
    print("productuct name ",name)

def product_view():
    print("________________")
    print("------------------_")
    print("productuct name ",name,)

    
