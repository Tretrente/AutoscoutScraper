from flask import Flask, render_template, request, jsonify


carList = {'audi': 'a1', 'audi': 'a2', 'audi': 'a3', 'audi': 'a4', 'toyota': 'prius', 'toyota': 'rav4', 'nissan': 'micra', 'ford': 'mondeo'}

app = Flask(__name__)

@app.route('/')
def index():
    global carList
    options_dropdown1 = list(carList.keys())
    return render_template('index.html', options_dropdown1=options_dropdown1)

@app.route('/update_values', methods=['POST'])
def update_values():
    data = request.get_json()
    target_id = data['targetId']
    options_dropdown2 = makeDropdownPopulator(target_id)
    return render_template('index.html', options_dropdown2=options_dropdown2)

def makeDropdownPopulator(make):
    global carList
    models = [valore for chiave, valore in carList.items() if chiave == make]
    return models


if __name__ == '__main__':
    app.run(debug=True)