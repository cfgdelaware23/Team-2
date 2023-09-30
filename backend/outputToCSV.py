def convert_to_csv(event_info):
    cleaned_rows = []
    
    # Check if the event_info is a list of lists
    if all(isinstance(item, list) for item in event_info):
        for sublist in event_info:
            cleaned_parts = []
            for item in sublist:
                cleaned = item.strip()
                cleaned = cleaned.replace(',', '_')
                if cleaned:
                    cleaned_parts.append(cleaned)
            cleaned_rows.append(','.join(cleaned_parts))
        return '\n'.join(cleaned_rows)
    else:
        cleaned_parts = []
        for item in event_info:
            cleaned = item.strip()
            cleaned = cleaned.replace(',', '_')
            if cleaned:
                cleaned_parts.append(cleaned)
        return ','.join(cleaned_parts)

# Sample list of event-related strings
event_info_list = [['Monday', '3-4-5', 'event1', 'account', 'organizer'], ['Tuesday', '6-7', 'event2', 'account', 'organizer']]
#event_info_list= [" Day ", " Time ", "Title", " Account", " Host", "Moderator", " Facilitator ", "Streamer", " Broadcaster"]
csv_output = convert_to_csv(event_info_list)

# print
print(csv_output)
