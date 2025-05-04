from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        # Get data from request (works for both JSON and form-data)
        data = request.get_json() if request.is_json else request.form

        # Validate required parameters
        required = ['total_sqft', 'location', 'bhk', 'bath']
        if not all(key in data for key in required):
            return jsonify({'error': 'Missing required parameters'}), 400

        # Convert and validate values
        try:
            total_sqft = float(data['total_sqft'])
            location = str(data['location'])
            bhk = int(data['bhk'])
            bath = int(data['bath'])
        except (ValueError, TypeError) as e:
            return jsonify({'error': f'Invalid parameter value: {str(e)}'}), 400

        # Get prediction
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        if estimated_price is None:
            return jsonify({'error': 'Prediction failed'}), 500

        response = jsonify({
            'estimated_price': estimated_price,
            'currency': 'INR',
            'parameters': {
                'location': location,
                'total_sqft': total_sqft,
                'bhk': bhk,
                'bath': bath
            }
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True, host='0.0.0.0', port=5000)