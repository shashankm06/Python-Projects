print("Welcome to The Movie World")
print("You have 5 options to select from")

age = int(input("enter age:"))


print("1.KGF")
print("2.Fast & Furious")
print("3.Mission Impossible")
print("4.Kabir Singh")
print("5.Anora")


movie = int(input("select (1/2/3/4/5) acc to the movie you want to watch: "))

if movie == 1:
    print("get your tickets at the counter ")

elif movie == 2:
    print("get your tickets at the counter")

elif movie == 3:
    print("get your tickets from the counter")

elif movie == 4 and age < 18:
    print("ineligible for the selected movie") 

elif movie == 4 and age >= 18: 
    print("you are eligible, get your tickets at the counter")

elif movie == 5 and age < 18:
    print("ineligible for the selected movie") 
    
elif movie == 5 and age >= 18: 
    print("you are eligible, get your tickets at the counter")

else:
    print("invalid input")