# Raspberry-Pi-Spy-Rover
<img src="https://user-images.githubusercontent.com/25673428/30251974-671f310e-9638-11e7-95a8-465ec3651c9f.jpg" alt="https://user-images.githubusercontent.com/25673428/30251974-671f310e-9638-11e7-95a8-465ec3651c9f.jpg" class="shrinkToFit" width="569" height="320">

## Motivation

This past summer I wanted to build a remote controlled car that would be able to stream video from its point of view, so that I would be able see what it “sees” while controlling it from somewhere else. After researching different options, I decided that using a raspberry pi was the best choice for building this spy rover because there were many available Raspberry Pi kits, tutorials and resources that would help me out. After constructing the spy rover, I then wanted to be able to control it through a GUI because I was not satisfied with just controlling it with a python program through a terminal using ssh. This is what led me to create the Spy Rover GUI.

## Lessons Learned

* **Time management:**
	One of the primary lessons that this project reinforced in me was that everything takes more time than you think it will. While I am quite good at planning my time in regards to school work, the fact that this project was not preplanned by one of my professors resulted in me running into lots of unexpected problems. Now I have become much better at planning for these unexpected problems.

* **Familiarity with Linux:**
	Since I used Raspbian, which is based on the Debian Linux distribution, for my Raspberry Pi’s operating system, this project helped me become much more familiar with using a Linux terminal.

* **More Experience with Python:**
	While the python coding that I did for this project was much less complicated than what I did in the python course I took at Penn State, this project still helped me keep my python skills from growing dull and it taught me a bunch about the python TkInter GUI library.

## Prerequisites
**Hardware**
  * Raspberry Pi 3 Model B
  * Raspberry Pi NoIR Camera
  * Raspberry Pi Camera Mount
  * RasPiRobot Rover Kit (I used: https://www.monkmakes.com/pi-rover/ )
  * USB Mouse & Keyboard
  * Micro-SD card (I reccommend getting it preloaded with NOOBS)
  * HDMI cable
  * LCD Screen or other monitor that has HDMI connection
  * Laptop and Wifi connection
  * Power cable of Raspberry Pi
  
**Software**
  * Putty
  * Xming
  
## Procedure

1.	Build RasPi rover using kit from https://www.monkmakes.com/pi-rover/
2.	Download Putty, a free ssh client for Windows
3.	Follow the kit instructions and use code from Simon Monk’s raspirobotboard3 github repository to make sure you can control the rover remotely over Putty
4.	Set up RasPi live web camera server using tutorial below:
http://www.toptechboy.com/tutorial/low-cost-raspberry-pi-ip-camera/
5.	Change the –w and –h parameters on the raspivid command to adjust the size of the videostream and change the –rot parameter to adjust perspective of the stream to your liking. 
6.	Then change the dimensions of the embed small web format (.swf) media player in the index.html, file from the tutorial, to fit the size of the stream.
7.	Download Xming, a X11 display server for Windows that will allow you to display GUI’s to your laptop from the Raspberry Pi through the Putty ssh connection.
8.	Make sure your current Putty session has X11 forwarding enabled
9.	Use the following command in the Putty terminal to start Xming server display: startlxde
10.	Download all Spy Rover programs from this repository and rrb3.py from Simon Monk’s raspirobotboard3 github repository, if you have not done so already
11.	Run SpyRoverGUI.py
12.	You should now able to run your own RasPi spy rover remotely through a GUI interface.

## Future Plans
Right now I am figuring out the best way to use IR LEDs to give the spy rover night vision. I will update this file once I have completed this improvement.

## Pictures of Spy Rover GUI

<img src="https://user-images.githubusercontent.com/25673428/30251704-5c4ec83e-9633-11e7-83dd-5ef2f005d711.PNG" alt="https://user-images.githubusercontent.com/25673428/30251704-5c4ec83e-9633-11e7-83dd-5ef2f005d711.PNG" class="shrinkToFit transparent" width="373" height="320">

<img alt="spyrover_roversettings" src="https://user-images.githubusercontent.com/25673428/30251852-08678d16-9636-11e7-84a7-070a334c7390.PNG" style="max-width:100%;" width="373">
