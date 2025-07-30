# Captsone
WGU Machine Learning Algorithm Captsone Project

This README will cover the basic functions found within the main.py file of this project, the requirements and a brief overview of the expected results.

------Function-------
When utilizing the source file 'main.py' understand that there are no catch, exceptions, warnings, or other implementations for faulty data entry
Any entry that does not fit exactly the required commands will result in a fault and crash the python program

Imported libraries which may require additional installation of extensions are listed below:
pandas
seaborn
matplotlib.pyplot
sklearn.model_selection import train_test_split
sklearn import preprocessing
sklearn.cluster import KMeans
sklearn.metrics import silhouette_score


To install and run the application, complete the following steps:
1.	Download the main.py file
2.	Download the vgsales.csv file to the designated pathway by importing it directly into the project folder
3.	Open PyCharm Community Edition (all other editions of PyCharm should be acceptable)
4.	Import any necessary libraries listed above into the project
5.	With the project open: if there are errors associated with the above-mentioned libraries, right-click the highlighted sections and give PyCharm permission to download necessary libraries.
6.	Click ‘Run’ in the top right of the IDE to begin running the program.
7.	While the program is running, there will be several prompts to guide you.
8.	Please note: all inputs are case sensitive and there are no error detection mechanisms, any mistyped input will result in the program faulting in error.
9.	Prompt 1 will ask for your input of a specific console, enter your selection in the command window and press the enter key.
10.	Prompt 2 will ask for your input on the available genres for that console that are offered within the database, enter your selection into the command window and press the enter key.
11.	Prompt 3 will ask for your input on the available titles, enter your selection of the title not including the associated numbers attached to the title, only the title itself, and press the enter key.
12.	Prompt 4 will follow the list of the associated clusters based on the selections made in prompts 1, 2, and 3, you will be asked if you are satisfied with the selection or would like to run the search again. In the available space in the command window, enter ‘1’ if you would like to repeat the search or enter ‘0’ if you like to exit the program followed by pressing the enter key.

------Requirements------
PyCharm Community Edition 3.14 or newer (other IDEs may be sufficient but this is the original development environment)
If running on Linux OS '-pip install' of the various libraries may be required

------Overview-------
This program was developed for a Capstone Project for Western Governor's University utilizing Machine Learning to develop a need of a business to help drive an end goal. The choice of selection was a recommendation platform that utilized kmeans clustering to provide similar items in a suggestive platform towards customers with the ultimate goal being a customer facing kiosk or interactive display online. This is the command line interface version of the application and there is a potential for future updates to include a GUI that will better display the results. The .csv file is a collection pulled from Kaggle.com so its validity or accuracy of information should not be taken into account. There are various parts of the program which are commmented out for the availability of running the application upon download and for smoothness.

Initially, the program takes several factors out of the .csv file by removing null values and removing unnecessary data to transform the information into a usable subset. Taking an additional step further, the data is further reduced based on customer usability and viability for a marketplace. This was performed by removing the lower values from the pool of collections that did not meet a certain metric of total sales in the North American Sales region. Next the data is taken into the kmeans training set and testing sets to be assigned cluster values and are grouped together utilizing the values of the total sales, the year of release, and the unique key identifiers (which in the data set appeared to represent total global sales). When tested by silhouete score, the data yielded a 0.57 at the actual level of clusters provided. The amount of clusters are broken down into a smaller subset than typically seen by kmeans clustering for usability on this specific platform. The maximum clustering for the highest amount of accuracy was 15 clusters at the original, or starting, list. Given this information, the further steps could be taken to start with those 15 clusters and one could create micro-clusters from that point by grouping towards genre of the game(s) to allow for a higher level of input validation as well as increasing the overall accuracy of the output. However, while the data is not a realistic subset pulled from reputable sources gathering the world's sales data of video games, the microsets were not developed as it would not have likely increased the overall display of the output to have met expectations. There are no further stages of expected code or algorithm development at this time. 
