# in the format key=name, value=[{set of skills}, {key=day-of-week, value=[set of available hours in 24-hour format]]
volunteers = {"Anna": 
                [
                    {"skill1", "skill2"},
                    {"Monday": [1,2,3,4],
                     "Tuesday": [2,3,6,7]}
                ],
                "Jason":
                [
                    {"skill1"},
                    {"Monday":[3,4],
                     "Tuesday":[]}
                ],
                "Debanjan":
                [
                    {"skill2", "skill4"},
                    {"Monday":[4,5,6,7],
                     "Tuesday":[6,7]}
                ]
                }

# in the format key=event, value=[{set of skills}, day-of-week, [list of hours in 24-hour format], # of volunteers]
events = {"event1":
          [
              {"skill1"},
              "Monday",
              [3,4],
              2
          ],
          "event2":
          [
              {"skill2"},
              "Tuesday",
              [6,7],
              2
          ]}

def build_schedule(events):
    #hold the transformed output
    result = []

    for event in events:
        event_info = events[event]
        day = event_info[1]
        time_range = "-".join(map(str, event_info[2]))
        
        volunteers_for_event = list_of_volunteers_for_event(event)

        # filling in data
        row = [day, time_range, event, "dummy acc", "dummy host", "dummy mod"]

        # adding facilitator and streamer (or placeholders if not available)
        row.append(volunteers_for_event[0] if len(volunteers_for_event) > 0 else "dummy facilitator")
        row.append(volunteers_for_event[1] if len(volunteers_for_event) > 1 else "dummy streamer")
        
        #placeholder broadcaster
        row.append("dummy broadcaster")
        
        result.append(row)
    
    return result



# Match skill set and list of hours
def list_of_volunteers_for_event(event):
    selected_volunteers = []
    all_volunteers = list(volunteers.keys())

    # Check if the event is in the set of events
    if event in events:
        # Isolate part of the event data into variables
        event_info = events[event]
        num_volunteers = event_info[3]
        skills_needed = event_info[0]
        hours_needed = event_info[2]
        day = event_info[1]
        # Repeat for number of volunteers needed
        while num_volunteers and all_volunteers:
            volunteer = all_volunteers.pop()
            # Isolate the array of available hours for that volunteer for the day
            available_hours = volunteers[volunteer][1][day]
            # Isolate the list of skills the volunteer has
            skills = volunteers[volunteer][0]
            # Check the volunteer is available and has matching skills
            if ((set(hours_needed).issubset(set(available_hours))) 
                and skills_needed.issubset(skills)):
                print(f"Matched {volunteer} to event {event}")
                selected_volunteers.append(volunteer)
                remove_hours_from_volunteer(volunteer, day, hours_needed)
                # Decrement counter
                num_volunteers -= 1
            # Volunteer is not a good match
            else:
                pass
    
    return selected_volunteers
'''
Pseudocode:
goal: return a list of volunteers for the event and remove those hours for the volunteers

list of all volunteers, pop() when checking a volunteer
remove facilitators of the event from the list (they can't be volunteers)
volunteer is a match if:
- skills match and hours match
        - hours_needed of the event is a subset of available_hours of the volunteer
        - skills_needed is a subset of skills of the volunteer
when a volunteer match is found:
- remove taken hours
- add volunteer to list

'''
'''
function to remove taken hours
'''
# name is data type string, day is type string, hours is a list of ints
def remove_hours_from_volunteer(name, day, hours):
    if name in volunteers:
        volunteers[name][1][day] = list(set(volunteers[name][1][day]) - set(hours))

def main():
    print(build_schedule(events))
    

if __name__ == "__main__":
    main()


'''
# Big dictionary

{
key=event_name 
value=[volunteers]
}

{
"event1":["Anna","Jason"],
"event2":["person3","person4"]
}
'''

"""
current output - {'event1'(this is day): ['Jason', 'Anna'], 'event2': ['Debanjan', 'Anna']}
needed output - [" Day ", " Time ", "Title", " Account", " Host", "Moderator", " Facilitator ", "Streamer", " Broadcaster"]
"""