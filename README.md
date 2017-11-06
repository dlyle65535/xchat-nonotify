# NoNotify for XChat

## Selectively turn off notifications per channel

## Installation
Copy __src/nonotify.py__ to your user scripts directory (~.config/xchat2 on linux, xchat -u will show)

From xchat window call

   `/load nonotify.py`
   
You should see:


`Module No Notify Loaded.`

## Usage
NoNotify will keep a list supress notification on a list of channels you set up. There are 3 commands.

- /nonotify #channel

   Suppress notifications for #channel.

- /nonotify remove #channel
   
   Remove #channel from the list of channels where notification is suppressed. 
     
- /nonotify show
   
   Show list of suppressed channels.
