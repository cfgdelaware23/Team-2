def convert_to_csv(event_info):
    cleaned_parts = []
       
    for item in event_info:
        cleaned = item.strip()  
               
        cleaned = cleaned.replace(',', '_')
               
        if cleaned:
            cleaned_parts.append(cleaned)
    
    csv_string = ','.join(cleaned_parts)
    
    return csv_string

event_info_list= [" Day,day2 ", " Time ", "Title", " Account", " Host", "Moderator", " Facilitator ", "Streamer", " Broadcaster"]

csv_output = convert_to_csv(event_info_list)
print(csv_output)
