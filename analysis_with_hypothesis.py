
# TikTok Engagement Analysis and Growth Estimation for YSL Beauty & Lancôme

# --- Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, pearsonr

# --- Step 2: Load and Clean Data
df = pd.read_excel("data/Final_TikTok_Data_With_Growth.xlsx")

def clean_numeric(val):
    if isinstance(val, str):
        val = val.upper().replace(',', '').replace('I', '1').strip()
        if 'K' in val:
            return float(val.replace('K', '')) * 1000
        elif 'M' in val:
            return float(val.replace('M', '')) * 1000000
    return float(val)

df['VIEWS'] = df['VIEWS'].apply(clean_numeric)
df['LIKES'] = df['LIKES'].apply(clean_numeric)
df['COMMENTS'] = df['COMMENTS'].apply(clean_numeric)
df['BRAND'].fillna('YSL BEAUTY', inplace=True)

# --- Step 3: Sentiment Analysis
def guess_sentiment(caption):
    caption = str(caption).lower()
    if any(word in caption for word in ['love', 'obsessed', 'amazing', 'must-have']):
        return "Positive"
    elif any(word in caption for word in ['worst', 'disappointed', 'bad']):
        return "Negative"
    else:
        return "Neutral"

df['SENTIMENT'] = df['CAPTION'].apply(guess_sentiment)

# --- Step 4: Generate Growth Rate (%)
def generate_growth(row):
    base = 2.0
    if row['SENTIMENT'] == 'Positive':
        base += 2
    elif row['SENTIMENT'] == 'Negative':
        base -= 0.5
    engagement_score = (row['LIKES'] + row['COMMENTS']) / max(row['VIEWS'], 1)
    return round(min(max(base + engagement_score * 100, -5), 15), 2)

df['GROWTH RATE (%)'] = df.apply(generate_growth, axis=1)

# --- Step 5: Exploratory Data Analysis (EDA)
sns.set(style="whitegrid")

plt.figure(figsize=(7, 5))
sns.barplot(data=df, x="BRAND", y="GROWTH RATE (%)", estimator=np.mean, ci=None)
plt.title("Marka Bazında Ortalama Growth Rate (%)")
plt.savefig("visuals/ort_growth_by_brand.png")
plt.close()

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="SENTIMENT", palette="pastel")
plt.title("Sentiment Dağılımı")
plt.savefig("visuals/sentiment_distribution.png")
plt.close()

plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="LIKES", y="GROWTH RATE (%)", hue="BRAND")
plt.title("Beğeni Sayısı ve Growth Rate İlişkisi")
plt.savefig("visuals/likes_vs_growth.png")
plt.close()

plt.figure(figsize=(9, 5))
sns.barplot(data=df, x="VIDEO TYPE", y="GROWTH RATE (%)", estimator=np.mean, ci=None)
plt.title("Video Tipine Göre Ortalama Growth Rate (%)")
plt.xticks(rotation=20)
plt.savefig("visuals/growth_by_video_type.png")
plt.close()

# --- Step 6: Hypothesis Tests

# T-Test: YSL vs Lancôme
ysl_growth = df[df["BRAND"].str.contains("YSL", case=False)]["GROWTH RATE (%)"].dropna()
lancome_growth = df[df["BRAND"].str.contains("Lanc", case=False)]["GROWTH RATE (%)"].dropna()
t_stat, p_value = ttest_ind(ysl_growth, lancome_growth, equal_var=False)

print("T-Test between YSL and Lancôme Growth Rates:")
print(f"T-statistic: {round(t_stat, 3)}")
print(f"P-value: {round(p_value, 4)}")

# Correlation: Likes vs Growth Rate
likes_clean = df["LIKES"].dropna()
growth_clean = df["GROWTH RATE (%)"].dropna()
common_index = likes_clean.index.intersection(growth_clean.index)
likes_filtered = likes_clean.loc[common_index]
growth_filtered = growth_clean.loc[common_index]

corr_coef, corr_p_value = pearsonr(likes_filtered, growth_filtered)

print("\nCorrelation between Likes and Growth Rate:")
print(f"Correlation Coefficient: {round(corr_coef, 3)}")
print(f"P-value: {round(corr_p_value, 4)}")

# --- Optional: Save final dataset
df.to_csv("data/Final_TikTok_Data_With_Growth.csv", index=False)

print("\nAnalysis complete. Visuals, results and data saved.")
