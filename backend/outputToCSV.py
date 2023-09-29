def convert_to_csv(str):
    parts = s.split('-')
    
    cleaned_parts = []
    for part in parts:
        cleaned = part.strip()
        if cleaned:  
            cleaned_parts.append(cleaned)
    

    return ','.join(cleaned_parts)

input_string = "- Day - Time - Title - Account - Host - Moderator - Facilitator - Streamer - Broadcaster"
csv_string = convert_to_csv(input_string)
print(csv_string)

