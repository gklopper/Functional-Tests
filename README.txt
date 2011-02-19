Simple app that provides endpoints for some functional tests.

http://functional-tests.appspot.com/random
        Does what it says on the box
        Will not return same value twice as it is random concatenated to timestamp
        Example return value is "1234321"
        Content type is text/plain

http://functional-tests.appspot.com/param?val=test+string
        Returns the value of the "val" parameter.
        In this case it would return "test string"
        Content type is text/plain