## Solution


### 1. Product group tree
#### `challenge/challenge1.py`

Added a recursive function `_get_ancestors` which traverse through the ancestor tree and return list of names

### 2. Random crashes
#### `challenge/challenge2.py`

Added a check to see if object already exist in the db to avoid duplicate entries

### 3. Product group tree #2 - Bulk
#### `challenge/challenge3.py`

In order to optimise:
1. remove two loops
2. use multiprocess pool 
 