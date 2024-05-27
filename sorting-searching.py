from datetime import datetime 

file2 = open("sorted.txt","a+")
string = ""
array = []
        
def search(arr, num):
    stir = input("Enter keyword: ")
    linear_search(array, stir, num)

def linear_search(array, target, num):
    string = ""
    exist = False
    check = False

    for i in range(len(array)):
        if ((target.upper() == (array[i][1]).upper())
        or (target.upper() == (array[i][2]).upper())
        or (target.upper() == (array[i][3]).upper())
        or (target.upper() == (array[i][5]).upper())):
            if num == 0:
                print(array[i])
            if num == 1:
                string += (array[i][2].lower() + "." +
                array[i][1][0].lower() + array[i][6][:2] + "@gmail.com")
                
                print("Email for ", array[i][2], array[i][1], ": ", string)
                string = ""
            exist = True
        check = False
            
    if exist is False:
        print("Entry not found")

                    
def Sorting(sub_li, ind): #method for sorting
    popped_list = []
    ind_list = []
    var= ""
    if ind != 6:    
        return(sorted(sub_li, key = lambda x: x[ind]))
    else:

        for i in range(len(sub_li)):
            if str(sub_li[i][ind]) == '00-00-0000':
                ind_list.append(i)
        for i in range(len(ind_list)):
            popped_list.append(sub_li[ind_list[i]])
            del(sub_li[ind_list[i]])
            if i != len(ind_list) - 1:
                ind_list[i+1] = ind_list[i+1] - 1

        sub_li = sorted(sub_li, key = lambda x: datetime.strptime(x[6], '%m-%d-%Y'))

        for i in range(len(sub_li)):
            popped_list.append(sub_li[i])

        return popped_list

def last_name(array):
    arr = Sorting(array,1)
    printing(arr, "last name")

def first_name(array):
    arr = Sorting(array,2)
    printing(arr, "first name")
    
def printing(arr, name):
    for i in range(len(arr)):
        string = ""
        for j in range(len(arr[i])):
            string += arr[i][j] + ", "
        string = string[:-2]
        file2.write(string + "\n")
    file2.write("File was sorted by " + name + "\n\n")
    
def gender(array):
    arr = Sorting(array,4)
    printing(arr, "gender")

def bday(array):
    arr = Sorting(array,6)
    printing(arr, "birthday")

def address(array):
    arr = Sorting(array,5)
    printing(arr, "address")

file1 = open("project_names(edited).txt","r+")
array = file1.readlines()[0:]

header = array.pop(0)
array.pop(0)

for i in range(len(array)):
    array[i] = array[i].split(", ")
    array[i][6] = array[i][6][:-2]

while True:
    print("What do you want to do?")
    print("[1]Search\n[2]Sort")
    print("[0]End Program")

    try:
        ans = int(input("Choose a number: "))
        
        if ans == 1:
            print("")
            print("Search using name: ")
            print("[1]Print name\n[2]Create Email")
            try:
                inp = int(input("Choose a number: "))
                
                if inp == 1:
                    print("Search name...")
                    search(array, 0)
                    print("")
                    
                elif inp == 2:
                    print("Create email..")
                    search(array, 1)
                    print("")
                else:
                    1/0

            except:
                print("Please Enter properly.\n")
                
        elif ans == 2:
            print("")
            print("How do you want it to be sorted?")
            print("[1]Last Name\n[2]First Name")
            print("[3]Gender\n[4]Birthday\n[5]Address")
            try:
                inp = int(input("Choose a number: "))
                
                if inp == 1:
                    print("Sorted by Last Names...")
                    file2.write(header)
                    last_name(array)
                    print("")
                    
                elif inp == 2:
                    print("Sorted by First Names...")
                    file2.write(header)
                    first_name(array)
                    print("")
                        
                elif inp == 3:
                    print("Sorted by Gender...")
                    file2.write(header)
                    gender(array)
                    print("")
                    
                elif inp == 4:
                    print("Sorted by Birthday...")
                    file2.write(header)
                    bday(array)
                    print("")

                elif inp == 5:
                    print("Sorted by Address...")
                    file2.write(header)
                    address(array)
                    print("")
                    
                else:
                    1/0
            except:
               print("Please Enter properly.\n")

        elif ans == 0:
            break
        
        else:
            1/0
    except:
       print("Please Enter properly.\n")

file2.close()
