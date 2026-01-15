# AI Jobs Big Data Analysis

This project is part of the **Big Data** course assignment.  
The main focus of this project is **data cleaning** and **data insertion into MongoDB** using Python.

The dataset used in this project is related to **AI-related job listings** and was obtained from **Kaggle**.

---

## 📌 Project Scope
This project focuses on:
- Cleaning raw data from a large dataset
- Preparing structured data for database storage
- Inserting cleaned data into MongoDB for data management

⚠️ This project does **not** include data analysis, visualization, or machine learning modeling.

---

## 📂 Dataset
- Source: **Kaggle**
- Topic: **AI Jobs Dataset**
- Format: JSON
- Note:  
  The full dataset is not included in this repository due to file size considerations.  
  Only the data processing logic is provided.

---

## 🛠️ Technologies Used
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="50"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mongodb/mongodb-original.svg" width="50"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/apachespark/apachespark-original-wordmark.svg" width="50"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/json/json-original.svg" width="50"/>

---

## 🔄 Workflow
1. Load raw AI Jobs dataset from Kaggle
2. Perform data cleaning:
   - Remove unnecessary fields
   - Handle missing or invalid values
   - Standardize data format
3. Save cleaned data into JSON format
4. Insert cleaned data into MongoDB using PyMongo

---

## 🧪 MongoDB Implementation
- Database name: `bigdata_ai`
- Collection name: `ai_jobs`
- MongoDB is used as a data storage solution to manage large-scale datasets.

MongoDB runs locally using the default port: 
mongodb://localhost:27017/

---

## ▶️ How to Run
1. Make sure **MongoDB** is installed and running
2. Install required dependencies: pip install -r requirements.txt
3. Run the data insertion script: python insert_to_mongodb.py

---

## 📄 Notes
- MongoDB database files are not included in this repository
- This repository focuses on demonstrating data handling logic, not database deployment
- The dataset belongs to its original author on Kaggle

---

## 👤 Author
Elsa Anggraini  
Computer Science Student (Semester 5)

---

## 📚 Course Information
Big Data  
Academic Project
