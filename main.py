from flask import Flask, request, jsonify
import pandas as pd
from identity_colum import get_colm
from answers import get_answer
from gender import get_gender
from recommendation import get_recommendation
from datetime import datetime

app = Flask(__name__)

# Load your DataFrame
csv_file_path = 'sales_data_sample.csv'
sale_df = pd.read_csv(csv_file_path, encoding='latin-1')

csv_file_path = 'orders.csv.csv'
order_df = pd.read_csv(csv_file_path, encoding='latin-1')

@app.route('/get_answer', methods=['POST'])
def get_answer_api():
    try:
        data = request.get_json()
        question = data['question']

        col = get_colm(question, sale_df.columns)

        answer = get_answer(sale_df, question, col)

        return jsonify({'answer': answer.to_dict()})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/predict_gender', methods=['POST'])
def predict_gender():
    try:
        data = request.get_json()
        order_id = data['Order_id']

        gender = get_gender(sale_df, order_id)

        return jsonify({'gender': gender})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/recommendation', methods=['POST'])
def recommendation():
    try:
        data = request.get_json()
        month = data['month']
        recommendations = get_recommendation(sale_df, order_df, month)
        print('recommendations: ',recommendations)
        return jsonify({'recommendations': recommendations})
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(debug=True)
