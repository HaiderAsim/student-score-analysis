#  Student Performance Data Analysis

##  Project Overview

This project analyzes a student performance dataset using **Python** and the **Pandas** library.
The goal is to explore patterns in student scores and generate insights based on different factors such as gender, lunch type, parental education, and test preparation.

---

##  Technologies Used

* Python 
* Pandas 
* kaggle for sample data set
---

##  Dataset

The dataset used:

* `study_performance.csv` (original dataset)
* `study_performance_cleaned.csv` (processed dataset)

---

##  Features & Analysis

The script performs the following operations:

* Displays basic dataset information
* Checks for missing values
* Analyzes average scores by gender
* Examines test preparation impact
* Compares performance by:

  * Parental education
  * Race/ethnicity
  * Lunch type
* Calculates:

  * Average score
  * Pass/Fail result (Pass ≥ 55)

---

##  Sample Code

```python
df["average_score"] = (df["math_score"] + df["reading_score"] + df["writing_score"]) / 3
df["result"] = df["average_score"].apply(lambda x: "Pass" if x >= 55 else "Fail")
```

---

##  How to Run

1. Install dependencies:

```bash
pip install pandas
```

2. Run the script:

```bash
python analysis.py
```

---

##  Output

* Console insights (statistics and grouped analysis)
* Cleaned dataset saved as:

  * `study_performance_cleaned.csv`

---

##  Author

Haider Asim

---

##  Notes

This is a beginner-friendly data analysis project to practice data cleaning and exploration using Pandas.
