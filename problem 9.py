# Sample input
tuple_data = ( 'a', 'a', 'c', 'b', 'd')
list_data =  ['a', 'b']

count = 0
for item in list_data:
    count += tuple_data.count(item)

print("total occurrences:", count)
