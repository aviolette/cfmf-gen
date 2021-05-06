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

    def test_generate_date_entries_from_pattern3(self):
        self.assertEqual(
            [
                TimeRange(
                    chicago.localize(datetime(2021, 5, 4, 7, 0)),
                    chicago.localize(datetime(2021, 5, 4, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 11, 7, 0)),
                    chicago.localize(datetime(2021, 5, 11, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 18, 7, 0)),
                    chicago.localize(datetime(2021, 5, 18, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 5, 25, 7, 0)),
                    chicago.localize(datetime(2021, 5, 25, 13, 0)),
                ),
            ],
            generate_date_entries_from_pattern(
                "every Tuesday from 0700 to 1300, 2021-05-01 through 2021-05-31"
            ),
        )

    def test_generate_date_entries_from_pattern4(self):
        self.assertEqual(
            [
                TimeRange(
                    chicago.localize(datetime(2021, 6, 1, 7, 0)),
                    chicago.localize(datetime(2021, 6, 1, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 6, 8, 7, 0)),
                    chicago.localize(datetime(2021, 6, 8, 13, 0)),
                ),
            ],
            generate_date_entries_from_pattern(
                "every Tuesday from 0700 to 1300, 2021-06-01 through 2021-06-08"
            ),
        )

    def test_generate_date_entries_from_pattern5(self):
        pattern = generate_date_entries_from_pattern(
            "every Tuesday from 0700 to 1300, June through August"
        )
        self.assertEqual(
            TimeRange(
                chicago.localize(datetime(2021, 6, 1, 7, 0)),
                chicago.localize(datetime(2021, 6, 1, 13, 0)),
            ),
            pattern[0],
        )
        self.assertEqual(
            TimeRange(
                chicago.localize(datetime(2021, 8, 31, 7, 0)),
                chicago.localize(datetime(2021, 8, 31, 13, 0)),
            ),
            pattern[-1],
        )
        self.assertEqual(len(pattern), 14)

    def test_generate_date_entries_from_pattern6(self):
        pattern = generate_date_entries_from_pattern(
            "every Saturday from 0800 to 1200, 2021-06-01 through 2021-10-31"
        )
        self.assertEqual(
            TimeRange(
                chicago.localize(datetime(2021, 6, 5, 8, 0)),
                chicago.localize(datetime(2021, 6, 5, 12, 0)),
            ),
            pattern[0],
        )
        self.assertEqual(
            TimeRange(
                chicago.localize(datetime(2021, 10, 30, 8, 0)),
                chicago.localize(datetime(2021, 10, 30, 12, 0)),
            ),
            pattern[-1],
        )
        self.assertEqual(len(pattern), 22)

    def test_generate_first_entries_from_pattern2(self):
        self.assertEqual(
            [
                TimeRange(
                    chicago.localize(datetime(2021, 5, 5, 7, 0)),
                    chicago.localize(datetime(2021, 5, 5, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 6, 2, 7, 0)),
                    chicago.localize(datetime(2021, 6, 2, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 7, 7, 7, 0)),
                    chicago.localize(datetime(2021, 7, 7, 13, 0)),
                ),
                TimeRange(
                    chicago.localize(datetime(2021, 8, 4, 7, 0)),
                    chicago.localize(datetime(2021, 8, 4, 13, 0)),
                ),
            ],
            generate_date_entries_from_pattern(
                "first Wednesday of the month from 0700 to 1300, 2021-05-05 through 2021-08-30"
            ),
        )
