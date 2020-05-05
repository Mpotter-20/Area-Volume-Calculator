import math

#shared variables
invalid = "INVALID KEY PLEASE TRY AGAIN."
variables = ["Enter the length of the", "Enter the height of the", "Enter the base of the","Enter the radius of the", "Enter the width of the", ]

def area_calc():
    #area specific variables
    area_message = "The area of the"

    #area specific list
    shapes = ["square", "rectangle", "triangle", "circle", "parrallelogram"]
    square_values = []
    rectangle_values = []
    triangle_values = []
    circle_values =[]
    parrallelogram_values = []

    #introduction
    print("You have selected the AREA CALCULATOR \n")

    #allows user to select a shape
    while True:
        try:
            option_select = int(input(f"""Please select a shape by selecting its number
[1] {shapes[0]}
[2] {shapes[1]}
[3] {shapes[2]}
[4] {shapes[3]}
[5] {shapes[4]}
>>> """))
        #Checks for invalid types
        except ValueError:
            print(invalid)
            continue
        
    #Calculates Area of a Square
        if option_select == 1:
            while True:
                try:
                    length = float(input(f"{variables[0]} {shapes[0]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    area = length * length
                    print(f"{area_message} {shapes[0]} is {area} \n")
                    square_values.insert(0, area)
                    break            
            
    #Calculates Area of a Rectangle   
        elif option_select == 2:
            while True:
                try:
                    length = float(input(f"{variables[0]} {shapes[1]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    break
            while True:
                try:
                    width = float(input(f"{variables[4]} {shapes[1]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    area = length * width
                    print(f"{area_message} {shapes[1]} is {area} \n")
                    rectangle_values.insert(0, area)
                    break
            
    #Calculates Area of a Triangle
        elif option_select == 3:
            while True:
                try:
                    height = float(input(f"{variables[1]} {shapes[2]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    break
            while True:
                try:
                    base = float(input(f"{variables[2]} {shapes[2]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    area = (height * base)/2
                    print(f"{area_message} {shapes[2]} is {area} \n")
                    triangle_values.insert(0, area)
                    break
            
    #Calculates Area of a Circle
        elif option_select == 4:
            while True:
                try:
                    radius = float(input(f"{variables[3]} {shapes[3]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    area = math.pi * radius ** 2
                    print(f"{area_message} {shapes[3]} is {area_circle}\n")
                    circle_values.insert(0, area)
                    break
    #Calculates area of a parrallelogram
        elif option_select == 5:
            while True:
                try:
                    base = float(input(f"{variables[2]} {shapes[4]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    break
            while True:
                try:
                    height = float(input(f"{variables[1]} {shapes[4]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    area = height * base
                    print(f"{area_message} {shapes[4]} is {area} \n")
                    parrallelogram_values.insert(0, area)
                    break

    #checks intial user input for invalid options
        elif option_select != len(shapes):
            print(invalid)
            continue

    #allows user to run the program again or terminate it
        while True:
            rerun = input("would you like to find the area of another shape? y or n \n >>> ")
            if rerun.lower() == "y":
                print("\n")
                i = 0
                break
            elif rerun.lower() == "n":
                #prints values for all calculations done
                if len(square_values) > 0:
                    print(f"area for each square calculated:\n {square_values} \n")
                if len(rectangle_values) > 0:
                    print(f"area for each rectangle calculated:\n{rectangle_values} \n")
                if len(triangle_values) > 0:
                    print(f"area for each triangle calculated:\n{triangle_values} \n")
                if len(circle_values) > 0:
                    print(f"area for each cricle calculated:\n{circle_values} \n")
                if len(parrallelogram_values) > 0:
                    print(f"area for each parrollelogram calculated:\n{parrallelogram_values} \n")      
                input("press any KEY continue")
                i = 1
                break
            elif rerun.lower() != "y" or "n":
                print(invalid)
                continue
        if i == 0:
            continue

        if i == 1:    
            break
        break
    return""

def volume_calc():        
    #varibales
    area_message = "The volume of the"

    #list
    shapes = ["square", "rectangle", "pyramid", "sphere", "cylinder"]
    square_values = []
    rectangle_values = []
    pyramid_values = []
    circle_values =[]
    cylinder_values = []

    #introduction
    print("You have selected the VOLUME CALCULATOR! \n")

    #allows user to select a shape
    while True:
        try:
            option_select = int(input(f"""please select a shape by selecting its number
[1] {shapes[0]}
[2] {shapes[1]}
[3] {shapes[2]}
[4] {shapes[3]}
[5] {shapes[4]}
>>> """))
        #Checks for invalid types
        except ValueError:
            print(invalid)
            continue
        
    #Calculates Volume of a Square
        if option_select == 1:
            while True:
                try:
                    length = float(input(f"{variables[0]} {shapes[0]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    volume = length * length * length
                    print(f"{area_message} {shapes[0]} is {volume} \n")
                    square_values.insert(0, volume)
                    break            
            
    #Calculates Volume of a Rectangle   
        elif option_select == 2:
            while True:
                try:
                    length = float(input(f"{variables[0]} {shapes[1]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    break
            while True:
                try:
                    height = float(input(f"{variables[1]} {shapes[1]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    break
            while True:
                try:
                    width = float(input(f"{variables[4]} {shapes[1]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    volume= length * width * height
                    print(f"{area_message} {shapes[1]} is {volume} \n")
                    rectangle_values.insert(0, volume)
                    break
            
    #Calculates Volume of a pyramid
        elif option_select == 3:
            while True:
                try:
                    height = float(input(f"{variables[1]} {shapes[2]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    break
            while True:
                try:
                    length = float(input(f"{variables[0]} {shapes[2]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    break
            while True:
                try:
                    base = float(input(f"{variables[2]} {shapes[2]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    volume = (height * base * length) / 3 
                    print(f"{area_message} {shapes[2]} is {volume} \n")
                    pyramid_values.insert(0, volume)
                    break
            
    #Calculates Volume of a sphere
        elif option_select == 4:
            while True:
                try:
                    radius = float(input(f"{variables[3]} {shapes[3]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    volume = (4 / 3) * math.pi * radius ** 3
                    print(f"{area_message} {shapes[3]} is {volume}\n")
                    circle_values.insert(0, volume)
                    break
    #Calculates Volume of a cylinder
        elif option_select == 5:
            while True:
                try:
                    radius = float(input(f"{variables[3]} {shapes[4]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    break
            while True:
                try:
                    height = float(input(f"{variables[1]} {shapes[4]}.>>> "))
                except ValueError:
                    print(invalid)
                    continue
                else:
                    volume = math.pi * radius ** 2 * height
                    print(f"{area_message} {shapes[4]} is {volume} \n")
                    parrallelogram_values.insert(0, volume)
                    break

    #checks intial user input for invalid options
        elif option_select != len(shapes):
            print(invalid)
            continue

    #allows user to run the program again or terminate it
        while True:
            rerun = input("would you like to find the volume of another shape? y or n \n >>> ")
            if rerun.lower() == "y":
                print("\n")
                i = 0
                break
            elif rerun.lower() == "n":
                #prints values for all calculations done
                if len(square_values) > 0:
                    print(f"volume for each square calculated:\n {square_values} \n")
                if len(rectangle_values) > 0:
                    print(f"volume for each rectangle calculated:\n{rectangle_values} \n")
                if len(pyramid_values) > 0:
                    print(f"volume for each pyramid calculated:\n{pyramid_values} \n")
                if len(circle_values) > 0:
                    print(f"volume for each cricle calculated:\n{circle_values} \n")
                if len(cylinder_values) > 0:
                    print(f"volume for each cylinder calculated:\n{cylinder_values} \n")      
                input("press any KEY to continue")
                i = 1
                break
            elif rerun.lower() != "y" or "n":
                print(invalid)
                continue
        if i == 0:
            continue

        if i == 1:    
            break
        break
    return""

#allows user to select area or volume calculator / main screen
while True:
    try:
        function_select = int(input("""Please select a function
[1] Area calculator
[2] Volume calculator
[3] Exit Program
>>> """))
        #Checks for invalid types
    except ValueError:
        print(invalid)
        continue
    #runs area calculator
    if function_select == 1:
            print(area_calc())
    #runs volume calculator
    elif function_select == 2:
            print(volume_calc())

    elif function_select == 3:
            exit()
    elif function_select != 1 or 2 or 3:
            print(invalid)
            continue

