# Kemper-Rig-Manager-.db-Sorter
Scripts and instructions on how to sort Kemper Rig Manager databases.

USE WITH CAUTION: CREATE BACKUPS. IF YOU'RE NOT SURE WHAT YOU'RE DOING, ASK!

I have about 8000 rigs in my Kemper rig manager library. Of course browsing that big of a list is extremely cumbersome. The two scripts and these instructions will sort the giant single database into a more logical order for easier use. 

This is certianly not a 'one size fits all' solution, but it's what worked for me. Obviously, you can edit the scripts to sort however you want to.

It sorts the database in this way:

1st into 'Studio' and 'Direct' <-- this is whether or not the rig has a cabinet model
2nd into a manufacturer folder ie.. Marshall, Fender etc..
3rd by amp name. 

In oder to this to work, you really need all of your rigs in a single folder. Just create a new folder in rig manager and drag all of your rigs into it. I had a folder with a pile of .kipr files in it. It was a mess of folders and sub-folders. I just dragged the whole mess in, folders and all. Rig manager will ignore the folders and other trash and just import the rigs.

the .db file is located in %LOCALAPPDATA%\Kemper Amps\RigManager in the new folder that you created. Mine was in 'local library'

The most tedious part of this process is 'fixing' the .db. You will need a program like DB Browser (free download) to open the .db. In order for the script to work properly, you have to ensure the 'Source Amp' and 'Amp Name' columns have useable names ie.. no "/", "\" or "*". Basically no special characters that cannot be used by windows to create folder names. You will also need to ensure there are no blank fields in any of those columns.

In each of the scripts, there are paths defined. You will need to edit these to fit your situation. I copied the .db into a folder on my desktop and did the work there. Once it was the way I wanted it, I dragged the folder structure back into %LOCALAPPDATA%\Kemper Amps\RigManager. 

Once the .db is fixed, with the names how you want them, there are 3 steps to sort it all out. 

1. Run the sort2_1.py script: <-- this creates the folder structure
2. copy this folder structure to %LOCALAPPDATA%\Kemper Amps\RigManager\(FOLDER) and open Rig Manager: <--when it opens, Rig manager will place an empty .db in each new folder. This takes a little time, so be patient. Once rig manager opens, you will see your empty folders. Close Rig Manager, copy the folder strucure back into whichever directory your script points to.
3. Run db_write.py: <-- once this finishes (~5 min for me) the folders are complete. Copy them back into %LOCALAPPDATA%\Kemper Amps\RigManager. I did not add a status bar or anything like that to indicate the script is running, so it sort of just 'sits' there until its finished. This script looks for the folders and .db files and will stop with an error if something is missing. 

* You can do all of this in %LOCALAPPDATA%\Kemper Amps\RigManager without all of the copying and dragging etc.. I just did it in a folder on my desktop. Just make sure your script has the correct path. 
