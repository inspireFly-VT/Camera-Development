This repository documents the camera developments of inspireFly. This will one day have the following:
1. A detailed description of the process the team went through in getting the camera working
2. Good documentation on how everything fits together

Current Issues:
The 3MP startup routine function bricks the camera, so we commented it out. Its purpose was to take a dummy picture so that the actual picture wasn't tinted yellow.
The current workaround is to use the take multiple pictures function we have.
TODO: Modify the multiple picture functions so that it takes two pictures, and deltes the first.
