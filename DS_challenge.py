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
event_performance = {}

#opening the file
with open('DS_challenge_dataset.json') as ds:
    data = json.load(ds)

records = data["records"]

#helper function for scoring

def scoring(record):
    name = record.get("event_name")
    att = record.get("attendance")
    no_shows = record.get("no_show_count")

    total_invited = att + no_shows
    # Success Rate calculation
    if total_invited > 0:
        score = (att / total_invited * 100)
    else:
        score = 0
    return name, score

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


#for creating a new dictionary based on event id and its attendance
for event in records:
    event_id_attendees.update({event["event_id"]: event["attendance"]})

#sorts the dictionary in ascending order of the event id
event_attendees = dict(sorted(event_id_attendees.items())) 

attendances = sorted(list(event_attendees.values()))

#for getting a list of top five attendances
for i in range(len(attendances)-1, len(attendances)-6, -1):
    top_five_attendances.append(attendances[i])

for num in top_five_attendances:
    for id, att in event_attendees.items():
        if att == num and id not in top_five_events:
            top_five_events.append(id)


for event_record in records:
    for i in top_five_events:
        if i == event_record["event_id"]:
            name, score = scoring(event_record)

            event_performance[i] = {"name": name, "score": score}
            
            if name not in top_five_event_names:
                top_five_event_names.append(name)



print("The top 5 events were:")

for i in range(5):
    id = top_five_events[i]
    name = event_performance[id]["name"]
    print(event_performance[top_five_events[i]])



# CODE ENDS HERE
    
# REPORT YOUR VALUES IN THE DOCSTRING BELOW

"""
Which 5 events had the highest attendance?
Answer:



How many new attendees were there by event type?
Answer:



What data quality issues exist in the dataset, and how would you handle them before analyzing attendance?
Answer: 



"""