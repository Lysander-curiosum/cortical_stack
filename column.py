

"""
SO MUCH OF THIS INFORMATION IS ABSTRACTED
Techincal information on how these layers work
(Biologically, how does this result in substantial behaviours?)
and how can we represent this in code
"""

# a program meant to stimulate some of the activity in the cortical stack
# displays the general flow of activity for the state change
# emulates the layer-to-layer communication (from the cell state up to the layerstate)


# purpose: 
# A better understanding of the mechanics within the cortical cytoarchitecture
# This process in many ways allows us to exist in the world as moral agents.


# In a more pracitcal sense, for the purposes of this project, 
# Layers I-III compile the information, and define the action set (what must be carried out)
# the supragranular layers

# Layer IV communicates with the thalamus, and the rest of the cortical stack

# Layers V-VI (Intragranular layers) 
# Processes the commands, sends the information to the thalamus


# So, in the space of this program: 
# The layers will be tuned to the makeup of their biological counterpart

# The instruction set is activated in the soma of the pyramidal cells in the upper layers
# In matrix form, the math of the communication is unclear (how the signals result in substantial actions)


# Process a mathematical operation (representative of an action), the "anticipation" or the compilation of
# the information occurs before the actual operation is carried out
# Here, it will be a bunch of matrix operations meant to translate into an instruction set



# NOTE: How can the cortical stack tie to the working memory program? Is there any efficiency to this process
# beyond its obvious biological application?

# Evolutionary history??


import numpy as np
from pyramidal import pyramidal


"""
In terms of functionality that is important:
    Each cortical column must have a goal set, and initiate the state
    that is necessary to reach that goal. 

    Then, define a set of possible actions that allow the change from
    one state to another.
    -- what is necessary for the desired functionality to be carried out.

    Define the intermediate subgoals. 
    -- these are the "bullet points", or the subgoals.
    -- sections of the problem that need to be processed, in order for the larger "goal"
       to be accomplished

    Complete the intermediate subgoals
    -- execute that which will bring the desired change in state

    REMEMBER: The cortex can operate in parallel mode, so multiple problems 
    can be handled at once.
"""

# made up of six layers
# each layer is a class of its own
class column(object):
    def __init__(self, molecular, extern_pyramidal, extern_granular, intern_pyramidal, intern_granular):
        self.molecular = molecular
        self.extern_pyramidal = extern_pyramidal
        self.extern_granular = extern_granular



"""
Going foward:

Continue to flush out the biological structure for the Pyramidal Cell

"Either the neuron fires, or it doesn't"

You will obviously have the biological model
(Do you want to use machine learning, or kinda start from scratch?) <-- yes

But the neuron "firing" or not, why does this happen? (Synaptic pathways)
^
| 
-- for this, I would look at some specific papers

(keep in mind, that the pyramidal cells will be mass produced, in order for them
to cohesively work in the cortical stack)

How many? How many are firing, and to what end? In terms of true functionality,
you stand on the edge of an ocean

"""
