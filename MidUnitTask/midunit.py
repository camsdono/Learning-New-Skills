#Restraunt Manager

def getInputs(f_names, f_tel_no, f_group_size, f_rating):
    loop = True
    while loop == True:
        f_names.append(str(input("Enter name: ")))
        f_tel_no.append(str(input("Enter telephone number: ")))
        
        
        c = (int(input("Enter group size: ")))
        
        while inputCheck(c, 1, 20) == False:
            c = int(input("Enter group size: "))
        f_group_size.append(c)
        
        r = float(input("Enter rating: "))

        while inputCheck(r, 1, 10) == False:
             r = float(input("Enter rating: "))

        f_rating.append(r)

        choice = str(input("Do you wish to add another y/n? "))
             
        if choice == "y":
            loop = True

        elif choice == "n":
            loop = False

        else:
            print("An Error has occured")

    return f_names, f_tel_no, f_group_size, f_rating
        
        
def inputCheck(n, minValue, maxValue):

    if n > maxValue:
        return False
    if n < minValue:
        return False
        
    return True

        

#main program
#initalise variables

names = []
tel_no = []
group_size = []
rating = []
maximum = 6

getInputs(names, tel_no, group_size, rating)
