import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load data
raw_mail_data = pd.read_csv('data/mail_data.csv')
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)), '')

# Encode labels
mail_data.loc[mail_data['Category'] == 'spam', 'Category'] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category'] = 1

# Split data
X = mail_data['Message']
Y = mail_data['Category'].astype('int')
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

# Feature extraction
vectorizer = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_train_features = vectorizer.fit_transform(X_train)

# Train the model
model = LogisticRegression()
model.fit(X_train_features, Y_train)

# Save the model and vectorizer
with open('backend/model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('backend/vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("Model and vectorizer saved successfully.")