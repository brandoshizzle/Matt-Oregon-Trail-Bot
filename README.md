# Matt (Oregon Trail Bot)
Don't die of dysentry

## Set up
This bot must be run locally on a host computer - someone who is in the discord channel. The host needs to run a version of Oregon Trail, then stream the video to the discord channel.
**The host CANNOT focus away from the Oregon Trail game while the bot is running!**
The bot simulates key strokes on your computer to input controls into the game. It is recommended that the host join the server from their phone to enter text and leave the host computer be.

## Development thoughts
- Cooldown should be 2 seconds or so
- Matt alerts the players that the cooldown is done
- Matt should start the 5 second collection when the first person starts typing after the cooldown
- Players can type in 'hunt' and it starts hunt mode: all commands are entered with no democracy
- Check if the input is a number, a word, or a letter. If they are word answers, maybe assume it's names and take first 4 instead of most popular?
