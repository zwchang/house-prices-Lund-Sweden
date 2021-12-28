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

This project is still ongoing. The majority work has been done. Currently I am building
a website to deploy the trained model, and I expect the final product would be a website with
API endpoint where you provide the relevant features of a property (e.g. address, size, build
year, number of rooms, etc.) or even just a simple Hemnet link to the listing, then with one
click, it shows the estimated price. The model should be continuously refined and validated by
taking streaming data from Hemnet (using MLOps) as the new listings keep coming in.

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

[Here is the example](/notebooks/hemnet_page50.ipynb) of how we 
can scrap the first 
layer 
info. Then we 
can use [this script](/notebooks/hemnet_csv.ipynb) to generate 
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
[Here is the example](/notebooks/hemnet_2nd_layer_test.ipynb) of how to extract the second 
layer info. 
Then it is fairly straightforward to generalize this code to all 1972 items using [this script](/notebooks/hemnet_2nd_layer.ipynb).



### Data Analysis

Using the data we collected, we are able to do some analysis which give us a general picture of the Lund apartment sales. Actually we are able to answer the first and second question we brought up in previous section using these data. 

### Model prediction

We first put all info from first and second layer together and merge them into a CSV file (check [here](/notebooks/hemnet_dataCleaning.ipynb) for details). Then we can convert the addresses to the lan and longitude, and then use a Google map API to plot a 2D heat map showing the price distribution (check [here](/notebooks/Hemnet_map.ipynb)). Then we can do some feature engineering by dealing with missing data, outliers, and data transformation. 

For the model training part, We first split the data into train (70%) and
test (30%) sets, then we test three commonly used ensemble algorithms: gradient boosting, xgboost, and random forest. For all three models trained with including all numerical features, we are able to slightly outperform the brokers’ evaluation from comparing with the asking price MAE. xgboost and
random forest performed especially well. 

Here we only used the default parameters for these algorithms provided by scikit-learn, we
could definitely do better by fine-tuning these parameters, i.e. learning rate, sample number,
etc. We could also try more algorithms like Lasso, Ridge, Elastic-Net regression, CatBoost,
LightGBM, etc. Each model may capture certain part of the data pattern, which may have
overfitting/underfitting problem. We could blend these models to get a better prediction. However, there are two important factors we can not include our model. First, Hemnet does not
provide the overall quality info for the sold property. A well renovated apartment can easily
sold for additional 100-200 tSEK compared to a moderated one. Second, the bidding process
is often unpredictable, sometimes even unreasonable when the market is hot. Therefore, the
MAE of our trained models might be reasonable. Despite missing these two important factors,
we can still provide a good estimating price for an apartment given the information we have.
Maybe the user could somehow modify the predicted price based on how well his/her apartment
is renovated and the hotness of the current housing market.


I also listed the asking, final sold prices as well as our model prediction using random forest algorithm for the six randomly picked apartments sold recently. Our model
perform pretty well especially when the price is not too high. See [here](/notebooks/hemnet_model_pre.ipynb) for details. [Here](predict.py) is the Python code I used for the prediction.  

[Here](/notebooks/Lund_apartment_sales_211228.pdf) is the summary notes for the work I've done so far.

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










