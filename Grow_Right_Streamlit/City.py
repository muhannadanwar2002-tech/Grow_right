#in this file it is strictly only cities of KSA databases since including more could be come tedious 

from Plants import Dictionary_Plants     #this the dictionary of the plant obj which we have discussed in the plant section

#the class City includes :    a vast of functions(by that i mean three :) )

#the score calculator function :  determines if that plant is ideal for said city 

#   however it isn't a strict schedule of a function and by that i mean in agriculture. Plants have tendencies to survive and adapt 
#   meaning even though a plant prefers a range of said temp or humidity it can survive if it lets extended it by 1c or 5c 
#   like saying you prefer eat 2 salad bawls but you ended up eating 3 or 4 its quite the same though it will require more caring 
#   like interms of tomato's they can be planted in a vacuum in winter and they will still grow 
#   so what the function is doing is trying to give a score if it is within the prefered plant a 100
#   but if it isn't then check it to a margin of 5 or so and give a a different score 

#the suitability function : is the displayer of the score_calculator function 

#   by using simple logic the function compares the score to a certain value or above it and displays that the plant is suitable or not for said city

#the third and final function is the top_3_plants function :
#   by using the score function again we can then determine the top 3 plants of said city 


class City :
 
  
    def __init__(self , name , temp , hum):
        self.name = name                                           #the name of city
        self.temp = temp                                            #the temperature of each season of the city
        self.hum = hum                                              # the humidity of each season of the city (as keywords like how it was used in plants) 
    
    def score_calculator(self,plant_name):
        
        plant=Dictionary_Plants[plant_name]                           #defining plant as a container of the Dictionary for simpler viewing and understanding rather than just implementing it in the condition
        
        season=plant.P_season                                       #the prefered season of the plant is defined to be used on the dict of the city attributes
        
        if min(plant.temp)<= self.temp[season] <=max(plant.temp): #is a strict condition where if the plant temp is within range of city temp 
        
            temp_score=60                                           #when satisfied provide 60 score in temperature
        
        elif min(plant.temp) -5 <= self.temp[season] <=max(plant.temp) +5:#a less strict version where a margin of 5 is add 
        
            temp_score=30                                           #when satisfied provide 20 score in temperature because of the addition of the margin
        
        else:
        
            temp_score=0                                           #a score of zero is provide whenst the logic condition fails
        
        hum_lvl={"Low":1,"Medium":2,"High":3}                      #creating a value equivelant for calculating the difference (remember we must not be so strict or the plant wouldn't be assigned to a city ) 
        
        if abs(hum_lvl[plant.hum]-hum_lvl[self.hum[season]])==0:    #a strict condition that calculates the absolute difference of humidity and must be equal=0 (meaning no difference at all)
        
            hum_score=40                                            #similar as temp provide a score in humidity of 40  
        
        elif abs(hum_lvl[plant.hum]-hum_lvl[self.hum[season]])==1:  #less strict condition where the plant humidity and the city humidity can tolerate a difference of 1 
        
            hum_score=20                                            #similar as temp provide a score in humidity of 20 (less strict) 
        
        else:
        
            hum_score=0                                             #condition fails humidity score assigned as zero
        
        return hum_score+temp_score                                 #returns total score
            
    
    def suitability(self,plant_name):                               #the displayer of score_calculator based on conditions

        score=self.score_calculator(plant_name)                     #defining score by calling score_calculator (which returns score of the plant)
        
        if score>= 80:                                              #threshold set to 80 or above for plants that are very suitable
        
            print("Suitability Score:" , score , "%")               
        
            print("Highly Suitable") 
      
        elif score >= 60:                                           #threshold set to 60 for just suitable 
        
            print("Suitability Score:" , score , "%")
        
            print("Suitable")
    
        else :
            print("Suitability Score:" , score, "%")                #otherwise not suitable
        
            print("Not Suitable")
            
            
            
#(as you can see that by allowing score (score_calculator() ) to have two ways of conditioning (strict and semi strict) we allowed flexibility for the plants )
    
    # def p(self , name1 , plant_name1 ):
    #   if self.name == name1:
    #     for x in self.suit:
    #       if x.lower() == plant_name1 :
    #         return Dictionary_Plants[plant_name1].GROW_RIGHT()
    
    def top_3_plants(self):                             #returns best 3 of city or top3
    
        best=[]                                          #empty list to store the reordering of the plants based on score for each city
    
        for p in Dictionary_Plants:  
    
            sc=self.score_calculator(p)                 #sends each plant in the dictionary to the score calculator
    
            best.append((p,sc))                         #appends a tuple of plant and score of the plant
    
        best=sorted(best,key=lambda x:x[1],reverse=True)#sorts best list in reverse order so that highest is first and lowest is last 
    
        return best[:3]                                 #returns the list of top 3
    
    
    
    
#---------------------------------KSA City Database--------------------------------------------------
Riyadh = City( "Riyadh"
              ,{"Winter": 15.4, "Spring": 27.0, "Summer": 35.7, "Autumn": 26.9},
              {"Winter": "Low","Spring": "Low","Summer": "Low","Autumn": "Low"})

Makkah = City( "Makkah",
              {"Winter": 22.5,"Spring": 28.9,"Summer": 33.5,"Autumn": 29.3},
              {"Winter": "Medium","Spring": "Low","Summer": "Low","Autumn": "Medium"})

Madinah = City( "Madinah",
               {"Winter":18.4,"Spring": 27.4,"Summer": 34.5,"Autumn": 28.6},
               {"Winter": "Low","Spring": "Low","Summer": "Low","Autumn": "Low"})

Jazan = City( "Jazan",
             {"Winter": 26.2,"Spring": 29.9,"Summer": 32.7,"Autumn": 30.7},
             {"Winter": "High","Spring": "High","Summer": "High","Autumn": "High"})

Al_Qassim = City( "Al_Qassim",
                 {"Winter": 14.2,"Spring": 25.8,"Summer": 35.0,"Autumn": 26.3},
                 {"Winter":"Medium","Spring": "Low","Summer": "Low","Autumn": "Low"})

Al_Baha = City( "Al_Baha",
               {"Winter": 15.8,"Spring": 21.0,"Summer": 25.3,"Autumn": 20.7},
               {"Winter": "Medium","Spring":"Medium","Summer":"Low","Autumn": "Medium"})

Abha = City( "Abha",
            {"Winter": 15.7,"Spring": 20.0,"Summer": 22.6,"Autumn": 18.6},
            {"Winter": "High","Spring": "Medium","Summer": "Medium","Autumn": "Medium" })

#similar to Plants will be using Dictionary for a quick and easy import as well as making it simpler for any viewer of code
Dictionary_Cities = {
  "riyadh" : Riyadh,
  "makkah" : Makkah ,
  "madinah" : Madinah,
  "jazan" : Jazan,
  "al_qassim" : Al_Qassim  ,
  "al_baha" : Al_Baha  ,
  "abha" : Abha  
}