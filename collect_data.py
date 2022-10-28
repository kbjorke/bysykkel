import json
import urllib.request
import datetime
import time

sname = ["Stensparken", "Pilestredet", 	"Thereses gate", "Bislett Stadion", "Henrik Ibsens gate", "Sørvest for Slottsparken", 
        "7. juni-plassen", "Saga Kino"]
spacing = ["\t", "\t\t", "\t\t", "\t\t", "\t\t\t", "\t\t\t", "\t\t\t", "\t\t\t"]
sids = [163, 112, 96, 251, 122, 105, 30, 195]

while(True):
    f_bikes = open("data/num_bikes.txt", "a")
    f_docks = open("data/num_docks.txt", "a")

    url = urllib.request.urlopen("https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json")
    data = json.load(url)
    #print(data["last_updated"])
    
    update_time_posix = data["last_updated"]
    update_time = datetime.datetime.fromtimestamp(update_time_posix)
    
    #print(update_time)
    
    output_bikes_string = "%s" % update_time
    output_docks_string = "%s" % update_time
    
    #line = f.readline()
    #print(line)
    for i in range(len(sids)):
        #print(sname[i])
        #print(data["data"]["stations"][sids[i]])
        #print("[B: %2d / D: %2d]" % (data["data"]["stations"][sids[i]]["num_bikes_available"],
        #        data["data"]["stations"][sids[i]]["num_docks_available"]))
        
        output_bikes_string += "%s%2d" % (spacing[i], data["data"]["stations"][sids[i]]["num_bikes_available"])
        output_docks_string += "%s%2d" % (spacing[i], data["data"]["stations"][sids[i]]["num_docks_available"])
    
    output_bikes_string += "\n"
    output_docks_string += "\n"
    
    #print(output_string)
    f_bikes.write(output_bikes_string)
    f_docks.write(output_docks_string)

    f_bikes.close()
    f_docks.close()
    time.sleep(600)
