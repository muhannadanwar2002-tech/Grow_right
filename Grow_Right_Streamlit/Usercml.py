from City import Dictionary_Cities
from Plants import Dictionary_Plants
print("Grow Right - Saudi Planting Advisor")
print()
print("Option 1 — Grow a Plant \nOption 2 — Best Plants for My City")
print()
    
try:
    choice = int(input("Your choice is: "))

    if choice == 1:
        plant = input("Enter plant: ").lower()
        
        city = input("Enter city: ").lower()
        
        print("Plant you choose is :" , plant )
        print("city you choose is :" , city )
        print()
        try:
            print("debugging")
            print(Dictionary_Cities[city].suitability(plant))
            print("debugging")
            print("Growing Guide:")
            print(Dictionary_Plants[plant].grow_right())
        except(Exception):
            print("Not in DataBase")  
        
        
        
    

    elif choice == 2:
        city = input("Enter city: ").lower()
        print("Top plants in Your city is : ")
        for x in Dictionary_Cities[city].top_3_plants():
            print(x[0] ,":", x[1], "%")
       
        

       

    else:
        raise ValueError 

except ValueError:
    print("Please enter a number 1 or 2  only.")