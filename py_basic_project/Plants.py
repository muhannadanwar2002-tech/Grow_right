#this code contains the database of the plants collected 

#it has a class defined a Plants and a function 

#the grow_right is a display function that'll display the required info to the user 

class Plants:
  
    def __init__(self  , temp ,  hum , P_season , Soil , Watering , SunExposure , location):
        self.temp = temp                            #the temperature range that the plant prefers 
        self.hum = hum                              # the humidity interms of key words which is derived from the precintile found below 
        self.P_season = P_season                    #plants prefered season which should contain only the worldly seasons like summer winter, spring, autumn/falls meaning non specific seasons sa. rainy seasons (which could mean both summer and spring)
        self.Soil = Soil                            #returns a deep description on which soil the plant prefers
        self.Watering = Watering                    #in terms of weeks
        self.SunExposure = SunExposure              # three categorical which are Full Sun, slightly Shade, full Shade
        self.location = location                    # does it grow indoors or outdoors or is it both
  
  
    
#
    def grow_right(self):
        
        return (
            f"Optimal Temperature range: {self.temp[0]} to {self.temp[1]}\n"
            f"Humidity: {self.hum}\n"
            f"Best Season: {self.P_season}\n"
            f"Soil: {self.Soil}\n"
            f"Watering: {self.Watering}\n"
            f"Sun Exposure: {self.SunExposure}\n"
            f"Location: {self.location}"
            )
#by calling the Plant class we can create Objects where each object is a plant this way its more simpler when visualizing it as code rather than having them as classes( which we did do :) )
#and can be grouped together in a simple dictionary and only that dictionary is imported to other classes 
    
#for determining the Humidity will be labeling them based on these precentiles Low = 0-40 ,Medium = 40-70, High= 70-100
#------------------------------Plant DataBase-------------------------------------------------------------------
Rosemary = Plants((15, 30),
                  "Low",
                  "Autumn",
                  "Sandy, well-drained soil",
                  "1-2 Times a week",
                  "Full Sun", 
                  "Outdoor")

Tomato = Plants((18, 30),
                "Medium",
                "Spring",
                "Well-drained soil",
                "3 Times a week",
                "Full Sun",
                "Outdoor")

Lettuce = Plants((10, 22),
                 "Medium",
                 "Winter",
                 "Loose, moist soil",
                 "4 Times a week",
                 "Partial Shade",
                 "Indoor / Outdoor")

Cucumber = Plants((20, 32),
                  "Medium",
                  "Spring",
                  "Rich, well-drained soil",
                  "4 Times a week",
                  "Full Sun",
                  "Outdoor")

Mint = Plants((15, 28),
              "Medium",
              "Spring",
              "Moist, rich soil",
              "4 Times a week",
              "Partial Shade",
              "Indoor / Outdoor")

Basil=Plants((22,42),
             "Medium",
             "Summer",
             " Fertile, loose, well-drained nutrient-dense mix",
             "2 to 4 times a week",
             "Full Sun",
             "Indoor / Outdoor") 

Thyme=Plants((12,40),
             "Low",
             "Spring",
             "Calcareous, gritty, sandy, or loose chalky soils with excellent aeration",
             "Once a week",
             "Full Sun",
             "Indoor / Outdoor")

Parsley=Plants((10,28),
               "Medium",
               "Autumn",
               "Deep, fertile sandy loam rich in organic compost",
               "2 to 3 times a week",
               "Partial Shade",
               "Indoor / Outdoor")
        
#-------------------------------------------------------------------------------------------------------------------------
#as stated before the dictionary's only purpose is to allow a quick access to all of the plants via either user selection or input
Dictionary_Plants = {
  "rosemary":Rosemary,
  "tomato" : Tomato,
  "lettuce" : Lettuce,
  "cucumber" : Cucumber,
  "mint" : Mint ,
  "basil" : Basil,
  "thyme" : Thyme,
  "parsley": Parsley 
}
