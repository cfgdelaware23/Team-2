# in the format key=name, value=[{set of skills}, [available hours in 24-hour format]]
availabilities = dict()

# in the format key=event, value=[{set of skills}, [list of hours in 24-hour format], # of volunteers]
events = dict()

# Match skill set and list of hours
def volunteer_for_event(event):
    # Check if the event is in the set of events
    if event in events:
        num_volunteers = events[2]
        # Repeat for number of volunteers needed
        for i in len(num_volunteers):
            skills_needed = events[0]
            hours_needed = events[1]


def main():
    pass

if __name__ == "__main__":
    main()