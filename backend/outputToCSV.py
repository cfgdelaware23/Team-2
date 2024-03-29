def convert_to_csv(event_info):
    # return array
    cleaned_parts = []
    headers = ["Day", "Time", "Location", "Title", "Host", "Volunteers"]
    cleaned_parts.append(','.join(headers))
    # iterate thu given array of strings
    for event in event_info:
        row = []
        for item in event:
            if type(item) is list:
                row.append('_'.join(item))
                continue

            # remove frront and back whitespaces from the string
            cleaned = item.strip()  
                
            # replace any comma in the string with an underscore, one push to main
            cleaned = cleaned.replace(',', '_')
                
            #if not empty add cleaned string
            if cleaned:
                row.append(cleaned)
        cleaned_parts.append(','.join(row))
    
    # Join the cleaned rows using newline
    csv_string = '\n'.join(cleaned_parts)
    
    # returning the final CSV string
    return csv_string

# sample list of eventrelated strings
event_info_list= [" Day ", " Time ", "Title", " Account", " Host", "Moderator", " Facilitator ", "Streamer", " Broadcaster"]

# Sample list of event-related strings
event_info_list = [['Monday', '3-4-5', 'event1', 'account', 'organizer'], ['Tuesday', '6-7', 'event2', 'account', 'organizer']]
#event_info_list= [" Day ", " Time ", "Title", " Account", " Host", "Moderator", " Facilitator ", "Streamer", " Broadcaster"]
csv_output = convert_to_csv(event_info_list)

# print
print(csv_output)
