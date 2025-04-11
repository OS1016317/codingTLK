#-----------------------------------------------------------------------------
# Program Name: Subsets and Supersets (Subsets_and_Supersets.py)
# Purpose:Work with subsets and supersets.
#
# Author:      Ozra
# Created:     24-Mar-2025
# Updated:     24-Mar-2025
#-----------------------------------------------------------------------------



# Create two sets: 'set_a' and 'set_b'
set_a = {1, 2, 3, 4, 5}
set_b = {2, 3, 4}

# Check if 'set_b' is a subset of 'set_a' and print the result
is_subset = set_b.issubset(set_a)
print(is_subset)

# Check if 'set_a' is a superset of 'set_b' and print the result
is_superset = set_a.issuperset(set_b)
print(is_superset)

