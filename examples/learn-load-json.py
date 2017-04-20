# ==============================================================================
# title           : lean-load-json
# description     :
# author          : Julien Reynier
# date            : 31/03/2017
# version         :
# IDE             : PyCharm Community Edition
# ==============================================================================


import wepy.configuration  as cf
import json
import os
import re
from pprint import pprint
import dotmap

# The file location that is in our config file
path_trips = cf.PATHS.trips

# Now find the files with answers
list_files = os.listdir(path_trips)

r = re.compile('response.txt')
list_files = list(filter(r.search, list_files))
len(list_files)

# loads a particular file
data_file = open(path_trips + list_files[0])

# this builds a dictionnary from the json file
data_answer = json.load(data_file)
data_sent = json.load(open(path_trips + str.replace(list_files[0],
                                                    'response', 'sent')))

# a first way to print the content
pprint(data_answer)
# now data is a regular dictionary accessible like this
data_answer['fuelEstimation']['co2Emission']

# dotmap transform dictionaries into structure (easier completion)
simple_answer = dotmap.DotMap(data_answer)
simple_sent = dotmap.DotMap(data_sent)
# the somewhat simpler dotmap access:
simple_answer.fuelEstimation.co2Emission
simple_answer.fuelEstimation.fuelVolume

print(simple_sent.keys())
simple_sent.vehicle
