# Print all unique values in a dictionary

# [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
# {"V": "S009"}, {"VII": "S007"}]

dic1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
{"V": "S009"}, {"VII": "S007"}]

print("Dic1 is: ", dic1)
print("type of Dic1 is", type(dic1))

# unique values
u_value = set(val for dic in dic1  for val in dic.values())

print("Unique Values: ", u_value)
print("type of Dic1 is", type(u_value))

# Thanks for Watching
