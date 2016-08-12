# rasp-pi-timelapse
[WIP]
A Python 3 program to take photos for a timelapse. This program runs only in *Python 3*.

## Execution:
Download the file into the present directory. Afterwards run:
```
% python3 timeLapse.py
```

There are 2 options you can run the python program:
* with CLI options - `python3 timeLapse.py -vf 0.5 -s 1000 -o image.jpg -p ./documents/users/testCode` 
* without CLI options (the program will guide you through the process) `python3 timeLapse.py` 

### CLI Arguments: 
* `-f` - frequency of shots (in seconds)
* `-s` - number of shots to take
* `-o` - ouput image file
* `-p` - path to store the image files
* `-v` - verbose output
* `-h` - help manual

### Basic Usage: 
1. Enter Arguments (via CLI or not)

2. Confirm Arguments
``` python
  Shot Frequency: 5 seconds
  Number of Shots: 300
	Total time (freq x shots): 
		1500.0 seconds 
		25.0 minutes 
		0.4 hours
	Path: ./
	Filename: image.jpg 
> Confirm details [Y/N]: 
```

3. Take a test shot
``` python
> Do you want to take a test shot [Y/N]: Y
. 
[Done]
```
4. Take multiple shots
This will print out the number of shots taken so far.

```python
. . . . 5 . . . . 10 . . . . 15 . . . . 20 . . . . 25 . . . . 30 . . . . 35 . . . . 40 . . . . 45 . . . . 50 . . . . 55 . . . . 60 . . . . 65 . . . . 70 . . . . 75 . . . . 80 . . . . 85 . . . . 90 . . . . 95 . . . . 100 

. . . . 105 . . . . 110 . . . . 115 . . . . 120 . . . . 125 . . . . 130 . . . . 135 . . . . 140 . . . . 145 . . . . 150 . . . . 155 . . . . 160 . . . . 165 . . . . 170 . . . . 175 . . . . 180 . . . . 185 . . . . 190 . . . . 195 . . . . 200 
```
