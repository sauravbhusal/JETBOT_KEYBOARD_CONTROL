I am trying to control the jetbot using pygame so this is our trial code:

day 1:
the code that detect the keypress is done.
now it's time to set the pressed key function and when the specific key is pressed, we need to assign the pressed key value to a variable that will preform specific operation in jetbot.
this file will be updated timely until the code is completed.

day 2:
I tried running the pygame code on jetbot, but we had to face a problem.
problem is that we are controlling bot using ssh TUI and from the terminal we can't access the video from the jetbot or any frame.
so i think i need to try another way to control the bot.
I think i'm gonna use the flask server to localhost the opened file and i'll use jetbot code as a client code and than i'll try to run the bot.
let's see what happens tomorrow.

day 3:
finally my code worked.
now we are able to control our bot with our keyboard.
what is did was i streamed the output written in the keyboard.txt from the flask server.
http client was used to get the value from the server and according to the recieved value,i executed the functions.


