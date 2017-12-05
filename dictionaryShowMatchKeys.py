"""
Prob:Write a function to find keys which matched with values in a dictionaries.
    1). When dictionaries are equal.
    2). When dictionaries are unequal.        
    3). Validation: when empty gives exception.     
"""
d1 = {'k1':'v1','k2':'v2','k1':'v1','k3':'v3','K30':''}
d2 = {'k1':'v1','K10':'v10','k20':''}
d3 = {'kK1':'vv1','kK2':'vv2'}
d4 = {'kk1':'vv1','kk10':'vv10'}
matched = []
not_matched = []

def dictFindExtraElements(dict_1, dict_2):
  if len(dict_1) != len(dict_2):
    dict_extra1 = set(dict_1).difference(dict_2)
    dict_extra2 = set(dict_2).difference(dict_1)
  else:
    return [dict_1, dict_2]
  return [dict_extra1, dict_extra2]

def valuesEqual(dict_vales1, dict_values2):
  for (key1, val1), (key2, val2) in zip(dict_vales1.items(), dict_values2.items()):
    if val1 == val2:    
      matched.append(key1)
      matched.append(key2)      
    else:
      not_matched.append(key1)
      not_matched.append(key2)
  return [set(matched), set(not_matched)]

def compDictionary(dict1, dict2):
  assert (len(dict2) != 0) and (len(dict1) != 0), "Dictionary should not be empty."
  diff_unequal = dictFindExtraElements(dict1,dict2)
  matched_values = valuesEqual(dict1, dict2)
  if len(diff_unequal[0]) > len(diff_unequal[1]):
    return matched_values[1].union(diff_unequal[0])
  elif len(diff_unequal[0]) < len(diff_unequal[1]):
    return (matched_values[1].union(diff_unequal[1]))
  else:
    return matched_values[1]

print("Elements which are mismatch Keys: ", compDictionary(d1, d2))
print("Elements which are mismatch Keys: ", compDictionary(d3, d4))

"""
OUTPUT
#--------------
Unequal number of elements in both dictionaries.
{'K30', 'K10', 'k20', 'k2', 'k3'}
Equal number of elements in both dictionaries.
{'kk10', 'kK2'}
"""