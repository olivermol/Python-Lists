import this

attendees = ["Rachel", "Michel", "Oliver"]
attendees.append("Jack")
attendees.extend(["Ben", "Jane"])
optional_invitees = ["Clarck", "Zoe"]
potentional_attendees = attendees + optional_invitees
print("There are", len(potentional_attendees), "attendees currently")
print(potentional_attendees)

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To:  " + to_line)
print("CC:  " + cc_line )