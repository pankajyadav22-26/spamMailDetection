from flask import Flask, request, jsonify
import pickle

from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)

# Load the model and vectorizer
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_message = data['message']
    input_features = vectorizer.transform([input_message])
    prediction = model.predict(input_features)
    result = "Ham Mail" if prediction[0] == 1 else "Spam Mail"
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)