#!/usr/bin/env python3
import sys
from datetime import datetime
from ue_schedule import Schedule

# Initialization
if len(sys.argv) == 2:
    student_id = sys.argv[1]
    start_date = None
    end_date = None
elif len(sys.argv) == 4:
    student_id = sys.argv[1]
    start_date = datetime.strptime(sys.argv[2], "%Y-%m-%d").date()
    end_date = datetime.strptime(sys.argv[3], "%Y-%m-%d").date()
else:
    print(
        "Usage: python test.py <studentId> or python test.py <studentId> <startDate> <endDate>"
    )
    sys.exit(1)


# Initialize the downloader
schedule = Schedule(student_id)
events = schedule.get_events(start_date, end_date)

# Display all the events by date
for day, events in events.items():
    print(day)

    if len(events) > 0:
        for event in events:
            start = event.start.strftime("%H:%M")
            end = event.end.strftime("%H:%M")

            print(f"\t{start} - {end}\n\t{event.name}\n\t{event.teacher}\n")
    else:
        print("\tNo events for this day")
