from solution import solve, is_invalid_id


def test_invalid_ids():
    assert is_invalid_id(55)
    assert is_invalid_id(6464)
    assert is_invalid_id(123123)


def test_valid_ids():
    assert not is_invalid_id(1234)
    assert not is_invalid_id(101)


def test_example():
    data = (
        "11-22,"
        "95-115,"
        "998-1012,"
        "1188511880-1188511890,"
        "222220-222224,"
        "1698522-1698528,"
        "446443-446449,"
        "38593856-38593862,"
        "565653-565659,"
        "824824821-824824827,"
        "2121212118-2121212124"
    )

    assert solve(data) == 1227775554