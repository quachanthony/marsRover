# marsRover

This project is the solution to the Mars Rover problem. I like to think of this problem as a real world scenario to inform how 
I would go about implementing some of the behaviors. If I were a NASA engineer responsible for these really expensive rovers, 
I would definitely be as conservative as possible when it comes to their safety. How I picture this working in the real world is
that a satellite is probably taking images of the red planet and some NASA folks are studying these images to for two key factors:
(1) do we want to explore this area to learn something and (2) is it safe to go over there? This would probably happen incrementally.
so the rovers would explore a known boundary for awhile until the next boundary is defined.

Since the prompt to this problem was a little open ended, here are the key behavioral decisions I made and why:
- Since there are 2 real life Mars Rovers, Spirit and Opportunity, I will be referring to them by name to discern the difference between 
  the two. Spirit is the first rover and Opportunity the second.
- If the Rovers are about to move off the Plateau, we should stop them from doing that for safety. However, if downstream instructions 
  put them back on the plateau, that should be allowed. 
- Since the Rovers move sequentially, even if Spirit receives bad instructions, that does not prevent Opportunity from moving and vice versa
- The two rovers are allowed to occupy the same space on Mars. It is a huge planet and I am assuming that the instructions and coordinates 
  given from NASA is to go to a certain sector on the planet.
- The Rovers are smart and can handle "close enough" instructions such as too many spaces between inputs and lowercase letters
- I was considering creating a class to represent the Planet itself, but thinking more on that I believed it overcomplicated the solution. 
  The Rovers should have equipment on board that allows them to keep track of where it is and thus I put most of the responsibility on the 
  Rover class. 

### Prerequisites

- This project was built on Python 3.8.2
- You will get error from contextlib --> surpress if you try to run this with Python 2.7

### Executing the Program

## Single Standalone Execution of marsRover.py 
- To execute the program, please navigate to the marsRover directory in the terminal and enter:

$ python3 marsRover.py baseCase.txt

This will run the program with the given example from the prompt. The output should be displayed in the terminal

### Running the Tests

- This will run a series of tests that I have provided. The text files used for these tests reside in the directory /test_files

$ python3 roverTest.py 

## Running Custom Tests

- This will allow you to test any input file you'd like, where input_file.txt is one that you provide
- The caveat here is that you will need to know what the expected output is to compare it to the result in the terminal

$ python3 marsRover.py <input_file.txt> 

### Sample Tests

In general there a 3 kinds of test cases, here are examples of each:

1. Something is wrong with the file

    a. Wrong file extension
    Input = baseCase.jpg
    Output = (None, None) "Invalid file type. Please send new instructions."

    b. Extra info in the middle of the file
    Input = 
    5 5
    1 2 N
    14236lrmpadnio
    LMLMLMLMM
    3 3 E
    MMRMMRMRRM

    Output = ('Spirit: 1 3 N', None) 
    **Please note that there are valid commands in that line that would act as Spirits commands and would make it move N 1 space

2. Something in the file is invalid

    a. Invalid Plateau character
    Input = 
    5 a 
    1 2 N
    LMLMLMLMM
    3 3 E
    MMRMMRMRRM

    Output = (None,None) Invalid plateau dimensions. Please send new instructions.
    **Without a properly defined plateau, it is unsafe to move the rovers at all. Best to stay put

    b. Rover heading as a word 
    Input=
    5 5
    1 2 Nope
    LMLMLMLMM
    3 3 E
    MMRMMRMRRM

    Output = (None, Opportunity: 5 1 E) Heading must be a single letter.
    **This might look like it would pass since the first letter is a valid one, but just to be sure we reject this

3. Rover behavior

    b. Rover is moving off the Plateau, stops then is given more commands that allow it to move
    5 5
    1 2 N
    RMMMMMLMM
    3 3 E
    MMRMMRMRRM

    Output = 
    Spirit is about to fall off the plateau. Stopping here: 5 2 E
    (Spirit: 5 4 N, Opportunity: 5 1 E)

    **Spirit was heading E but then it got th LMM command which made it go 2 spaces N

    b. Rover is about to move off the Plateau and just stops with no more valid commands

        Input = 
        5 5
        1 2 N
        LMMM
        3 3 E
        MMRMMRMRRM

        Output = Spirit: 0 2 W, Opportunity: 5 1 E
        Spirit is about to fall off the plateau. Stopping here: 0 2 W
        Spirit is about to fall off the plateau. Stopping here: 0 2 W

        **Spirit already reached the edge of the plateau after its first move, and is getting more commands to move
          it stops there instead and that remains its final position