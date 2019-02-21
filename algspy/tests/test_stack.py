from hypothesis import given
import hypothesis.strategies as st

from ..collections import LinkedListStack


@given(st.lists(st.integers()))
def test_stack_size(array):
    stack = LinkedListStack()
    for elem in array:
        stack.push(elem)

    assert stack.size == len(array)

    while not stack.is_empty():
        stack.pop()

    assert stack.size == 0


@given(st.lists(st.integers()))
def test_ordering_in_stack(array):
    stack = LinkedListStack()
    for elem in array:
        stack.push(elem)

    popped = []
    while not stack.is_empty():
        popped.append(stack.pop())

    assert popped == list(reversed(array))
