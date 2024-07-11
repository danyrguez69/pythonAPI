from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
CORS(app)


@app.route('/predice', methods=['POST'])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_, index=[0])
    query = pd.get_dummies(query_df.Processed_Review)
    
    vectorizer = joblib.load('vectorizer.pkl')
    classifier = joblib.load('classifier.pkl')
    X = vectorizer.transform(query).toarray()
    prediction = classifier.predict(X)
    return jsonify(f'El Review enviado es {prediction[0]}')
   


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=808, debug=True)
