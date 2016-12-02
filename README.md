# HicklesClassroom
   To play this game you need two things
    
    1. Download and install Git
        - Git is what I use to share the code.
        - For more information on installing git, 
          visit: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
          or ask your parents or teacher for help.
    2. Download and install Python 3.5.2
        - Python is the programming language I use to write the game.
        - For more information on installing python,
          visit: https://wiki.python.org/moin/BeginnersGuide/Download
          or ask your parents or teacher for help.


First, ask your parents which operating system your computer has installed.
Then, follow the instructions below for your operating system.


1. a) Downloading Git for Windows:
      - Just go to http://git-scm.com/download/win and the download will start automatically.
        Follow the instructions to complete the installation.

1. b) Downloading Git for Mac:
      - You can go to https://git-scm.com/download/mac to download.
        Follow the instructions to complete the installation.
      
1. c) Downloading Git for Linux:
      
      - Depending on which distrobution of linux you are using,
      
         - Debian/Ubuntu linux users can run:

               $ sudo apt-get install git-all

         - Fedora users can run:

               $ sudo yum install git-all


Once Git is installed, check your installation by typing

    $ git

in the terminal/command line. You should see something like this:
  
    $ git
        usage: git [--version] [--help] [-C <path>] [-c name=value]
                   [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
                   [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
                   [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
                   <command> [<args>]These are common Git commands used in various situations:

        start a working area (see also: git help tutorial)
           clone      Clone a repository into a new directory
           init       Create an empty Git repository or reinitialize an existing one

        work on the current change (see also: git help everyday)
           add        Add file contents to the index
           mv         Move or rename a file, a directory, or a symlink
           reset      Reset current HEAD to the specified state
           rm         Remove files from the working tree and from the index

          . . .
 
 
Finally, install Python 3.5.2.
First of all check that you don't already have Python 3 installed by entering 

    $ python3 --version

in a command line window. It should look something like this:

    $ python3 --version
      Python 3.5.2

If you see this, you are all ready TO BEGIN!
If not, follow the instructions below.

2. a) Downloading Python for Windows:
      - Go to https://www.python.org/downloads/release/python-352/
        and find "Windows x86-64 executable installer" and click the link.
        This should work for most Windows systems. 
        Ask your parents or teacher if you are not sure.
      - Open the .exe file when the download is complete and
        follow the instructions to complete the installation.
      
2. b) Downloading Python 3.5.2 for Mac:
      - Go to https://www.python.org/downloads/release/python-352/
        and find "Mac OS X 64-bit/32-bit installer" and click the link.
        This should work for most Mac systems.
        Ask your parents or teacher if you are not sure.
      - Open the .pkg file when the download is complete and
        follow the instructions to complete the installation.
        
2. c) Linux users should have Python 3 already installed.
      Ask your parents or teacher for help if you need it.
      

# TO BEGIN!

Once you have these two things installed, you can install this game by typing
 
    $ git clone https://github.com/loayzag91/HicklesClassroom
  
Then type
  
    $ cd Classroom/
   
in your terminal to go into the folder. To see what's inside, type:


    > dir
  
for windows, or
  
    $ ls

for mac. You will see something like this:

      $ ls
         Final.py  guessTheNumber.py  Second.py  Start.py
 
You can have fun making changes to guessTheNumber.py so that it looks like Second.py or even Final.py
and you can play your version with 
  
    $ python3 guessTheNumber.py

or, to play any version of the game you can type:

    $ python3 <file>.py

If you ever want to start over, simply type:

    $ git reset --hard HEAD

and all your changes will go back to how they were when you first installed the game.

# ENJOY CODING!
