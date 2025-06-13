numbers = []
num_count = int(input("enter num: "))

for i in range(num_count):
    num = int(input("enternumber: "))
    if num == 3:
        break
    numbers.append(num)

print("3-ის გამოჩენამდე შეყვანილი რიცხვები:", numbers)