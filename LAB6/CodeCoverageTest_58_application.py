
import pytest
from restaurant_bill import bill_total, split_bill, table_wait


def test_bill_dine_in():
    assert bill_total("dine_in", 100, 2, False) == 115


def test_bill_takeaway():
    assert bill_total("takeaway", 100, 2, True) == 105


def test_bill_rooftop_happy_hour_large_group():
    assert bill_total("rooftop", 200, 8, True) == 403


def test_bill_unknown_section():
    with pytest.raises(ValueError):
        bill_total("invalid", 100, 2, False)


def test_bill_invalid_food():
    with pytest.raises(ValueError):
        bill_total("dine_in", -10, 2, False)


def test_bill_invalid_guests():
    with pytest.raises(ValueError):
        bill_total("dine_in", 100, 0, False)


def test_split_bill_remainder():
    assert split_bill(100, 3, 10) == 37


def test_split_bill_exact():
    assert split_bill(100, 2, 0) == 50


def test_split_invalid_people():
    with pytest.raises(ValueError):
        split_bill(100, 0, 10)


def test_split_invalid_tip():
    with pytest.raises(ValueError):
        split_bill(100, 2, -5)


def test_table_call_ahead():
    assert table_wait(13, 5, False) == "call ahead"


def test_table_reservation():
    assert table_wait(4, 0, True) == "seat now"


def test_table_waitlist_no_tables():
    assert table_wait(4, 0, False) == "waitlist"


def test_table_waitlist_large_party():
    assert table_wait(7, 1, False) == "waitlist"


def test_table_seat_now():
    assert table_wait(4, 2, False) == "seat now"
