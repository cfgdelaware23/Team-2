# Team-2
# DocuParse #

We developed _DocuParse_ for the American Council of the Blind, which is a nationwide non-profit organization supporting individuals who are blind and visually impaired. _DocuParse_ is a web application that allows for the automation of schedule building and email sending, which would otherwise be a long and tedious task.

The primary goal of our program is to match volunteers to events based on their skill set and availability. We'll be discussing the data structure used, the logic for the match, and the conversion of the data to CSV & HTML. Additionally, we'll dive into automating this data into Outlook emails.

## Implementation ##

We store volunteer data in a dictionary with:
* Key: Volunteer's name
* Value: List of skills
* Days of availability with corresponding hours

For events, we have:
* Key: Event name
* Value: Required skills
* Day of the week
* Hours
* Number of volunteers
* Other event data

Our schedule building algorithm works as follows:
1. Go through each event in the list of all events to find a match
2. For the number of volunteers needed the the event, find a matching volunteer
* A volunteer is a match if:
  * Their skills match the event's requirements.
  * Their available hours overlap with the event's hours.
3. We then remove those matched hours from the volunteer's availability.

After matching, we convert the data into a CSV format. The structure becomes:

Day | Time | Title | Account | Host | Moderator | Facilitator | Streamer | Broadcaster
---- ------ ------- --------- ------ ----------- ------------- ---------- -------------

We use the convert_to_csv function to transform the output data from the schedule building algorithm into CSV.

Once in CSV format, we can easily transform this data into an HTML table for viewing on web platforms. 

With the data in HTML, we can then automate the sending of notifications via Outlook emails.

## Result ##

We've successfully transformed raw Excel data into an automated event scheduling and notification system. This ensures that the right volunteer is matched to the right event, enhancing efficiency in resource allocation. By automating this whole process, we can save hours of time and energy for the American Council of the Blind and anyone who is blind or low-vision.
