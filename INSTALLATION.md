Installation Instructions
==========================
Hardware Setup
-------------------
1. Ensure telescope motors are connected properly to the control board and the control board connected to the raspberry pi's GPIO pins.
2. Insert SD Card preloaded with raspian wheesy into the RPi's SD card slot.
3. Connect webcam USB into USB slot of RPi
4. Connect Network cable or wifi dongle
5. Connect any other accesories such as Wifi Dongle, Monitor or keyboard/mouse

Networking Setup
------------------
There are two way's a RPi can get an IP address

1. DCHP - This is where your network router will provide a dynamic IP address, This means you will have to have a monitor connected to the RPi to find the IP
2. Static - This is where the RPi is setup to have one specific IP - This is the IP that you will use

Software Setup
-----------------

Either through direct input or over ssh:

1. Update all packages on your system `sudo apt-get update` and `sudo apt-get upgrade` This may take some time
2. Install the required packages `sudo apt-get install motion apache2 php5`
3. Install the [WiringPi GPIO Utility](http://wiringpi.com/download-and-install/) included with the WiringPi python libraries
4. Ensure that [cgi-bin is enabled on apache server](http://www.techrepublic.com/blog/diy-it-guy/diy-enable-cgi-on-your-apache-server/)
5. Copy everything from the MotorScripts to /usr/lib/cgi-bin
6. Copy the text from rc.local to /etc/rc.local
7. Copy everything from the ControlWebsite folder to /var/www/
8. Restart your RPi

Usage
-------------

You can control your Telescope through the command line, Just execute the scripts in /usr/lib/cgi-bin as root
You can also control the motors via the website, located on the IP address from earlier. This also gives you the live stream from the webcam.
