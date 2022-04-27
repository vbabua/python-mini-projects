user_input = str(input("Enter a sentence : "))
text = user_input.split()
acronym = ""

for i in text:
    print(i)
    acronym += str(i[0]).upper()

print("Acronym of the sentence \"{t}\" is : {a} ".format(t=user_input, a=acronym))