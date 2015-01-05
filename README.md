Instructions Manual for "Recommender System for Consumer Products"(RecoProd)
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

Sentiment Analysis algorithms like Naive Bayes and SVM (Support Vector Machine) are used to
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


Database(s) Required(Back End):
--------------------------------
1.Microsoft Excel (for Spreadsheet)

2.Notepad

About the Dataset:
------------------
The dataset contains two directories - 'pos' and 'neg' . Each folder contains 1000 reviews each. 

The dataset must be used to train the classifier model.


How To Run The Project:
----------------------------
1. The Python files required to run the project are

	a.IR_Component_module1.py
	b.mod2.py
	c.rating.py
	d.module3_int.py
	e.plotmod3inp.py
	f.mod4.py
	g.new_gui.py


2. The Java file required to run the project is:

	a.Sample.java

3. Three RapidMiner processes are used. The respective XML codes are stored in testfiles are

	a.linsvmmodel.txt   - Training the Classifier Model
	b.linsvmtest.txt    - Classification for Module 2
	c.mod3.txt          - Classification for Module 3

4. The Excelfiles and folders stored in the "Files" MUST not be deleted.

5. The RapidMiner processes ust be created using the XML codes and suitable editing must be made to execute them.

6. The paths of the files created in Python must be suitably edited.

7. The project can be run by executing the Java file:Sample.java

WARINING:A fast working internet connection is required. The folders and spreadsheets created before must not be deleted. 