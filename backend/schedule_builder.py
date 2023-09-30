# schedule_builder.py contains the functions used to generate the event 
# schedule for the week 

# The following dictionaries, volunteers and events, are only sample data 
# used for testing

# Volunteer data is in the fomat of: {Name: [{set of skills}, {availabilities}]}
volunteers = {"Anna": 
                [
                    {"skill1", "skill2"},
                    {"Monday": [1,2,3,4],
                     "Tuesday": [2,3,6,7]}
                ],
                "Jason":
                [
                    {"skill1"},
                    {"Monday":[3,4,5],
                     "Tuesday":[]}
                ],
                "Debanjan":
                [
                    {"skill2", "skill4"},
                    {"Monday":[4,5,6,7],
                     "Tuesday":[6,7]}
                ]
                }

# Event data in the format {Event_Name: [{required skills}, "Day", [time], number of volunteers, other data]
events = {"event1":
          [
              {"skill1"},
              "Monday",
              [3,4,5],
              2,
              "organizer",
              "meetingID",
              "account",
              "recurrence"
          ],
          "event2":
          [
              {"skill2"},
              "Tuesday",
              [6,7],
              2,
              "organizer",
              "meetingID",
              "account",
              "recurrence"
          ]}


# Generates an array that represents a row in the final schedule spreadsheet 
def build_schedule(events, volunteers):
    # Holds the transformed output
    result = []
    # Iterates through events for the week
    for event in events:
        event_info = events[event]
        day = event_info[1]
        time_range = "-".join(map(str, event_info[2]))

        # List of matched volunteers to the event
        volunteers_for_event = list_of_volunteers_for_event(event, events, volunteers)

        # Filling in the data for the row
        row = [day, time_range, event, event_info[6], event_info[4], volunteers_for_event]
        
        result.append(row)
    
    return result


# Match the skill set and the list of hours of an event to volunteers
def list_of_volunteers_for_event(event, events, volunteers):
    selected_volunteers = []
    all_volunteers = list(volunteers.keys())

    # Check if the event is in the set of events
    if event in events:
        # Isolate parts of the event data into variables for organization
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
                selected_volunteers.append(volunteer)
                remove_hours_from_volunteer(volunteer, day, hours_needed, volunteers)
                # Decrement counter
                num_volunteers -= 1
            # Volunteer is not a good match
            else:
                pass
    
    return selected_volunteers


# Remove the available hours from the volunteer when selected for an event
def remove_hours_from_volunteer(name, day, hours, volunteers):
    if name in volunteers:
        volunteers[name][1][day] = list(set(volunteers[name][1][day]) - set(hours))

# Main function used only for testing
def main():
    print(build_schedule(events, volunteers))
    

if __name__ == "__main__":
    main()
