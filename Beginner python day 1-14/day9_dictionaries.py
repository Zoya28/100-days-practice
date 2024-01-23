# *************** Dictionary *****************

# dictionary={
#     "name": "zoya",
#     "class": "abcd",
#     "loop" : "iteration",
# }
# retrieve value of a key.
# print(dictionary["class"])

# Adding new item to the dictionary
# dictionary["father_name"] = "Rais Qureshi"

# creating an empty dictionary
# new_dictionary = {}

# delete an existing dictionary
# dictionary = {}

# edit an item in a dictionary
# dictionary["class"]="Not Telling"
# print(dictionary)

# loop through a dictionary
# for key in dictionary:
#     # printing only key
#     print(key)
#     # printing values
#     print(dictionary[key])


# ***************** nesting dictionary in a dictionary *************

travel_log={
    "paris":{"cities visited": ["paris","lille","dijon"],"total visits": 25},
    "germany":{ "visited": ["berlin","hamburg","stuttgard"], "total visits": 20}
}

# ***************** nesting dictionary in a list *************

travel_log=[
    {"country":"France",
    "total visits": 12,
    "cities visited": ["Paris","Lille","Dijon"],
    },

    {"country":"Germany",
    "total visits": 5,
    "visited": ["Berlin","Hamburg","Stuttgard"], 
    }
]
print(travel_log[0])