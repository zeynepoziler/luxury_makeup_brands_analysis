# Luxury Makeup Brand Analysis – DSA210 Project

An analysis of luxury makeup brands’ social media engagement and estimated sales impact using real-world TikTok content and Python-powered data sources.

---

## Overview
This project examines the relationship between **social media engagement** and **estimated sales growth** for two leading luxury makeup brands which are — **YSL Beauty** and **Lancôme** — by manually collecting TikTok data and analyzing it through Python-based data science tools.

---

## Objectives
- Investigating whether **higher TikTok engagement (views, likes, comments)** translates to **greater sales growth**.
- Identify which brand has stronger performance across TikTok.
- Compare **engagement effectiveness** between YSL Beauty and Lancôme.

---

## Data Collection
- **32 TikTok videos were manually collected**, 16 per brand (YSL Beauty and Lancôme).
- Data covered the period between **January–April 2025**, with **4 videos per month per brand**.
- Each row included: **Date**, **Brand**, **Views**, **Likes**, **Comments**, **Caption**, **Video Type**, and **Why Selected**.
- The dataset was manually created by reviewing each brand’s official TikTok content(@yslbeauty & @lancome.official) and curated based on engagement variety, content diversity, and brand activity.

---

## Synthetic Data (AI-assisted)
Two key variables were **generated programmatically using Python and AI-supported logic**:

1. **Sentiment Analysis (`SENTIMENT`)**:
   - A **rule-based sentiment classifier** was applied to captions using Python.
   - Positive, Neutral, and Negative labels were assigned based on keyword matches (e.g., “love”, “obsessed”, “worst”, etc).

2. **Growth Rate Estimation (`GROWTH RATE (%)`)**:
   - A custom metric was created based on engagement score:
     
     \[ \text{Engagement Score} = \frac{Likes + Comments}{Views} \]

   - A base score was modified depending on the sentiment, ranging from -5% to +15% estimated growth.

---

## Exploratory Data Analysis (EDA)
Using **pandas, seaborn, and matplotlib**, several visual analyses were performed:

- **Average Growth Rate by Brand** – barplot comparing YSL vs Lancôme
- **Sentiment Distribution** – countplot of all video sentiments
- **Likes vs Growth Rate** – scatterplot showing linear correlation
- **Video Type vs Growth Rate** – barplot by content category

 All visual outputs are stored under: `visuals/`

---

## Hypothesis Testing
Conducted using `scipy.stats`:

1. **T-Test**:
   - Compared mean growth rates between YSL and Lancôme
   - **Result:** No statistically significant difference (p = 0.8978)

2. **Pearson Correlation**:
   - Examined relationship between Likes and Growth Rate
   - **Result:** Moderate positive correlation (r = 0.366, p = 0.043)

Code for hypothesis testing is included in the file: `code/analysis_with_hypothesis.py`

---

## Repository Structure
```
 data/
    └── Final_TikTok_Data_With_Growth.xlsx
 visuals/
    ├── ort_growth_by_brand.png
    ├── sentiment_distribution.png
    ├── likes_vs_growth.png
    └── growth_by_video_type.png
 code/
    └── analysis_with_hypothesis.py
 README.md
```

---

## Tools & Technologies
- Python 3.9
- pandas, numpy
- matplotlib, seaborn
- scipy.stats
- openpyxl

---

## Final Insights
- TikTok engagement metrics alone are **not sufficient** to explain differences in sales growth across luxury brands
- **Sentiment and engagement quality (likes/comments ratio)** play a more critical role than volume alone
- Data-driven estimation and hypothesis testing enable clear differentiation between content effectiveness

---

## ✅ Summary
This project showcases how **real-world social data** combined with **AI-supported feature engineering** and **Python-based analytics** can lead to actionable insights in digital marketing for luxury cosmetics brands.
