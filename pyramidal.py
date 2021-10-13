import numpy as np
import math
import perceptron as pc
import basal as bs



"""
Herein lies the code for the pyramidal cell.

(General purpose, for many state changes)

Three types:
Commissural
-- Form the corpus callosum

Association
-- 
Projection
"""

# how to make this a signal terminal?
# An instance of an object, which can be activate at any time?
# Passing a signal to a preexisting instance would perhaps
# just involve setting the adjacent cell

# Either it fires, or it doesn't 

"""
Parameters:
Type
- ensures that the cell falls into one of the categories listed above
- represented as a String here
Soma
- Body of the cell (variability of this across the different types of cortical cells
is something of importance)
- Holds genetic information (nucleus), while also ensuring the stability of the cell
- Also powers the rest of the cell
- The genes are the "instruction set" of the cell itself, so this portion of the brain
    holds enormous importance
- Represented as a matrix of values, which is the "instruction" set for what
  neuron is meant to accomplish (how the state of the stack will change)

basal_dendrites
- Recieve the input from adjacent neurons, what can lead to the
  neuron firing

ESPS (Excitatory Postsynaptic Potential)
- fet the information from the instruction set
"""

class pyramidal(object):
    def __init__(self, type: str, soma: int, basal_dendrites: bs, apical_dendrite, axon, collateral_axon,
    ESPS):
        self._type =  type
        self._soma = soma
        self._basal_dendrites = basal_dendrites
        self._apical_dendrite = apical_dendrite
        self._axon = axon
        self._collateral_axon = collateral_axon
        self._ESPS = ESPS
    
    # general notes for the class:
    # some functions that are relevant to the pyramidal cell
    # the dendrite is the signal receiving area of the cell
    # "highly branched", so it can recieve signals from many 
    # different directions

    # large amounts of voltage gated ion channels
    # activated by: Na+, Ca2+, and k+

    # Excitatory Postsynaptic Potential is what activates the ION
    # channels


    """
    codify_soma
    input: code[int][int] --> the genetic information of the pyramidal
    cell, which can be clarified post declaration

    """
    def codify_soma(self, code):
      # gather length of the matrix
      height = len(self._soma)
      length = len(self._soma[0])
      for x in range(height):
        for y in range(length):
          self._soma[x][y] = code[x][y]


    # returns the type of this pyramidal neuron, makes complexity of 
    # the instruction set apparent
    def ret_type(self, to_change):
     self._type = to_change
    



    """
    A neuron either fires, or doesn't
    Contritbutes to the global instruction set of all the neurons in the layer, which dictate towards
    an instruction
    Fires to a global matrix, which is the product of all the individual neurons (Average/Collection)
    Releases either a 1 or a 0
    Notes:
      So, how does a neuron truly intepret a signal?
      - Each dendrite receives a variety of signals
      - Obeys the rules of a logic gate to decide which signal to pass on
      - So for each dendrite, should there be a separate intepretation?
    """
    def fire(self):
      return 0

    def intepret_signals(self):
      # so each of the basal dendrites will have signals stored
      # or, they can be set?
      return 0



