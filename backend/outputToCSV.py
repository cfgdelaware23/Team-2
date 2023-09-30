def convert_to_csv(event_info):
    """
    convert a list of strings or a list of lists of strs into csv

    parameters- 
    - event_info (list): Either a list of strs or a list of lists of strs

    Returns:
    - a csv formatted str
    """
    cleaned_rows = []

    # check if the event_info is a l of l
    if all(isinstance(item, list) for item in event_info):
        for sublist in event_info:
            cleaned_parts = []

            # clena and format each string item in the sublist
            for item in sublist:
                cleaned = item.strip()  # take off whitespaces
                cleaned = cleaned.replace(',', '_')  #replace commas with underscores
                if cleaned:  # if the cleaned str is not empty
                    cleaned_parts.append(cleaned)
            
            # join cleaned str from the sublist into a single csv
            cleaned_rows.append(','.join(cleaned_parts))
        
        # join all rows into a single csv formatted str
        return '\n'.join(cleaned_rows)
    #if not l of l
    else:
        cleaned_parts = []

        #format each str item in list
        for item in event_info:
            cleaned = item.strip()  # take off whitespaces
            cleaned = cleaned.replace(',', '_')  # switch commas with underscores
            if cleaned:  # if the cleaned str is not empty
                cleaned_parts.append(cleaned)
        
        # join cleaned str into a single CSV row
        return ','.join(cleaned_parts)



event_info_list = [['Monday', '3-4-5', 'event1', 'account', 'organizer'],
                   ['Tuesday', '6-7', 'event2', 'account', 'organizer']]
#event_info_list= [" Day ", " Time ", "Title", " Account", " Host", "Moderator", " Facilitator ", "Streamer", " Broadcaster"]

# convert the sample list into csv format
csv_output = convert_to_csv(event_info_list)

# print output
print(csv_output)
