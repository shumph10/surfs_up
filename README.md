# **surfs_up**
Analysis of Hawaii weather data for investment portfolio of a surf and ice cream shop.

--------------------------------------

##**Overview**
Analysis of Oahu, Hawaii island weather for potential investment in a surf and shake shop. Desired information included details of precipitation and temperature trends that would effect the buisness ability to open and therefore the business' profits. A flask app was developed to display this information(code available in app.py). Further, the weather in both June and December was analyze in depth to determine if the business would be able to remain open year-round. SQLite was used to reflect the data in the hawaii.sqlite file into a database, which was then queried and filtered for the desired paramaters, temperatures in June and December, respectively. This information was inputted into a database, and summary statistics were done to see the mean, minimum, maximum, and percentiles. 

--------------------------------------

##**Resources**

- Data Source: [hawaii.sqlite](https://github.com/shumph10/surfs_up/blob/main/hawaii.sqlite) </br>
- Software: Python 3.9.7, Jupyter Notebook 6.4.0, SQLite, Flask 2.1.2

--------------------------------------

##**Results**
- The average temperature for June in Oahu is 77.2 degrees Fahrenheit.
- The minimum temperature for June is 71.0 degrees.
- This is ideal weather for surfing, meaning the shop should have little trouble closing due to temperature conditions in the summer months if trends follow Junes statistics.
- The June weather summary statistics are as follows:

![June_Temps_sum_stats_screenshot](https://user-images.githubusercontent.com/100040705/168492206-b260512c-8619-4ecb-8dce-fc109b797579.png)


- The average temperature for December in Oahu is 71.1 degrees Fahrenheit. There is not a major difference in the temperatures between June and December averages, therefore there should no issue opening the surf shop in this month. This indicates the shop could stay open year round.
- The minimum temperature is 60.0 degrees Fahrenheit, with the bottom 25th percentile occuring between that and 69.0 degrees.
- The December weather summary statistics are as follows:


![Dem_Temps_sum_stats_screenshot](https://user-images.githubusercontent.com/100040705/168492236-4dc1f1b0-220d-4ac4-b97f-d1a65b41c6fc.png)

- A histogram plot was developed to visualize the frequency of temperatures occurance throughout the year. The majority of temperatures occur in a range that would be ideal for outdoor activites like surfing (70+ degrees Fahrenheit). 
- The graph is as displayed below:

![temp_freq_histogram_graph](https://user-images.githubusercontent.com/100040705/168492849-12666f9e-d701-4e75-90a4-e650b693a82b.png)


- Precipitation information was gathered and graphed, most days throughout the year seem to get a small amount of precipitation, with a small percentage recieving an amount of rain significant enough to hinder business. This data was visualized as shown below:

![precip_graph_screenshot](https://user-images.githubusercontent.com/100040705/168492784-fb4dc8e7-6e4f-4135-ad78-7ef5f7d50735.png)

--------------------------------------

##**Summary**

The summary statistics for both June and Decemeber show ideal temperatures on majority of days for surfing, thus the shop should be able to stay open year round. Based on these trends, there are minimal days in the coldest months the shop would close due to temperature conditions. The December summary statistics show the bottom 25th percentile being 69.0 degrees or lower, this shows there is not a major difference in the average and minimum, and there would be few days that the surf show would close for weather condititons. If the remained open any time the temperature was over 70.0 degrees, they would need to close on average 7 days in December. From the histogram of temperature frequency throughout the year, a conclusion can be drawn that the majority of the days temperature would not affect business in the shop. Overall, from the information gathered, the shop would need to close a small percentage of the time due to weather conditions.
Further information should be collected for summaries of other months of concern, like January and February to calculate the total number of days the shop would be closed. This could be used in relation to potential profits per day in those months to predict total loss of revenue. 
Additional queries could be performed to combine temperature and precipitation information to predict the number of days per year or month the shop may need to close. Information could be gathered through APIs to inquire about weather conditions such as cloudiness that could additionally affect the business.  

--------------------------------------

##**Contact Me**

Email: sarahhumphrey2016@outlook.com </br>
[LinkedIn](https://www.linkedin.com/in/sarah-humphrey-data-analyst/)

