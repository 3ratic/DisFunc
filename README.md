# DisFunc PoC

## About
Just like before, this project is another DiscordRAT. This time however it is more compact and small while still packing the same amount of userability. DisFunc will
allow a user to take control of a users conputer and run the usual system commands you would run in the command prompt. For example `netstat -an` or `netsh wlan show profiles [WIFI_NAME] key=clear`. This gives DisFunc more options for the user unlike Deadware. 

## How to use
DisFunc is easy and quick to set up. The requirments for you to run this script are python 3 and make sure you have installed the discord python module. First, you will want to go to the Discord Developer Portal and create a Discord bot and invite it to your server. Then, in line 26 you will want to change the ID to your desired notification channel within your Discord server. From there, you will want to scroll down to line 48 and change where it says `TOKEN-HERE` to your Discord bot token. Now you're ready to go and ready to use DisFunc!

You could also use pyinstaller to compile the script as a `.exe`. This will then allow you to run the script on any Windows operating systems however the file size will increase. You can use the `builder.bat` to do this automatically for you. Please not, you must have pyinstaller installed onto your system before you use `builder.bat`.

The basic command syntax for DisFunc is `?cmd [command]` for example `?cmd netsh wlan show profiles`
