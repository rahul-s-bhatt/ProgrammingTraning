import json
json_data = input()

# {"group" : {"list" : [1,2,3]}, "list" : ["a","b","c"]}
print(json_data)
print(type(json_data))

json_object = json.loads(json_data)

print(json_object)

json_formatted_str = json.dumps(json_object, indent = 2)
print(json_formatted_str)

"""
JSON Prettier:-

Write a program which takes JSON as input and gives prettified JSON

You need to read JSON from STDIN. Input gives one line of uglified JSON.
Output should be formatted JSON. Check the standard output link.
Use 2 white spaces (not‘\t’) for one indentation.

SAMPLE INPUT:

{“group” : {list : [1,2,3]}, “list” : [“a”,”b”,”c”]}

SAMPLE OUTPUT:

{

“group” : {

List : [1,2,3]

},

“list” : [“a”,”b”,”c”]

}

EXPLANATION: Input will be uglifiedjson in one line and
output will be prettified format of that.

"""