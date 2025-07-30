
## 🔐 Smart Login Risk Score Generator

A **data-driven anomaly detection system** that analyzes login activity and assigns a real-time **risk score** to each login attempt. Designed to flag suspicious behavior using user metadata and ML-based risk prediction — a practical cybersecurity project to showcase **Pandas, Scikit-learn, and SQL** skills.

---
### Try It Out
Explore the live Streamlit app:  https://smart-app-risk-score-generator-ijzfligpxkjqkoivrbfpg2.streamlit.app/

---

### Features

*  Analyzes login patterns from structured CSV data
*  Machine Learning model (Random Forest) predicts suspicious logins
*  Precision-Recall curve used for custom threshold setting
*  Generates a **Risk Score (0–100%)** for each login
*  Clean dashboard using **Streamlit** for easy visualization

---

### Tech Stack

* **Python** (Pandas, NumPy, Matplotlib, Scikit-learn)
* **Streamlit** for UI
* **Google Colab** (for model training)
* **VS Code + Git + GitHub** (for deployment & version control)

---

### 📁Dataset

Custom-built dataset with:

* User ID
* Login Timestamp
* IP Address & Device Metadata
* Label: `1 = Suspicious`, `0 = Normal`

---

### How to Run

```bash
streamlit run app.py
```

Then open the browser tab to view the login risk detection dashboard.

---

### Use Case

Can be extended for:

* **Enterprise-level login monitoring**
* Fraud detection
* Cybersecurity dashboards
* Authentication analytics

---



