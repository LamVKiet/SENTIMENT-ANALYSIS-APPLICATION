from flask import Flask, render_template, request, jsonify
import pickle
import os

app = Flask(__name__)

# Tải các mô hình và vectorizer đã được lưu
MODEL_PATH = os.path.join('models', 'svm_model.pkl')
VECTORIZER_PATH = os.path.join('models', 'tfidf_vectorizer.pkl')
LABEL_ENCODER_PATH = os.path.join('models', 'label_encoder.pkl')

with open(MODEL_PATH, 'rb') as file:
    svm_model = pickle.load(file)
with open(VECTORIZER_PATH, 'rb') as file:
    vectorizer = pickle.load(file)
with open(LABEL_ENCODER_PATH, 'rb') as file:
    label_encoder = pickle.load(file)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    review = request.json['review']
    review_tfidf = vectorizer.transform([review])
    predicted_label = svm_model.predict(review_tfidf)
    predicted_label_name = label_encoder.inverse_transform(predicted_label)[0]

    result = {
        'sentiment': 'Positive' if predicted_label_name == 'Positive' else 'Negative',
        'image_path': 'static/pos.png' if predicted_label_name == 'Positive' else 'static/neg.png'
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
