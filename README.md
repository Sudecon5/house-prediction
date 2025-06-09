# house-prediction
<img width="1455" alt="Screenshot 2025-05-06 at 10 31 52" src="https://github.com/user-attachments/assets/58559bf1-7b46-455f-9956-45bba963b914" />
The house price prediction model uses sklearn library and linear regression to predict properties in bangalore. The dataset is from <a href ='https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data'>Kaggle.</a> The features of the model are area_type, availability, location, size, society, total_sqft, bath, balcony and the target is the price. Linear Regression is found adequate for the model as this data set falls in the regression type of Machine Learning. Additionally, a python flask server is used that enables the saved model to serve http requests. Also, for a user interface a website is built in html, css and javascript that allows to enter the home square ft area, bedrooms etc and in return it calls upon the python flask server to retreive the predicted price. The data modeling process included numerous steps of data science concepts like-</br>
* Data Load and Data Cleaning </br>
* Outlier Detection and Removal</br>
* Feature Engineering</br>
* Dimensionality reduction</br>
* Gridsearchcv for Hyperparameter tuning</br>
* K Cross Validation</br>

## Technology and tools used-</br>
1. Python</br>
2. Numpy and Pandas for data cleaning</br>
3. Matplotlib for data visualization</br>
4. Sklearn for model building</br>
5. Jupyter notebook, visual studio code and pycharm for IDE</br>
6. Python flask for http server</br>
7. HTML for UI  </br>
