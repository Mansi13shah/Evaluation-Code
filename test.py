from flask import Flask
from flask import Flask, request, jsonify
import configparser
import pandas as pd
app = Flask(__name__)

# Load configuration from file
def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

# Load configuration
config = load_config('constants.ini')

# Set Flask app configuration
app.config['HOST'] = config.get('APP', 'HOST')
app.config['PORT'] = int(config.get('APP', 'PORT'))


# Root route handler 
@app.route('/') 
def home(): return "Welcome to the API. Available endpoints: /joinDataframes" 
@app.route('/joinDataframes', methods=['POST']) 
def join_dataframes():

    try:
        # Get the dataframes from the request
        data = request.get_json()
        dataframe1 = pd.DataFrame(data['dataframe1'])
        dataframe2 = pd.DataFrame(data['dataframe2'])

        # Perform the left join operation
        joined_dataframe = pd.merge(dataframe1, dataframe2, how='left')

        # Convert the resulting dataframe to JSON
        result = joined_dataframe.to_json(orient='records')

        return jsonify(result), 200

    except Exception as e:
        error_message = {'error': str(e)}
        return jsonify(error_message), 400

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
