counties=["Arapahoe","Denver","jefferson"]
if counties[1]=='Denver':
    print(counties[1])
counties=["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("EL Paso is in the list of counties.")    
else:
    print("El Paso is not in the list of counties")
if "Arapahoe" in counties and "El Paso" in counties:
    print ("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
for county in counties:
    print("Arapahoe")
for county in counties:
    print("Denver")
for county in counties:
    print("Jefferson")
numbers = [0,1,2,3,4]
for num in numbers:
    print(num)
for i in range(len(counties)):
    print (counties[0])
counties_tuple = ("Arapahoe","Denver","Jefferson")
for i in range(len(counties_tuple)):
    print(counties_tuple[0])
counties_tuple = ("Arapahoe","Denver","Jefferson")
for i in range(len(counties_tuple)):
    print(counties_tuple[1])  
counties_dict = {"Arapahoe":422829,"Denver":463353,"jefferson":432438}
for county in counties_dict:
    print(counties_dict.get(county))
counties_dict = {"Arapahoe":422829,"Denver":463353,"jefferson":432438}
for county, voters in counties_dict.items():
    print(county, voters)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "rgistered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "rgistered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "rgistered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
        print(county_dict['county'])
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
        print(county + " county has " + str(voters) + " registered voters.")
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
        print(f"{county}  county has {voters} registered voters.")






