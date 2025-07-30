import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Reading in from CSV file attached to project
df = pd.read_csv("vgsales.csv")

# Transforming data table so that exterior regions' sales are not included for US consumer base
df = df.drop(["EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"], axis=1)
# Removing less popular video games that lack North American Sales from DataFrame
df = df.drop(df[df['NA_Sales'] <= 1].index)
# Removing Null value cells and rows containing Null
df = df.dropna()

# Establishing different platforms used for dropdown box selection
platforms = df["Platform"].unique()

# Beginning our KMeans data for tested constraints for visualization of data and patterns
X_train, X_test, y_train, y_test = train_test_split(df[['Year', 'NA_Sales']], df[['Rank']], test_size=1, random_state=0)
X_train_norm = preprocessing.normalize(X_train)
X_test_norm = preprocessing.normalize(X_test)

# Initiating Machine Learning through KMeans Clustering algorithm to establish patterns in data
kmeans = KMeans(n_clusters=int(max(df['Rank'].unique()/10)), random_state=0, n_init='auto')
kmeans.fit(X_train_norm)
df = df.drop(df.index[-1])
df.loc[:, "cluster_data"] = kmeans.labels_

'''
# https://www.datacamp.com/tutorial/k-means-clustering-python
# the above link was utilized in building the tests below and assisted with the plot-design
K = range(2, 195)
fits = []
score = []

for k in K:
    model = KMeans(n_clusters=k, random_state=0, n_init='auto').fit(X_train_norm)
    fits.append(model)
    score.append(silhouette_score(X_train_norm, model.labels_, metric='euclidean'))

sns.lineplot(x=K, y=score)
plt.show()

# Displays scatterplot data
sns.scatterplot(data=X_train, x='Year', y='NA_Sales', hue=kmeans.labels_)
plt.show()
'''

selection = 1

while selection == 1:
    print("Welcome to Nostalgic Labs, where we aim to connect you with the games of your past")
    # ensuring we refresh the values of the dataframe through every loop
    filtered_df = df

    # receive user input for platform selection
    print("Please select from the following Consoles by typing the name in the command line:")
    print(platforms)
    platform_selection = input()
    filtered_df = filtered_df.drop(filtered_df[filtered_df['Platform'] != platform_selection].index)

    # receive user input for genre selection
    print("Please select a genre for a type of game you remember or want to find:")
    genres = filtered_df['Genre'].unique()
    print(genres)
    genre_selection = input()
    filtered_df = filtered_df.drop(filtered_df[filtered_df['Genre'] != genre_selection].index)

    # receive user input for specific game title
    print("Please select a game from the list provided to see some familiar titles from your childhood:")
    print(filtered_df['Name'])
    game_selection = input()
    filtered_df = filtered_df.drop(filtered_df[filtered_df['Name'] != game_selection].index)
    game_selection_clusterID = filtered_df.loc[filtered_df['Name'] == game_selection, 'cluster_data'].iloc[0]
    cluster = df[df['cluster_data'] == game_selection_clusterID]
    # display the video games which have been sorted by kmeans into the respective cluster
    print("We suggest these games to help bring back some nostalgic moments of your youth;")
    print(cluster['Name'])

    selection = input("Would you like to look for a different set of games? Please enter 1 if you would like to "
                      "continue and 0 if you would like to exit the program: ")
