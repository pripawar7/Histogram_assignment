import os
import json
import sys

if (len(sys.argv)!=2):
    print ("Error in number of aurguments for generator.py.")

else:
    filename = "data.txt"
    file = open(filename, "r")
    candidate_dict= {}
    for line in file:
        splitter= line.split("|")
        if (splitter[6]=="CAN"):
            if (splitter[7] in candidate_dict):
                candidate_dict[splitter[7]] = candidate_dict[splitter[7]] + int(splitter[14])
            else:
                candidate_dict[splitter[7]] = int(splitter[14])

    sorted_json_array=sorted([(value,key) for (key,value) in candidate_dict.items()],reverse=True)
    counter=0
    candidate_dict= {}
    while counter < int(sys.argv[1]):
        candidate_dict[sorted_json_array[counter][1]]= sorted_json_array[counter][0]
        counter = counter + 1


    dumps= json.dumps(candidate_dict)
    with open('data.json', 'w') as outfile:
        json.dump(dumps, outfile) 
    
  

    


