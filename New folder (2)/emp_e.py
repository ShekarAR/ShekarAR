import Admin_m
def emp_opt():
    print("________________")
    print("1 add employee ")
    print("2 view employee ")
    print("3 Delete emploee ")
    print("0 prious menu ")
    print("9 Main menu ")
    print("________________")
    s=int(input("slect the option "))
    match(s):
        case 1:
            print("Employee added sucessfully....")
            emp_add()
            print("________________")
        case 2:
            print("Employee Viewed sucessfully....")
            emp_view()
            print("________________")
        case 3:
            print("======================")
            print("employe deleted suceussfuly,,,,,,")
            emp_del()
        case 0:
            emp_opt()
        case 9:
            Admin_m.option()
        


def emp_add():
    print("________________")
    name=(input("enter the name ofemployee"))
    age=int(input("enter the age of employee"))
    print("employe name ",name,"age",age)

def emp_view():
    print("________________")
    print("employe name ","name","age","age",)

def emp_del():
    print("------------------------")
    print("delete the employe")
    
    

                    
