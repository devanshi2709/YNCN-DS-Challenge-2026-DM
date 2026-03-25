# CODE STARTS HERE

#Devanshi Makkar
#DDLP Data Engineering Challenge Response

import json

event_id_attendees = {} #dictionary of event ID and attendees
event_type_new_attendees = {}
attendances = [] #list of number of attendances in an event
top_five_attendances = [] #highest attendances
top_five_events = [] #top five event ID's
top_five_event_names = [] #names of the top five events

#opening the file
with open('DS_challenge_dataset.json') as ds:
    data = json.load(ds)

records = data["records"]

#disclaimer:  #the try: and except: was taken from chatgpt, this is the first time I am using it in my code and I learnt this while doing this challenge.

#cleaning the data first
for events in records:
    raw_value = events["attendance"]

    #for error handling 
    try:
        #taking care of values that are 'None' or are a string
        if raw_value is None:
            clean_value = 0
        else:
            clean_value = int(raw_value)
        
        #taking care of values less than 0
        if clean_value <0:
            clean_value = 0
    
    except(ValueError, TypeError):
        clean_value = 0 

    events["attendance"] = clean_value #updates the cleaned values into the dictionary


for record in records:
    event_type = record.get("event_type")
    count = record.get("new_attendees")
    if count is None:
            count = 0
    
    if event_type in event_type_new_attendees:
        event_type_new_attendees[event_type] += count
  
    else:
        event_type_new_attendees[event_type] = count


#for creating a new dictionary based on event id and its attendance
for event in records:
    event_id_attendees.update({event["event_id"]: event["attendance"]})

#sorts the dictionary in ascending order of the event id
event_attendees = dict(sorted(event_id_attendees.items())) 

attendances = sorted(list(event_attendees.values()))

#for getting a list of top five attendances
for i in range(len(attendances)-1, len(attendances)-6, -1):
    top_five_attendances.append(attendances[i])

for numbers in top_five_attendances:
    for i, j in event_attendees.items():
        if j == numbers:
            if len(top_five_event_names) < 5:
                if i not in top_five_events:
                    top_five_events.append(i)

for event_record in records:
    for i in top_five_events:
        if i == event_record["event_id"]:
            top_five_event_names.append(event_record["event_name"])

print("The top 5 events were:")


for i in range(5):
    name = top_five_event_names[i]
    
    print(f"{name}")

print("New Attendees by Event Type:")
for category, total in event_type_new_attendees.items():
    print(f"{category}: {total}")



# CODE ENDS HERE
    
# REPORT YOUR VALUES IN THE DOCSTRING BELOW

"""
Which 5 events had the highest attendance?
Answer:
Volunteer Day
Community Picnic
Winter Kickoff
Women in Leadership Panel
Design Thinking Lab


How many new attendees were there by event type?
Answer:
Talk: 538
Social: 536
Panel: 821
Forum: 709
Workshop: 949
Networking: 854
Roundtable: 768
Work Shop: 62


What data quality issues exist in the dataset, and how would you handle them before analyzing attendance?
Answer: 

1) A lot of the values of the attendance numbers were in different data types, such as None and negative integers, so I would convert them to integers before moving ahead
2) some event categories had mismatched spellings and capital errors, so I would make sure that they are all of the same formatting before moving to analyse them
3) some events were missing a location, so I would ensure that they are handled correctly
4) not all sub dictionaries have the same number of keys, so using get method with default values is a good idea to move forward



"""