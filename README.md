# Keylogger
 An example of how to write your own keylogger. The program intercepts the keys and takes screenshots only in the programs that we specify in the settings. In addition, the output file will contain the name of the browser tab where the user entered the data.
It will then send the logs to your email. (set send_logs to True in config.py, and spy_these_programs to for example ["Mozilla Firefox"]). The sent data will be automatically deleted from the disk.
   
   
# A few words about this keylogger
Let's be honest, python is not a good language for writing good malware (C/C++ will remain in my heart forever ❤).
For example, Python code compiled into an executable can be decompiled into source code very easily.
Moreover, multithreading is constrained by the GIL, so we are losing a bit in performance (You can use a different version of python such as Jython or IronPython). This keylogger is just a template to show the idea behind how the keylogger works. 
Meaningful functions have not been implemented so that a person who cannot write code and would like to use it for illegal purposes could be easily traced and the program on the victim's computer can be easily exposed.
The keyboard library does not work well if the user is typing quickly :( When I have a little more time, I will write my own.

# Installation
* Recommended python version: 3.9
* pip install -r requirements.txt   
* Set the options you are interested in in the config.py file.
Use app password instead of account password. (https://support.google.com/mail/answer/185833?hl=en-GB)
* Run main.py
