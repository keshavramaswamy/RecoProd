"Recommender System for Consumer Products"(RecoProd)
============================================================================

About the Project
------------------
------------------

RecoProd- a recommender system which uses sentiment analysis techniques to provide
the best products for the customers is proposed. The techniques involved in Sentiment
Analysis are used to classify the reviews by the sentiment of the words into positive or
negative. Using the sentiment expressed in the words, opinions on any entity can be
categorized into positive or negative.

The system uses the existing product reviews and sentiment classification of the reviews
is carried out. RecoProd consists of an Information Retrieval component which extracts the
reviews from the e-commerce websites using the product names as queries. 

Sentiment Analysis algorithms like __Naive Bayes__ and __SVM (Support Vector Machine)__ are used to
categorize the reviews and opinion scores are assigned to the reviews. A comparative study
on the accuracy of the sentiment analysis algorithms used is also carried out. Aspect based
summary of opinions for each product is carried out and visually compared. The products are
displayed to the user.

The project is developed in Python,Java and RapidMiner.

Language(s) required:
------------------- 
1. Python 2.7

2. Java 7

Software(s) Required:
---------------------
1. RapidMiner 5


About the Dataset:
------------------
The dataset contains two directories - 'pos' and 'neg' . Each folder contains 1000 reviews each. 

The dataset must be used to train the classifier model.



How To Run The Project:
----------------------------
1. The Python files required to run the project are

	a.IR_Component_module1.py - Information Retrieval Component. Web scraper built using __Beautiful Soup__. Basic Front-End built using __Tkinter__.

	b.mod2.py - Sentiment Analysis Component with predictive model built in __RapidMiner__. 

	c.rating.py - Sentiment Rating given for each product.

	d.module3_int.py - Aspect based Opinion Summarisation for each product.

	e.plotmod3inp.py - Aspect based Opinion Visual Summarisation using __matplotlib__ and __NumPy__.

	f.mod4.py - Content based Recommender component using clustering based on Euclidian Distance.matplotlib used.

	g.new_gui.py - Final GUI built using Tkinter.


2. The Java file required to run the project is:

	a.Sample.java - Integrates the Rapidminer processes and python files.

3. Three RapidMiner processes are used. The respective XML codes are stored in testfiles are

	a.linsvmmodel.txt   - Training the Classifier Model
	b.linsvmtest.txt    - Classification for Module 2
	c.mod3.txt          - Classification for Module 3

4. The Excelfiles and folders stored in the "Files" MUST not be deleted.

5. The RapidMiner processes must be created using the XML codes and suitable editing must be made to execute them.

6. The paths of the files created in Python must be suitably edited.

7. The project can be run by executing the Java file:Sample.java

WARNING:A fast working internet connection is required. The folders and spreadsheets created before must not be deleted. 