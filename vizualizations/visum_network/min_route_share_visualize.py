'''
Created on 26 Feb 2020

@author: thenuwan.jayasinghe
'''

import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv("C:\\Users\\thenuwan.jayasinghe\\OneDrive - tum.de\\Thesis\\2_Presentations\\8_Update_to_Dr_Rau_26022020\\min_route_share_99_26022020.csv")

od_total_threshold = 0
min_route_trip_threshold = 0
od_total_filter = (data_df['TotalODTrips'] >= od_total_threshold) & (data_df['MinRouteTrips'] >= min_route_trip_threshold)

od_filter_df = data_df[od_total_filter]
print od_filter_df

#visualization

min_route_pec_list = od_filter_df['MinSharePEC'].tolist()
_ = plt.hist(min_route_pec_list, bins = 50)
_ = plt.xticks(list(range(50)))
_ = plt.xlabel("Minimum route share %")
_ = plt.ylabel("Count")
_ = plt.title("Minimum route share distribution")
plt.show()
