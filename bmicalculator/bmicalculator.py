height = float(input("Enter the height in cms : ")) / 100
weight = float(input("Enter the weight in Kgs : "))

bmi_index = weight / (height * height)

print("Body mass index : ", bmi_index)

if bmi_index > 0:
    if bmi_index <= 16:
        print("Severely Underweight")
    elif bmi_index <= 18.5:
        print("Underweight")
    elif bmi_index <= 25:
        print("Healthy")
    elif bmi_index <= 30:
        print("Overweight")
    else:
        print("Severely Overweight")
else:
    print("Enter valid details...")
