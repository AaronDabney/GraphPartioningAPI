import sys, json
import numpy as np
import partition_algorithm

def main(aListJSON):
    aList = json.loads(aListJSON)
    partitionData = partition_algorithm.partitionGraph(aList)
    return partitionData

if __name__ == '__main__':
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        output = main(sys.argv[1])
        print(output)
    else:
        print(json.dumps({"error": "No parameter provided"}))
