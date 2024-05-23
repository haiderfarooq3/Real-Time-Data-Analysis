import json
#Opening sampled data set
with open('Sampled_Amazon_eta2.json', 'r') as readfile, open('cleandata.json', 'w') as outfile:
#Cleaning data
    for line in readfile:
        json_data = json.loads(line)
        cleandata = {
            "also_buy": json_data.get("also_buy", []),
            "asin": json_data.get("asin", "")
        }
#Writing clean data in file
        json.dump(cleandata, outfile)
        outfile.write('\n')  
