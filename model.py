import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("dataset.csv")

X = data[['failed_logins', 'traffic']]
y = data['threat']

model = LogisticRegression()
model.fit(X, y)

def predict_threat(failed_logins, traffic):
    prediction = model.predict([[failed_logins, traffic]])
    return prediction[0]
