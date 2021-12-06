# Analysis and Prediction of Apartment Sales in Lund, Sweden

## Project overview

The aim of this project is to provide a thorough analysis and eventually
build model using machine learning algorithms to predict the housing prices in 
the city of [Lund](https://en.wikipedia.org/wiki/Lund) where I am currently 
living. I hope this project could not only provide a general 
overview of the recent Lund housing market, but also answer business-like questions for the potential housing buyers/sellers like:

* When is the best time to sell/buy an apartment/house?
* If you are going to sell a property, which agency (or even more 
  progressively, whom) 
  you should call?
  
* What is the reasonable price for a given property with parameters like 
  location, living area size, number of rooms, floor number, year of build, 
  etc.?


This project is still ongoing.

## Progress so far:

### Web scrapping

The first task is to collect data. I used Python and a web scrapping module 
[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to 
scrap 2500 properties sold in Lund for the past year (dated from 2020-10-30 to 
2021-10-21) from [Hemnet](https://www.hemnet.se/), the go-to website where people look for housings 
in Sweden. Note that the data I collected are all public information, but for 
privacy concerns, I did not upload the generated full csv file 
which contain private info like addresses. These files can be provided upon 
request. 

Hemnet constructs the information of the sold properties as two layers. The 
first layer provides following items:
* address
* housing type
* area
* number of rooms
* monthly fee
* individual link
* sold price

[Here is the example](hemnet_page50.ipynb) of how we 
can scrap the first 
layer 
info. Then we 
can use [this script](hemnet_csv.ipynb) to generate 
a csv file for all 2500 items.  

With the individual link provided for each sold property, we 
are able to click in and find the info contained in the second layer such as:
* asking price
* year of build
* agent/agency who sold this property

If the property is apartment, it also provides additional info:
* if there's a balcony or not
* if there's an elevator or not
* which floor/total building floor

Out of 2500 sold properties 1972 of them are apartment, so we first 
focus on this category and later we can do similar analysis to houses. 
[Here is the example](hemnet_2nd_layer_test.ipynb) of how to extract the second 
layer info. 
Then it is fairly straightforward to generalize this code to all 1972 items using [this script](hemnet_2nd_layer.ipynb).



### Data Analysis

Using the data we collected, we are able to do some analysis which give us a general picture of the Lund apartment sales. Actually we can answer the first and second question we brought up in previous section using these data. Please 
[check here for details](Lund_apartment_analysis_211206.pdf).

## Ongoing work/future plan:

* Convert the addresses to the lan and longitude, and then use a Google map 
  API to plot a 2D heat map showing the price distribution. 
  
* Based on such distribution, I am expecting a clustering algorithm 
like K-means could divide Lund into several regions based on price per 
square meters which could be a very useful feature in model training. 
  
* Split data into train and test sets.
  
* Train different models e.g., multiple linear regression, random 
  forest, etc. and evaluate performances.
  
* It might be useful to do a time series analysis to predict the price 
oscillation within a short time window. 
  
* Build an API endpoint which is able to take in a request with a list of values from a property listing and return an estimated price.








