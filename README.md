# Analysis and prediction of housing prices in Lund, Sweden

## Project overview

Nearly everyone cares about their housing. As the Wall Street legend 
Peter Lynch wrote in his book "Before you do invest anything in stocks, you 
ought to consider buying a house, since a house, after all, is the one good 
investment that almost everyone manages to make". Many people have 
made sizable profit in the transition from small apartment to a larger one 
and eventually to a house.

The aim of this project is to provide a thorough analysis and eventually
build model using machine learning algorithms to predict the housing prices in 
the city of [Lund](https://en.wikipedia.org/wiki/Lund) where I am currently 
living. I hope this project could not only provide a general 
overview of the recent Lund housing market, but also answer business-like questions for the potential housing buyers/sellers like:

* When is the best time to sell/buy an apartment/house?
* If you are going to buy/sell a property, which agency (or even more 
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
privacy concerns, I did not upload the downloaded webpages and generated full csv file 
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

[Here is the example]() of how we can scrap the first layer info. Then we 
can use [this script]() to generate a csv file for all 2500 items.  

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
[Here is the example]() of how to extract the second layer info. 
It is fairly straightforward to generalize this code to all 2500 items which I 
am currently working on.

These parameters obtained from 2nd layer may be important when we later train 
machine learning 
algorithms for the prediction of the housing prices. Also, it could answer 
the second question I brought up in the previous section by evaluating 
agency/agent's performance. 


### Data Analysis

Even with the 
first layer info, we could still do some analysis which give us some pretty 
useful insights. Actually we can answer the first question (when is the best 
time to buy or sell a house) just using these data. Please 
[check here for details]().

## Ongoing work/future plan:

Many things could affect the housing price, but for the same housing type,
   it is a common sense that 
   the location is usually the decisive factor. Nearly all agents I talked to, would repeat "Location! Location!
    Location is everything!" There are many housing data sets hosted on 
   [Kaggle](https://www.kaggle.com/) and some of them listed over 100 
   features but omitted the location. Then you see the analysis, some of 
   them are reasonable like prices are strongly correlated to the overall 
   quality of the building, living area size, etc. But some show that whether 
   there is a full bath could also be decisive. A full bath? Really? 
   
To avoid such mistake, I am going to convert the addresses to the lan and 
longitude, and then use a Google map API to plot a 2D heat map showing the price
distribution. I am expecting a clustering algorithm like 
K-means could divide Lund into several regions where each of them could be 
analyzed separately. Then for an apartment with given location, we first 
identify which region it belongs and then adding features listed in the 
previous section (maybe try multiple linear regression and random forest). 
Such model should give us a reasonable estimate of the price.  








