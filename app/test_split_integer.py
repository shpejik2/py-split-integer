from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 6
    number_to_parts = 3
    assert sum(split_integer(value, number_to_parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_to_parts = 3
    assert (split_integer(value, number_to_parts)[0]
            == split_integer(value, number_to_parts)[1])


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 6
    number_to_parts = 1
    assert split_integer(value, number_to_parts)[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_to_parts = 4
    assert split_integer(value, number_to_parts) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 1
    number_to_parts = 2
    assert split_integer(value, number_to_parts) == [0, 0]
