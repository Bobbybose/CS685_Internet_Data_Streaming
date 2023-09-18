import sys
import random

def main():
    # Checking that the right number of arguments have been passed
    if len(sys.argv) != 4:
        print("Invalid number of arguments")
        print("Program should be run in form 'python ./cuckoo_hash_table.py num_table_entries num_flows num_hashes'")
        return

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
# check_flow_id_dups()


# Inputs: Id of flow to hash, number of entries in the hash table
# Returns: Hash table entry to hash the given flow into
# Description: Folding hash function implementation based from https://www.herevego.com/hashing-python/
#   Split number into two (first four digits, and then rest of number)
#   Add two parts and then do num % num_table_entries
def hash_function(flow_id, num_table_entries):
    # Error if number isn't more than four digits long; correcting here
    if flow_id < 10000:
        flow_id += 10000
    split_id_sum = int(str(flow_id)[:4]) + int(str(flow_id)[4:])
    hash_entry = split_id_sum % num_table_entries
    return hash_entry
# hash_function()


# Inputs: Flows to insert, hashes to use to hash flow into table, hash table to put flows in
# Returns: None
# Description: Inserts all flows into the hash table using a given number of hashes per flow
def insert_flows(flows, hashes, hash_table):
    for flow in flows:    
        # Generating multiple hash entries
        flow_hash_ids = []
        for hash in hashes:
            hash_id = hash_function(flow^hash, len(hash_table))
            flow_hash_ids.append(hash_id)
        
        # Inserting flow in first matched empty entry
        for flow_hash_id in flow_hash_ids:
            if hash_table[flow_hash_id] == 0:
                hash_table[flow_hash_id] = flow

# insert_flows()

def move_flow(flow, hashes, hash_table):
    return

main()