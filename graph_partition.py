import sys, json
import numpy as np
import partition_algorithm

def main(adjacency_list_JSON):
    adjacency_list = json.loads(adjacency_list_JSON)
    partition_data = partition_algorithm.partition_graph(adjacency_list)
    return partition_data

if __name__ == '__main__':
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        output = main(sys.argv[1])
        print(output)
    else:
        print(json.dumps({"error": "No parameter provided"}))
