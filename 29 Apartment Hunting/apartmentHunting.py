
# json_obj = {
#   "blocks": [
#     {
#       "gym": "false",
#       "school": "true",
#       "store": "false"
#     },
#     {
#       "gym": true,
#       "school": false,
#       "store": false
#     },
#     {
#       "gym": true,
#       "school": true,
#       "store": false
#     },
#     {
#       "gym": false,
#       "school": true,
#       "store": false
#     },
#     {
#       "gym": false,
#       "school": true,
#       "store": true
#     }
#   ],
#   "reqs": ["gym", "school", "store"]
# }

json_obj = {
    "blocks": [
        {
            "gym": False,
            "school": True,
            "store": False
        },
        {
            "gym": True,
            "school": False,
            "store": False
        },
        {
            "gym": True,
            "school": True,
            "store": False
        },
        {
            "gym": False,
            "school": True,
            "store": False
        },
        {
            "gym": False,
            "school": True,
            "store": True
        }
    ],
    "reqs": ["gym", "school", "store"]
}




import json
import copy

def apartmentHunting(blocks, reqs):
    bestSuitedBlock = 0

    minDistanceFromEachBlock = {}

    for index, block in enumerate(blocks):
        minDistanceFromEachBlock[index + 1] = copy.deepcopy(blocks[index])
    

    for req in reqs:
        currVal = minDistanceFromEachBlock[1][req] 
        minDistanceFromEachBlock[1][req] = 0 if currVal else float('+inf') 



    currMin = copy.deepcopy(minDistanceFromEachBlock[1])

    for block in blocks[1:]:
        count = 2
        for req in reqs:
            print(minDistanceFromEachBlock[count][req])
            if currMin[req] != float('inf'):
                if block[req] is True:
                    currMin[req] = minDistanceFromEachBlock[count][req] = 0
                else:
                    print(currMin, "--")
                    minDistanceFromEachBlock[count][req] = currMin[req] + 1
                    currMin[req] += 1
        count += 1

    for b in minDistanceFromEachBlock:
        print(minDistanceFromEachBlock[b])
    
    


    return bestSuitedBlock


blocks = json_obj["blocks"]
reqs = json_obj["reqs"]

print(apartmentHunting(blocks, reqs))