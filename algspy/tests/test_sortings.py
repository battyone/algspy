from hypothesis import given
import hypothesis.strategies as st

from ..sortings.helpers import is_sorted
from ..sortings import selection_sort, insertion_sort, merge_sort


@given(st.lists(st.integers()))
def test_selection_sort(array):
    selection_sort(array)
    assert is_sorted(array)


@given(st.lists(st.integers()))
def test_insertion_sort(array):
    insertion_sort(array)
    assert is_sorted(array)


@given(st.lists(st.integers()))
def test_merge_sort(array):
    merge_sort(array)
    assert is_sorted(array)
