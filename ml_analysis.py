
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Loading data
df = pd.read_excel("Extended_TikTok_Data_With_Growth.xlsx")

# Converting categorical and sentiment data
df['SENTIMENT'] = df['SENTIMENT'].map({'positive': 1, 'neutral': 0, 'negative': -1})
df['SENTIMENT'].fillna(0, inplace=True)
df['VIDEO TYPE'] = df['VIDEO TYPE'].astype('category').cat.codes

# Selecting features and target
features = ['VIEWS', 'LIKES', 'COMMENTS', 'SENTIMENT', 'VIDEO TYPE']
target = 'GROWTH RATE (%)'
X = df[features]
y = df[target]

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R² Score:", r2)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
