# hkt-autocorrect

## Instructions
Replace the two files in the directory with your own hkt files named "melody.hkt" and "harmony.hkt"

Go into your command line and type
```
python autocorrect.py
```

It will ask you for the probability of an "off" note autocorrecting to the harmony. It ranges from 0-1 inclusive. 
0 means that none of the notes will be corrected.
1 means that all the notes will be corrected.
0.5 would mean that there is a 50% chance that when an "off" note is discovered, it will be autocorrected.

The output of the test file is a string of scale degrees. 
Changed notes are demarkated by [x->y] - meaning that "off" scale degree x has been changed to the "correct" scale degree y.

## Example
If your melody was originally:
```
1 2 3
```
A sample output could be:
```
1 [2->5] 3
```
Meaning that you should change the 2nd note from the second scale degree to the fifth.

## TODO
Add support for non diatonic melodies and chords.
