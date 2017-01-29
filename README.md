# Project Description
Contributors: Kathleen Gegner, Aileen Bai, and Zack Tucker
Code last modified: 12/7/2016

This a game that helps students better visualize physics problems. (Add more later)

# Installing Software

## Install Python 3.4
1. Download the appropriate Python file for your computer version here:  
https://www.python.org/downloads/release/python-343/

2. Once the download is complete, click on the file and the installer will start.

3. Follow the installation steps, until it is finished.

## Install Kivy
For more help see: https://kivy.org/docs/installation/installation-osx.html 

1. Open a terminal window (this assumes you are using OSX)

2. Copy the following into the command prompt, to install homebrew (See http://brew.sh/ for more info):  
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

3. Install the required files for Kivy, by copying the following into the same terminal window command line:    
brew install sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer

4. Install Cython and Kivy, by copying the following into the same terminal window command line. Enter each one separately.  
pip install -I Cython==0.23
USE_OSX_FRAMEWORKS=0 pip install kivy


# Download the files from GitHub

1. Go to https://github.com/kgegner/physics-game, select the green button "Clone or Download", and select "Download Zip File"

2. Drag the zip file from your downloads folder to the folder you want, and then double click on the zip file to extract everything (or manually extract the files)

3. Make sure your folder includes all the files, listed on Git Hub.

4. Navigate to the folder where all these files are saved in a terminal window. For example, if you saved everything in the Documents folder, then in another folder called School, and then finally in a folder called Game, this is what you should copy into your command line:  
cd ~/Documents/School/Game

5. Type the following into the command line to make sure all the files you expect are in the right place:  
ls


# Running the Application
1. If you have not just completed step 4 from the previous section, navigate to the folder where all the project files are saved, in a terminal window. For example, if you saved everything in the Documents folder, then in another folder called School, and then finally in a folder called Game, this is what you should copy into your command line:  
cd ~/Documents/School/Game

2. Run the application by typing the following into your terminal window:  
python transfer.py
