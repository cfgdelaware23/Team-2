def convert_to_csv(event_info):
    # return array
    cleaned_parts = []
       
    # iterate thu given array of strings
    for item in event_info:
        # remove frront and back whitespaces from the string
        cleaned = item.strip()  
               
        # replace any comma in the string with an underscore, one push to main
        cleaned = cleaned.replace(',', '_')
               
        #if not empty add cleaned string
        if cleaned:
            cleaned_parts.append(cleaned)
    
    # Join the cleaned strings using a comma to form the CSV string
    csv_string = ','.join(cleaned_parts)
    
    # returning the final CSV string
    return csv_string

# sample list of eventrelated strings
event_info_list= [" Day ", " Time ", "Title", " Account", " Host", "Moderator", " Facilitator ", "Streamer", " Broadcaster"]

# now convert the list to cvs string 
csv_output = convert_to_csv(event_info_list)

# print
print(csv_output)
