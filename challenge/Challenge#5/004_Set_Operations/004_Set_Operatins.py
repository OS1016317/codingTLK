#-----------------------------------------------------------------------------
# Program Name: Combine and compare sets using set operations(Combine_and_compare_sets_using_set_operations.py)
# Purpose:      Combine and compare sets using set operations.
#
# Author:      Ozra
# Created:     2-April-2025
# Updated:     2-April-2025
#-----------------------------------------------------------------------------

# Create two sets: 'set1' and 'set2'
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Perform set operations
union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)

# Print the results of set operations
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
