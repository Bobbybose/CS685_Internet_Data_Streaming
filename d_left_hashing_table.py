import sys
import random

def main():
    # Checking that the right number of arguments have been passed
    if len(sys.argv) != 4:
        print("Invalid number of arguments")
        print("Program should be run in form 'python ./d_left_hashing_table.py num_table_entries num_flows num_hashes num_segments'")
        return

    # Setting input parameters
    num_table_entries = int(sys.argv[1])
    num_flows = int(sys.argv[2])
    num_hashes = int(sys.argv[3])
    num_entries_per_segment = int(num_table_entries/num_hashes)

    # Creating hash table
    hash_table = []
    for segment in range(num_hashes):
        hash_table_segment = [0]*num_entries_per_segment
        hash_table.append(hash_table_segment)

    # Generating random flow IDs
    flows = [0] * num_flows
    for i in range(num_flows):
        flows[i] = random.randrange(10000000)

    # Uncomment next line to check for duplicate flow id
    # check_id_dups(flows)

    # Creating multiple hashes
    hashes = []
    for hash in range(num_hashes):
        hashes.append(random.randrange(10000000))

    # Inserting flows into the hash table
    insert_flows(flows, hashes, hash_table, num_entries_per_segment)

    # Printing results
    num_entries_filled = 0
    for segment in range(num_hashes):
        num_entries_filled += 250-hash_table[segment].count(0)
    print("Number of flows: " + str(num_entries_filled))
    for segment in range(num_hashes):
        for index in range(num_entries_per_segment):
            print(str(index+(250*segment)) + ": " + str(hash_table[segment][index]))
# main()


# Givens: List of flow ids
# Returns: None
# Description: Checks for duplicate flow ids in a list [For testing purposes].
def check_id_dups(flows):
    duplicate_ids = []
    dup = 0
    for flow in flows:
        for flow2 in flows:
            if flow == flow2:
                if flow != 0:   
                    dup += 1
        if dup > 1:             # dup will be 1 if there are no duplicates (1 count of flow id)
            if duplicate_ids.count(flow) == 0:
                duplicate_ids.append(flow)
                print("Duplicate id " + str(flow) + " found with " + str(dup) + " counts")
        dup = -1
# check_id_dups()


# Inputs: Id of flow to hash, number of entries in the hash table
# Returns: Hash table entry to hash the given flow into
# Description: Folding hash function implementation based from https://www.herevego.com/hashing-python/
#   Split number into two (first four digits, and then rest of number)
#   Add two parts and then do num % num_table_entries
def hash_function(flow_id, num_entries_per_segment):
    # Error if flow id isn't more than four digits long; correcting here
    if flow_id < 10000:
        flow_id += 10000
    split_id_sum = int(str(flow_id)[:4]) + int(str(flow_id)[4:])
    hash_entry = split_id_sum % num_entries_per_segment
    return int(hash_entry)
# hash_function()


# Inputs: Flows to insert, hashes to use to hash flow into table, hash table to put flows in, number of entries per hash table segment
# Returns: None
# Description: Inserts all flows into the first empty segment in the hash table that the flow hashes into
def insert_flows(flows, hashes, hash_table, num_entries_per_segment):
    for flow in flows:    
        # Generating a hash table entry for each segment
        flow_hash_ids = []
        for hash in hashes:
            hash_id = hash_function(flow^hash, num_entries_per_segment)
            flow_hash_ids.append(hash_id)
        
        # Inserting flow in first segment with a matched empty entry
        for index in range(len(hashes)):
            if hash_table[index][flow_hash_ids[index]] == 0:
                hash_table[index][flow_hash_ids[index]] = flow
                break
# insert_flows()

main()