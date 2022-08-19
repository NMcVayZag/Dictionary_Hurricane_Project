import numpy as np
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def clean_damages(lista):
    nlist = []
    for i in lista:
        if i == "Damages not recorded":
            nlist.append(i)
        elif "M" in list(i): 
            data = list(i)
            data.pop()
            data = "".join(data)
            data = round(float(data),2)
            data = data *1000000
            nlist.append(data)
        else:
            data = list(i)
            data.pop()
            data = "".join(data)
            data = round(float(data),2)
            data = data *1000000000
            nlist.append(data)
    return(nlist)
damages_n = clean_damages(damages)
damages = damages_n
print(damages)


# write your construct hurricane dictionary function here:
def dictionary_build(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    new_dict = {}
    for i in range(len(names)):
        nest_dict = {}
        nest_dict_data = ('Name',names[i]),("Month",months[i]),("Year",years[i]),("Max Sustained Wind",max_sustained_winds[i]),("Areas Affected", areas_affected[i]),("Damages", damages[i]),("Deaths",deaths[i])
        nest_dict.update(nest_dict_data)
        new_dict[names[i]] = nest_dict
    return new_dict
hurricane_data = dictionary_build(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
print(hurricane_data)


# write your construct hurricane by year dictionary function here:
def year_sort_dictionary(hurricane_data,years):
    sorted_dictionary = {}
    for i in range(len(years)):
        entry_list = []
        for e in hurricane_data:
            hurricane = hurricane_data[e]
            if hurricane["Year"] == years[i]:
                entry_list.append(hurricane)
        sorted_dictionary[years[i]] = entry_list
    return sorted_dictionary
sorted_dict = year_sort_dictionary(hurricane_data,years)
print(sorted_dict)


# write your count affected areas function here:
def count_impacted_areas(areas_affected):
    concated_list = [y for x in areas_affected for y in x]
    unique_list = np.unique(concated_list)
    unique_list = unique_list.tolist()
    counting_dict = {}
    for i in range(len(unique_list)):
        count = concated_list.count(unique_list[i])
        counting_dict[unique_list[i]] = count
    return counting_dict
    
affected_area_count_dict = count_impacted_areas(areas_affected)
print(affected_area_count_dict)

# write your find most affected area function here:
def most_impacted_area(dict):
    max_count = 0 
    max_area = ""
    key_list = list(dict.keys())
    val_list = list(dict.values())
    for i in range(len(dict)):
        if val_list[i] > max_count:
            max_count = val_list[i]
            position = val_list.index(max_count)
            max_area = key_list[position]
    return(max_area,max_count)
Area_of_impact, Impact_count = most_impacted_area(affected_area_count_dict)
print(Area_of_impact,Impact_count)








# write your greatest number of deaths function here:







# write your catgeorize by mortality function here:







# write your greatest damage function here:







# write your catgeorize by damage function here:
