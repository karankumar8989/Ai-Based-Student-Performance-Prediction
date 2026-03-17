import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("../datasets/Student_data.csv")

# Features
X = data[['study_hours','attendance','previous_score','assignments']]

# Target
y = data['final_score']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train,y_train)

# Save model
pickle.dump(model,open("student_model.pkl","wb"))

print("Model trained successfully!")