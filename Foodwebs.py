"""looking at foodwebs, 

we want to report mean nubmer of species, mean number of connections, number of webs
and spatial level(transect, locale, quadrat, Site)

so let's give it a shot"""

import csv
import scipy
import scipy.stats

f = open("C:/Users/Patrick/Documents/Python/AllesinaLab-isc-e278c8656868/Python/data/Wood_etal_2015_data.csv","r")

csvr = csv.reader(f)

header = next(csvr)
print(header)

my_data = list(csvr)

f.close()

#now we have all of our data transform to array for slicing

my_data = scipy.array(my_data)
print(my_data.shape)

webID = set(my_data[:,0])
#print(webID)

def one_site_stats(total, webID):
    workingwith = total[total[:,0] == webID,]
    #print(workingwith)
    site_type_check = set(workingwith[:,1])
    if len(site_type_check) > 1:
        print("something has gone wrong, multiple spatial types for webID: ", webID)
    else:
        site_type = site_type_check.pop()
    pred_num = list(workingwith[:,3])
    prey_num = list(workingwith[:,4])
    species_num = len(set(pred_num + prey_num))
    #print(species_num)
    connections = workingwith.shape[0]
    
    return [webID, site_type, species_num, connections]

Quadrat = {"Spatial Level" : "Q", "Mean Species" : 0 ,"Mean Connections" : 0, "Number of webs" : 0}
Site  = {"Spatial Level" : "S", "Mean Species" : 0 ,"Mean Connections" : 0, "Number of webs" : 0}
Transect = {"Spatial Level" : "T", "Mean Species" : 0 ,"Mean Connections" : 0, "Number of webs" : 0}
Locale = {"Spatial Level" : "L", "Mean Species" : 0 ,"Mean Connections" : 0, "Number of webs" : 0}


for i in webID:
    temp = one_site_stats(my_data, i)
    if temp[1] == "Q" :
        Quadrat["Number of webs"] += 1
        Quadrat["Mean Species"] = (Quadrat["Mean Species"] + temp[2]) 
        Quadrat["Mean Connections"] = (Quadrat["Mean Connections"] + temp[3])
    elif temp[1] == "S" :
        Site["Number of webs"] += 1
        Site["Mean Species"] = (Site["Mean Species"] + temp[2]) 
        Site["Mean Connections"] = (Site["Mean Connections"] + temp[3]) 
    elif temp[1] == "L" :
        Locale["Number of webs"] += 1
        Locale["Mean Species"] = (Locale["Mean Species"] + temp[2]) 
        Locale["Mean Connections"] = (Locale["Mean Connections"] + temp[3]) 
    else:
        Transect["Number of webs"] += 1
        Transect["Mean Species"] = (Transect["Mean Species"] + temp[2]) 
        Transect["Mean Connections"] = (Transect["Mean Connections"] + temp[3])

enddata = [Quadrat, Site, Transect, Locale]

for spatial in enddata:
    print("Spatial Level: ", spatial["Spatial Level"])
    print("Average Number of Species = ", (spatial["Mean Species"] / spatial["Number of webs"]))
    print("Average Number of connections = ", (spatial["Mean Connections"] / spatial["Number of webs"]))
    print("Total Number of Webs = ", spatial["Number of webs"], "\n")
