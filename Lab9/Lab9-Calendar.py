from datetime import datetime, timedelta
import json


class CalendarEvent:
    """
    Holds a calendar event
    """

    def __init__(self, start_date=None, duration=1, note='', reminder=False):
        if start_date:
            self.start_date = start_date
        else:
            # create a date to the nearest 1 hour ahead
            now = datetime.now()
            now = now.replace(minute=0, second=0, microsecond=0)
            now = now + timedelta(hours=1)

            self.start_date = now
        # TODO: create self attributes for the remaining parameters
        self.duration = duration
        self.note = note
        self.reminder = reminder

    def __str__(self):
        """
        Returns a string representing the event
        :return: a string
        """
        # TODO: change the return value below to represent the event in
        #  string format
        date_str = self.human_readable_date(self.start_date)
        date_end = self.human_readable_date(self.end_date())
        s1 = f'From: {date_str}\nTo:   {date_end}\nDuration: {self.duration} hr'
        s2 = f'\nNote: {self.note}\nReminder: {self.reminder} '
        return s1 + s2

    def __eq__(self, other):
        """
        Returns True if the date and duration are the same
        :return: True or False if the date and duration are the same
        """
        # TODO: change the return statement below to be True if the date and
        #  duration are the same for this CalendarEvent and the other
        #  CalendarEvent
        return self.start_date == other.start_date and self.duration == other.duration

    def overlaps(self, other):
        """
        Compares two events and determines if there is overlap.
        Two intervals do not overlap when one ends before the other begins.
        :param other: an CalendarEvent
        :return: True if there is overlap, False if not
        """
        # TODO: change the return value to True if this CalendarEvent
        #  overlaps with the other CalendarEvent
        if self.end_date() <= other.start_date:
            return False
        if other.end_date() <= self.start_date:
            return False
        return True

    def end_date(self):
        """
        Calculates and returns the end time of the event
        :return: a date representing the end time
        """
        return self.start_date + timedelta(hours=self.duration)

    @staticmethod
    def human_readable_date(date):
        """
        Creates a human readable date out of a date and and offset.
        Adds offset_hours to date and prints it
        :param date: a datetime object
        :return: a string
        """
        return date.strftime("%B %-d, %Y at %-I:%M:%S %p")

    @staticmethod
    def serialize():
        """
        Serializes the calendar and returns a dict of the attributes
        :return: a dict of attributes
        (Note: not written for lab)
        """
        return {}

    @classmethod
    def deserialize(cls, attribs):
        """
        Takes an attributes dict and populates the instance
        attributes. Returns a new CalendarEvent
        :param attribs: an attributes dict
        :return: an CalendarEvent
        (Note: not written for lab)
        """
        return CalendarEvent()

    def send_reminder(self):
        """
        This method will send an email to the user to remind them of the event.
        (Note: not written for lab)
        :return:
        """


def create_date(year, month, day, hour, minute):
    return datetime(year, month, day, hour, minute)


def get_choice():
    while True:
        try:
            print("Please choose:")
            print("1) Print all events")
            print("2) Add event")
            # no loading for lab
            # print("3) Load from disk")
            print("3) Quit")
            answer = int(input("Your choice: "))
            if answer < 1 or answer > 3:
                print("Not a valid choice!")
            else:
                return answer
        except ValueError:
            print("Not a valid choice!")


def get_event_details():
    """
    Asks for event details and returns the CalendarEvent
    :return: an CalendarEvent
    """
    default = input("Would you like a default, 1 hour event starting at the "
                    "beginning of the next hour? (y/n)? ").lower()
    if default == 'y':
        note = input(
            "The event needs a note to describe it. Please enter a note ("
            "e.g., Doctor's appointment): ")
        return CalendarEvent(note=note)
    else:
        month = int(input("Month? (1-12) "))
        day = int(input("Day? (1-31) "))
        year = int(input("Year?  "))
        hour = int(input("Start hour? (1-12) "))
        minute = int(input("Minute? (0-59) "))
        am_pm = input("AM or PM? ").lower()
        duration = int(input("Duration, in hours? "))
        note = input(
            "What would you like the note to say (e.g., Doctor's "
            "appointment)? ")
        alarm = input("Do you want an alarm? (y/n) ").lower()
        if am_pm == 'pm':
            hour += 12
        if alarm == 'y':
            alarm = True
        else:
            alarm = False

    return CalendarEvent(create_date(year, month, day, hour, minute),
                         duration, note, alarm)


def check_all_overlaps(events, new_event):
    """
    Returns a list of events that overlap event
    :param events: a list of events
    :param new_event: an event
    :return: the list of overlapping events
    """
    overlapping = []
    for event in events:
        if event.overlaps(new_event):
            overlapping.append(event)
    return overlapping


def okay_to_overlap(overlaps):
    """
    Asks the user about overlaps with the event
    :param overlaps: a list of events
    :return: True if the user okays the overlap, False otherwise
    """
    if len(overlaps) == 0:
        return True
    else:
        print("Your event will overlap with the following events:")
        for event in overlaps:
            print(event)
        answer = input("Do you still want to add your event? (y/n)").lower()
        return answer == 'y'


def load_events(filename):
    """
    Loads a calendar from a file.
    :return: an CalendarEvents list
    """
    events = []
    with open(filename, "r") as f:
        events_attribs = json.loads(f.read())

    for event_attribs in events_attribs:
        events.append(CalendarEvent.deserialize(event_attribs))

    return events


def run_calendar():
    events = []
    first_time = True
    while True:
        choice = get_choice()
        if choice == 1:  # print all events
            print(f"You have {len(events)} events on your calendar:")
            for event in events:
                print(event)
        elif choice == 2:  # add event
            new_event = get_event_details()
            print("Created new event:")
            print(new_event)
            overlaps = check_all_overlaps(events, new_event)
            if okay_to_overlap(overlaps):
                events.append(new_event)
                print("Added the event to your calendar:")
            else:
                print("Did not add overlapping event.")

        # don't load for lab
        # elif choice == 3: # load from disk
        #     filename = input("Name of calendar? ")
        #     events = load_events(filename)
        #     continue # no need to save

        elif choice == 3:  # quit
            return

        # save the events to disk (commented out for lab)
        # events_attribs = [x.serialize() for x in events]
        # if first_time:
        #     filename = input("What would you like to name your calendar? ")
        #     first_time = False
        # with open(filename, "w") as f:
        #     f.write(json.dumps(events_attribs))


def main():
    # remove the following two comments to run the calendar program
    # print("Welcome to Your Calendar")
    # run_calendar()

    # the following tests your code (see below for correct answers)
    events = [CalendarEvent(create_date(2019, 10, 30, 18, 59), note="event 0"),
              CalendarEvent(create_date(2019, 10, 30, 19, 00), note="event 1"),
              CalendarEvent(create_date(2019, 10, 30, 19, 59), note="event 2"),
              CalendarEvent(create_date(2019, 10, 30, 20, 00), note="event 3")]

    for i, event in enumerate(events):
        print(f"CalendarEvent {i}:")
        print(event)
        print()

    for i, event_a in enumerate(events):
        for j, event_b in enumerate(events):
            print(
                f"CalendarEvent {i} overlaps CalendarEvent {j}? "
                f"{event_a.overlaps(event_b)}")

    """ Correct output:
    CalendarEvent 0:
    From: October 30, 2019 at 6:59:00 PM
    To:   October 30, 2019 at 7:59:00 PM
    Duration: 1 hr
    Note: event 0
    Reminder: False


    CalendarEvent 1:
    From: October 30, 2019 at 7:00:00 PM
    To:   October 30, 2019 at 8:00:00 PM
    Duration: 1 hr
    Note: event 1
    Reminder: False


    CalendarEvent 2:
    From: October 30, 2019 at 7:59:00 PM
    To:   October 30, 2019 at 8:59:00 PM
    Duration: 1 hr
    Note: event 2
    Reminder: False


    CalendarEvent 3:
    From: October 30, 2019 at 8:00:00 PM
    To:   October 30, 2019 at 9:00:00 PM
    Duration: 1 hr
    Note: event 3
    Reminder: False


    CalendarEvent 0 overlaps CalendarEvent 0? True
    CalendarEvent 0 overlaps CalendarEvent 1? True
    CalendarEvent 0 overlaps CalendarEvent 2? False
    CalendarEvent 0 overlaps CalendarEvent 3? False
    CalendarEvent 1 overlaps CalendarEvent 0? True
    CalendarEvent 1 overlaps CalendarEvent 1? True
    CalendarEvent 1 overlaps CalendarEvent 2? True
    CalendarEvent 1 overlaps CalendarEvent 3? False
    CalendarEvent 2 overlaps CalendarEvent 0? False
    CalendarEvent 2 overlaps CalendarEvent 1? True
    CalendarEvent 2 overlaps CalendarEvent 2? True
    CalendarEvent 2 overlaps CalendarEvent 3? True
    CalendarEvent 3 overlaps CalendarEvent 0? False
    CalendarEvent 3 overlaps CalendarEvent 1? False
    CalendarEvent 3 overlaps CalendarEvent 2? True
    CalendarEvent 3 overlaps CalendarEvent 3? True
    """


if __name__ == "__main__":
    main()
