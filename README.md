# Sentiment Analysis Application

## Introduction
The "Sentiment Analysis" application is a project for analyzing restaurant reviews using Python and Flask. The application allows users to input text, analyze its sentiment, and display an image corresponding to the analysis result.

## About the Data
- **Source**: [Restaurant Review Sentiment Analysis](https://github.com/manthanpatel98/Restaurant-Review-Sentiment-Analysis/tree/master)
- **Description**: The dataset includes 10,000 rows and 8 columns.
- **Columns used**: `Review` and `Rating`
- **Goal**: Perform sentiment analysis by classifying reviews with a rating above 3 as "Positive" and below 3 as "Negative".

## Model
The project uses three models: Naive Bayes, SVM, and LSTM to measure performance and select the best model.

## Directory Structure
- `app.py`: The main file to run the Flask application.
- `notebook.ipynb`: Jupyter Notebook containing the code for training and evaluating the models.
- `requirements.txt`: List of required Python libraries.
- `index.html`: Web interface for the application.
- `label_encoder.pkl`: File storing the label encoder.
- `svm_model.pkl`: File storing the trained SVM model.
- `tfidf_vectorizer.pkl`: File storing the TF-IDF vectorizer.

## Installation and Running Instructions
### Step 1: Install Required Libraries
Install the necessary Python libraries by running:
```bash
pip install -r requirements.txt
```

### Step 2: Create Directory Structure
Ensure the following files and directories are created:
- `app.py`
- `notebook.ipynb`
- `requirements.txt`
- `index.html`
- `label_encoder.pkl`
- `svm_model.pkl`
- `tfidf_vectorizer.pkl`

### Step 3: Train and Save the Model
Open and run the `notebook.ipynb` to train and save the models.

### Step 4: Run the Flask Application
Run the Flask application using the command:
```bash
python app.py
```

### Step 5: Test the Application
Open a web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the application in action. Enter text and click the "Analyze" button or press "Enter" to view the sentiment analysis results.

## Interface

Below are some images of the application's interface.
### Application Launch
<p align="center">
  <img src="static/app.png" alt="User Interface">
</p>

After running the application, open a web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the application in action.

### Home Page

<p align="center">
  <img src="static/giaodien.png" alt="User Interface">
</p>

### Sentiment Analysis (Positive)
<p align="center">
  <img src="static/positive.png" alt="User Interface">
</p>

### Sentiment Analysis (Negative)
<p align="center">
  <img src="static/negative.png" alt="User Interface">
</p>

## Contact
For any questions or feedback, please contact via email: dailoi.ddl@gmail.com.
