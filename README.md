WEB TRAFFIC TIME SERIES FORECASTING 
using Python, Matplotlib

1. Motivation
This is the self-extended exercise of SEO Analysis course from Udemy that I try to train models to predict possible problems of web traffic for big data (approximately 145,000 Wikipedia articles). It helps to provide an optimization solution for web traffic in the future.

2. Dataset

Unclean dataset from Kaggle about approximately 145,000 Wikipedia articles. There are no differences between traffic values of zero and missing values so data mining needs to be done before training

3. Method
Python, Matplotlibs, Time Series models including CNN

4. Project targets

Be familiar with and get some interesting perspectives by completing the following key highlights:

a. Performed time series analysis, anomaly detection using Isolation Forest (then, interpolation using the rolling mean)
b. Explored various time series forecasting models including CNN (then, ARMA, ARIMA, Exponential Smoothing, Prophet, Auto-Arima, and if possible compared performance using RMSE)
c. Developed flask app to render forecast plots generated using saved models ( if not possible, show the visualization)
d. Performed fetching data from AWS S3 using boto3 and if possible, deployed the flask app on AWS EC2 instance using nginx and gunicorn
Execution
e. Practice requirements.txt file to install the dependencies 
f. Learn how to prepare for model training
5. Preparation for model training

pip install -r req.txt
To run the application on local system.

python app.py
Time series analysis, anomaly detection, and forecasting
To view various analyses on the web traffic time-series data, steps taken to detect and handle anomalies, model training, testing, and forecasting, view the following Jupyter notebooks:

forecast.ipynb
forecast_CNN.ipynb
forecast_LSTM.ipynb
Model performance
Model	RMSE
ARMA	1.732618
ARIMA	1.734711
Auto-arima	2.148956
Exponential Smoothing	2.186610
Prophet	3.525529

6. Project Result

Practice at the basic level from target a to f and took note what I can not do, what I like most.

Things are not done completely is that I can not run the model by myself because of the big amount of data. Therefore, the visualization is not valuable.
7. Improvement:

- Stronger laptop to train data by myself, then make good visualization
- Study more about the above technologies used and how to use them frequently.

