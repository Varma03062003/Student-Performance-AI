# Student Performance AI

An AI-based student performance prediction and recommendation system built using Machine Learning, Python, and Streamlit.

## Project Overview

This project predicts a student's final exam score based on:

- Study Hours
- Attendance
- Previous Score
- Practice Tests
- Sleep Hours

The system also provides personalized study recommendations based on the student's current habits.

## Objectives

- Predict student final exam performance
- Analyze factors related to student performance
- Classify predicted performance level
- Provide personalized study recommendations
- Deploy the machine learning model as a web application

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- Machine Learning
- Data Analysis
- Data Visualization

## Machine Learning Model

A Linear Regression model was used to predict the student's final score.

## Model Performance

- **MAE:** 3.91
- **R² Score:** 0.73

The model explains approximately 73% of the variation in the target variable on the test data.

## Recommendation System

The application includes a rule-based recommendation layer.

Examples:

- Low study hours → Increase study hours
- Low attendance → Improve attendance
- Few practice tests → Complete more practice tests
- Low sleep hours → Improve sleep habits

## Application Features

- Student information input
- Final score prediction
- Performance classification
- Student analytics visualization
- Personalized recommendations
- Interactive Streamlit interface

## Author

Ravi Varma
AI & Data Science Graduate
