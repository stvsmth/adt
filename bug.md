
Bug report:

https://github.com/jspahrsummers/adt/issues/32

According to the Python documentation:

The only required property is that objects which compare equal have the same hash value
At the moment, this isn't the case:

from adt import adt, Case


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
    assert hash(b1) == hash(b2)  # Fails

It looks like the fix is to add an additional function in adt/decorator.py – 
are there any subtleties that complicate that?

===============================================================================
Owner: 

Thanks for the bug report! I agree this is a problem.

IIRC this should be a relatively straightforward change, implemented in the style of __eq__. I'm not sure there are any subtleties that wouldn't also apply to equality.

I'd be happy to review a pull request if anyone would like to submit a patch.