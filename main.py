from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def read_file(country_code):
    with open("./dataset/"+country_code+".json", "r") as read_file:
        data = json.load(read_file)
        return(data)

@app.route('/<country_code>', methods=['GET'])
def country(country_code):
    data = read_file(country_code)
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
