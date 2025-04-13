reference_number=50

user_input=int(input("შეიყვანეთ რიცხვი:"))

if user_input < reference_number:
    print("თქვენი რიცხვი ნაკლებია ცნობისთვის მოცემულ რიცხვზე.")
elif user_input > reference_number:
    print("თქვენი რიცხვი მეტია ცნობისთვის მოცემულ რიცხვზე.")
else:
    print("თქვენი რიცხვი ტოლია ცნობისთვის მოცემულ რიცხვზე.")    