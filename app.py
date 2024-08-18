import json
from flask import Flask, jsonify

app = Flask(__name__)

feeding_stats = []
petting_stats = []

@app.route('/stats', methods=['GET'])
def stats():
    with open('data/log.json', 'r') as f:
        STATS = json.load(f)
    return jsonify(STATS)

if __name__ == "__main__":
    app.run(debug=False)