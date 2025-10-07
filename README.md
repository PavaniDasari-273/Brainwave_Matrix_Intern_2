# Brainwave_Matrix_Intern_2

# 💳 Credit Card Fraud Detection using Machine Learning

📌 **Overview**
Credit card fraud is a growing threat, costing billions worldwide. This project detects fraudulent credit card transactions in real-time using Machine Learning techniques, helping protect users and financial institutions from losses.

I also built an **interactive Streamlit Web App** that allows users to input transaction details and instantly check whether a transaction is **Legitimate** or **Fraudulent**.

⚡ **Features**
✅ Detects if a transaction is legitimate or fraudulent
✅ Handles imbalanced datasets effectively
✅ Feature scaling and preprocessing for accurate predictions
✅ Trained Random Forest / Logistic Regression model for classification
✅ Interactive UI built with Streamlit

🛠 **Tech Stack**

* Python 3
* Streamlit – Web App Framework
* Scikit-learn – Machine Learning Algorithms
* Joblib – Model persistence
* Pandas / Numpy – Data handling

📂 **Project Structure**

```
├── app.py                 # Streamlit web app  
├── model.jb               # Trained ML model  
├── scaler.jb              # Scaler / Preprocessing objects  
├── requirements.txt       # Required dependencies  
├── dataset/               # Credit card transaction dataset  
└── README.md              # Project documentation  
```

## 🚀 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Credit-Card-Fraud-Detection.git
   cd Credit-Card-Fraud-Detection
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open the link shown in the terminal (default: [http://localhost:8501](http://localhost:8501))

📸 **Screenshots**

 **Interactive UI:** ![image alt](https://github.com/PavaniDasari-273/Brainwave_Matrix_Intern_2/blob/74c64e18533fbeb5667fb4b65b15f82c88930bad/Screenshot%202025-10-07%20220813.png)(https://github.com/PavaniDasari-273/Brainwave_Matrix_Intern_2/blob/509b57193bfc05f965902530c5496947db96991d/Screenshot%202025-10-07%20222734.png)
 Clean and intuitive interface built with Streamlit. Users can enter transaction details and click “Check Transaction” to get instant results.
 **Fraudulent Transaction:**  ![image alt]()
  Suspicious transactions are flagged in red for immediate attention.
 **Legitimate Transaction:** ![image alt]()
  Safe transactions are shown in green, giving users confidence.
 **Input Validation:** ![image alt]()
   Alerts users when transaction details are missing or invalid.

🔮 **Future Enhancements**

* Integrate deep learning models (e.g., LSTM, Autoencoders) for higher accuracy
* Deploy on Heroku / Streamlit Cloud for public access
* Add real-time transaction monitoring & alert system

🙏 **Acknowledgement**
Special thanks to **Brainwave _Matrix_Solution** for providing this project opportunity.

📌 **Author**
👩‍💻 Pavani Dasari

📫 **Connect with me:** [LinkedIn](https://www.linkedin.com/in/pavani-dasari-691bb5321) | [GitHub](https://github.com/PavaniDasari-273)
