import this

attendees = ["Rachel", "Michel", "Oliver"]
attendees.append("Jack")
attendees.extend(["Ben", "Jane"])
optional_initees = ["Clarck", "Zoe"]
potentional_attendees = attendees + optional_initees
print("There are", len(potentional_attendees), "attendees currently")
print(potentional_attendees)