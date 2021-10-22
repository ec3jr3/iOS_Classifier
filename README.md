# iOS_Classifier
Tutorial on how to create a model using Xcode, Turi and Python 

## INSTALL TURI IN YOUR TERMINAL

To install Turi Create, go to Terminal.app and type the following command:

<img width="620" alt="Screen Shot 2021-10-22 at 4 35 10 PM" src="https://user-images.githubusercontent.com/50173053/138525808-29ac1953-c446-4da0-a88b-16458b18fe84.png">

After installing the Python package, we will create a new Python project, by doing the following steps:

1. Create a folder named iOSClassifier
2. Open Xcode and create a new file (xcode link: https://apps.apple.com/us/app/xcode/id497799835?mt=12)

<img width="700" alt="Screen Shot 2021-10-22 at 4 39 45 PM" src="https://user-images.githubusercontent.com/50173053/138525986-63ef9b9f-4412-4bf3-98ae-e0124429441f.png">

3. Select an Empty file from any section

<img width="701" alt="Screen Shot 2021-10-22 at 4 41 51 PM" src="https://user-images.githubusercontent.com/50173053/138526121-bedd159d-a45e-4684-8ced-6ecbc0a29d4f.png">

4. Name the file: classifier.py
5. Save it to the iOSClassifier folder

### FINDING A DATASET

https://datasetsearch.research.google.com

In this example were going to use a data set of diabetes ".csv"
**if you have problems with the dataset** check the documentation of Turi https://apple.github.io/turicreate/docs/api/generated/turicreate.SFrame.read_csv.html

Now that we find our data set
link for the data set : https://www.kaggle.com/mathchi/diabetes-data-set

**Make sure your dataset file is in the folder we created**

1. Open the classifier.py file and import turicreate by adding this line:

<img width="265" alt="Screen Shot 2021-10-22 at 4 53 48 PM" src="https://user-images.githubusercontent.com/50173053/138527089-3bd3fa5c-e687-4228-9452-47e2e8151721.png">

2. then add the following line to  load the data from the dataset file:

<img width="264" alt="Screen Shot 2021-10-22 at 4 55 15 PM" src="https://user-images.githubusercontent.com/50173053/138527196-0d1973f0-4bcb-4399-a07d-32f04b7dec24.png">

3. We are going to take all our features from our dataset aka dependent variables

**if you want to now the name of your variables add this line of code**

<img width="184" alt="Screen Shot 2021-10-22 at 5 00 49 PM" src="https://user-images.githubusercontent.com/50173053/138527657-05aa199b-32bb-4d49-93ce-6d77d7bf5939.png">

<img width="735" alt="Screen Shot 2021-10-22 at 5 29 56 PM" src="https://user-images.githubusercontent.com/50173053/138529691-af30948f-0373-40b2-8a9b-3d39ecf93431.png">

## Building machine learning model

In this phase, we will start building our model using the given dataset above. Before we begin, we need to split our dataset into a training set and a testing set. The training set will be 75%, and the testing set will be 25%.

### Data Splitting

<img width="401" alt="Screen Shot 2021-10-22 at 5 03 03 PM" src="https://user-images.githubusercontent.com/50173053/138527819-aeb84da6-d60b-45f7-b527-f1976830012d.png">

### Modelling algorithm

<img width="525" alt="Screen Shot 2021-10-22 at 5 04 28 PM" src="https://user-images.githubusercontent.com/50173053/138527911-3f340659-4fce-4bd4-84a2-1e1964d587cf.png">

uriCreate supports different classification algorithms, in our case, we will use the logistic regression https://en.wikipedia.org/wiki/Logistic_regression. We use logistic regression since our model has a binary output. Thus, our output can be either positive or negative to show if a person is at risk of getting diabetes or not.

Logistic regression is better suited for our problem since this algorithm gives higher accuracy and is less inclined to over-fitting.

To use the logistic regression algorithm use the following command:

<img width="523" alt="Screen Shot 2021-10-22 at 5 07 09 PM" src="https://user-images.githubusercontent.com/50173053/138528137-e16c0102-6b71-4ab3-95b4-1ae110c81fa5.png">

**Turi has a multiple classifier you can use**
1. Boosted tree Classifier: https://en.wikipedia.org/wiki/Gradient_boosting
2. Decision tree Classifier: https://en.wikipedia.org/wiki/Decision_tree
3. Logistic Regression: https://en.wikipedia.org/wiki/Logistic_regression
4. Nearest neighbor Classifier: https://en.wikipedia.org/wiki/Nearest_neighbor_search
5. Random forest Classifier: https://en.wikipedia.org/wiki/Random_forest
6. Support Vector Machines: https://en.wikipedia.org/wiki/Support-vector_machine

**You may wonder which one is the best one. Each one has some pros and cons to learn more go to the links of each one. Turi has a was to Automatically picks the right model based on your data**

<img width="373" alt="Screen Shot 2021-10-22 at 5 15 33 PM" src="https://user-images.githubusercontent.com/50173053/138528698-19bac51f-8fc8-491a-b284-ae05bddc0483.png">

### Next, we will evaluate the test data to determine the model accuracy:

<img width="320" alt="Screen Shot 2021-10-22 at 5 16 50 PM" src="https://user-images.githubusercontent.com/50173053/138528790-77aef9f5-c13c-4a4a-9ce4-3a0fec369d22.png">

## Lastly, insert the following code to save the model and export the  classification model as a CoreML model:

<img width="310" alt="Screen Shot 2021-10-22 at 5 17 49 PM" src="https://user-images.githubusercontent.com/50173053/138528870-5216f396-d08f-404e-ad6f-7de5831ba88c.png">

### Your classifier.py file should look like this:

<img width="780" alt="Screen Shot 2021-10-22 at 5 18 47 PM" src="https://user-images.githubusercontent.com/50173053/138528946-b3dfaf38-6979-4f63-acc4-b307dd9d2e3b.png">

### Now it’s time to run our code! To do so, go to Terminal.app and change to the iOSClassifier folder. Then run the classifier.py file like this:

**To change to the folder of our project. My folder is in the desktop**

<img width="278" alt="Screen Shot 2021-10-22 at 5 21 30 PM" src="https://user-images.githubusercontent.com/50173053/138529135-875eb33b-e1c0-4c09-a855-39431a40f907.png">

My path would be: cd Desktop/iOS_Classifier

To run the file type : "python classifier.py" **you need to be in the path of your folder**

<img width="612" alt="Screen Shot 2021-10-22 at 5 43 28 PM" src="https://user-images.githubusercontent.com/50173053/138530655-c5ee9aba-c83a-4340-8167-4de14d730240.png">

