
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# importing the data 
df = pd.read_excel("Final_TikTok_Data_With_Growth.xlsx")

# Sentiment into numbers
df["SENTIMENT_NUM"] = df["SENTIMENT"].map({
    "Negative": -1,
    "Neutral": 0,
    "Positive": 1
})

# Video Type'ı one-hot encoding ile çevir
video_dummies = pd.get_dummies(df["VIDEO TYPE"])
df = pd.concat([df, video_dummies], axis=1)

# Özellikleri ve hedef değişkeni tanımla
features = ["LIKES", "COMMENTS", "VIEWS", "SENTIMENT_NUM"] + list(video_dummies.columns)
target = "GROWTH RATE (%)"

# Eksik değerleri temizle
df_cleaned = df.dropna(subset=features + [target])
X = df_cleaned[features]
y = df_cleaned[target]

# Eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# teaching the model
model = LinearRegression()
model.fit(X_train, y_train)

# prediction
y_pred = model.predict(X_test)

# calculating performance metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# printing the results
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)
