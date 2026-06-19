'''
Reader module for PEER NGA ground motion files
'''


import numpy as np 
import os 



def read_peer_file(file_path):
    '''
    Read a PEER NGA format ground motion file

    Parameters:
        file_path: str 
            Path to the .at2 file

    Returns:
        tuple (time, acceleration, metadata)
            time -> numpy array of time points (seconds)
            acceleration -> numpy array of acceleration values (in g)
            metadata -> dict containing record imformation
    '''
