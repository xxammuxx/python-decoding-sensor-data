# Runner script for all modules
from load_data import load_sensor_data          # module 1
   

#######################################
# Do not remove these two lines
# if you do, it will break the unittest
data = []                   
print("Sensor Data App")
#######################################

# YOUR CODE HERE

# Module 1
data = load_sensor_data()
print("Loaded records: {}".format(len(data)))
