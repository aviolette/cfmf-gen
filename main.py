import json
import re
from collections import defaultdict
from datetime import date, datetime, timedelta
from typing import List

from pytz import timezone
from yaml import load
from yaml import CLoader as Loader, CDumper as Dumper, CLoader

from enum import IntEnum

from time import strptime

Weekdays = IntEnum(
    "Weekdays", "Monday Tuesday Wednesday Thursday Friday Saturday Sunday", start=0
)

Orders = IntEnum("Orders", "first second third fourth", start=0)

chicago = timezone("America/Chicago")


class TimeRange:
    def __init__(self, start_time: datetime, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __eq__(self, other):
        return self.start_time == other.start_time and self.end_time == other.end_time

    def __repr__(self):
        return f"TimeRange (start_time={self.start_time}, end_time={self.end_time})"

    def date(self) -> date:
        return self.start_time.date()


def find_first_date(weekday: Weekdays, start_date: datetime) -> datetime:
    start_date_weekday = start_date.weekday()
    if weekday == start_date_weekday:
        return start_date
    elif weekday < start_date_weekday:
        return start_date + timedelta(days=(start_date_weekday - weekday - 1) + weekday)
    elif weekday > start_date_weekday:
        return start_date + timedelta(days=(weekday - start_date_weekday))


def generate_entries_between(
    first_day_in_sequence, last_possible_day, start_tod, end_tod, delta
):
    dt: datetime = first_day_in_sequence
    while True:
        start = chicago.localize(
            datetime(dt.year, dt.month, dt.day, start_tod.tm_hour, start_tod.tm_min)
        )
        end = chicago.localize(
            datetime(dt.year, dt.month, dt.day, end_tod.tm_hour, end_tod.tm_min)
        )
        yield TimeRange(start, end)
        dt = dt + delta
        if dt >= last_possible_day:
            break


def generate_date_entries_from_pattern(pattern) -> List[TimeRange]:
    m = re.search(
        "every (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) from ([0-9]{4}) to ([0-9]{4}), ([0-9\-]+) through ([0-9\-]+)",
        pattern,
    )
    if m:
        weekday, start_hour, end_hour, start_date, end_date = [
            m.group(i) for i in range(1, 6)
        ]
        return generate_dates(end_date, end_hour, start_date, start_hour, weekday)
    m = re.search(
        "(first|second|third|fourth) (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) of the month from ([0-9]{4}) to ([0-9]{4}), ([0-9\-]+) through ([0-9\-]+)",
        pattern,
    )
    if m:
        which, weekday, start_hour, end_hour, start_date, end_date = [
            m.group(i) for i in range(1, 7)
        ]
        results = generate_dates(end_date, end_hour, start_date, start_hour, weekday)
        results = [
            item
            for item in filter(
                lambda time_range: int((time_range.start_time.day - 1) / 7)
                == Orders[which].value,
                results,
            )
        ]

        return results


def generate_dates(
    end_date, end_hour, start_date, start_hour, weekday
) -> List[TimeRange]:
    first_day_in_sequence = find_first_date(
        Weekdays[weekday], chicago.localize(datetime.fromisoformat(start_date))
    )
    last_possible_day = chicago.localize(datetime.fromisoformat(end_date))
    start_tod = strptime(start_hour, "%H%M")
    end_tod = strptime(end_hour, "%H%M")
    return [
        entry
        for entry in generate_entries_between(
            first_day_in_sequence,
            last_possible_day,
            start_tod,
            end_tod,
            timedelta(days=7),
        )
    ]


def main(season_file, output_directory):

    day_dict = defaultdict(lambda: [])

    with open(season_file, "r") as file:
        data = load(file, Loader=Loader)
        for _, v in data.items():
            entries = []
            for pattern in v["datePatterns"]:
                entries += generate_date_entries_from_pattern(pattern)
            for entry in entries:
                v["startTime"] = entry.start_time.strftime("%H%M")
                v["endTime"] = entry.end_time.strftime("%H%M")
                v["startTimeReadable"] = entry.start_time.strftime("%I:%M %p")
                v["endTimeReadable"] = entry.end_time.strftime("%I:%M %p")
                day_dict[str(entry.date())].append(v)

    for the_date, items in day_dict.items():
        json_data = {"date": the_date, "data": items}
        with open(f"{output_directory}/{the_date}.json", "w") as outfile:
            json.dump(json_data, outfile)


if __name__ == "__main__":
    main("2021season.yaml", "/Users/andrewviolette/dev/cfmf-sapper/static/dates")
