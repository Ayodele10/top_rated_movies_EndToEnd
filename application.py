from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import pickle


application = Flask(__name__)
app = application


# import the model
rfr_model = pickle.load(open('model/rfr_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'POST':
        data = request.get_json(force=True)
        # Extract features from the input data
        features = [data['vote_average'], data['vote_count'], data['year'], data['month'], 
                    data['day'], data['weighted_rating'], data['is_sequel'], data['engagement_score'], data['id']]
        
        final_features = [np.array(features)]
        prediction = rfr_model.predict(final_features)

        output = round(prediction[0], 2)

        return render_template('index.html', results = output[0])
    else:
        return render_template('index.html')
    

    if __name__ == "__main__":
        app.run(debug=True)