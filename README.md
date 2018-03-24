# PY-UNO
A pygame version of the fun board game UNO! In which a single human
player can face off with 6 other decision tree based AIs. This was my final
CMPUT 275 project for the 2017 winter semester.

## Install and Running Instructions:

### Requirements:

**Python3.6:** Python3.6 (and pip) is needed to run PY-UNO it can be downloaded
for multiple OSes here:

<pre>https://www.python.org/downloads/release/python-360/</pre>

**Pygame:** After installing python3.6 use pip to install pygame using the pip
command:

<pre>$pip install pygame</pre>

**Operating system:** PY-UNO has been successfully run on windows 7-10, Linux
Ubuntu 14.04. Other operating systems are likely possible if they can
correctly operate python, and pygame.

### Startup:

Using either git to pull a copy of PY-UNO or extracting the zip containing the
main working files of PY-UNO, use terminal to navigate to the now extracted
PY-UNO folder. Then use python to run the main starting script, the following
command is required:

<pre>your_directory_path/PY-UNO> python PY-UNO.py</pre>

After this PY-UNO should be running and you are free to enjoy.

## Controls:

**Left Arrow Key:**  iterates selection (card or target) to the left

**Right Arrow Key:**  iterates selection (card or target) to the right

**Up Arrow Key:**  confirms and plays the selected card or target

After a game of Uno is done the player can re-hit the up arrow key to restart
to a new game of Uno.

**Window Exit Button:** varies from each operating system but clicking on your
operating window close button will exit the current instance of PY-UNO.

## Additional info:

**Game AI:** Within the release version of PY-UNO only one human player is
present. The other players (6 others) within the game are all AI's using an
multiple decision tree AI method. Essentially, the AI's act like a large
pachinko machine, in which the current board state is reviewed and actions are
dependent on the current situation. The two main decision trees used within
PY-UNO are a Main_Decision_Tree and Card_Choose_Tree. Another experimental
memory tree  Card_Guess_Tree was also developed but its full implementation is
not developed yet. The game AI as of know is developed to be a flash frame state
AI in which only current events and the present state make an impact onto the
AI's decisions. However, historic events are also used as the AI's will remember
players that use negative actions against them and will on occasion attack them
over other actions. Work was done to make this AI a future guessing AI but it
was not developed within time.

**Main_Decision_Tree:** Handles decisions that are critical to winning or losing
(eg: playing a winning move, or countering a potential winner). If no critical
decisions are nesicarry it passes turn decisions onto Card_Choose_Tree onto
figuring out what the most effective card is to be played. When a turn is played
main diecision tree is the first to be traveled down to. And can result into
different options being accessed. (eg: the main tree could be traveled into
stopping a player from winning, or moving onto Card_Choose_Tree for an arbitrary
card to be played).

**Card_Choose_Tree:** Simply figures out what card would be the most helpful to
be played for the current turn if no critical actions are required to be taken
(eg: playing the most common color or type in the players hand in a attempt to
maybe play another of the same color the next turn).

**Card_Guess_Tree:** Is a depth based tree method that keeps appending
new cards to the tree. Within this appending memory tree card data such as
card color, type, and the player who played are all stored. However, to
emulate actual memory limitations all of these values have different depth
levels attached to it (color = depth, type = depth + 1, played by = depth
+2). Each AI would potentially have a max memory depth and as a result when
the AI would check its memory it could only go so for to extract or
interpolate data. Additionally, as more cards are added to the memory tree
the past card memory values would increase in tree depth thus eventually
becoming  "forgotten". A small test function for Card_Guess_Tree is provided within
its file for an example of its use and how it was properly constructed
but is never implemented.

**Display Resizing:** Within PY-UNO the native supported and boot resolution is
1600x900 (16:9 aspect ratio). Users are free to resize the window to their
display needs but must keep in mind the limitations that are present with
pygame and sprite scaling. (eg: scaling the window to 20x4000 would be a bad
idea for actual use).

**Card Game Engine:** PY-UNO handles deck generation, turn logic, turn
iteration, card logic, display output, input controll, and AI implementation.
But due to the nature of these developed modules it can be easy to swap out
specific PY-UNO modules (such as AI or card_logic) to create other styles of
games. Using  defined files such as game_classes, deck_gen, and display_funct
one can likely adapt these broad scripts to accept new styles of card games.

## Uno Card Assets:

Uno card images are sourced from opengameart.org created by the author ikmhr.
Used under open source development, full credits go to ikmhr on creating this
awesome set of images. Link detailing the download of these assets and ikmhr's
page is shown below:

<pre>https://opengameart.org/content/uno-playing-cards-2d</pre>
