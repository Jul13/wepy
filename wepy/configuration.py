"""This config file is just a dictionnary of useful values."""
# Author: Juju

import os
from pathlib import Path
import dotmap

PATHS = dotmap.DotMap
DATA = dotmap.DotMap


OS = os.name
PATHS.lib = str(Path(os.path.abspath(__file__)).parent.parent)
# replace ~ by the full path name
PATHS.home = os.path.expanduser('~')


# TRIP DATA PATHS
if OS == "posix":
    # for the unix root, you should create a symbolic link to the data
    # folder by ln -s /media/sf_R_DRIVE/.../ ~/dev/data/
    # you can alternatively copy the data there
    PATHS.data = PATHS.home + '/dev/data/'
    if not os.path.exists(PATHS.data):
        Warning('# Please create a symbolic link to data in '
                'directory ' + PATHS.data + '!')
        PATHS.data = \
            '/media/sf_R_DRIVE/dev/data'
else:
    raise Exception('# NOT IMPLEMENTED FOR WINDOWS, MODIFY THE SCRIPT !')
    PATHS.data = '???'

PATHS.trips = PATHS.data + 'trip_data/'
