from flask import Flask, request, jsonify
import util
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Home Price Prediction API!"

@app.route('/get_location_names')
def get_location_names():
    response =jsonify({
            'locations': util.get_location_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    #total_sqft =float(request.form['total_sqft'])
    #location = request.form['location']
    #bhk = int(request.form['bhk'])
    #bath = int(request.form['bath'])
    try:
        # Get data from JSON (modern approach) or form-data
        if request.is_json:
            data = request.get_json()
            total_sqft = float(data['total_sqft'])
            location = data['location']
            bhk = int(data['bhk'])
            bath = int(data['bath'])
        else:
            total_sqft = float(request.form['total_sqft'])
            location = request.form['location']
            bhk = int(request.form['bhk'])
            bath = int(request.form['bath'])
        estimated_price = util.get_estimated_price(location,total_sqft,bhk,bath)

        response = jsonify({
        'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except KeyError as e:
        return jsonify({'error': f'Missing parameter: {str(e)}'}), 400

    except ValueError as e:
        return jsonify({'error': f'Invalid parameter value: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__== "__main__":
    print("Starting python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug =True)
