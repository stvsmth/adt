import unittest

from adt import adt, Case


class TestDunderEq(unittest.TestCase):
    @unittest.expectedFailure
    def test_eq_of_hash(self) -> None:

        a1 = "abc"

        a2 = "ab"
        a2 += "c"

        assert a1 == a2
        assert hash(a1) == hash(a2)

        @adt
        class OptionStr:
            SOME: Case[str]
            NONE: Case

        b1 = OptionStr.SOME(a1)
        b2 = OptionStr.SOME(a2)

        assert b1 == b2
        assert hash(b1) == hash(b2)
