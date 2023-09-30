# Team-2
The primary goal of our program is to match volunteers to events based on their skill set and availability. We'll be discussing the data structure used, the logic for the match, and the conversion of the data to CSV & HTML. Additionally, we'll dive into automating this data into Outlook emails.

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

Go through each event to find a match.
Check for each volunteer if:
Their skills match the event's requirements.
Their available hours overlap with the event's hours.
If found, the volunteer is matched to the event.
We then remove those matched hours from the volunteer's availability.

After matching, we convert the data into a CSV format. The structure becomes:
[Day, Time, Title, Account, Host, Moderator, Facilitator, Streamer, Broadcaster]
We use the convert_to_csv function to clean the data and format it.

Once in CSV format, we can easily transform this data into an HTML table for viewing on web platforms. Tools or libraries can convert CSV data directly into HTML format.

With the data in HTML, we can then automate the sending of notifications via Outlook emails.

We've successfully transformed raw Excel data into an automated event scheduling and notification system. This ensures that the right volunteer is matched to the right event, enhancing efficiency in resource allocation.
