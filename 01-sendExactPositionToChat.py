#!/usr/bin/env python

#!/usr/bin/env python
# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *


# Ensures that code in block is only run if script directly invoked
if __name__ == "__main__":

    """
    First thing you do is create a connection to minecraft
    This is like dialling a phone.
    It sets up a communication line between your script and the minecraft world
    """

    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()
        
    # Get the block that the player is currently in
    playerPosition = mc.player.getPos()
    
    
    # create the output message as a string
    # Python 2 only version for reference
    #message = "You are at (%.1f, %.1f, %.1f)" % (playerPosition.x, playerPosition.y, playerPosition.z)
    # Python 2 and 3
    message = "You are at ({0:.1f}, {1:.1f}, {2:.1f})".format(playerPosition.x, playerPosition.y, playerPosition.z)

    # print to the python interpreter standard output (terminal or IDLE probably)
    print(message)
        
    # send message to the minecraft chat
    mc.postToChat(message) 
