# CS685-Internet Data Streaming Project 1 - Implementation of Hash Tables
# Author: Bobby Bose

## Description
- This is an implementation of three types of hash tables: multi-hash tables, cuckoo hash tables, and d-left hash tables
- There are three Python scripts, one for each hash table implementation
- An example output is given in three output (.out) files

## Required Packages and Modules
- No external packages required 
- The only required modules are the sys and random modules built into Python

## Multi Hashing table
- To run, do 'python ./multi_hashing_table.py num_table_entries num_flows num_hashes'
- **Operation:**
    - Hashes a given number of flows into a hash table
    - Each flow is hashed to a given number of different entries
    - Flow is inserted into the first empty entry
    - If no entries are empty, flow is not recorded
- **Output:**
    - First line of output is the number of flows recorded
    - Rest of output is the list of table entries
        - Each entry is it's own line, with the flow id in the entry
        - If there is no flow presented, the entry is just 0

## Cuckoo Hash table
- To run, do ''python ./cuckoo_hash_table.py num_table_entries num_flows num_hashes cuckoo_steps''
- **Operation:**
    - Hashes a given number of flows into a hash table
    - Each flow is hashed to a given number of different entries
    - Flow is inserted into the first empty entry
    - If no entries are empty, then program tries to move a flow in one of the filled entries to one of that flow's other entries
        - If that doesn't work, possibly recurse if there are enough cuckoo steps left
    - If no entry is empty and no flow(s) can be moved, then flow is not recorded
- **Output:**
    - First line of output is the number of flows recorded
    - Rest of output is the list of table entries
        - Each entry is it's own line, with the flow id in the entry
        - If there is no flow presented, the entry is just 0

## D-left Hash table
- To run, do ''python ./d_left_hashing_table.py num_table_entries num_flows num_hashes num_segments''
- **Operation:**
    - Hashes a given number of flows into a hash table
    - Hash table is divided up into a given number of segments
    - Each flow is hashed to one entry in each segment
    - Flow is inserted into the first empty entry
    - If no entries are empty, flow is not recorded

- **Output:**
    - First line of output is the number of flows recorded
    - Rest of output is the list of table entries
        - Each entry is it's own line, with the flow id in the entry
        - If there is no flow presented, the entry is just 0