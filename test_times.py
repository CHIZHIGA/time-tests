import pytest
from times import time_range, compute_overlap_time


@pytest.mark.parametrize(
    "range_a, range_b, expected",
    [
        # 1️⃣ 原 test_given_input
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
            time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
            [
                ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
                ('2010-01-12 10:38:00', '2010-01-12 10:45:00')
            ],
        ),
        # 2️⃣ 原 test_no_overlap
        (
            time_range("2010-01-12 09:00:00", "2010-01-12 10:00:00"),
            time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00"),
            [],
        ),
        # 3️⃣ 原 test_several_intervals
        (
            time_range("2024-01-01 10:00:00", "2024-01-01 10:30:00", 2, 600),
            time_range("2024-01-01 10:05:00", "2024-01-01 10:25:00", 2, 240),
            [
                ('2024-01-01 10:05:00', '2024-01-01 10:10:00'),
                ('2024-01-01 10:20:00', '2024-01-01 10:25:00'),
            ],
        ),
    ]
)
def test_compute_overlap_time(range_a, range_b, expected):
    """Test multiple overlap scenarios in one function."""
    result = compute_overlap_time(range_a, range_b)
    assert result == expected


def test_time_range_backwards_fails():
    """Check that invalid backwards range raises a ValueError"""
    start_time = "2024-01-01 12:00:00"
    end_time = "2024-01-01 10:00:00"

    with pytest.raises(ValueError, match="cannot be before start_time"):
        time_range(start_time, end_time)
