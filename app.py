from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        json_data = request.form.get('json_data')
        json_data = json.loads(json_data)
        return render_template('response.html', json_data=json_data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
