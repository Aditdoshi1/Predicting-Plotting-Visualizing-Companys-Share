# Predicting, Plotting Visualizing Company's Share
The project deals with plotting the share price based on the Sentiments of a news Article per day. A rank is calculated based on the articles sentiment which is later used to predict the price of the Companies share. Along with predicting the share price, The project also deals with visualizing the articles based on the sentiments, finding what words are repeated in the articles related to a particular company.
A K-Mean Cluster is formed to represent related words in the set of articles returned and a word cloud is formed to represent the clusters.
The Whole project is deployed on a localhost website using Flask and HTML.

## Collecting & Cleaning WebArticles using the Inshort-API
This is an Indian News website which summarizes a News article in 60 words. We used Node.js to collect the articles data from the website [InShorts](https://www.inshorts.com/). The collected data is stored in JSON file which is later converted in Excel filel using python for further processing. The JSON data is also used in multiple occurences to clean and use in particular set of code. 
We did not have to Clean the data as we did only collect data columns which are necessary for the project.

## Visualizing the Dataset
We Used Matlab library to plot and visulize the dataset.
Some of the visualizations included -
- Line Graph
- Horizontal Bar Graph
- Stack Bar Graph
- Word Cloud

## Algorithm's Used
- K-Means Clustering
- Sentiment Analysis
- Inverted Index Information Retrieval

## Requirements
It will install all the required python libraries
* pip install -r requirements.txt

## Run
- python main.py
  - This will run the server which is deployed on localhost HTML using Flask.
 To Access the project, Open Web Browser and access localhost:5000
 
- node data.js
  - This will run the data collection code which will collect data from [InShorts](https://www.inshorts.com/) Website and store it in a "Output.Json" file.

