from __future__ import print_function
import spiceypy

def print_ver():
        """Prints the TOOLKIT version
        """
        print(spiceypy.tkvrsn('TOOLKIT'))

if __name__ == '__main__':
        print_ver()