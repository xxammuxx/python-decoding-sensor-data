# Runner script for all modules
from datetime import datetime, date
from load_data import load_sensor_data          # module 1
from house_info import HouseInfo                # module 2

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

# Module 2
house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area("id", rec_area=test_area)
print("\nHouse sensor records for area {} = {}".format(test_area, len(recs)))

test_date = datetime.strptime("5/9/20", "%m/%d/%y")
recs = house_info.get_data_by_date("id", rec_date = test_date)
print("House sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))
 

