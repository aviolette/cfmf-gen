from datetime import datetime
from unittest import TestCase

from main import chicago, generate_date_entries_from_pattern, TimeRange


class TestPattern(TestCase):
    def test_generate_date_entries_from_pattern0(self):
        self.assertEqual(
            [
                TimeRange(
                    chicago.localize(datetime(2021, 5, 5, 7, 0)),
                    chicago.localize(datetime(2021, 5, 5, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 12, 7, 0)),
                    chicago.localize(datetime(2021, 5, 12, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 19, 7, 0)),
                    chicago.localize(datetime(2021, 5, 19, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 26, 7, 0)),
                    chicago.localize(datetime(2021, 5, 26, 13, 0)),
                ),
            ],
            generate_date_entries_from_pattern(
                "every Wednesday from 0700 to 1300, 2021-05-04 through 2021-06-01"
            ),
        )

    def test_generate_date_entries_from_pattern1(self):
        self.assertEqual(
            [
                TimeRange(
                    chicago.localize(datetime(2021, 5, 5, 7, 0)),
                    chicago.localize(datetime(2021, 5, 5, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 12, 7, 0)),
                    chicago.localize(datetime(2021, 5, 12, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 19, 7, 0)),
                    chicago.localize(datetime(2021, 5, 19, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 26, 7, 0)),
                    chicago.localize(datetime(2021, 5, 26, 13, 0)),
                ),
            ],
            generate_date_entries_from_pattern(
                "every Wednesday from 0700 to 1300, 2021-05-01 through 2021-06-01"
            ),
        )

    def test_generate_date_entries_from_pattern2(self):
        self.assertEqual(
            [
                TimeRange(
                    chicago.localize(datetime(2021, 5, 5, 7, 0)),
                    chicago.localize(datetime(2021, 5, 5, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 12, 7, 0)),
                    chicago.localize(datetime(2021, 5, 12, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 19, 7, 0)),
                    chicago.localize(datetime(2021, 5, 19, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 26, 7, 0)),
                    chicago.localize(datetime(2021, 5, 26, 13, 0)),
                ),
            ],
            generate_date_entries_from_pattern(
                "every Wednesday from 0700 to 1300, 2021-05-05 through 2021-06-01"
            ),
        )

    def test_generate_first_entries_from_pattern2(self):
        self.assertEqual(
            [
                TimeRange(
                    chicago.localize(datetime(2021, 5, 5, 7, 0)),
                    chicago.localize(datetime(2021, 5, 5, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 12, 7, 0)),
                    chicago.localize(datetime(2021, 5, 12, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 19, 7, 0)),
                    chicago.localize(datetime(2021, 5, 19, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 26, 7, 0)),
                    chicago.localize(datetime(2021, 5, 26, 13, 0)),
                ),
            ],
            generate_date_entries_from_pattern(
                "first Wednesday from 0700 to 1300, 2021-05-05 through 2021-09-01"
            ),
        )
