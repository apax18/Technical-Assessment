
## Technical Assessment

This tool is a command line application that builds a square grid on terminal at a given location. Then the user can
move the curser by pressing associated letters on keyboard. The cursor is initially on the top left corner of the grid.
See below for the letters and associated functionality:

⋅⋅* u: Moves up
⋅⋅* d: Moves down
⋅⋅* l: Moves left
⋅⋅* r: Moves right
⋅⋅* p: Prints the cursor path
⋅⋅* e: Exits the program

Pressing any other key returns an error informing the user that the letter wasn't recognised.

*The size of the terminal requires to be larger than the gird that this tools build.*

#### Prerequisites

There libraries used in this code are python standard libraries and require no installation. However, For **Windows**
python standard library doesn’t have **curses** by default. It can be installed by using pip:

```pip install windows-curses```


#### Running the Application

This application can be run by below command:

```python3 techAssessment.py```

The default values can change, for instance the size of teh square. This can be done by giving arguments when
instantiating the class **CommndLineApplication**. See the code for more info.
Alternatively they can be given as an argument when running the code by using sys library and an small adjustment.