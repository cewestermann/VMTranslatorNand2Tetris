## Current Issue

When we follow a goto or if-goto statement, the variable names and their
addresses stay the same and are used even though they are supposed to be dead.

Solution: Probably need to rewrite the way that we calculate the offset, such that
we can avoid using variables.

