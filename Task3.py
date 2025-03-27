age = int(input("Enter your age: "))
exp = int(input("Enter your expirience: "))
quali = input("Do you have any qualifications (True/ False)").strip().lower() == "true"
if 25 <= age <= 50 and ( exp > 3 or quali is True):
    print("You are right for us ")
else:
   print("You are not suitable for us")
