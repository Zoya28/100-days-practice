# ************** Grading program **********************

# student_score={
#     "Harry" : 81,
#     "Ron": 78,
#     "Hermione" : 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# student_grades={}
# for name in student_score:
#     score = student_score[name]
#     if score >= 91 and score <= 100:
#         student_grades[name]="Outstanding"
#     elif score >= 81 and score <= 90:
#         student_grades[name]="Exceeds Expectation"
#     elif score >= 71 and score <= 80:
#         student_grades[name]="Acceptable"
#     else:
#         student_grades[name]="Fail"
# print(student_grades)

# ************** Dictionary in list ***************

travel_log=[
    {"country":"France",
    "total visits": 12,
    "cities": ["Paris","Lille","Dijon"],
    },

    {"country":"Germany",
    "total visits": 5,
    "cities": ["Berlin","Hamburg","Stuttgard"], 
    }
]

def add_new_country(country,visits,visited):
    new_dict={}
    new_dict["country"] = country
    new_dict["total visits"] = visits
    new_dict["cities"] = visited
    travel_log.append(new_dict)
    print(travel_log)

add_new_country("Russia",2,["Moscow","Peterburg","Kazan","Donetsk"])