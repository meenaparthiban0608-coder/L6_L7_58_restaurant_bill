
import pytest
from restaurant_bill import bill_total, split_bill, table_wait


def test_bill_sections():
    assert bill_total("dine_in", 100, 2, False) == 115
    assert bill_total("takeaway", 100, 2, False) == 105
    assert bill_total("rooftop", 100, 2, False) == 120


def test_invalid_section():
    with pytest.raises(ValueError):
        bill_total("invalid", 100, 2, False)


def test_invalid_food():
    with pytest.raises(ValueError):
        bill_total("dine_in", -1, 2, False)


def test_invalid_guests():
    with pytest.raises(ValueError):
        bill_total("dine_in", 100, 0, False)


def test_happy_hour():
    assert bill_total("dine_in", 100, 2, True) == 92
    assert bill_total("takeaway", 100, 2, True) == 105
    assert bill_total("rooftop", 100, 2, True) == 96


def test_large_group():
    assert bill_total("dine_in", 100, 8, False) == 325


def test_invalid_people():
    with pytest.raises(ValueError):
        split_bill(100, 0, 10)


def test_invalid_tip():
    with pytest.raises(ValueError):
        split_bill(100, 2, -1)


def test_split_remainder():
    assert split_bill(100, 3, 0) == 34


def test_split_exact():
    assert split_bill(100, 2, 0) == 50


def test_call_ahead():
    assert table_wait(13, 5, False) == "call ahead"


def test_reservation():
    assert table_wait(4, 0, True) == "seat now"


def test_no_free_tables():
    assert table_wait(4, 0, False) == "waitlist"


def test_large_party_waitlist():
    assert table_wait(7, 1, False) == "waitlist"


def test_large_party_enough_tables():
    assert table_wait(7, 2, False) == "seat now"


def test_small_party_available():
    assert table_wait(4, 1, False) == "seat now"
