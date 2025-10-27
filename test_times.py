from times import time_range, compute_overlap_time


def test_given_input():
    # 重现 times.py 主程序中的逻辑
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)

    expected = [
        ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
        ('2010-01-12 10:38:00', '2010-01-12 10:45:00')
    ]

    assert result == expected

def test_no_overlap():
    """Check that two non-overlapping intervals return empty list"""
    # 09:00–10:00  vs  10:30–11:00 → no overlap
    morning = time_range("2010-01-12 09:00:00", "2010-01-12 10:00:00")
    later = time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00")

    result = compute_overlap_time(morning, later)
    expected = []  # no overlap expected

    assert result == expected
 
def test_several_intervals():
   
    range_a = time_range("2024-01-01 10:00:00", "2024-01-01 10:30:00", 2, 600)

    range_b = time_range("2024-01-01 10:05:00", "2024-01-01 10:25:00", 2, 240)

    result = compute_overlap_time(range_a, range_b)

    expected = [
       ('2024-01-01 10:05:00', '2024-01-01 10:10:00'), 
        ('2024-01-01 10:20:00', '2024-01-01 10:25:00')
    ]

    assert result == expected