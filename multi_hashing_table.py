import sys
import random

def main():
    # Add checks for # cmd line args

    # Setting input parameters
    num_table_entries = int(sys.argv[1])
    num_flows = int(sys.argv[2])
    num_hashes = int(sys.argv[3])

    # Creating hash table
    hash_table = [0] * num_table_entries

    # Generating random flow IDs
    flows = [0] * num_flows
    for i in range(num_flows):
        flows[i] = random.randrange(10000000)

    # Creating multiple hashes
    hashes = []
    for hash in range(num_hashes):
        hashes.append(random.randrange(10000000))

    # Inserting flows into the hash table
    insert_flows(flows, hashes, hash_table)

    # Printing results
    print("Number of flows: " + str(1000-hash_table.count(0)))
    for index in range(len(hash_table)):
        print(str(index) + ": " + str(hash_table[index]))

# main()

# Checks number of duplicate IDs [For testing purposes]
def check_flow_id_dups(flows):
    dup = -1
    for flow in flows:
        for flow2 in flows:
            if flow == flow2:
                dup += 1
        if dup > 0:
            print(dup)
        dup = -1

# Implementing folding hashing
# Split number into two (first four digits, and then rest of number)
# Add two parts and then do num % num_table_entries
def hash_function(flow_id, num_table_entries):
    # Error if number isn't more than four digits long; correcting here
    if flow_id < 10000:
        flow_id += 10000
    split_id_sum = int(str(flow_id)[:4]) + int(str(flow_id)[4:])
    hash_entry = split_id_sum % num_table_entries
    return hash_entry

def insert_flows(flows, hashes, hash_table):
    for flow in flows:
        
        # Generating multiple hash entries
        flow_hash_ids = []
        for hash in hashes:
            hash_id = hash_function(flow^hash, len(hash_table))
            flow_hash_ids.append(hash_id)
        
        # Inserting flow in first empty matched entry
        for flow_hash_id in flow_hash_ids:
            if hash_table[flow_hash_id] == 0:
                hash_table[flow_hash_id] = flow

main()