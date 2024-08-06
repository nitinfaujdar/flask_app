from flask import Flask, jsonify
from data_storage import store_data, get_data
from data_processing import process_data
from fetch_data import fetch_mock_data

app = Flask(__name__)

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    raw_data = fetch_mock_data()
    processed_data = process_data(raw_data)
    store_data(processed_data)
    return jsonify({'message': 'Data fetched and processed successfully'})

@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    data = get_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
