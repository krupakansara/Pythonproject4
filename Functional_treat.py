#Data Analyzer and Transformer

dataset_summary = {}

#---Data Input---

def input_1d():
    """Take 1D list values from the user."""
    data = input("Enter numbers separated by space: ")
    data = list(map(int, data.split()))
    return data

def input_2d():
    """Take 2D list values from the user."""
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    data = []

    for i in range(rows):
        row = list(map(int,input("Enter values for row: ").split()))
        data.append(row)
    return data

def sample_data():
    """return sample 1D data."""
    return[[10,20,30,20,40,50,30]]

def sample_2d_data():
    """return sample 2D data."""
    return [[10,20,30],[5,15,25],[40,10,20]]

#----Built-in Functions-----

def basic_statistics(data):
    """Display basic statistics using built-in functions."""
    print("\n ======= Basic Statistics====")

    print("Number of values: ", len(data))
    print("Sum: ", sum(data))
    print("Minimum: ", min(data))
    print("Maximum: ", max(data))

    average = sum(data) / len(data)
    print("Average:", average)

    #---User Defined FUnctions---

def calculate_average(data):
    """Calculate the average of the dataset."""
    average = sum(data)/ len(data)
    return average

def find_duplicates(data):
     """Find duplicates values in the dataset"""
     duplicates = []

     for value in data:
         if data.count(value) > 1 and value not in duplicates:
            duplicates.append(value)
     return duplicates

def display_unique(data):
    """Display unique values from the datasets"""
    unique = []

    for value in data:
        if value not in unique:
            unique.append(value)
    print("Unique values:", unique)

##------Args------

def display_values(*args):
    """Accept and display multiple values using *args."""
    print("\n====*ARGS VALUES =====")

    for value in args:
        print(value)

        
#------ kwargs----

def dataset_characteristics(**kwargs):
    """Display dataset characteristics using **kwargs."""
    print("\n====Dataset summary===")

    for key, value in kwargs.items():
        print(key, ":", value)

    
#---recursion---

def factorial(number):
    """Calculate factorial using recursion."""
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number -1)


#lambda, map and filter

def lambda_operations(data):
    """use lambda functions with map and filter."""

    print("\n==lambda operations==")
    threshold=int(input("Enter threshold value: "))

    above = list(filter(lambda x: x> threshold, data))
    below = list(filter(lambda x: x < threshold, data))

    doubled = list(map(lambda x: x*2,data))

    print("Values above threshold: ", above)
    print("values below threshold: ", below)
    print("Values after multiplying by 2: ", doubled)

#Global Keyword

def update_global_summary(data):
    """store dataset summary using a global variable."""
    global dataset_summary

    total = len(data)
    average = sum(data)/len(data)

    dataset_summary={
        "Total Values" : total,
        "Overall Mean" : average

    }
    
def display_global_summary():
    """display the global dataset summary.."""
    print("\n==== global dataset summary===")

    for key, value in dataset_summary.items():
        print(key, ":", value)

#return multiple values

def multiple_statistics(data):
    """return minimum, maximum and average values."""
    minimum = min(data)
    maximum = max(data)
    average = sum(data) / len(data)

    return minimum, maximum, average

#2D list display
def display_2d(data):
    """Display a 2D list in grid format"""
    print("\n==== 2D list ===")

    for row in data:
        for value in row:
            print(value, end="\t")
        print()

#sorting
def sort_1d(data):
    """sort a 1D list using sort method"""
    print("\n==== 1D sorting ===")

    choice=input("Enter A for ascending or D for descending: ")

    if choice == "A" or choice == "a":
        data.sort()
        print("Ascending order: ",data)

    elif choice == "D" or choice == "d":
        data.sort(reverse=True)
        print("Descending order: ",data)

    else:
        print("Invalid choice.")

def sort_2d(data):
    """ sort rows of a 2d list using sorted functions"""
    print("\n === 2D sorting==")
    sorted_data = sorted (data)

    print("Original 2D list: ")
    display_2d(data)

    print("\n sorted 2D list:")
    display_2d(sorted_data)

#documantation

def show_documentation():
    """ Display documentation of all functions"""
    print("\n====Function documantation===")

    print("input_1d:",input_1d.__doc__)
    print("input_2d:",input_2d.__doc__)
    print("sample_data:", sample_data.__doc__)
    print("sample_2d_data: ", sample_2d_data.__doc__)
    print("basic_statistic: ", basic_statistics.__doc__)
    print("calculate_average: ", calculate_average.__doc__)
    print("find_duplicates: ", find_duplicates.__doc__)
    print("display_unique:", display_unique.__doc__)
    print("display_values: ",display_values.__doc__)
    print("dataset_characteristics:", dataset_characteristics.__doc__)
    print("factorial:", factorial.__doc__)
    print("lambda_operations:" , lambda_operations.__doc__)
    print("update_global_summary: ", update_global_summary.__doc__)
    print("display_global_summary: ", display_global_summary.__doc__)
    print("multiple_statistics: ", multiple_statistics.__doc__)
    print("display_2d: ", display_2d.__doc__)
    print("sort_1d:", sort_1d.__doc__)
    print("sort_2d:", sort_2d.__doc__)

#main program

print("=====================")
print("FUNCTIONAL TREAT")
print("=====================")

print("\n choose data type")
print("1. 1D list")
print("2. 2D list")

data_type=input("Enter your choice: ")

if data_type=="1":
    print("\n Choose Data input")
    print("1. Enter values menually")
    print("2. Use sample data")

    choice = input("Enter your choice: ")

    if choice == "1":
        data= input_1d()
    elif choice == "2":
        data = sample_data()
    else:
        print("Invalid chooce.")
        data = []

    if len(data) >0:
        update_global_summary(data)

        while True:
            print("\n ==== Main Menu===")
            print("1. Basic Statistics")
            print("2. Calculate Average")
            print("3. Find Duplicates")
            print("4. Display Unique values")
            print("5. Display values using *args")
            print("6. Dataset summary using **kwargs")
            print("7. Factorial using Recusrsion")
            print("8. Lambda, Map and Filter")
            print("9. Global Dataset Summary")
            print("10. Return multiple statistics")
            print("11. Sort 1D list")
            print("12. FUnction Documentation")
            print("13. Exit")

            choice= input("Enter your choice:")

            if choice == "1":
                basic_statistics(data)

            elif choice == "2":
                average = calculate_average(data)
                print("Average: ",average)

            elif choice == "3":
                duplicates = find_duplicates(data)
                print("Duplicate values: ", duplicates)

            elif choice == "4":
                display_unique(data)

            elif choice == "5":
                display_values(*data)

            elif choice == "6":
                dataset_characteristics(
                    Total_Values=len(data),
                    Sum=sum(data),
                    Minimum=min(data),
                    Maximum=max(data),
                    Average=sum(data)/len(data)
                    )
            
            elif choice == "7":
                number = int(input("Enter a number: "))

                if number >= 0:
                     result = factorial(number)
                     print("Factorial: ", result)
                else:
                    print("Enter a positive number.")
         
        
            elif choice == "8":
                lambda_operations(data)
                
            elif choice == "9":
                display_global_summary()

            elif choice == "10":
                minimum, maximum, average = multiple_statistics(data)

                print("Minimum: ", minimum)
                print("Maximum:", maximum)
                print("Average: ", average)

            elif choice == "11":
                sort_1d(data)

            elif choice == "12":
                show_documentation()

            elif choice == "13":
                print("Thank you for using functional treat!")
                break
             
            else:
                print("Invalid choice.")
    
elif data_type=="2":

    print("\nChoose Data Input")
    print("1. Enter values manually")
    print("2. Use sample data")

    choice = input("Enter your choice:")

    if choice == "1":
        data_2d = input_2d()
    elif choice == "2":
        data_2d = sample_2d_data()

    else:
        print("invalid choice.")
        data_2d = []

    if len(data_2d) > 0:

        while True:

            print("\n=== 2d list menu==")
            print("1.Display 2D list")
            print("2. Sort 2D list")
            print("3. Function Documentation")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                display_2d(data_2d)

            elif choice == "2":
                sort_2d(data_2d)
            elif choice == "3":
                show_documentation()

            elif choice == "4":
                print("Thank you for using Functional Treat!")
                break
            else:
                print("Invalid choice")
else:
    print("invalid data type choice")
    
        
            
            

        
            
    
    
    
    
        
    

        

    

        

    

    
        
    
    

        
        
    



    
    
